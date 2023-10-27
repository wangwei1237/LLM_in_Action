#encoding: utf-8

"""
@discribe: demo for the embedding visualization.
@author: wangwei1237@gmail.com
"""

import matplotlib.pyplot as plt
import numpy as np
from pymilvus import connections
from pymilvus import Collection
from sklearn.manifold import TSNE

connections.connect(
  host='127.0.0.1',
  port='8081'
)  # <1>

collection = Collection("LangChainCollection") # <2>

res = collection.query(
  expr = "pk >= 0",
  offset = 0,
  limit = 500, 
  output_fields = ["vector", "text", "source", "title"],
) # <3>

vector_list = [i["vector"] for i in res] # <4>

matrix = np.array(vector_list) # <5>

tsne = TSNE(n_components=2, perplexity=15, random_state=42, init='random', learning_rate=200)
vis_dims = tsne.fit_transform(matrix) # <6>

plt.scatter(vis_dims[:, 0], vis_dims[:, 1]) # <7>
plt.title("embedding visualized using t-SNE")
plt.show()
