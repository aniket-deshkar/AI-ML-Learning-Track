from google import genai
from google.genai.types import GenerateContentConfig
import os
from dotenv import load_dotenv
import asyncio

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

def prompt(input_prompt):
    try:
        print("Input prompt: \n", input_prompt)
        response = client.models.generate_content(model="gemini-3-flash-preview",contents=input_prompt, config=GenerateContentConfig(max_output_tokens=1000))
        return f"LLM Response: {response.text} \n"
    except Exception as e:
        print(f"Failed due to {e}")

in_prompt = """
Role: You are an exper AI Chef.
Instruction: You must only output valid JSON. Do not include any conversational text, explanations, or markdown formatting outside of the JSON object.
Task:
Generate a recipe for a "Classic Margherita Pizza".
Required JSON Schema:
{
"recipeName": "string",
"prepTime": "string",
"cookTime": "string",
"ingredients": ["string"],
"instructions": ["string"]
}
Constraints:
The ingredients and instructions fields must be arrays of strings.
All keys must match the schema exactly.
Final output must be a single, minified or pretty-printed JSON object.

"""

cot_prompt = prompt(in_prompt)
print("Prompting output: \n", cot_prompt)
