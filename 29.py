while True:
    user_input = input("Enter a number (or 'q' to quit): ")
    
    if user_input.lower() == 'q':
        break  # Exit the loop if the user enters 'q'
    
    try:
        number = float(user_input)  # Convert the input to a floating-point number
        total += number  # Add the number to the total
    except ValueError:
        print("Invalid input. Please enter a valid number or 'q' to quit.")

# Display the sum of the entered numbers
print(f"The sum of the entered numbers is: {total}")