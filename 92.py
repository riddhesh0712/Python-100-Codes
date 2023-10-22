def are_dicts_equal_ordered(dict1, dict2):
    return list(dict1.items()) == list(dict2.items())

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3}
dict2 = {'a': 1, 'b': 2, 'c': 3}

# Check if the dictionaries are equal (considering order)
result = are_dicts_equal_ordered(dict1, dict2)

# Output the result
print(result)
