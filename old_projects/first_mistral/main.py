import os
from mistralai import Mistral
from dotenv import load_dotenv, find_dotenv

load_dotenv(find_dotenv())

api_key = os.environ["TOKEN"]
model = "mistral-large-latest"

client = Mistral(api_key=api_key)

chat_response = client.chat.complete(
    model=model,
    messages=[
        {
            "role": "user",
            "content": "What is the best French cheese?",
        },
    ]
)
print(chat_response.choices[0].message.content)
