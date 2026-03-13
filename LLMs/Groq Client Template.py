import os
from groq import Groq

# 1. Initialize the client (ensure GROQ_API_KEY is in your env)
client = Groq(
    api_key=os.environ.get("GROQ_API_KEY"),
)

# 2. Create the chat completion
chat_completion = client.chat.completions.create(
    messages=[
        {
            "role": "system",
            "content": "You are a helpful assistant."
        },
        {
            "role": "user",
            "content": "Explain the speed of Groq in one sentence.",
        }
    ],
    model="llama-3.3-70b-versatile", # Supported models: llama-3.1-8b, mixtral-8x7b, etc.
    temperature=0.5,
    max_tokens=1024,
    top_p=1,
    stop=None,
    stream=False,
)

# 3. Print the response
print(chat_completion.choices[0].message.content)
