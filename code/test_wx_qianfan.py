"""
@discribe: demo for the ErnieBotChat.
@author: wangwei1237@gmail.com
"""

from langchain.chains import LLMChain
from langchain.chat_models import ErnieBotChat
from langchain.prompts import ChatPromptTemplate

system = "你是一个能力很强的机器人，你的名字叫 小叮当。"
prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{query}"),
    ]
)
llm = ErnieBotChat(model_name="ERNIE-Bot-4", system=system)
chain = LLMChain(llm=llm, prompt=prompt, verbose=True)
res = chain.run(query="你是谁？")
print(res)