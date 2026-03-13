import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain.chat_models import init_chat_model
from langchain_core.prompts import PromptTemplate
from langchain_google_genai import ChatGoogleGenerativeAI

load_dotenv()

os.getenv("GEMINI_API_KEY")
# model = ChatGoogleGenerativeAI(
#     model="gemini-3-flash-preview",
#     temperature=1.0,  # Gemini 3.0+ defaults to 1.0
#     max_tokens=100,
#     timeout=None,
#     max_retries=2,
#     # other params...
# )

# response = model.invoke("Why do parrots talk?")
# print("Response: ", response.text)

