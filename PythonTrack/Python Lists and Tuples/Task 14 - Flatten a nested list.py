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

