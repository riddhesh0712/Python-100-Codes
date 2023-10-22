# Function to count the number of vowels and consonants in a string
def count_vowels_and_consonants(input_string):
    vowels = "AEIOUaeiou"
    consonants = "BCDFGHJKLMNPQRSTVWXYZbcdfghjklmnpqrstvwxyz"
    
    num_vowels = 0
    num_consonants = 0
    
    for char in input_string:
        if char in vowels:
            num_vowels += 1
        elif char in consonants:
            num_consonants += 1
    
    return num_vowels, num_consonants

# Input a string
input_string = input("Enter a string: ")

vowels, consonants = count_vowels_and_consonants(input_string)

print("Number of vowels:", vowels)
print("Number of consonants:", consonants)
