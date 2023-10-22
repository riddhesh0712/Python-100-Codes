# Function to find the intersection of two lists using list comprehension
def list_intersection(list1, list2):
    return [value for value in list1 if value in list2]

# Example lists
list1 = [1, 2, 3, 4, 5]
list2 = [3, 4, 5, 6, 7]

intersection = list_intersection(list1, list2)
print("Intersection of lists:", intersection)
