"""
@discribe: Semantic Kernel Planner.
@author: wangwei1237@gmail.com
"""

import asyncio
import semantic_kernel as sk
from plugins.Math import MathPlugin
from semantic_kernel.connectors.ai.open_ai import OpenAIChatCompletion
from semantic_kernel.planning.sequential_planner import SequentialPlanner

kernel = sk.Kernel()

api_key, org_id = sk.openai_settings_from_dot_env()
kernel.add_chat_service("chat-gpt", 
                        OpenAIChatCompletion(ai_model_id="gpt-3.5-turbo", 
                                             api_key=api_key))

math_plugins = kernel.import_skill(MathPlugin(), "MathPlugin")  #<1>
planner = SequentialPlanner(kernel) #<2>

ask = "If my investment of 2130.23 dollars increased by 23%, how much would I have after I spent $5 on a latte?"
plan = asyncio.run(planner.create_plan_async(ask)) #<3>
result = plan.invoke() #<4>