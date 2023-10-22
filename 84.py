# Function to find common elements between two dictionaries
def common_elements(dict1, dict2):
    common = {key: value for key, value in dict1.items() if key in dict2 and dict2[key] == value}
    return common

# Example dictionaries
dict1 = {'a': 1, 'b': 2, 'c': 3, 'd': 4}
dict2 = {'b': 2, 'c': 3, 'e': 5, 'f': 6}

common = common_elements(dict1, dict2)

print("Common Elements:")
for key, value in common.items():
    print(f"{key}: {value}")
