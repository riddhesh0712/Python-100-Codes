def is_perfect_number(number):
    if number <= 1:
        return False

    divisors_sum = 1  # Start with 1 since all numbers are divisible by 1

    # Check divisors from 2 up to the square root of the number
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            divisors_sum += i
            if i != number // i:  # Avoid adding the same divisor twice
                divisors_sum += number // i

    return divisors_sum == number

# Input a number
num = int(input("Enter a number: "))

if is_perfect_number(num):
    print(f"{num} is a perfect number.")
else:
    print(f"{num} is not a perfect number.")
