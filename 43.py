# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end=" ")
        print()

# Function to find the transpose of a matrix
def transpose_matrix(matrix):
    rows, cols = len(matrix), len(matrix[0])
    transposed = [[0 for _ in range(rows)] for _ in range(cols)]
    
    for i in range(rows):
        for j in range(cols):
            transposed[j][i] = matrix[i][j]
    
    return transposed

# Create a sample matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Original Matrix:")
print_matrix(matrix)

# Find the transpose of the matrix
transposed_matrix = transpose_matrix(matrix)

print("\nTransposed Matrix:")
print_matrix(transposed_matrix)
