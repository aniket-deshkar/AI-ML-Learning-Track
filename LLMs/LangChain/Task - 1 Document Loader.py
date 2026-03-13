from langchain_community.document_loaders import WebBaseLoader

URL = "https://docs.langchain.com/oss/python/integrations/document_loaders/wikipedia"

loader = WebBaseLoader(URL)
documents = loader.load()

"""LangChain loaders operate Documents objects containing page_content and metadata"""

print(f"Actual Data:\n{documents[0].page_content}")
print(f"Meta Data:\n{documents[0].metadata}\n")

