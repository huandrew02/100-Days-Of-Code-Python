############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.
import random
from art import logo
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]


def isover21(card):
    if hasAce(card) > 21:
        return True


def hasAce(user):
    Sum=0
    for element in user:
        Sum += element
    for i in user:
        if i == 11 and Sum > 21:
            return Sum - 10
    return Sum


def drawCards():
    done = False
    while not done:
        if sum(cCard) < 16:
            cCard.append(random.choice(cards))
        anotherCard = input("Type 'y' to get another card, type 'n' to pass: ")
        if anotherCard == 'n':
            done = True
            break
        uCard.append(random.choice(cards))

        print(f"Your cards: {uCard}, current score: {hasAce(uCard)}")

        if isover21(uCard) == True:
            print("You lose!")
            break

if input("Do you want to play backjack? 'y' or 'n': ") == 'n':
    quit();
print(logo)

donePlaying = False
while not donePlaying:
    uCard = random.choices(cards, k=2)
    cCard = random.choices(cards, k=2)
    # Starting cards
    print(f"Your cards: {uCard}, current score: {hasAce(uCard)}")
    print(f"Computer's first card: {cCard[0]}")

    drawCards()
        
    print(f"Your final hand: {uCard}, final score: {hasAce(uCard)}")
    print(f"Computer's final hand: {cCard}, final score: {hasAce(cCard)}")

    if hasAce(uCard) == hasAce(cCard):
        print("Draw!🙃")
    elif hasAce(uCard) == 21:
        print("Win with a Blackjack")
    elif hasAce(cCard) == 21:
        print("Lose, opponent has Blackjack 😱")
    elif hasAce(uCard) > 21:
        print("You went over. You lose 😭")
    elif hasAce(cCard) > 21:
        print("Opponent went over. You win 😁")
    elif hasAce(uCard) > hasAce(cCard):
        print("You win 😃")
    else:
        print("You lose 😤")
    
    if input("Play again? enter 'y' or 'n': ") == 'n':
        donePlaying = True