# Function to check if two matrices are equal
def are_matrices_equal(matrix1, matrix2):
    if len(matrix1) != len(matrix2) or len(matrix1[0]) != len(matrix2[0]):
        return False

    for i in range(len(matrix1)):
        for j in range(len(matrix1[0]):
            if matrix1[i][j] != matrix2[i][j]:
                return False

    return True

# Define two matrices for comparison
matrix1 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix2 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

matrix3 = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 0]
]

# Check if matrix1 and matrix2 are equal
if are_matrices_equal(matrix1, matrix2):
    print("Matrix 1 and Matrix 2 are equal.")
else:
    print("Matrix 1 and Matrix 2 are not equal.")

# Check if matrix1 and matrix3 are equal
if are_matrices_equal(matrix1, matrix3):
    print("Matrix 1 and Matrix 3 are equal.")
else:
    print("Matrix 1 and Matrix 3 are not equal.")
