print("Welcome to the tip calculator!")
bill = float(input("What was the total bill? "))
tipPercentage = float(input("How much tip would you like to give? 10, 12, or 15? "))
numPeople = float(input("How many people to split the bill? "))


eachPerson = (bill + (bill * (tipPercentage / 100.00))) / numPeople
print(f"Each person should pay: {eachPerson}") 