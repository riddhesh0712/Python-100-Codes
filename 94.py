def first_non_repeated_character(input_string):
    char_count = {}

    # Count occurrences of each character
    for char in input_string:
        char_count[char] = char_count.get(char, 0) + 1

    # Find the first non-repeated character
    for char in input_string:
        if char_count[char] == 1:
            return char

    # If no non-repeated character is found
    return None

# Example string
my_string = "programming"

# Find the first non-repeated character
result = first_non_repeated_character(my_string)

# Output the result
print(result)
