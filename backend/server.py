from fastapi import FastAPI
from ollama import chat
from ollama import ChatResponse
from vector_db import getPinecone, upsert, search
from datetime import date
from preamble import preamble
import json

app = FastAPI()

@app.get('/')
async def read_root():
    print("Hello World")
    
    return 0


@app.get('/set_event')
async def process_set():
    pc = await getPinecone()
    query = "Hello I have a doctors appt on Friday."
    today = date.today()
    content = preamble(query, today)
    stream = chat(
        model='mistral:latest',
        messages=[{'role': 'user', 'content': content}],
        stream=True,
    )

    full_response = ""

    for chunk in stream:
        content = chunk['message']['content']
        print(content, end='', flush=True)  # Stream to console
        full_response += content  # Save for later

    llm_reply = json.loads(full_response)
    llm_reply["metadata"] == str(llm_reply["metadata"])

    await upsert(llm_reply["text"], pc,"100", llm_reply["metadata"])

@app.get('/get_event')
async def process_get():
    pass