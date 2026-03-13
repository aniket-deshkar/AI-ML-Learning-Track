import os
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core.llms import ChatMessage
from llama_index.core import VectorStoreIndex
from llama_index.core import download_loader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
from llama_index.readers.web import SimpleWebPageReader
from llama_index.core import load_index_from_storage, StorageContext
from llama_index.core.prompts import PromptTemplate
from llama_index.core import get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine
from llama_index.core import SummaryIndex




load_dotenv()
gemini_api_key = os.getenv("GEMINI_API_KEY")
Settings.embed_model=GoogleGenAIEmbedding(model_name="gemini-embedding-001",api_key=gemini_api_key,embed_batch_size=100)
Settings.llm=GoogleGenAI(model="gemini-3-flash-preview",api_key=gemini_api_key)

documents = SimpleWebPageReader().load_data(urls=["https://pallab29.medium.com/building-a-rag-pipeline-with-llamaindex-a-step-by-step-guide-1c7964e6d06a"])

documents[0]
# text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)
# Settings.text_splitter = text_splitter  

index = SummaryIndex.from_documents(documents)
index.storage_context.persist(persist_dir="./storage")

storage_context = StorageContext.from_defaults(persist_dir="./storage")
index = load_index_from_storage(storage_context)

template = """
You are a helpful assistant that helps people find information. You are particularly good at answering questions
about the content of documents. Use the following pieces of context to answer the question at the end. If you
don't know the answer, just say that you don't know, don't try to make up an answer.
\nQuestion: {query}
\nContext: {context}
\nAnswer:"""

prompt_template = PromptTemplate(template=template, template_var_mappings={"query_str":"query", "context_str": "context"})
# Set up the retriever and query engine
# retriever = VectorIndexRetriever(index=index, similarity_top_k=5)
# response_synthesizer = get_response_synthesizer()
# query_engine = RetrieverQueryEngine(retriever=retriever, response_synthesizer=response_synthesizer)
# query_engine.update_prompts({"response_synthesizer:text_qa_template": prompt_template})
# set Logging to DEBUG for more detailed outputs
query_engine = index.as_query_engine()
response = query_engine.query("How to integrate Llamaindex")
print(response)




# response = llm.complete("Who is Jose Mourinho?")
# print(response)

# index = VectorStoreIndex.from_documents(documents)

messages = [
    ChatMessage(
        role="system", content="When will ManUnited win Champions League"
    )
]