#encoding: utf-8

"""
@discribe: example for conversation agent.
@author: wangwei1237@gmail.com
"""

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts.chat import ChatPromptTemplate
from langchain_core.prompts import PromptTemplate
from langchain.chains import LLMChain
from langchain.chains import LLMMathChain
from langchain.agents import Tool
from langchain.agents import AgentExecutor, create_react_agent

llm = QianfanChatEndpoint(model="ERNIE-Bot-4")

llm_math = LLMMathChain.from_llm(llm)

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

# get the prompt template string from: 
# https://smith.langchain.com/hub/hwchase17/react-chat?organizationId=c4887cc4-1275-5361-82f2-b22aee75bad1
prompt_template = """..."""   #<1>

prompt = PromptTemplate.from_template(prompt_template)

conversation_agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

history = ["Human: 今年是哪一年？，AI: 今年是 1768。"] #<2>
querys = [
    "这一年，中国有什么重大事件发生？",
    "同年，其他国家有什么重大事件发生？",
]

agent_executor = AgentExecutor(agent=conversation_agent, tools=tools, verbose=True)

for query in querys:
    try:
        res = agent_executor.invoke({"input": query, "chat_history": "\n" . join(history)}) #<3>
    except Exception as e:
        res = {}

    history.append("Human: " + query + "\nAI: " + res.get("output", ""))

    print(res)