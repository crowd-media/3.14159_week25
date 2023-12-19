from dotenv import load_dotenv
from langchain.agents.agent import AgentFinish

from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.tools.render import format_tool_to_openai_function
from langchain.chat_models import ChatOpenAI
from langchain.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.agents import tool
from langchain.prompts import MessagesPlaceholder
from langchain_core.messages import AIMessage, HumanMessage
from langchain.agents import AgentExecutor
from langchain.memory import ConversationBufferMemory

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)


# @tool
# def listen_adversary():
#     """Returns the adversary answer. Always listen to the adversary."""
#     message = input("Please enter a response: ")
#     return message


tools = [get_word_length]
tool_dict = {t.name: t for t in tools}
# print(tool_dict)

chat_history = []

MEMORY_KEY = "chat_history"
AGENT_SCRATCHPAD_KEY = "agent_scratchpad"
prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            # "You are very powerful assistant, but bad at calculating lengths of words.",
            """You are an amazing debater.

            You use short sentences always, not exceeding 50 words.

            Counterargument whatever is thrown to you.

            Use the tool listen_adversary to listen to my arguments
            
            You should always listen to the adversart. Your preferred action is to
            call `listen_adversary`
            """,
        ),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name=AGENT_SCRATCHPAD_KEY),
    ]
)

llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])


def create_agent_executor(agent):
    memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
    return AgentExecutor(agent=agent, tools=tools, verbose=True, memory=memory, max_execution_time=60, max_iterations=50)

def create_agent():
    agent = (
        {
            "input": lambda x: x["input"],
            AGENT_SCRATCHPAD_KEY: lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            )
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
    )

    agent_executor = create_agent_executor(agent)
    return agent_executor

# def agent_executor():
    # memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
# 

