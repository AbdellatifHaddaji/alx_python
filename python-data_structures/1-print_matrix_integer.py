def print_matrix_integer(matrix=[[]]):
    if not matrix:
        print("Empty matrix")
        return

    for row in matrix:
        for i, num in enumerate(row):
            # Use str.format() to print integers
            if i < len(row) - 1:
                print("{:d} ".format(num), end="")
            else:
                print("{:d}".format(num), end="")
        print()  # Move to the next line after printing a row

# Test cases
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print_matrix_integer(matrix)
print("--")
print_matrix_integer()