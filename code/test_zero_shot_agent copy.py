#encoding: utf-8

"""
@discribe: example for zero shot agent.
@author: wangwei1237@gmail.com
"""

from langchain.chat_models import ErnieBotChat
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.agents import initialize_agent

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
    description='use this tool for general purpose queries.'
)

# when giving tools to LLM, we must pass as list of tools
tools = [math_tool, llm_tool]

zero_shot_agent = initialize_agent(
    agent="zero-shot-react-description",
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3
)

res = zero_shot_agent("what's 4.1*7.9=?")
print(res)