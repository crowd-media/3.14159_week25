import os
from typing import List
from fastapi import FastAPI, WebSocket, HTTPException
import yaml

import sys

sys.path.append("..")
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
    fname = f"assets/{body.config_id}.yaml"

    if os.path.isfile(fname):
        raise HTTPException(409, {"message": "already exists"})

    with open(fname, "w") as config_file:
        yaml.dump(body.model_dump(), config_file)
    return {"message": "saved"}


@app.put("/config")
async def config(body: RunConfig):
    """Rewrites a config file"""
    fname = f"assets/{body.config_id}.yaml"
    if os.path.isfile(fname):
        with open(fname, "w") as config_file:
            yaml.dump(body.model_dump(), config_file)
        return {"message": "saved"}
    raise HTTPException(404, {"message": "not found"})


@app.get("/config")
async def config() -> List[str]:
    return os.listdir("assets")


@app.get("/config/{config_id}")
async def config(config_id: str)-> RunConfig:
    fname = f"assets/{config_id}.yaml"
    if os.path.isfile(fname):
        with open(fname, "r") as config_file:
            return yaml.safe_load(config_file)
    raise HTTPException(404, {"message": "not found"})


@app.delete("/config/{config_id}")
async def config(config_id: str):
    fname = f"assets/{config_id}.yaml"
    if os.path.isfile(fname):
        os.remove(fname)
        return {"message": "deleted"}
    raise HTTPException(404, {"message": "not found"})


@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()

    conversation_id = await websocket.receive_text()
    fname = f"assets/{conversation_id}.yaml"

    async for msg in converse(fname):
        await websocket.send_json(msg)

    await websocket.close()
