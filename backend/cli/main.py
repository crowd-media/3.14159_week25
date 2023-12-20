import sys
from time import perf_counter

import yaml

# i hate python
sys.path.append("..")
sys.path.append(".")
sys.path.append("../backend")
sys.path.append("./backend")
sys.path.append("../../backend")

from dotenv import load_dotenv  


from langchain.agents.agent import AgentFinish
from langchain.llms.openai import OpenAI

from backend.pi.agents import create_agent
from backend.pi.agents import create_referee
from backend.pi.agents import MEMORY_KEY
from backend.pi.agents import create_prompt
from backend.pi.agents import MemoryWithId
from backend.models.models import RunConfig

load_dotenv()

async def converse(config_path: str):
    config = yaml.safe_load(open(config_path, "r"))
    config = RunConfig(**config)

    intermediate_steps = []

    # this is shared, since it is a conversation where all participants are
    conversation_memory_1 = MemoryWithId(
        llm=OpenAI(model_name="text-davinci-003"),
        memory_key="chat_history",
        return_messages=True,
    )

    conversation_memory_2 = MemoryWithId(
        llm=OpenAI(model_name="text-davinci-003"),
        memory_key="chat_history",
        return_messages=True,
    )

    prompt_1 = config.debater_prompt_prefix + config.debater_1_prompt
    prompt_2 = config.debater_prompt_prefix + config.debater_2_prompt

    agent_1 = create_agent(
        conversation_memory_1, agent_id="agent_1", prompt=create_prompt(prompt_1)
    )
    agent_2 = create_agent(
        conversation_memory_2, agent_id="agent_2", prompt=create_prompt(prompt_2)
    )

    # Agent 1 starts. we save it to both memory objects
    yield {"speaker": "agent_1", "text": config.referee_prompt}
    conversation_memory_1.chat_memory.add_ai_message(config.referee_prompt)
    conversation_memory_2.chat_memory.add_user_message(config.referee_prompt)

    # agent 1 "asks" agent 2
    output = await agent_2.ainvoke(
        {
            "input": config.referee_prompt,
            "intermediate_steps": intermediate_steps,
            "agent_id": "agent_2", 
        }
    )
    input_for_agent_1 = output.return_values["output"]

    yield {"speaker": "agent_2", "text": input_for_agent_1}
    # save agent 2 response in agent 1 memory
    conversation_memory_1.chat_memory.add_user_message(input_for_agent_1)

    # TODO: delete
    answers = set()

    answers.add(input_for_agent_1)

    i = 0
    while i < 6:
        i += 1
        agent_1_response = await agent_1.ainvoke(
            {
                "input": input_for_agent_1,
                "intermediate_steps": intermediate_steps,
                "agent_id": "agent_1",
            }
        )

        if isinstance(agent_1_response, AgentFinish):
            input_for_agent_2 = agent_1_response.return_values["output"]
            conversation_memory_2.chat_memory.add_user_message(input_for_agent_2)

            # print(
            #     f"{perf_counter()-t:.4f}", "agent_1 response:\n\t", input_for_agent_2, end="\n\n"
            # )
            yield {"speaker": "agent_1", "text": input_for_agent_2}
            t = perf_counter()
        else:
            print("agent 1 doing some action, not responding")
            # handle actions
            pass

        answers.add(input_for_agent_2)

        agent_2_response = await agent_2.ainvoke(
            {
                "input": input_for_agent_2,
                "intermediate_steps": intermediate_steps,
                "agent_id": "agent_2",
            }
        )

        if isinstance(agent_2_response, AgentFinish):
            input_for_agent_1 = agent_2_response.return_values["output"]
            conversation_memory_1.chat_memory.add_user_message(input_for_agent_1)

            # print(
            #     f"{perf_counter()-t:.4f}", "agent_2 response:\n\t", input_for_agent_1, end="\n\n"
            # )
            yield {"speaker": "agent_2", "text": input_for_agent_1}
            t = perf_counter()

        else:
            # handle actions
            print("agent 2 doing some action, not responding")
            pass

        if input_for_agent_1 in answers:
            print("conversation repeated")
            yield {"speaker": "referee", "text": "conversation repeated, stoping"}
            break

        answers.add(input_for_agent_1)

    # conv finished, referee evaluation
    referee = create_referee()
    evaluation = await referee.ainvoke(
        {MEMORY_KEY: conversation_memory_1.load_memory_for_refereee()}
    )
    yield {"speaker": "referee", "text": evaluation}


# need to asyncio this main to use cli
if __name__ == "__main__":
    import asyncio

    async def do():
        config_path = "assets/configurations/aliens.yaml"
        print("calling converse")
        async for msg in converse(config_path):
            # print(msg)
            print("\n\n\n\n")

    asyncio.run(do())
