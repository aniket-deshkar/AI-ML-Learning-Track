# %%
#Task 1 - List Creation and Access
list1 = [1,2,3,0,-2,-5,5,9,-6,10]
print("First Element:",list1[0])
print("Last Element:",list1[-1])
print("Middle 3 elements:",list1[3:6])
list1.clear()
# %%
#Task 2 - List Mutability Test
list2 = [1,2,3,4,5]
print(list2)
list2[0] = 6
print("First element change",list2)
list2[-1]   = 7
print("Last element change",list2)
list2.clear()
#Since list is unordered and mutable, we can change the values at any given index making it dynamic.
# %%
#Task 3 - Slice Manipulation
list3 = []
for i in range(1,16):
    list3.append(i)
print(list3)
print("Even Indexed Elements:",list3[1::2])
print("Index 3 to 10 elements",list3[3:11])
print("Reversed list using slicing: ",list3[::-1])

# %%
#Task 4 - List Method Playground
list4 = []
for i in range(1,6):
    list4.append(i)
print(list4)
print("Inserting value at index 2:", end=' ')
list4.insert(2,6)
print("List after inserting value at 2nd index",list4)
list4.remove(2)
print("List after removing 2",list4)
list4.pop()
print("List after popping last value",list4)
list4.sort()
print("List after sorting",list4)
list4.reverse()
print("List after reversing",list4)

# %%
#Task 5 - Duplicate Finder
list5 = [1,2,3,4,5,2,4,6,7,1]
duplicate_list = []
print("Original List: ",list5)
for i in list5:
    if i not in duplicate_list and list5.count(i)>1:
        duplicate_list.append(i)
print("List with duplicates",duplicate_list)

# %%
#Task 6 - Tuple vs List Behaviour
list6 = [1,2,3,4,5]
tuple6 = (1,2,3,4,5)
print("List:",list6)
print("Tuple:",tuple6)
list6[2] = 6
print("List after append: ",list6)
tuple6[2] = 6
print("Tuple after append",tuple6)
#Since list is mutable, we can change elements, whereas if the same operation of reassigning an index for a tuple throws TypeError as elow as it doesn't support item assignment.
# TypeError                                 Traceback (most recent call last)
# Cell In[50], line 8
#       6 list6[2] = 6
#       7 print("List after append: ",list6)
# ----> 8 tuple6[2] = 6
#
# TypeError: 'tuple' object does not support item assignment


# %%
#Task 7 - Tuple Unpacking
tuple7 = ("John", 30, "London")
name,age,city = tuple7
print("Name:",name)
print("Age:",age)
print("City:",city)
# %%
#Task 8 - Swap Values using Tuple Unpacking
first_number = int(input("Enter first number: "))
second_number = int(input("Enter second number: "))

first_tuple = (first_number,second_number)
print("First Tuple: ",first_tuple)
(second_number,first_number) = first_tuple
second_tuple = (first_number,second_number)
print("Second Tuple: ",second_tuple)
# %%
#Task 9 - String indexing and slicing
user_string = input("Enter a string: ")
print("First character:",user_string[0])
print("Last character:",user_string[-1])
print("Excluding first and last character: ", user_string[1:-1])
print("Reverse string using slicing: ", user_string[::-1])
# %%
#Task 10 - String Methods Practice
input_sentence = input("Please enter a sentence: ")
print("User input:",input_sentence)
print("After .strip(): ", input_sentence.strip())
print("To lowercase: ", input_sentence.lower())
print("Replacing a word in sentence: ", input_sentence.replace(" ","<Space>"))
print("Index of a word in sentence: ", input_sentence.index("fox"))

# %%
#Task 11 - Word Counter
input_sentence = input("Please enter a sentence: ")
print("User input:",input_sentence)
input_sentence.strip()
print("Word count", input_sentence.count(" ") + 1)
# %%
#Task 12 - Nested List Access
nested_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Given Matrix:")
for i in nested_matrix:
    print(i)
print("First Row: ", nested_matrix[0])
print("First Column: ")
for columns in nested_matrix:
    print(columns[0])
print("Diagonal: ")
print(nested_matrix[0][0])
print(nested_matrix[1][1])
print(nested_matrix[2][2])



# %%
#Task 13 - Modify Nested List
nested_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Given Matrix:")
for i in nested_matrix:
    print(i)
print("Matrix after modifying middle element:")
nested_matrix[1]=[10,20,30]
for i in nested_matrix:
    print(i)
# %%
#Task 14 - Flatten a nested list
nested_list = [[1,2,3],[4,5,6],[7,8,9]]
print("Given List:")
for i in nested_list:
    print(i)
flattened_list = []
for inner_elements in nested_list:
    for element in inner_elements:
        flattened_list.append(element)
print("Flattened List:", flattened_list)


# %%
#Task 15 = Mixed Nested Structure
nested_tuple = ([1,2,3],[4,5,6],[7,8,9])
print("Given Tuple:", nested_tuple)
nested_tuple[1][0] = 10
nested_tuple[1][1] = 20
nested_tuple[1][2] = 30
print(nested_tuple)


# %%
