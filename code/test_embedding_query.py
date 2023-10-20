#encoding: utf-8

"""
@discribe: example for milvus embedding query
@author: wangwei1237@gmail.com
"""

from langchain.embeddings import QianfanEmbeddingsEndpoint
from langchain.vectorstores import Milvus

vector_db = Milvus.from_documents(
    [],
    QianfanEmbeddingsEndpoint(),
    connection_args ={"host": "127.0.0.1", "port": "8081"},
)

query = "什么是 RD曲线？"
docs = vector_db.similarity_search(query)
print(docs)

