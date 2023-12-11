def square_matrix_simple(matrix=[]):
    # Create a new matrix with the same size as the input matrix
    new_matrix = []
    for row in matrix:
        new_row = [x ** 2 for x in row]
        new_matrix.append(new_row)
    return new_matrix

# Test case
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

new_matrix = square_matrix_simple(matrix)
print(new_matrix)
print(matrix)
