from google import genai
from config import gemini_api_key
from centralized_logger import logger

client = genai.Client(api_key=gemini_api_key)
try: 
    user_input = input(print("Enter prompt: "))
    
    logger.info(f"user_input: {user_input}")

    gemini_response = client.models.generate_content(model="gemini-3-flash-preview",contents=user_input)

    logger.info(f"LLM Response: {gemini_response.text}")

    print(f"Response: {gemini_response.text}")
except Exception as e:
    logger.error(e)    