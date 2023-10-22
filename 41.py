# Function to calculate the nth term of an arithmetic progression
def nth_term_of_ap(a1, n, d):
    nth_term = a1 + (n - 1) * d
    return nth_term

# Input the first term, position of the term (n), and the common difference (d)
a1 = float(input("Enter the first term (a1): "))
n = int(input("Enter the position of the term you want to find (n): "))
d = float(input("Enter the common difference (d): "))

# Calculate the nth term
nth_term = nth_term_of_ap(a1, n, d)

# Print the result
print(f"The {n}th term of the arithmetic progression is: {nth_term}")
