def is_subset_method(list1, list2):
    return set(list1).issubset(set(list2))

# Example lists
list1 = [1, 2, 3]
list2 = [1, 2, 3, 4, 5]

# Check if list1 is a subset of list2 using issubset()
result = is_subset_method(list1, list2)

# Output the result
print(result)
