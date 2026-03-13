from langchain_core.tools import tool

@tool
def get_word_length(word: str) -> int:
    """This function calculates the length of a word"""
    return len(word)
print("Word Length: ",get_word_length.invoke("Word Category"))