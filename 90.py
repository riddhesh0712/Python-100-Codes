from collections import Counter

def find_mode(input_list):
    # Count occurrences of each element in the list
    count_dict = Counter(input_list)

    # Find the element with the maximum count (mode)
    mode = max(count_dict, key=count_dict.get)

    return mode

# Example list
my_list = [1, 2, 2, 3, 3, 3, 4, 4, 5]

# Find the mode of the list
result = find_mode(my_list)

# Output the result
print("Mode:", result)
