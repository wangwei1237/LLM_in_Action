"""
@discribe: demo for the QianfanChatEndpoint.
@author: wangwei1237@gmail.com
"""

from langchain_community.chat_models import QianfanChatEndpoint
from langchain.chains import LLMChain
from langchain_core.prompts.chat import ChatPromptTemplate

system = "你是一个能力很强的机器人，你的名字叫 小叮当。"
prompt = ChatPromptTemplate.from_messages(
    [
        ('system', system),
        ("human", "{query}"),
    ]
)
llm = QianfanChatEndpoint(model="ERNIE-Bot-4")
chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
res = chain.invoke(input={"query": "你是谁？"})
print(res)