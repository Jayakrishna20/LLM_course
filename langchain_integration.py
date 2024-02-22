import os

import chainlit as cl
import openai
from langchain import PromptTemplate, OpenAI, LLMChain

os.environ['OPENAI_API_KEY'] = 'OPENAI_API_KEY'
openai.api_key = 'OPENAI_API_KEY'

template = """Question: {question}

Answer: Let's think step by step."""


@cl.on_chat_start
def main():
    prompt = PromptTemplate(template=template, input_variables=["question"])
    llm_chain = LLMChain(prompt=prompt, llm=OpenAI(temperature=0, streaming=True), verbose=True)

    cl.user_session.set("llm_chain", llm_chain)


@cl.on_message
async def main(message: str):
    llm_chain = cl.user_session.get("llm_chain")

    res = await llm_chain.acall(message, callbacks=[cl.AsyncLangchainCallbackHandler()])

    await cl.Message(content=res["text"]).send()
