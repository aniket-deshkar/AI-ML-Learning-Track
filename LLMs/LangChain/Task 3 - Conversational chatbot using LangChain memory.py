from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import InMemoryChatMessageHistory
import os
from dotenv import load_dotenv

load_dotenv()
api_key = os.getenv("GEMINI_API_KEY")

model = ChatGoogleGenerativeAI(model="gemini-3-flash-preview", google_api_key=api_key)

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder(variable_name="history"),
    ("human", "{input}")
])

chain = prompt | model

store = {}

def get_session_history(session_id: str):
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]

config_chain = RunnableWithMessageHistory(
    chain,
    get_session_history,
    input_messages_key="input",
    history_messages_key="history"
)

def extract_text_from_response(response):
    """Extract clean text from response content"""
    content = response.content
    
    # If content is a list of dictionaries (structured response)
    if isinstance(content, list):
        text_parts = []
        for item in content:
            if isinstance(item, dict) and 'text' in item:
                text_parts.append(item['text'])
        return '\n'.join(text_parts)
    
    # If content is already a string
    return str(content)

# Dynamic conversation loop
print("Conversational Chatbot (type 'exit' or 'quit' to end)")
print("-" * 50)

session_id = "user_1"

while True:
    user_input = input("\nYou: ").strip()
    
    if user_input.lower() in ['exit', 'quit', 'bye']:
        print("Chatbot: Goodbye! Have a great day!")
        break
    
    if not user_input:
        continue
    
    try:
        response = config_chain.invoke(
            {"input": user_input},
            config={"configurable": {"session_id": session_id}}
        )
        
        # Extract and print clean text
        clean_text = extract_text_from_response(response)
        print(f"\nChatbot: {clean_text}")
        
    except Exception as e:
        print(f"Error: {e}")
 