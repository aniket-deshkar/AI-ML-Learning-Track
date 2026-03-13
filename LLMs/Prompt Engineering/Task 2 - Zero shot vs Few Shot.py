from google import genai
from google.genai.types import GenerateContentConfig
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def prompt(input_prompt):
    try:
        print("Input prompt: ", input_prompt)
        response = client.models.generate_content(model="gemini-3-flash-preview",contents=input_prompt, config=GenerateContentConfig(max_output_tokens=200))
        return f"LLM Response: {response.text} \n"
    except Exception as e:
        print(f"Failed due to {e}")

zero_shot_prompt = "How does zero shot prompting works?"

few_shot_prompt= """
    Classify the sentiment of the following sentences as Positive, Neutral, or Negative.

    Sentence: I love this new phone!
    Sentiment: Positive

    Sentence: The movie was okay, nothing special.
    Sentiment: Neutral

    Sentence: The service was terrible and slow.
    Sentiment: Negative

    Sentence: The concert was fantastic!
    Sentiment:
"""


prompt1 =  prompt(zero_shot_prompt)
print("Zero Shot Prompting output: \n", prompt1)
prompt2 =  prompt(few_shot_prompt)
print("\n Few Shot Prompting output: ", prompt2)
