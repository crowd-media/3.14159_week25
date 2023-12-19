import sys

# i hate python
sys.path.append("..")

from langchain.agents.agent import AgentFinish
from langchain.llms.openai import OpenAI

from backend.pi.agents import create_agent
from backend.pi.agents import create_prompt
from backend.pi.agents import SharedMemory


intermediate_steps = []

# this is shared, since it is a conversation where all participants are
conversation_memory = SharedMemory(
    llm=OpenAI(model_name="text-davinci-003"),
    memory_key="chat_history",
    return_messages=True,
)


prompt_1 = "Answer in less than 50 words at a time. You hate inequality. You love all lifeforms equally, even if it is a tree compared to a human"
prompt_2 = "Answer in less than 50 words at a time. You always invite woman for dinner. You pay for them. you do not pay dinner if it is for another man."

agent_1 = create_agent(
    conversation_memory, agent_id="agent_1", prompt=create_prompt(prompt_1)
)
agent_2 = create_agent(
    conversation_memory, agent_id="agent_2", prompt=create_prompt(prompt_2)
)


input_ini = "Hi, let's start the debate. Do you think woman should pay for dinner?"

output = agent_2.invoke(
    {
        "input": input_ini,
        "intermediate_steps": intermediate_steps,
        "agent_id": "referee",
    }
)

input_1 = output.return_values["output"]

print("referee question:\n\t", input_ini, end="\n\n")
print("agent 2 response:\n\t", input_1, end="\n\n")

while True:
    agent_1_response = agent_1.invoke(
        {
            "input": input_1,
            "intermediate_steps": intermediate_steps,
            "agent_id": "agent_1",
        }
    )

    if isinstance(agent_1_response, AgentFinish):
        input_2 = agent_1_response.return_values["output"]
        print("agent 1 response:\n\t", input_2, end="\n\n")
    else:
        print("agent 1 doing some action, not responding")
        # handle actions
        pass

    agent_2_response = agent_2.invoke(
        {
            "input": input_2,
            "intermediate_steps": intermediate_steps,
            "agent_id": "agent_2",
        }
    )

    if isinstance(agent_2_response, AgentFinish):
        input_1 = agent_2_response.return_values["output"]
        print("agent 2 response:\n\t", input_1, end="\n\n")

    else:
        # handle actions
        print("agent 2 doing some action, not responding")
        pass
