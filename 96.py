def remove_whitespace_replace(input_string):
    return input_string.replace(" ", "").replace("\t", "").replace("\n", "")

# Example string
my_string = "  Hello, \tworld!\nHow are you?  "

# Remove whitespace using replace()
result = remove_whitespace_replace(my_string)

# Output the result
print(result)
