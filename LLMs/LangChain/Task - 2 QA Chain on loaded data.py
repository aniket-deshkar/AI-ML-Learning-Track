from langchain_community.document_loaders import WebBaseLoader
from langchain_google_genai import GoogleGenerativeAIEmbeddings, ChatGoogleGenerativeAI
from langchain_core.prompts import PromptTemplate
from langchain_community.document_loaders import TextLoader
import os
from dotenv import load_dotenv

load_dotenv()
os.getenv("GOOGLE_API_KEY")


URL = "https://docs.langchain.com/oss/python/integrations/document_loaders/wikipedia"

loader = WebBaseLoader(URL)
documents = loader.load()

print(f"Actual Data:\n{documents[0].page_content}")
print(f"Meta Data:\n{documents[0].metadata}\n") 
 
document_text = documents[0].page_content
 
llm = ChatGoogleGenerativeAI(model = "gemini-2.5-flash")
 
template = """
Answer the question only using the documents below.
If qs is not from the document, say "I don't know".
Document: {document}
Question: {question}
"""
prompt = PromptTemplate(template=template, input_variables=["document","question"])
chain = prompt | llm
response = chain.invoke({"document": document_text, "question":"How is wikipedia integration done?"})
print(response.text)