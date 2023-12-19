from pydantic import BaseModel


class RunConfig(BaseModel):
    config_id: str

    debater_prompt_prefix: str
    debater_1_prompt: str
    debater_2_prompt: str

    referee_prompt: str
