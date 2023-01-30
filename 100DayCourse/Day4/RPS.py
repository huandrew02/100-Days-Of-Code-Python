import random

user_score = 0
comp_score = 0

print("Welcome to RockaPaperScizzas!")

options = [0, 1, 2]
# 0 = rock, 1 = paper, 2 = scissors
ascii_hand = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)''', '''
     _______
---'    ____)____
           ______)
          _______)
         _______)
---.__________)''', '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)''']

while True:
    user_input = input("Type Number (0)Rock/(1)Paper/(2)Scissors or Q to quit: ").lower()
    if user_input == 'q':
        break
    if int(user_input) not in options:
        continue

    comp_pick = random.randint(0, 2)
    # 0 = rock, 1 = paper, 2 = scissors

    if int(user_input) == comp_pick:
        print("TIE!")
        print(f"You picked {ascii_hand[int(user_input)]} \nComputer picked {ascii_hand[comp_pick]}\n")

    elif int(user_input) == 0 and comp_pick == 2:
        print("You Win!")
        print(f"You picked {ascii_hand[int(user_input)]} \nComputer picked {ascii_hand[comp_pick]}\n")
        user_score += 1

    elif int(user_input) == 1 and comp_pick == 0:
        print("You Win!")
        print(f"You picked {ascii_hand[int(user_input)]} \nComputer picked {ascii_hand[comp_pick]}\n")
        user_score += 1

    elif int(user_input) == 2 and comp_pick == 1:
        print("You Win!")
        print(f"You picked {ascii_hand[int(user_input)]} \nComputer picked {ascii_hand[comp_pick]}.\n")
        user_score += 1

    else:
        print("You Lose \U0001F613")
        print(f"You picked {ascii_hand[int(user_input)]} \nComputer picked {ascii_hand[comp_pick]}\n")
        comp_score += 1


print(f"Final Scores: \
User: {user_score} \
Computer: {comp_score}")

print("GOODBYE!") 

    

