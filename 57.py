# Function to calculate the average of elements in a list using a set
def average_with_set(input_list):
    unique_set = set(input_list)
    total = sum(unique_set)
    count = len(unique_set)
    average = total / count
    return average

# Input a list of numbers
input_list = [1, 2, 2, 3, 4, 5, 5]

average = average_with_set(input_list)

print("Original List:", input_list)
print("Average (with set):", average)
