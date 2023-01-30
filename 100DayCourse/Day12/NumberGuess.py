import random

EASY_LEVEL = 10
HARD_LEVEL = 5

number = random.randint(0, 101) # 0-100
print("Welcome to Number Guessing Game!\nIm thinking of a number between 1 and 100.")


def set_difficulty():
    difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
    if difficulty == 'easy':
        return EASY_LEVEL
    elif difficulty == 'hard':
        return HARD_LEVEL
    print(f"You have {attempts} remaining to guess the number.")


attempts = set_difficulty()

while attempts != 0:
    user = int(input("Make a guess: "))
    if user == number:
        print("Correct!")
        break
    elif user < number:
        attempts -= 1
        print(f"Too low.\nGuess Again.\nYou have {attempts} remaining to guess the number.")
    elif user > number:
        attempts -= 1
        print(f"Too high.\nGuess Again.\nYou have {attempts} remaining to guess the number.")

