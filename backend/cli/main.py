from langchain.agents.agent import AgentFinish
from time import sleep

# import the backend.pi.agents

import sys

# i hate python
sys.path.append("..")

from backend.pi.agents import create_agent


agent1 = create_agent()
agent2 = create_agent()

agent1_history = []
agent2_history = []

intermediate_steps = []

input_ini = "lets have a friendly discussion!"

output = agent2.invoke(
    {
        "input": input_ini,
        "chat_history": agent2_history,
        "intermediate_steps": intermediate_steps,
    }
)

input_1 = output.return_values["output"]

while True:
    agent_1_response = agent1.invoke(
        {
            "input": input_1,
            "chat_history": agent1_history,
            "intermediate_steps": intermediate_steps,
        }
    )

    if isinstance(agent_1_response, AgentFinish):
        input_2 = agent_1_response.return_values["output"]
        print("agent 1 response", agent_1_response)
        print(input_2)
    else:
        print("agent 1 doing some action, not responding")
        # handle actions
        pass

    agent_2_response = agent2.invoke(
        {
            "input": input_2,
            "chat_history": agent2_history,
            "intermediate_steps": intermediate_steps,
        }
    )

    if isinstance(agent_2_response, AgentFinish):
        input_1 = agent_2_response.return_values["output"]
        print("agent 2 response", agent_2_response)
        print(input_2)
    else:
        # handle actions
        print("agent 2 doing some action, not responding")
        pass

    print(input_1)

    sleep(5)
