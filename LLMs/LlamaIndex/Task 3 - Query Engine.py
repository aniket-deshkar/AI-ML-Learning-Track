import os
from dotenv import load_dotenv
from llama_index.llms.google_genai import GoogleGenAI
from llama_index.embeddings.google_genai import GoogleGenAIEmbedding
from llama_index.core import SimpleDirectoryReader
from llama_index.core.node_parser import SentenceSplitter
from llama_index.core import Settings
from llama_index.core import VectorStoreIndex
from llama_index.core import load_index_from_storage, StorageContext
from llama_index.core.prompts import PromptTemplate
from llama_index.core import get_response_synthesizer
from llama_index.core.retrievers import VectorIndexRetriever
from llama_index.core.query_engine import RetrieverQueryEngine



load_dotenv()

#Config and loading model
Settings.embed_model=GoogleGenAIEmbedding(model_name="gemini-embedding-001",api_key=os.getenv("GEMINI_API_KEY"),embed_batch_size=100)
Settings.llm=GoogleGenAI(model="gemini-3-flash-preview",api_key=os.getenv("GEMINI_API_KEY"))

#Loading multiple documents in LlamaIndex
documents = SimpleDirectoryReader(input_files=["MD_FILE_1.md", "MD_FILE_2.md"]).load_data()

#Defining Chunk Sizes
text_splitter = SentenceSplitter(chunk_size=512, chunk_overlap=10)
Settings.text_splitter = text_splitter

#Creating Index
index = VectorStoreIndex.from_documents(documents, transformations=[text_splitter])
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
retriever = VectorIndexRetriever(index=index, similarity_top_k=5)
response_synthesizer = get_response_synthesizer()

#Task - 3 Building Query Engine
query_engine = RetrieverQueryEngine(retriever=retriever, response_synthesizer=response_synthesizer)
query_engine.update_prompts({"response_synthesizer:text_qa_template": prompt_template})

response = query_engine.query("What are the steps to use Document Loader?")
print(response)