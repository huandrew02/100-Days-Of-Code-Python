import random

names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")

# spin = random.randint(0, len(names) - 1)
#
# print(f'{names[spin]} is going to buy the meal today!')

# OR

print(f'{random.choice(names)} is going to buy the meal today!')
