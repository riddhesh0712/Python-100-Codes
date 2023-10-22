# Input coefficients of the quadratic equation
a = float(input("Enter the coefficient a: "))
b = float(input("Enter the coefficient b: "))
c = float(input("Enter the coefficient c: "))

# Calculate the discriminant
discriminant = b**2 - 4*a*c

# Check if the discriminant is positive, negative, or zero
if discriminant > 0:
    # Two real and distinct roots
    root1 = (-b + (discriminant)**0.5) / (2*a)
    root2 = (-b - (discriminant)**0.5) / (2*a)
    print(f"Two real roots: {root1} and {root2}")
elif discriminant == 0:
    # One real root (repeated)
    root1 = -b / (2*a)
    print(f"One real root: {root1}")
else:
    # Complex roots
    real_part = -b / (2*a)
    imaginary_part = (abs(discriminant)**0.5) / (2*a)
    print(f"Complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i")
