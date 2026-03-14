#Task 13 - Modify Nested List
nested_matrix = [[1,2,3],[4,5,6],[7,8,9]]
print("Given Matrix:")
for i in nested_matrix:
    print(i)
print("Matrix after modifying middle element:")
nested_matrix[1]=[10,20,30]
for i in nested_matrix:
    print(i)