from langchain.chat_models import ChatOpenAI
from langchain.schema import (
    HumanMessage,
    SystemMessage,
)
from backend.models.models import Agent

def generate_first_statement(agent: Agent, topic: str, word_limit: int, ) ->str:
    message = HumanMessage(
            content=f"""
            
            You are {agent.name}
            You are described as {agent.description}
            You want to start a discussion about {topic} 
            Please reply with a statement about the topic that can be discussed
            You need to choose a side
            Do not excede {word_limit} words.
            """
        ),
    
    resp = generate_from_prompt(message, 1.0)
    return resp


def generate_agent_description(agent: Agent, conversation_description, word_limit,) -> str:

    agent_descriptor_system_message = SystemMessage(
    content="You can add detail to the description of the conversation participant."
    )

    agent_specifier_prompt = [
        agent_descriptor_system_message,
        HumanMessage(
            content=f"""{conversation_description}
            Please reply with a creative description of {agent.name}, in {word_limit} words or less
            while taking into account the following characteristics {agent.characteristics}. 
            Speak directly to {agent.name}.
            Give them a point of view.
            Do not add anything else."""
        ),
    ]

    resp = generate_from_prompt(agent_specifier_prompt, 1.0)
    return resp

def generate_from_prompt(prompt, temperature):
    response = ChatOpenAI(temperature=temperature)(prompt).content
    return response

def generate_system_message(agent: Agent, conversation_description):
    return f"""{conversation_description}
    
    Your name is {agent.name}.

    Your description is as follows: {agent.description}

    Your goal is to persuade your conversation partner of your point of view.
    """