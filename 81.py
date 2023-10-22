# Function to remove all occurrences of an element from a list using list comprehension
def remove_element_from_list(input_list, element_to_remove):
    return [item for item in input_list if item != element_to_remove]

# Example list
my_list = [1, 2, 2, 3, 4, 2, 5]
element_to_remove = 2

result_list = remove_element_from_list(my_list, element_to_remove)

print("Original List:", my_list)
print("List after removing", element_to_remove, ":", result_list)
