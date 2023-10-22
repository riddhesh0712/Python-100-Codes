import math

num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: ")

# Calculate the GCD (Greatest Common Divisor)
gcd = math.gcd(num1, num2)

# Calculate the LCM (Least Common Multiple)
lcm = (num1 * num2) // gcd

print(f"GCD of {num1} and {num2} is: {gcd}")
print(f"LCM of {num1} and {num2} is: {lcm}")
