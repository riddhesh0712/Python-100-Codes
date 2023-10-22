#Find the prime factors of a number
def prime_factors(n):
    factors = []
    
    # Divide by 2 while it's even
    while n % 2 == 0:
        factors.append(2)
        n //= 2
    
    # Divide by odd numbers starting from 3
    for i in range(3, int(n**0.5) + 1, 2):
        while n % i == 0:
            factors.append(i)
            n //= i
    
    # If n is still greater than 1, it's a prime factor itself
    if n > 1:
        factors.append(n)
    
    return factors

# Input a number
num = int(input("Enter a number: "))

# Find and print the prime factors
factors = prime_factors(num)
print(f"Prime factors of {num}: {factors}")
