"""
@discribe: functions description.
@author: wangwei1237@gmail.com
"""

functions = [
    {
        "name": "get_current_news",
        "description": "Get the current news based on the location.",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
            },
            "required": ["location"],
        },
        "responses": {
            "type": "object",
            "properties": {
                "news": {
                    "type": "string",
                    "description": "The current news based on the location.",
                }
            }
        }
    },
    {
        "name": "get_current_weather",
        "description": "Get the current weather in a given location",
        "parameters": {
            "type": "object",
            "properties": {
                "location": {
                    "type": "string",
                    "description": "The city and state, e.g. San Francisco, CA",
                },
                "unit": {"type": "string", "enum": ["celsius", "fahrenheit"]},
            },
            "required": ["location"],
        },
        "responses": {
            "type": "object",
            "properties": {
                "temperature": {
                    "type": "string",
                    "description": "The temperature in the given location.",
                }
            }
        }
    },
]