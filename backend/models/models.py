from pydantic import BaseModel
from typing import List, Optional, Literal

# endpoint receive this
Models = Literal["gpt-4", "gpt-3.5-turbo-1106", "gpt-4-0613", "gpt-4-32k-0613", "text-davinci-003"]

class Agent(BaseModel):
    name: str
    characteristics: Optional[List[str]] = []
    description: Optional[str] = ""
    model: Optional[Models] = ""
    prompt: Optional[str] = ""

class SetupConfig(BaseModel):
    topic: str
    word_limit: int
    first_agent: Agent
    second_agent: Agent

class SaveAgents(BaseModel):
    first_agent: Agent
    second_agent: Agent
    prompt_prefix: str
    first_statement: str

class Configuration(BaseModel):
    id: str
    topic: str
    first_agent: Agent
    second_agent: Agent
    prompt_prefix: str
    first_statement: str