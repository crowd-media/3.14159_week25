import os
import yaml
import json
from typing import List
from uuid import uuid4
import sys
from .helper.config import load_config, save_config, delete_config, update_config

sys.path.append("..")

from dotenv import load_dotenv

from fastapi import FastAPI, WebSocket, HTTPException
from fastapi.middleware.cors import CORSMiddleware


from backend.cli.main import debate
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


# f in chat
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.post("/descriptions")
async def do_setup(setup: SetupConfig):
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


@app.get("/configuration/{id}")
async def get_configuration(id: str):
    return load_config(id)


@app.delete("/configuration/{id}")
async def delete_configuration(id: str):
    delete_config()
    return {"message": "success"}


@app.put("/configuration/{id}")
async def delete_configuration(config: Configuration):
    return update_config(config)


@app.post("/configuration")
async def post_configuration(configuration: Configuration):
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

    save_config(configuration)

    return {"message": "saved", "configuration_id": configuration.id}


@app.websocket("/ws/{id}/{turns}")
async def websocket_endpoint(websocket: WebSocket, id: str, turns: int):
    await websocket.accept()

    messages = []

    async for msg in debate(id, turns):
        msg["url"] = tts(msg["text"])
        messages.append(msg)
        await websocket.send_json(msg)

    json.dump(messages, open(f"assets/debate_results/{id}-result.json", "w"))

    await websocket.send_json({"message": "conversation_finish"})
    await websocket.close()
