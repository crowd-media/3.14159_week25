import os
import yaml
import json
from typing import List
from uuid import uuid4
import sys

sys.path.append("..")

from fastapi import FastAPI, WebSocket, HTTPException


from backend.cli.main import converse
from backend.models.models import RunConfig


app = FastAPI(
    title="El Debate API",
    description="An API for the El Debate project",
    version="0.0.0 (leets keep it this way forever)",
)


@app.post("/config")
async def config(body: RunConfig):
    """saves a config to a file"""
    fname = f"assets/configurations/{body.config_id}.yaml"

    if os.path.isfile(fname):
        raise HTTPException(409, {"message": "already exists"})

    with open(fname, "w") as config_file:
        yaml.dump(body.model_dump(), config_file)
    return {"message": "saved"}


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


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    conversation_id = await websocket.receive_text()
    fname = f"assets/conversations/{conversation_id}.yaml"

    messages = []

    async for msg in converse(fname):
        messages.append(msg)
        await websocket.send_json(msg)

    conv_id = uuid4().__str__()
    json.dump(messages, open(f"assets/{conv_id}.json", "w"))

    await websocket.send_json({"message": "conversation_finish", "id": conv_id})
    await websocket.close()
