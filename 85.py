# Function to create a list of unique elements from a list with duplicates
def unique_elements(input_list):
    unique_list = list(set(input_list))
    return unique_list

# Example list with duplicates
my_list = [1, 2, 2, 3, 4, 4, 5]

unique_list = unique_elements(my_list)

print("Original List with Duplicates:", my_list)
print("List of Unique Elements:", unique_list)
