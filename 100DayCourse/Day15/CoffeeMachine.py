import data

money = 0.0


def update_ingredients(u):
    data.resources['water'] -= data.MENU[u]['ingredients']['water']
    data.resources['milk'] -= data.MENU[u]['ingredients']['milk']
    data.resources['coffee'] -= data.MENU[u]['ingredients']['coffee']


def ingredient_check(u):
    if data.MENU[u]['ingredients']['water'] > data.resources['water']:
        return True
    if data.MENU[u]['ingredients']['milk'] > data.resources['milk']:
        return True
    if data.MENU[u]['ingredients']['coffee'] > data.resources['coffee']:
        return True
    return False


def missing_ingredient(u):
    if data.MENU[u]['ingredients']['water'] > data.resources['water']:
        print("Sorry there is not enough water.")
    if data.MENU[u]['ingredients']['milk'] > data.resources['milk']:
        print("Sorry there is not enough milk.")
    if data.MENU[u]['ingredients']['coffee'] > data.resources['coffee']:
        print("Sorry there is not enough coffee.")


def serve(u, t):
    print(f"Here is your change: ${round(t - data.MENU[u]['cost'], 2)}")
    print(f"Here is your {u} ☕ Enjoy!")


off = False
while not off:
    user = input("What would you like?(espresso/latte/cappuccino): ")
    if user == "off":
        print("Machine turned off!")
        off = True
        break
    elif user == "report":
        print(f"Water: {data.resources['water']}ml\n"
              f"Milk: {data.resources['milk']}ml\n"
              f"Coffee: {data.resources['coffee']}g\n"
              f"Money: ${money}")
        user = input("What would you like?(espresso/latte/cappuccino): ")
    if ingredient_check(user) is False:
        print("Please insert coins.")
        q = int(input("How many quarters: "))
        n = int(input("How many nickels: "))
        d = int(input("How many dimes: "))
        p = int(input("How many pennies: "))
        total = (.25 * q) + (.10 * d) + (.05 * n) + (.01 * p)

        if total > data.MENU[user]['cost']:
            money += data.MENU[user]['cost']
            serve(user, total)
            update_ingredients(user)
        else:
            print("Sorry that's not enough money. Money refunded")
    else:
        missing_ingredient(user)



