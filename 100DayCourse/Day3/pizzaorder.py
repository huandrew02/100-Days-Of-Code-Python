print("Welcome to Python Pizza Deliveries!")

size = input("What size pizza do you want? S, M, or L ").lower()
add_pepperoni = input("Do you want pepperoni? Y or N ").lower()
extra_cheese = input("Do you want extra cheese? Y or N ").lower()

total = 0

if size == 's':
    total += 15
    if add_pepperoni == 'y':
        total += 2
    if extra_cheese == 'y':
        total += 1

elif size == 'm':
    total += 20
    if add_pepperoni == 'y':
        total += 3
    if extra_cheese == 'y':
        total += 1

elif size == 'l':
    total += 25
    if add_pepperoni == 'y':
        total += 3
    if extra_cheese == 'y':
        total += 1


print(f'Your final bill is ${total}')
