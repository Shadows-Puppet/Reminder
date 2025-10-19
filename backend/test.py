from ollama import chat
stream = chat(
        model='mistral:latest',
        messages=[{'role': 'user', 'content': 'hi'}],
        stream=True,
    )

for chunk in stream:
        content = chunk['message']['content']
        print(content, end='', flush=True)  # Stream to console