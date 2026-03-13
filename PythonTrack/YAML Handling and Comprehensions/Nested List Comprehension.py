matrix = [[1,2,3],
          [4,5,6],
          [7,8,9]]

print("Flattened Matrix:")

flattened_matrix = [element for inner_element in matrix for element in inner_element ]
print("Flattened Matrix: ",flattened_matrix)

diagonal_elements = [matrix[i][i] for i in range(len(matrix))]
print("Diagonal Elements: ",diagonal_elements)

even_numbers = [num for num in flattened_matrix if num % 2 == 0]
print("Even Numbers: ",even_numbers)