#encoding: utf-8

"""
@discribe: example for chat conversation agent.
@author: wangwei1237@gmail.com
"""

from langchain.chat_models import ErnieBotChat
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory
from langchain.agents import initialize_agent

memory = ConversationBufferMemory(memory_key="chat_history")

llm = ErnieBotChat(model_name="ERNIE-Bot-4")

# initialize the math tool
llm_math = LLMMathChain(llm=llm)
math_tool = Tool(
    name='Calculator',
    func=llm_math.run,
    description='Useful for when you need to answer questions about math.'
)

# when giving tools to LLM, we must pass as list of tools
tools = [math_tool]

chat_conversation_agent = initialize_agent(
    agent="chat-conversational-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    memory=memory
)

chat_conversation_agent("4.1*7.9=?")
chat_conversation_agent("2 * 2")