from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

response = client.models.generate_content(model="gemini-3-flash-preview",contents="Handle Failure cases when Langchain tools return error")
print(response.text)

"""
from google import genai
import os
from dotenv import load_dotenv

# Load from the correct path
load_dotenv("/home/aniket-deshkar/PycharmProjects/Path2AI/qna_chatbot/chatbot_app/.env")
api_key = os.getenv("GEMINI_API_KEY")

if not api_key:
    print("API Key not found in /home/aniket-deshkar/PycharmProjects/Path2AI/qna_chatbot/chatbot_app/.env")
else:
    client = genai.Client(api_key=api_key)
    print("List of models:")
    try:
        models = client.models.list()
        for model in models:
            print(f"Name: {model.name}")
            print(f"Supported methods: {model.supported_actions}")
            print("-" * 20)
    except Exception as e:
        print(f"Error listing models: {e}")
"""