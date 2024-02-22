import os

import chainlit as cl
import openai

os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY'
openai.api_key = 'OPENAI_API_KEY'


@cl.on_message
async def main(message: cl.Message):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": "you are an assistant that is obsessed with potatoes and will never stop talking about them"},
            {"role": "user", "content": message}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    await cl.Message(content=f"{response['choices'][0]['message']['content']}", ).send()
