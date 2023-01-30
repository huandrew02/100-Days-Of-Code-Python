print("Welcome to the Love Calculator!")

name1 = input("What is your name? \n").lower()
name2 = input("What is their name? \n").lower()


t = name1.count('t') + name2.count('t')
r = name1.count('r') + name2.count('r')
u = name1.count('u') + name2.count('u')
e = name1.count('e') + name2.count('e')
l = name1.count('l') + name2.count('l')
o = name1.count('o') + name2.count('o')
v = name1.count('v') + name2.count('v')

true = t + r + u + e
love = l + o + v + e
love_score = str(true) + str(love)
love_score = int(love_score)

if love_score < 10 or love_score > 90:
    print(f'Your score is {love_score}, you go together like coke and mentos.')
elif 40 <= love_score <= 50:
    print(f'Your score is {love_score}, you are alright together.')
else:
    print(f'Your score is {love_score}')


