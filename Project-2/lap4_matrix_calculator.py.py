# Matrix Calculator Using Multidimensional Lists

# Define Matrices
matrix_A = [
    [1, 2],
    [3, 4]
]

matrix_B = [
    [5, 6],
    [7, 8]
]

# Initialize Result Matrix (2x2 with zeros)
result_matrix = [
    [0, 0],
    [0, 0]
]

# Perform Matrix Addition using Nested Loops
for row_index in range(2):  # Rows 0 and 1
    for col_index in range(2):  # Columns 0 and 1
        result_matrix[row_index][col_index] = (
            matrix_A[row_index][col_index] +
            matrix_B[row_index][col_index]
        )

# Function to Print Matrix Neatly
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()  # New line after each row

# Display Results
print("Matrix A:")
print_matrix(matrix_A)

print("\nMatrix B:")
print_matrix(matrix_B)

print("\nSum of Matrices (A + B):")
print_matrix(result_matrix)