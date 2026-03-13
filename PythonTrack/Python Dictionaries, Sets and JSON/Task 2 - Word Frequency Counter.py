user_input = input("Enter a sentence: ").split()
print("User input: ",user_input)


frequency_list = {}

for words in user_input:
    if words  in frequency_list:
        frequency_list[words]+= 1
    else:
        frequency_list[words] = 1
print("Frequency list: ",frequency_list)
frequent_words = max(frequency_list, key=frequency_list.get)
print("Most Occurring words: ",frequent_words)