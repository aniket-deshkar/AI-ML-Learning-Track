from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def prompt_pipeline(task, description,example):
    try:
        input_prompt = f"Task:{task} \n, Description: {description} \n, Example: {example}"
        print("Input prompt: ", input_prompt)
        response = client.models.generate_content(model="gemini-3-flash-preview",contents=input_prompt)
        print(f"LLM Response: {response.text}")
    except Exception as e:
        print(f"Failed due to {e}")

in_task = "Sentiment-Analysis"
in_description = "The beach is near my house."
in_example = "Review: 'The food was amazing!' -> Sentiment: Positive"
prompt_pipeline(in_task, in_description,in_example)