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
from backend.models.models import RunConfig, SetupConfig

from backend.api.helper.agent import generate_agent_description, generate_system_message
from backend.models.models import Agent, SaveAgents

from backend.pi.tts import tts

load_dotenv()

app = FastAPI(
    title="El Debate API",
    description="An API for the El Debate project",
    version="0.0.0 (leets keep it this way forever)",
)


@app.get('/descriptions')
async def topic(setup: SetupConfig):

    conversation_description = f"""Here is the topic of conversation: {topic}
    The participants are: {setup.first_agent}, {setup.second_agent} """

    description_agent_1 = generate_agent_description(setup.first_agent, conversation_description, setup.word_limit)
    description_agent_2 = generate_agent_description(setup.second_agent, conversation_description, setup.word_limit)

    response = {
        setup.first_agent.name: description_agent_1,
        setup.second_agent.name: description_agent_2
    }
    
    return response


@app.post('/save-agents')
async def topic(saveAgents: SaveAgents):

    conversation_description = f"""Here is the topic of conversation: {saveAgents.topic}
    The participants are: {saveAgents.first_agent.name, saveAgents.second_agent.name}"""

    first_agent_system_messages = generate_system_message(saveAgents.first_agent, conversation_description)
    second_agent_system_messages = generate_system_message(saveAgents.second_agent, conversation_description)

    conversation_id = uuid4().__str__()

    fname = f"assets/configurations/{conversation_id}.yml"

    if os.path.isfile(fname):
        raise HTTPException(409, {"message": "already exists"})
    
    with open(fname, "w") as config_file:
        yaml.dump(saveAgents.model_dump(), config_file)
    return {"message": "saved", "conversation_id": conversation_id}


@app.put("/config")
async def config(body: RunConfig):
    """Rewrites a config file"""
    fname = f"assets/configurations/{body.config_id}.yaml"
    if os.path.isfile(fname):
        with open(fname, "w") as config_file:
            yaml.dump(body.model_dump(), config_file)
        return {"message": "saved"}
    raise HTTPException(404, {"message": "not found"})


@app.get("/config")
async def config() -> List[str]:
    return os.listdir("assets/configurations")


@app.get("/config/{config_id}")
async def config(config_id: str) -> RunConfig:
    fname = f"assets/configurations/{config_id}.yaml"
    if os.path.isfile(fname):
        with open(fname, "r") as config_file:
            return yaml.safe_load(config_file)
    raise HTTPException(404, {"message": "not found"})


@app.delete("/config/{config_id}")
async def config(config_id: str):
    fname = f"assets/configurations/{config_id}.yaml"
    if os.path.isfile(fname):
        os.remove(fname)
        return {"message": "deleted"}
    raise HTTPException(404, {"message": "not found"})


@app.websocket("/ws/{conversation_id}")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    conversation_id = await websocket.receive_text()
    fname = f"assets/configurations/{conversation_id}.yaml"

    messages = []

    async for msg in converse(fname):
        msg["url"] = tts(msg['text'])
        messages.append(msg)
        await websocket.send_json(msg)

    conv_id = uuid4().__str__()
    json.dump(messages, open(f"assets/debate_results/{conv_id}.json", "w"))

    await websocket.send_json({"message": "conversation_finish", "id": conv_id})
    await websocket.close()
