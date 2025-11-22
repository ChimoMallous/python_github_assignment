print("Welcome to my Python program!")

# Get users weekly savings amount
savings = input("How much money do you save per week? ")

# Check if user input is a numerical value
try:
    savings = float(savings)
# Exit if user inputs non numeric value
except ValueError:
    print("Please enter a valid number.")
    exit()

# Calculate users total yearly savings
yearly_savings = savings * 52

# Display final output
print(f"You are on track to save ${yearly_savings:,.2f} in a year")