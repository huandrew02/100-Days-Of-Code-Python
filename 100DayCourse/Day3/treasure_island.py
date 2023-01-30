print('''
                           ___
                          ( ((
                           ) ))
  .::.                    / /(
 'M .-;-.-.-.-.-.-.-.-.-/| ((::::::::::::::::::::::::::::::::::::::::::::::.._
(J ( ( ( ( ( ( ( ( ( ( ( |  ))   -====================================-      _.>
 `P `-;-`-`-`-`-`-`-`-`-\| ((::::::::::::::::::::::::::::::::::::::::::::::''
  `::'                    \ \(
                           ) ))
                          (_((

''')

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

left_right = input("You have come upon a sign that cannot be read anymore. It points to two direction, which way do "
                   "you want to go? Type 'left' or 'right': \n")

if left_right == 'left':
    river = input("There is a river and the current is strong. Do you cross or wait? Type 'cross' or 'wait': \n")
    if river == 'wait':
        boat = input("Three boats came. First boat has 5 strong men. Second boat has a SUS man. Third boat has 3 "
                     "females. Which boat do you board? Type 'boat 1' or 'boat 2' or 'boat 3' : \n")
        if boat == 'boat 2':
            print('ALIVE BUT HELPLESS. You are forced to be his play thing...')
        elif boat == 'boat 3':
            print('ALIVE and HAPPY. You ride into the sunset with the 3 women but without the treasure...')
        elif boat == 'boat 1':
            print('Congrats! The 5 strong men seemed to have found the treasure and wants to split it with you!')
        else:
            print("DEAD! Not a choice, you have been smited!")

    else:
        print('DEAD. You were almost there but then multiple hungry alligators appeared...')
else:
    print('DEAD. You stepped on a landmine...')


