import os

import yaml
from models.models import Configuration
from fastapi import HTTPException

config_savespot = os.environ["CONFIG_SAVESPOT"]

def write_config_to_file(path: str, config: Configuration) -> Configuration:
    with open(path, "w") as config_file:
        yaml.dump(config.model_dump(), config_file)
    return config

def load_config(filename: str) -> Configuration:
    path = f"{config_savespot}{filename}.yml"

    if not os.path.exists(path):
        raise HTTPException(409, {"message": "file does not exist or was not found"})

    config = yaml.safe_load(open(path, "r"))
    config = Configuration(**config)

    return config

def save_config(config: Configuration) -> Configuration:
    path = f"{config_savespot}{config.id}.yml"
    
    if os.path.isfile(path):
        raise HTTPException(409, {"message": "already exists"})

    return write_config_to_file(path, config)
    

def delete_config(filename: str) -> None:
    path = f"{config_savespot}{filename}.yml"

    if not os.path.exists(path):
        raise HTTPException(409, {"message": "file does not exist or was not found"})

    os.remove(path)
    return

def update_config(new_config: Configuration) -> Configuration: 
    path = f"{config_savespot}{new_config.id}.yml"

    old_config = load_config(new_config.id)

    for key, value in new_config.model_dump().items():
        if getattr(old_config, key) != value:
            setattr(old_config, key, value)

    return write_config_to_file(path, old_config)

    





        

