from nltk.tokenize import word_tokenize
from centralized_logger import logger


import_data = "I am learning Generative AI."

try:
    nltk_output = word_tokenize(import_data)

    print(f"Token length using nltk is {len(nltk_output)} for tokens {nltk_output}")
except Exception as e:
    logger.error("Failed with exception",e)