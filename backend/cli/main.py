import sys
from time import perf_counter

import yaml


# i hate python
sys.path.append("..")
sys.path.append(".")
sys.path.append("../backend")
sys.path.append("./backend")
sys.path.append("../../backend")

from langchain.agents.agent import AgentFinish
from langchain.llms.openai import OpenAI

from backend.pi.agents import create_agent
from backend.pi.agents import create_prompt
from backend.pi.agents import SharedMemory
from backend.models.models import RunConfig


async def converse(config_path: str):
    print("converse")
    config = yaml.safe_load(open(config_path, "r"))
    config = RunConfig(**config)
    print("config")
    print(config)
    intermediate_steps = []

    # this is shared, since it is a conversation where all participants are
    conversation_memory = SharedMemory(
        llm=OpenAI(model_name="text-davinci-003"),
        memory_key="chat_history",
        return_messages=True,
    )

    prompt_1 = config.debater_prompt_prefix + config.debater_1_prompt
    prompt_2 = config.debater_prompt_prefix + config.debater_2_prompt

    agent_1 = create_agent(
        conversation_memory, agent_id="agent_1", prompt=create_prompt(prompt_1)
    )
    agent_2 = create_agent(
        conversation_memory, agent_id="agent_2", prompt=create_prompt(prompt_2)
    )

    t = perf_counter()
    output = await agent_2.ainvoke(
        {
            "input": config.referee_prompt,
            "intermediate_steps": intermediate_steps,
            "agent_id": "referee",
        }
    )
    yield {"speaker": "referee", "text": config.referee_prompt}
    input_1 = output.return_values["output"]
    yield {"speaker": "agent_2", "text": input_1}
    answers = set()

    answers.add(input_1)

    print("referee question:\n\t", config.referee_prompt, end="\n\n")
    print(f"{perf_counter()-t:.4f}", "juan initial response:\n\t", input_1, end="\n\n")
    t = perf_counter()
    while True:
        agent_1_response = await agent_1.ainvoke(
            {
                "input": input_1,
                "intermediate_steps": intermediate_steps,
                "agent_id": "agent_1",
            }
        )

        if isinstance(agent_1_response, AgentFinish):
            input_2 = agent_1_response.return_values["output"]
            print(
                f"{perf_counter()-t:.4f}", "agent_1 response:\n\t", input_2, end="\n\n"
            )
            yield {"speaker": "agent_1", "text": input_2}
            t = perf_counter()
        else:
            print("agent 1 doing some action, not responding")
            # handle actions
            pass

        if input_2 in answers:
            print("conversation repeated")
            yield {"speaker": "referee", "text": "conversation repeated, stoping"}
            break

        answers.add(input_2)

        agent_2_response = await agent_2.ainvoke(
            {
                "input": input_2,
                "intermediate_steps": intermediate_steps,
                "agent_id": "agent_2",
            }
        )

        if isinstance(agent_2_response, AgentFinish):
            input_1 = agent_2_response.return_values["output"]
            print(
                f"{perf_counter()-t:.4f}", "agent_2 response:\n\t", input_1, end="\n\n"
            )
            yield {"speaker": "agent_2", "text": input_1}
            t = perf_counter()

        else:
            # handle actions
            print("agent 2 doing some action, not responding")
            pass

        if input_1 in answers:
            print("conversation repeated")
            yield {"speaker": "referee", "text": "conversation repeated, stoping"}
            break

        answers.add(input_1)


if __name__ == "__main__":
    config_path = "assets/dinner_time.yaml"
    print("calling converse")
    for msg in converse(config_path):
        print(msg)
    print("called convere")
