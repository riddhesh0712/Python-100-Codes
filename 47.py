# Function to print a matrix
def print_matrix(matrix):
    for row in matrix:
        for element in row:
            print(element, end="\t")
        print()

# Function to extract a submatrix from a larger matrix
def extract_submatrix(matrix, start_row, end_row, start_col, end_col):
    submatrix = []
    for i in range(start_row, end_row + 1):
        row = matrix[i][start_col:end_col + 1]
        submatrix.append(row)
    return submatrix

# Define a larger matrix
larger_matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Larger Matrix:")
print_matrix(larger_matrix)

# Extract a submatrix from the larger matrix
start_row = 1
end_row = 2
start_col = 1
end_col = 2

submatrix = extract_submatrix(larger_matrix, start_row, end_row, start_col, end_col)

print("\nExtracted Submatrix:")
print_matrix(submatrix)
