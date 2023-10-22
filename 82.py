# Function to find the second largest element in a list
def find_second_largest(input_list):
    if len(input_list) < 2:
        return "The list does not have a second largest element."
    
    first_max = second_max = float('-inf')

    for num in input_list:
        if num > first_max:
            second_max = first_max
            first_max = num
        elif num > second_max and num != first_max:
            second_max = num

    return second_max

# Example list
my_list = [12, 34, 56, 78, 90, 45, 23]

second_largest = find_second_largest(my_list)

print("Second largest element:", second_largest)
