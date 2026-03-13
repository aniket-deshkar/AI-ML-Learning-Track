from google import genai
from config import gemini_api_key
from centralized_logger import logger

client = genai.Client(api_key="")

try:
        prompt_1 = client.models.generate_content(
            model="gemini-3-flash-preview", contents="What is cat in 20 words?"
        )
        print("Response 1: ",prompt_1.text)
        logger.info(prompt_1.text)

        prompt_2 = client.models.generate_content(
            model="gemini-3-flash-preview", contents="What is jungle cat in 20 words?"
        )
        print("Response 1: ",prompt_2.text)
        logger.info(prompt_2.text)

        prompt_3 = client.models.generate_content(
            model="gemini-3-flash-preview", contents="Is toger a cat? in 20 words"
        )
        print("Response 1: ",prompt_3.text)
        logger.info(prompt_3.text)
except Exception as e:
        logger.error("Exception failed with ",e)

