#encoding: utf-8

"""
@discribe: example for milvus embedding 
@author: wangwei1237@gmail.com
"""

from langchain.document_loaders import WebBaseLoader
from langchain.document_loaders.recursive_url_loader import RecursiveUrlLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.document_loaders import WebBaseLoader
from langchain.embeddings import QianfanEmbeddingsEndpoint
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.vectorstores import Milvus
import time

URL_ROOT = "https://wangwei1237.github.io/2023/02/13/duzhiliao/"
loader = RecursiveUrlLoader(url=URL_ROOT, max_depth=2)
docs = loader.load()

URLS = []
for doc in docs:
    url   =  doc.metadata["source"]
    URLS.append(url)

print("URLS length: ", len(URLS))

text_splitter = RecursiveCharacterTextSplitter(
    chunk_size = 200,
    chunk_overlap  = 20,
    length_function = len,
    add_start_index = True,
)

for url in URLS:
    print('-------------', url, '----------------')
    loader = WebBaseLoader([url])
    doc = loader.load()
    texts = text_splitter.split_documents(doc)
    vector_db = Milvus.from_documents(
        texts,
        QianfanEmbeddingsEndpoint(),
        connection_args ={"host": "127.0.0.1", "port": "8081"},
    )
    print("    . insert ", len(texts), " texts embeddings successful")
    time.sleep(5)