"""
@discribe: Semantic Kernel Function.
@author: wangwei1237@gmail.com
"""

import semantic_kernel as sk
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
import asyncio

topic = input("Your Request: ")
prompt = f"写一首包含 {topic} 的藏头诗"  #<1>

kernel = sk.Kernel()  #<2>

api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_text_completion_service("chat-gpt", 
                                   OpenAIChatCompletion(ai_model_id="gpt-3.5-turbo", 
                                                        api_key=api_key))  #<3>

semantic_function = kernel.create_semantic_function(prompt) #<4>
result = asyncio.run(kernel.run_async(semantic_function))
print(result)

