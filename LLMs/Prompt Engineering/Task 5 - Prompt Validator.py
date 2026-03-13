from google import genai
import os
from dotenv import load_dotenv
from google.genai import types
load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def prompt_vaidator(prompt,instructions):
    custom_safety_settings= [
    types.SafetySetting(
        category=types.HarmCategory.HARM_CATEGORY_HATE_SPEECH,
        threshold=types.HarmBlockThreshold.BLOCK_LOW_AND_ABOVE,
    ),
    ]

    try:
        response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=f"Instructions:{instructions}\n, Prompt:{prompt} ",
            config=types.GenerateContentConfig(
                safety_settings=custom_safety_settings
            ),
        )
        print("Response: ",response.text)

    except Exception as e:
        print(f"Content generation failed or was blocked: {e}")
input_instructions="Filter the response, if the output contains swear words, throw exception or filter."
input_prompt = "Write a list of 5 very rude and swearing things that I might say to someone after stubbing my toe."
prompt_vaidator(input_prompt, input_instructions)