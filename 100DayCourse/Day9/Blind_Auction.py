import art
from replit import clear

print(art.logo)
bidders = []


def add_bidders(n, b):
    new_bidder = {"name": n, "bid": b}
    bidders.append(new_bidder)


more_bidders = True
while more_bidders:
    name = input("What is your name?: ")
    bid = int(input("What is your bid?: $"))
    add_bidders(name, bid)

    again = input("Are there any other bidders? Type 'yes' or 'no.\n")
    if again == "no":
        break
    clear()

highest_bid = 0
highest_bidder = ""
for i in bidders:
    if i["bid"] >= highest_bid:
        highest_bid = i["bid"]
        highest_bidder = i["name"]
print(f"The winner is {highest_bidder} with a bid of ${highest_bid}.")
