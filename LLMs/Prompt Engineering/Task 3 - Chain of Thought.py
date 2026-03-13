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

in_cot_prompt = """Solve the following math problems step by step:

Example 1:
Problem: If a train travels at 60 miles per hour for 2.5 hours, how far does it go?
Solution:
1. Identify the given information:
   - Speed of the train: 60 miles per hour
   - Time of travel: 2.5 hours
2. Use the formula: Distance = Speed x Time
3. Plug in the values:
   Distance = 60 miles/hour x 2.5 hours
4. Calculate:
   Distance = 150 miles
Therefore, the train travels 150 miles.

Problem: A bakery sold 136 cakes last week. This week, they sold 25% more. How many cakes did they sell this week?
Solution:
1. Identify the given information:
   - Last week's sales: 136 cakes
   - Increase: 25%
2. Calculate the increase:
   25% of 136 = 0.25 x 136 = 34 cakes
3. Add the increase to last week's sales:
   This week's sales = 136 + 34 = 170 cakes
Therefore, the bakery sold 170 cakes this week.

Here is a new question:
Problem: If a rectangle has a length of 15 meters and a width of 8 meters, what is its area?
Solution:
"""

cot_prompt = prompt(in_cot_prompt)
print("Prompting output: \n", cot_prompt)
