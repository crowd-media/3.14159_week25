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

load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)

@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)

@tool
def listen_adversary():
    """Returns the adversary answer. Always listen to the adversary."""
    message = input("Please enter a response: ")
    return message




tools = [get_word_length,listen_adversary]
tool_dict = {f.name : f for f in  tools}
# print(tool_dict)
# exit()
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
            """
        ),
        MessagesPlaceholder(variable_name=MEMORY_KEY),
        ("user", "{input}"),
        MessagesPlaceholder(variable_name=AGENT_SCRATCHPAD_KEY),
    ]
)

llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])

agent = (
    {
        "input": lambda x: x["input"],
        AGENT_SCRATCHPAD_KEY: lambda x: format_to_openai_function_messages(
            x["intermediate_steps"]
        ),
        "chat_history": lambda x: x["chat_history"],
    }
    | prompt
    | llm_with_tools
    | OpenAIFunctionsAgentOutputParser()
)

# agent.invoke({"input": "how many letters in the word educa?", "intermediate_steps": []})
# print(a)
user_input = "how many characters in 'world domination'"
user_input = "lets have a friendly discussion!"
intermediate_steps = []
while True:
    output = agent.invoke(
        {
            "input": user_input,
            "intermediate_steps": intermediate_steps, "chat_history": chat_history
        }
    )
    print(type(output))
    print(output)
    if isinstance(output, AgentFinish):
        chat_history.extend(
        [
            HumanMessage(content=user_input),
            AIMessage(content=output.return_values["output"]),
        ]
        )

    user_input = input("Please enter a response: ")
    if user_input == "q":
        break
    continue
    print(output, type(output))
    if isinstance(output, AgentFinish):
        final_result = output.return_values["output"]
        # break
    else:
        print(f"TOOL NAME: {output.tool}")
        print(f"TOOL INPUT: {output.tool_input}")
        tool_to_run = tool_dict.get(output.tool)
        # tool_to_run = listen_adversary
        observation = tool_to_run.run(output.tool_input)
        intermediate_steps.append((output, observation))
print(final_result)