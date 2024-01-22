#encoding: utf-8

"""
@discribe: example for docstore agent.
@author: wangwei1237@gmail.com
"""

from langchain_community.chat_models import QianfanChatEndpoint
from langchain_core.prompts import PromptTemplate
from langchain.agents import Tool
from langchain_community.tools.wikipedia.tool import WikipediaQueryRun
from langchain_community.utilities.wikipedia import WikipediaAPIWrapper
from langchain.agents import AgentExecutor, create_react_agent

llm = QianfanChatEndpoint(model="ERNIE-Bot-4")
wikipedia = WikipediaQueryRun(api_wrapper=WikipediaAPIWrapper())

# initialize the docstore search tool
search_tool = Tool(
    name="Search Engine Tool",
    func=wikipedia.run,
    description='search wikipedia'
)

# when giving tools to LLM, we must pass as list of tools
tools = [search_tool] #<1>

# get the prompt template string from: 
# https://smith.langchain.com/hub/hwchase17/react?organizationId=c4887cc4-1275-5361-82f2-b22aee75bad1
prompt_template = """..."""   #<2>

prompt = PromptTemplate.from_template(prompt_template)

docstore_agent = create_react_agent(
    llm=llm,
    tools=tools,
    prompt=prompt,
)

agent_executor = AgentExecutor(agent=docstore_agent, tools=tools, verbose=True)
res = agent_executor.invoke({"input": "What were Archimedes' last words?"})
print(res)