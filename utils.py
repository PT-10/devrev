from schema import step_1, step_2, step_3
from openai import OpenAI
from config import key


GPT_model = "gpt-3.5-turbo-1106"
client_1 = OpenAI(
    api_key=key
)


def get_completion_from_messages(messages, model=GPT_model, temperature=0, max_tokens=1000):
    response = client_1.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        max_tokens=max_tokens,
    )
    return response.choices[0].message.content


def CoT_Prompting(history):
    current = history.copy()
    response = get_completion_from_messages(current)
    if (response == '[]'):
        print("[]")
        return response
    current.append(
        {'role': 'assistant',
         'content': f"{response}"}
    )
    current.append(
        {'role': 'user',
         'content': f"{step_1}"}
    )
    response_1 = get_completion_from_messages(current)
    current.append(
        {'role': 'assistant',
         'content': f"{response_1}"}
    )
    current.append(
        {'role': 'user',
         'content': f"{step_2}"}
    )
    response_2 = get_completion_from_messages(current)
    current.append(
        {'role': 'assistant',
         'content': f"{response_2}"}
    )
    current.append(
        {'role': 'user',
         'content': f"{step_3}"}
    )
    response_3 = get_completion_from_messages(current)
    history.append(response_3)
    return response_3
