#encoding: utf-8

"""
@discribe: example for docstore agent.
@author: wangwei1237@gmail.com
"""

from langchain.chat_models import ErnieBotChat
from langchain.agents import Tool
from langchain import Wikipedia
from langchain.agents.react.base import DocstoreExplorer
from langchain.agents import initialize_agent

docstore=DocstoreExplorer(Wikipedia())

# initialize the docstore search tool
search_tool = Tool(
    name="Search",
    func=docstore.search,
    description='search wikipedia'
)

# intialize the docstore lookup tool
lookup_tool = Tool(
    name="Lookup",
    func=docstore.lookup,
    description='lookup a term in wikipedia'
)

# when giving tools to LLM, we must pass as list of tools
tools = [search_tool, lookup_tool]  # <1>


llm = ErnieBotChat()
docstore_agent = initialize_agent(
    agent="react-docstore",
    tools=tools,
    llm=llm,
    verbose=True,
    max_iterations=3,
)

docstore_agent("What were Archimedes' last words?")