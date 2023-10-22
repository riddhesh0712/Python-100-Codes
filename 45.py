# Function to find the sum of the main diagonal elements of a matrix
def sum_main_diagonal(matrix):
    if len(matrix) != len(matrix[0]):
        print("The matrix is not square, so it doesn't have a main diagonal.")
        return None
    
    diagonal_sum = 0
    for i in range(len(matrix)):
        diagonal_sum += matrix[i][i]
    
    return diagonal_sum

# Define a sample square matrix
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

print("Matrix:")
for row in matrix:
    print(row)

main_diagonal_sum = sum_main_diagonal(matrix)

if main_diagonal_sum is not None:
    print(f"\nSum of the main diagonal elements: {main_diagonal_sum}")
