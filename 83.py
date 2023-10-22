import random

# Function to shuffle a list randomly
def shuffle_list(input_list):
    random.shuffle(input_list)

# Example list
my_list = [1, 2, 3, 4, 5]

print("Original List:", my_list)

# Shuffle the list
shuffle_list(my_list)

print("Shuffled List:", my_list)
