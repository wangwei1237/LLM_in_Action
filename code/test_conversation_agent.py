#encoding: utf-8

"""
@discribe: example for conversation agent.
@author: wangwei1237@gmail.com
"""

from langchain.chat_models import ErnieBotChat
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.memory import ConversationBufferMemory        # <1>
from langchain.agents import initialize_agent

memory = ConversationBufferMemory(memory_key="chat_history") # <2>

llm = ErnieBotChat()
llm_math = LLMMathChain(llm=llm)

template = ChatPromptTemplate.from_messages([
    ("user", "你是一个能力非凡的人工智能机器人。"),
    ("assistant", "你好~"),
    ("user", "{user_input}"),
])
llm_chain = LLMChain(llm=llm, prompt=template)

# initialize the math tool
math_tool = Tool(
    name='Calculator',
    func=llm_math.run,
    description='Useful for when you need to answer questions about math.'
)

# initialize the general LLM tool
llm_tool = Tool(
    name='Language Model',
    func=llm_chain.run,
    description='Use this tool for general purpose queries.'
)

# when giving tools to LLM, we must pass as list of tools
tools = [math_tool, llm_tool]

conversation_agent = initialize_agent(
    agent="conversational-react-description",     # <3>
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
    memory=memory                                 # <4>
)

res = conversation_agent("1768年，中国有什么重大事件发生？")
print(res)

res = conversation_agent("同年，其他国家有什么重大事件发生？")
print(res)