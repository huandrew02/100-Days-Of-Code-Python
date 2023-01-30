import random
# from turtle import Turtle, Screen
# aliasing
import turtle as t
timmy = t.Turtle()


# timmy = Turtle()
timmy.shape("circle")


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return r, g, b


# challenge 1 make a square
# for i in range(4):
#     timmy.forward(50)
#     timmy.right(90)

# challenge 2 draw dashed line
# for i in range(15):
#     timmy.forward(10)
#     timmy.up()
#     timmy.forward(10)
#     timmy.down()

# challenge 3 draw different shapes
# colors = ["red", "brown", "green", "yellow", "blue", "cyan", "orange", "pink"]
# sides = 3
# while sides != 10:
#     timmy.color(random.choice(colors))
#     for i in range(sides):
#         timmy.forward(75)
#         timmy.right(360/sides)
#     sides += 1

# challenge 4 random walk
t.colormode(255)

# turns = [0, 90, 180, 270]
# timmy.pensize(10)
timmy.speed(30)
# for i in range(200):
#     timmy.setheading(random.choice(turns))
#     timmy.color(random_color())
#     timmy.forward(30)

# challenge 5 make a spirograph
timmy.pensize(2)
for i in range(72):
    timmy.color(random_color())
    timmy.left(5)
    timmy.circle(100)


t.Screen()
t.exitonclick()
