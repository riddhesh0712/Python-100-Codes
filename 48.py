# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

# Function to find the determinant of a square matrix using the Laplace expansion
def determinant(matrix):
    n = len(matrix)
    
    # Base case for a 1x1 matrix
    if n == 1:
        return matrix[0][0]

    det = 0
    for i in range(n):
        # Calculate the minor matrix
        minor_matrix = [row[:i] + row[i+1:] for row in matrix[1:]]
        
        # Add the determinant of the minor matrix with appropriate sign
        det += matrix[0][i] * determinant(minor_matrix) * (-1) ** i
    
    return det

# Define a square matrix for which you want to find the determinant
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
print_matrix(matrix)

det = determinant(matrix)

print("\nDeterminant:", det)
