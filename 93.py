def unique_elements_preserving_order(list_of_lists):
    seen = set()
    unique_elements_list = [x for sublist in list_of_lists for x in sublist if x not in seen and not seen.add(x)]
    return unique_elements_list

# Example list of lists
list_of_lists = [[1, 2, 3], [3, 4, 5], [5, 6, 7]]

# Get unique elements, preserving order
result = unique_elements_preserving_order(list_of_lists)

# Output the result
print(result)
