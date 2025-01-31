from openai import OpenAI
from config import config


def generate_response(system_prompt, user_prompt, model):

    client = OpenAI(
        api_key=config.OPENAI_API_KEY, 
        base_url="https://dashscope.aliyuncs.com/compatible-mode/v1",
    )

    result = client.chat.completions.create(
        model=model,
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ],
        temperature=0.5,
    )

    return result.choices[0].message.content