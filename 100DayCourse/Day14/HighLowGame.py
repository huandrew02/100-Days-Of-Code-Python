import art
import game_data
import random

score = 0
A = random.choice(game_data.data)
B = random.choice(game_data.data)
if A == B:
    B = random.choice(game_data.data)
correct = False
while not correct:
    print(art.logo)
    print(f"Compare A: {A['name']}, a {A['description']}, from {A['country']} ")
    print(art.vs)
    print(f"Against B: {B['name']}, a {B['description']}, from {B['country']} ")
    user = input("Who has more followers? Type 'A' or 'B': ")

    if user == 'A' and A['follower_count'] > B['follower_count']:
        score += 1
        B = random.choice(game_data.data)
        print(f"You're right! Current score: {score}")
    elif user == 'B' and A['follower_count'] < B['follower_count']:
        score += 1
        A = random.choice(game_data.data)
        print(f"You're right! Current score: {score}")
    else:
        print(f"Sorry, that's wrong. Final Score: {score}")
        correct = True


