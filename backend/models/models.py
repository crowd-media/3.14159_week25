from pydantic import BaseModel
from typing import List, Optional, Literal

class RunConfig(BaseModel):
    config_id: str

    debater_prompt_prefix: str
    debater_1_prompt: str
    debater_2_prompt: str

    referee_prompt: str

Models = Literal["gpt-4", "gpt-3.5-turbo-1106", "gpt-4-0613", "gpt-4-32k-0613"]

class Agent(BaseModel):
    name: str
    characteristics: Optional[List[str]] = []
    description: Optional[str] = ""
    model: Optional[Models] = ""

class SetupConfig(BaseModel):
    topic: str
    word_limit: int
    first_agent: Agent
    second_agent: Agent

class SaveAgents(BaseModel):
    topic: str
    first_agent: Agent
    second_agent: Agent
    prompt_prefix: str
    first_statement: str