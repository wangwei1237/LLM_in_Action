#encoding: utf-8

"""
@discribe: example for RetrivalQA.
@author: wangwei1237@gmail.com
"""

from langchain.chat_models import ErnieBotChat
from langchain.embeddings import QianfanEmbeddingsEndpoint
from langchain.vectorstores import Milvus
from langchain.chains import RetrievalQA
from langchain.vectorstores.base import VectorStoreRetriever
from retrieval_prompt import PROMPT_SELECTOR

retriever = VectorStoreRetriever(vectorstore=Milvus(embedding_function=QianfanEmbeddingsEndpoint(),
                                                    connection_args={"host": "127.0.0.1", "port": "8081"})) # <1>

llm = ErnieBotChat()
prompt = PROMPT_SELECTOR.get_prompt(llm)  # <2>
retrievalQA = RetrievalQA.from_llm(llm=llm, prompt=prompt, retriever=retriever) # <3>

query = "什么是度知了?"

res = retrievalQA.run(query) # <4>
print(res)
