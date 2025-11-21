print("Welcome to my Python program!")

savings = input("How much money do you save per week? ")

try:
    savings = float(savings)
except ValueError:
    print("Please enter a valid number.")
    exit()
    
yearly_savings = savings * 52

print(f"You are on track to save ${yearly_savings} in a year")