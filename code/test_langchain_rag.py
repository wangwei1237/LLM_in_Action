#encoding: utf-8

"""
@discribe: example for RAG 
@author: wangwei1237@gmail.com
"""

from langchain.chains.qa_with_sources import load_qa_with_sources_chain
from langchain.chat_models import ErnieBotChat
from langchain.embeddings import QianfanEmbeddingsEndpoint
from langchain.vectorstores import Milvus

llm = ErnieBotChat()
chain = load_qa_with_sources_chain(llm=llm, chain_type="refine", return_intermediate_steps=True)

query = "什么是度知了?"
vector_db = Milvus.from_documents(
    [],
    QianfanEmbeddingsEndpoint(),
    connection_args ={"host": "127.0.0.1", "port": "8081"},
)

docs = vector_db.similarity_search(query)
print(len(docs))

res = chain({"input_documents": docs, "question": query}, return_only_outputs=True)
print(res)

