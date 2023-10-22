# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

# Function to perform matrix multiplication
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        print("Matrix multiplication is not possible. The number of columns in the first matrix must match the number of rows in the second matrix.")
        return None
    
    result = []
    rows1, cols1 = len(matrix1), len(matrix1[0])
    cols2 = len(matrix2[0])

    for i in range(rows1):
        row = []
        for j in range(cols2):
            product = 0
            for k in range(cols1):
                product += matrix1[i][k] * matrix2[k][j]
            row.append(product)
        result.append(row)
    
    return result

# Define two matrices for multiplication
matrix1 = [
    [1, 2],
    [3, 4]
]

matrix2 = [
    [5, 6],
    [7, 8]
]

print("Matrix 1:")
print_matrix(matrix1)

print("\nMatrix 2:")
print_matrix(matrix2)

result_matrix = matrix_multiply(matrix1, matrix2)

if result_matrix:
    print("\nResult of Matrix Multiplication:")
    print_matrix(result_matrix)
