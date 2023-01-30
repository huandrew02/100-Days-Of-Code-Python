# Tip Calculator

print("Welcome to the tip calculator")

total = float(input("What was the total bill? $"))
split = float(input("How many people to split the bill? "))
tip =  float(input("What percentage tip would you like to give? 10, 12, or 15? "))

tip_amt = total * (tip/100)
per_person = (total + tip_amt)/split

print(f"Each person should pay: ${'{:.2f}'.format(per_person)}")
# {:.2f} gets the 2 decimals 