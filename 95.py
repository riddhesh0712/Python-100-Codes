# Function to check if a list is empty using len()
def is_empty_len(my_list):
    return len(my_list) == 0

# Example lists
empty_list = []
non_empty_list = [1, 2, 3]

# Check if the lists are empty using len()
result_empty = is_empty_len(empty_list)
result_non_empty = is_empty_len(non_empty_list)

# Output the results
print("Is empty list empty?", result_empty)
print("Is non-empty list empty?", result_non_empty)
