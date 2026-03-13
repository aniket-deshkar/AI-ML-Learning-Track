from google import genai
from google.genai import types
import pandas as pd
import numpy as np
from sklearn.metrics.pairwise import cosine_similarity
import os
from dotenv import load_dotenv
from centralized_logger import logger

load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
client = genai.Client(api_key=gemini_api_key)

try:

        input_text= [
                "What is AI?",
                "What is the generative AI",
                "What is Machine Learning!",
                "Cats and Dogs eat what?"
                ]

        result = client.models.embed_content(
                model="gemini-embedding-001",
                contents=input_text,
                config=types.EmbedContentConfig(task_type="SEMANTIC_SIMILARITY")
        )

        print("Task 2 Output: \n")

        embeddings = np.array([e.values for e in result.embeddings])

        print("\n Similarity Matrix")
        similarity_matrix = np.dot(embeddings, embeddings.T)
        dataframe = pd.DataFrame(similarity_matrix, index=input_text, columns=input_text)
        print(dataframe)

        print("\n Semantic Similarity matrix")
        print(dataframe.round(4))
except Exception as e:
        logger.error(f"Execption {e} casused")
