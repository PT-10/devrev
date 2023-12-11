from schema import agent_system
from utils import get_completion_from_messages
import gradio as gr

def predict(message, history):
    history_openai_format = [{
                'role': 'user', 
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

    response = get_completion_from_messages(history_openai_format)

    partial_message = ""
    for chunk in response:
        print(dir(chunk.choices[0].delta))
        if chunk.choices[0].delta.content is not None:
            partial_message = partial_message + \
                chunk.choices[0].delta.content
            yield partial_message


gr.ChatInterface(predict).queue().launch()
