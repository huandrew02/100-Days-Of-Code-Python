# Odd or Even

while True:
    num = input("Enter a whole number(press q to stop): ")
    if(num == 'q'):
        quit()

    if int(num)%2 == 0:
        print('This is an even number.')
    else:
        print('This is an odd number.')