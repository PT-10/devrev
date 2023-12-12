from schema import agent_system
from utils import CoT_Prompting
from schema import tool_info


def reset_history(tool_info):
    global history_openai_format
    global agent_system
    history_openai_format = [{
        'role': 'system',
        'content': agent_system
    }]
    agent_system = f"""
You are a function calling agent.You will be given a query.\
If the query is not relevant to the tools, return an empty python list.\
You have to think step by step five times to answer the queries.\ 

The functions are given below in JSON format.\

{tool_info}
"""


def predict(message, history):
    history_openai_format = [{
        'role': 'system',
                'content': agent_system
    }]
    for human, assistant in history:
        history_openai_format.append(
            {
                "role": "user",
                "content": human
            }
        )

        history_openai_format.append(
            {
                "role": "assistant",
                "content": assistant
            }
        )

    history_openai_format.append(
        {
            "role": "user",
            "content": message
        }
    )
    response = CoT_Prompting(history_openai_format)

    partial_message = ""
    for chunk in response:
        if chunk is not None:
            partial_message = partial_message + \
                chunk
            yield partial_message
