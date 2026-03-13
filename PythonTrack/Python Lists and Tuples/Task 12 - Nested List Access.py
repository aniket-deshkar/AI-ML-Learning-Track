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


