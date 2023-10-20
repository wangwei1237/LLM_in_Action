#encoding: utf-8

"""
@discribe: example for Ernie's calculate ability. 
@author: wangwei1237@gmail.com
"""

from langchain.chat_models import ErnieBotChat
from langchain.prompts import ChatPromptTemplate
from langchain.chains import LLMChain

template = ChatPromptTemplate.from_messages([
    ("user", "你是一个能力非凡的人工智能机器人"),
    ("assistant", "你好~"),
    ("user", "{user_input}"),
])

chat = ErnieBotChat()
chain =  LLMChain(llm=chat, prompt=template)
res =  chain.run(user_input="4.1*7.9=?")
print(res)