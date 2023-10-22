#Calculate compound interest
def calculate_compound_interest(principal, rate, time, compounding_frequency):
    # Convert the annual interest rate to decimal
    rate = rate / 100
    
    # Calculate the future value of the investment/loan
    amount = principal * (1 + rate / compounding_frequency) ** (compounding_frequency * time)
    
    # Calculate the interest earned/paid
    interest = amount - principal
    
    return amount, interest

# Input principal amount, annual interest rate, time, and compounding frequency
principal = float(input("Enter the principal amount: "))
rate = float(input("Enter the annual interest rate (in percentage): "))
time = float(input("Enter the number of years: "))
compounding_frequency = int(input("Enter the compounding frequency per year (e.g., 12 for monthly): "))

# Calculate compound interest
future_value, interest_earned = calculate_compound_interest(principal, rate, time, compounding_frequency)

# Print the results
print(f"Principal Amount: ${principal:.2f}")
print(f"Future Value: ${future_value:.2f}")
print(f"Interest Earned: ${interest_earned:.2f}")
