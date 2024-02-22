import os

import chainlit as cl
import openai

os.environ['OPENAI_API_KEY'] = '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'
openai.api_key = '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'


def get_gpt_output(user_message):
    response = openai.chat.completions.create(
        model="gpt-4",
        messages=[
            {"role": "system",
             "content": "you are an assistant that is obsessed with potatoes and will never stop talking about them"},
            {"role": "user", "content": user_message}
        ],
        temperature=1,
        max_tokens=256,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )

    return response


@cl.on_message
async def main(message: cl.Message):
    await cl.Message(content=f"{get_gpt_output(message)['choices'][0]['message']['content']}", ).send()
