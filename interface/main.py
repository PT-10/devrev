from schema import agent_system
from utils import CoT_Prompting
from schema import tool_info


def reset_history(tool_info):
    global agent_system
    agent_system = f"""
You are a function calling agent.You will be given a query.\
When thinking adhere only to the given information and don't make assumptions.\
If the query is not relevant to the tools, give an empty python list.\
You have to think step by step three times to answer the queries.\ 

First,think step by step and decide only about all the necessary functions which the user will need to solve the user query, using the function descriptions.\
when user object references are made, functions that give current user object references will always be considered.\
Whenever me/my/I/mine are used in the <query>, then functions that return ID's should always be thought upon.\
Think once more about the functions choosen and then sequence them accordingly.\

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
    # print(history_openai_format)
    partial_message = ""
    for chunk in response:
        if chunk is not None:
            partial_message = partial_message + \
                chunk
            yield partial_message
