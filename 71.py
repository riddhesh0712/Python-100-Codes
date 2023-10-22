# Function to convert a list of strings into a single string
def list_to_string(string_list, delimiter=' '):
    return delimiter.join(string_list)

# Example list of strings
string_list = ["Hello", "World", "Python", "Programming"]

# Convert the list to a single string with spaces as the default delimiter
result = list_to_string(string_list)
print("Single String:", result)

# You can also specify a custom delimiter, e.g., a comma
result_with_comma = list_to_string(string_list, ', ')
print("Single String with Comma:", result_with_comma)
