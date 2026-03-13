#Task 11 - Word Counter
input_sentence = input("Please enter a sentence: ")
print("User input:",input_sentence)
input_sentence.strip()
print("Word count", input_sentence.count(" ") + 1)