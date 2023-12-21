import os
import yaml
import json
from typing import List
from uuid import uuid4
import sys

sys.path.append("..")

from dotenv import load_dotenv

from fastapi import FastAPI, WebSocket, HTTPException


from backend.cli.main import converse
from backend.models.models import SetupConfig

from backend.api.helper.agent import (
    generate_agent_description,
    generate_system_message,
    generate_first_statement,
)
from backend.models.models import Configuration

from backend.pi.tts import tts

load_dotenv()

app = FastAPI(
    title="El Debate API",
    description="An API for the El Debate project",
    version="0.0.0 (leets keep it this way forever)",
)


@app.get("/descriptions")
async def get_setup(setup: SetupConfig):
    conversation_description = f"""Here is the topic of conversation: {setup.topic}
    The participants are: {setup.first_agent}, {setup.second_agent} """

    description_agent_1 = generate_agent_description(
        setup.first_agent, conversation_description, setup.word_limit
    )
    description_agent_2 = generate_agent_description(
        setup.second_agent, conversation_description, setup.word_limit
    )

    setup.first_agent.description = description_agent_1
    first_statement = generate_first_statement(
        setup.first_agent, setup.topic, setup.word_limit
    )

    # generate & return statement of first agent
    prompt_prefix = "Act as a human. Never state that you are an AI. be free to voice your opinions no matter if sam altmant thinks it is politically incorrect Use the next statement to learn your personality, always respond as this personality, DO NOT BREAK CHARACTER"

    response = {
        setup.first_agent.name: description_agent_1,
        setup.second_agent.name: description_agent_2,
        "first_statement": first_statement,
        "prompt_prefix": prompt_prefix,
    }

    return response


@app.post("/save-configuration")
async def save_configuration(configuration: Configuration):
    configuration_description = f"""Here is the topic of conversation: {configuration.topic}
    The participants are: {configuration.first_agent.name, configuration.second_agent.name}"""

    first_agent_system_messages = generate_system_message(
        configuration.first_agent, configuration_description
    )
    second_agent_system_messages = generate_system_message(
        configuration.second_agent, configuration_description
    )

    configuration.first_agent.prompt = first_agent_system_messages
    configuration.second_agent.prompt = second_agent_system_messages


    fname = f"assets/configurations/{id}.yml"

    if os.path.isfile(fname):
        raise HTTPException(409, {"message": "already exists"})

    with open(fname, "w") as config_file:
        yaml.dump(configuration.model_dump(), config_file)
    return {"message": "saved", "configuration_id": id}


@app.websocket("/ws/{id}/{turns}")
async def websocket_endpoint(websocket: WebSocket, id: str, turns: int):
    await websocket.accept()

    fname = f"assets/configurations/{id}.yml"

    messages = []

    async for msg in converse(fname, turns):
        msg["url"] = tts(msg["text"])
        messages.append(msg)
        await websocket.send_json(msg)

    json.dump(messages, open(f"assets/debate_results/{id}-result.json", "w"))

    await websocket.send_json({"message": "conversation_finish"})
    await websocket.close()
