#encoding: utf-8

"""
@discribe: example for struct agent.
@author: wangwei1237@gmail.com
"""

from langchain.agents import AgentExecutor, create_structured_chat_agent
from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts.chat import (
    AIMessage,
    ChatPromptTemplate,
    HumanMessage,
    HumanMessagePromptTemplate,
    MessagesPlaceholder,
    SystemMessagePromptTemplate,
)

from tools import PythagorasTool
from tools import CircumferenceTool

llm = QianfanChatEndpoint(model="ERNIE-Bot-4")

# when giving tools to LLM, we must pass as list of tools
tools = [CircumferenceTool(), PythagorasTool()]

# the prompt template can get from: 
# https://smith.langchain.com/hub/hwchase17/structured-chat-agent?organizationId=c4887cc4-1275-5361-82f2-b22aee75bad1
system_message_template = """..."""
human_message_template = """..."""

messages = [
    SystemMessagePromptTemplate.from_template(system_message_template),
    MessagesPlaceholder(variable_name="chat_history"),
    HumanMessagePromptTemplate.from_template(human_message_template),
]

input_variables = ["tools", "tool_names", "input", "chat_history", "agent_scratchpad"]
prompt = ChatPromptTemplate(input_variables=input_variables, messages=messages)

struct_agent = create_structured_chat_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)


agent_executor = AgentExecutor(agent=struct_agent, tools=tools, verbose=True)

history = []
querys = [
    """If I have a triangle with the opposite side of length 51 and the adjacent side of 40,
    what is the length of the hypotenuse?""",
]

for query in querys:
    try:
        res = agent_executor.invoke({"input": query, "chat_history": history})
    except Exception as e:
        res = {}

    history.append(HumanMessage(content=query))
    history.append(AIMessage(content=res.get("output", "")))
    
    print(res)