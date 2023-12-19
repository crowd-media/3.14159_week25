from typing import Any
from typing import Dict
from typing import List
from operator import itemgetter

from dotenv import load_dotenv

from langchain.agents import tool
from langchain.agents.agent import AgentFinish
from langchain.agents.format_scratchpad import format_to_openai_function_messages
from langchain.agents.output_parsers import OpenAIFunctionsAgentOutputParser
from langchain.chat_models import ChatOpenAI
from langchain.memory import ConversationSummaryBufferMemory
from langchain.prompts import ChatPromptTemplate
from langchain.prompts import MessagesPlaceholder
from langchain.prompts import MessagesPlaceholder
from langchain.tools.render import format_tool_to_openai_function

from langchain_core.messages import AIMessage
from langchain_core.messages import HumanMessage
from langchain_core.messages import SystemMessage
from langchain_core.runnables import RunnableLambda
from langchain_core.runnables import RunnablePassthrough
from langchain_core.runnables import RunnableSequence


load_dotenv()

llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)


@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)


# can add more tools here, they will be available to the agent
tools = [get_word_length]

tool_dict = {f.name: f for f in tools}

MEMORY_KEY = "chat_history"
AGENT_SCRATCHPAD_KEY = "agent_scratchpad"


def create_prompt(sys_prompt: str):
    return ChatPromptTemplate.from_messages(
        [
            (
                "system",
                sys_prompt,
            ),
            MessagesPlaceholder(variable_name=MEMORY_KEY),
            ("user", "{input}"),
            MessagesPlaceholder(variable_name=AGENT_SCRATCHPAD_KEY),
        ]
    )


llm_with_tools = llm.bind(functions=[format_tool_to_openai_function(t) for t in tools])


class AiMessageWithID(AIMessage):
    agent_id: str


class SharedMemory(ConversationSummaryBufferMemory):
    def load_memory_variables(self, inputs: Dict[str, Any]) -> Dict[str, Any]:
        """Converts a list of messages with id to the point of view of the
        current agent.
        """
        mssages_with_id: List[AiMessageWithID] = super().load_memory_variables(inputs)[
            MEMORY_KEY
        ]

        adjusted_messages_by_id = []

        for msg in mssages_with_id:
            if isinstance(msg, SystemMessage):
                adjusted_messages_by_id.append(msg)
                continue
            if msg.agent_id == inputs.get("agent_id"):
                adjusted_messages_by_id.append(HumanMessage(content=msg.content))
            else:
                adjusted_messages_by_id.append(AIMessage(content=msg.content))

        return {MEMORY_KEY: adjusted_messages_by_id}

    def save_messsage_with_id(self, message: str, agent_id: str):
        message = AiMessageWithID(content=message, agent_id=agent_id)
        self.chat_memory.add_message(message)

        self.prune()


def handleAgentOutput(agent_id: str, memory: SharedMemory):
    def _handle(output):
        if isinstance(output, AgentFinish):
            memory.save_messsage_with_id(output.return_values["output"], agent_id)
            return output
        else:
            return {
                "tool": output.tool,
                "tool_input": output.tool_input,
            }

    return _handle


def create_agent(memory: SharedMemory, agent_id: str, prompt) -> RunnableSequence:
    agent: RunnableSequence
    # memory_saver = MemorySaver(memory=memory)
    agent = (
        RunnablePassthrough.assign(
            chat_history=RunnableLambda(memory.load_memory_variables)
            | itemgetter(MEMORY_KEY)
        )
        | {
            "input": lambda x: x["input"],
            AGENT_SCRATCHPAD_KEY: lambda x: format_to_openai_function_messages(
                x["intermediate_steps"]
            ),
            MEMORY_KEY: lambda x: x[MEMORY_KEY],
            "_": lambda x: memory.save_messsage_with_id(x["input"], x["agent_id"]),
        }
        | prompt
        | llm_with_tools
        | OpenAIFunctionsAgentOutputParser()
        | handleAgentOutput(agent_id, memory)
    )
    return agent
