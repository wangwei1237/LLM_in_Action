# !/usr/bin/env python3
"""
@discribe: The function running for Ernie-Bot-4 Function Calling.
@author: wangwei1237@gmail.com
"""

from typing import (
    Any,
    Callable,
    Dict,
    Sequence,
    Type,
    Union,
)

from langchain.chains.ernie_functions import (
    convert_to_ernie_function,
)
from langchain.pydantic_v1 import BaseModel

from langsmith.run_helpers import traceable

@traceable(run_type="tool")  #<1>
def call_function(functions: Sequence[Union[Dict[str, Any], Type[BaseModel], Callable]],
                  fc_by_llm: dict) -> str:
    """Calling the function and return the result."""
    if not fc_by_llm or "name" not in fc_by_llm or "arguments" not in fc_by_llm:
        return ""
    func_list = [f for f in functions if f.__name__ == fc_by_llm["name"]]
    if len(func_list) != 1:
        return ""
    func = func_list[0]
    func_args_keys = convert_to_ernie_function(func)["parameters"]["properties"].keys()
    fc_args_by_llm = fc_by_llm["arguments"]
    func_args = {
        key: fc_args_by_llm[key] for key in func_args_keys if key in fc_args_by_llm
    }
    res = func(**func_args)
    return res
