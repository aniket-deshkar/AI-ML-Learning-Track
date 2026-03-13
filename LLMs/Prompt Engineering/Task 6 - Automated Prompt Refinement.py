from google import genai

from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))


def prompt_execute(prompt, model="gemini-2.5-flash"):
    response=client.models.generate_content(
    model=model,
    contents=prompt
)
    return response.text
 
def is_good_output(output):
    if len(output.strip())<50:
        return False
    vague_phrases=["Don't know ", "not sure", "it depends"]
    for phrase in vague_phrases:
        if phrase in output.lower():
            return False
 
def refine_prompt(prompt):
    return(prompt+"Avoid vague Sentences and give answers in one word and one example.")
 
def prompt_refinement_pipeline(initial_prompt, max_attempt=3):
    prompt=initial_prompt
 
    for attempt in range(max_attempt):
        print(f"Attempt {attempt+1}")
        print(f"Prompt: {prompt}")
 
        output=prompt_execute(prompt)
        print(f"Output: {output}")
 
        if is_good_output(output):
            print("Output accepted. Stopping refinement")
            return output
 
        print("Output not good enough. Refining prompt.")
        prompt=refine_prompt(prompt)
 
    print("Max attempts reached. Returning last output")
    return output
 
if __name__=="__main__":
    prompt=input("Enter initial prompt: ")
    final_output=prompt_refinement_pipeline(prompt)    