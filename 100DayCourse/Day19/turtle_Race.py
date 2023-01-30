from turtle import Turtle, Screen
import random

race_is_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_Bet = screen.textinput(title="Make a bet", prompt="Which turtle will win the race? Choose a color"
                                                       "(red/orange/yellow/green/blue/purple:")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70, -40, -10, 20, 50, 80]
all_turtle = []

for i in range(6):
    turtle = Turtle(shape="turtle")
    turtle.color(colors[i])
    turtle.up()
    turtle.goto(x=-230, y=y_pos[i])
    all_turtle.append(turtle)

if user_Bet:
    race_is_on = True

while race_is_on:
    for turtle in all_turtle:
        if turtle.xcor() > 230:
            race_is_on = False
            winner = turtle.pencolor()
            if user_Bet == winner:
                print(f"You win the bet! The {winner} turtle won!")
            else:
                print(f"You lost the bet. The {winner} turtle has won!")
        turtle.forward(random.randint(0, 10))

screen.exitonclick()