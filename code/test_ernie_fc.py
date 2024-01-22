# !/usr/bin/env python3
"""
@discribe: demo for the Ernie-Bot-4 Function Calling.
@author: wangwei1237@gmail.com
"""

import json

from langchain.chains import LLMChain
from langchain.chains.ernie_functions import (
    create_ernie_fn_chain,
)
from langchain.chat_models import ErnieBotChat
from langchain.prompts.chat import (
    ChatPromptTemplate,
)

from utils.call_function import call_function

def get_current_news(location: str) -> str:
    """Get the current news based on the location.'

    Args:
        location (str): The location to query.
    
    Returs:
        str: Current news based on the location.
    """

    news_info = {
        "location": location,
        "news": [
            "I have a Book.",
            "It's a nice day, today."
        ]
    }

    return json.dumps(news_info)

def get_current_weather(location: str, unit: str="celsius") -> str:
    """Get the current weather in a given location

    Args:
        location (str): location of the weather.
        unit (str): unit of the tempuature.
    
    Returns:
        str: weather in the given location.
    """

    weather_info = {
        "location": location,
        "temperature": "27",
        "unit": unit,
        "forecast": ["sunny", "windy"],
    }
    return json.dumps(weather_info)

llm = ErnieBotChat(model_name="ERNIE-Bot-4")

prompt = ChatPromptTemplate.from_messages(
    [
        ("human", "{query}"),
    ]
)
chain = create_ernie_fn_chain([get_current_weather, get_current_news], llm, prompt, verbose=True)
res = chain.run("北京今天的新闻是什么？")

if res:
    res_cf = call_function([get_current_news, get_current_weather], res)
    prompt_2 = ChatPromptTemplate.from_messages(
        [
            ("human", "从 {function} 中，我们得到如下信息：{function_res}，那么 {query}"),
        ]
    )
    chain_2 = LLMChain(llm=llm, prompt=prompt_2, verbose=True)
    res_2 = chain_2.run(function=res["name"], function_res=res_cf, query="北京今天的新闻是什么？")
    print(res_2)

