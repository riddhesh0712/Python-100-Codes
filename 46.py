# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

# Function to perform matrix addition
def matrix_addition(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrix addition is not possible. The matrices must have the same dimensions.")
        return None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0]):
            row.append(matrix1[i][j] + matrix2[i][j])
        result.append(row)
    
    return result

# Function to perform matrix subtraction
def matrix_subtraction(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        print("Matrix subtraction is not possible. The matrices must have the same dimensions.")
        return None
    
    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix1[0]):
            row.append(matrix1[i][j] - matrix2[i][j])
        result.append(row)
    
    return result

# Define two matrices for addition and subtraction
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [9, 8, 7],
    [6, 5, 4],
    [3, 2, 1]
]

print("Matrix 1:")
print_matrix(matrix1)

print("\nMatrix 2:")
print_matrix(matrix2)

# Perform matrix addition
result_addition = matrix_addition(matrix1, matrix2)
if result_addition:
    print("\nResult of Matrix Addition:")
    print_matrix(result_addition)

# Perform matrix subtraction
result_subtraction = matrix_subtraction(matrix1, matrix2)
if result_subtraction:
    print("\nResult of Matrix Subtraction:")
    print_matrix(result_subtraction)
