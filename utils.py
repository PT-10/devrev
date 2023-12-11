from schema import agent_system, step_1, step_2, step_3
from openai import OpenAI
from config import key

GPT_model = "gpt-3.5-turbo-1106"
client_1 = OpenAI(
    api_key = key
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
    # messages_cot_1 =  [  
    # {'role':'system', 
    #  'content': agent_system},
    # {'role':'user',
    # 'content': f"{query}"}
    # ]
    # history.append({'role':'user', 'content': f"{query}"})
    response = get_completion_from_messages(history)
    if(response == '[]'):
        print("[]")
        return response
    history.append(
    {'role':'assistant',
    'content':f"{response}"}
    ) 
    history.append(
    {'role':'user',
    'content':f"{step_1}"}
    )
    response_1 = get_completion_from_messages(history)
    history.append(
    {'role':'assistant',
    'content':f"{response_1}"}
    )
    history.append(
    {'role':'user',
    'content':f"{step_2}"}
    )
    response_2 = get_completion_from_messages(history)
    history.append(
    {'role':'assistant',
    'content':f"{response_2}"}
    )
    history.append(
    {'role':'user',
    'content':f"{step_3}"}
    )
    response_3 = get_completion_from_messages(history)
    return response_3
    # print(response_3)
   