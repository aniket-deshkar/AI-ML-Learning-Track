import os
import logging
from dotenv import load_dotenv

from llama_index.core import VectorStoreIndex, Document, Settings, get_response_synthesizer
from llama_index.core.evaluation import FaithfulnessEvaluator
from llama_index.core.query_engine import RetrieverQueryEngine


from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding

load_dotenv()

llm = GoogleGenAI(model="gemini-3-flash-preview")
embed_model = GoogleGenAIEmbedding(model_name="gemini-embedding-001")

Settings.llm = llm
Settings.embed_model = embed_model


documents = [Document(text = "Chicago Pile-1 (CP-1, USA, 1942): Led by Enrico Fermi, this was the world’s first artificial, self-sustaining nuclear reactor. Built under a squash court at the University of Chicago, it proved that a controlled chain reaction was possible, a key, necessary step for the Manhattan Project."),
                Document(text="Underwater fiction cities span from mythical, ancient civilizations like Atlantis to futuristic, colonized domes such as Pacifica, often serving as allegories for power, technology, and humanity's survival. Iconic examples include the sunken, technologically advanced Atlantis, the ship-constructed city of Armada, and sci-fi colonies designed to survive the depths. ")]

index = VectorStoreIndex.from_documents(documents,embed_model = embed_model)
retriever = index.as_retriever(similarity_top_k =2)
synthesizer = get_response_synthesizer(response_mode="compact", llm=llm)
query_engine = RetrieverQueryEngine(retriever=retriever, response_synthesizer=synthesizer)
print("+++Hallucination Detection+++")

query_str = "What is Chicago Pile-1?"
rag_response = query_engine.query(query_str)
evaluator =FaithfulnessEvaluator(llm=llm)
eval_result = evaluator.evaluate_response(response=rag_response)
print("Generated Answer: ", rag_response)
print("Faithfullness Score : ",eval_result.score, "Response passed? : ", eval_result.passing)

print("---Comparing Result---")

print("With Indexing: ", rag_response)

response_direct = llm.complete(query_str)
print("Without Indexing: ", response_direct)
print("---Comparision---")

if "1942" in str(rag_response) and "underwater" in str(rag_response):
    print("Indexing result accurate")
else:
    print("Indexing Result Failed")

if "1942" not in str(response_direct):
    print("Hallucinated - No Indexing Result")