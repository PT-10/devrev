from schema import agent_system
from utils import CoT_Prompting

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
    # print(tool_info)
    # print(history_openai_format)
    partial_message = ""
    for chunk in response:
        if chunk is not None:
            partial_message = partial_message + \
                chunk
            yield partial_message
