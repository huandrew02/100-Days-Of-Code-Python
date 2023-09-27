from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
import random

# ...

# Create an AI-controlled paddle for the left side
ai_paddle = Paddle((-350, 0))

# ...

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Top and bottom wall collision
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # AI Paddle movement (simple tracking of the ball's y-coordinate)
    if ai_paddle.ycor() < ball.ycor():
        ai_paddle.go_up()
    elif ai_paddle.ycor() > ball.ycor():
        ai_paddle.go_down()

    # Paddle collision
    if ball.check_collision(r_paddle) or ball.check_collision(ai_paddle):
        ball.bounce_x()

    # right and left paddle missed ball
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.increase_l_score()
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.increase_r_score()

    # Optional: Add a bit of randomness to AI's movement
    # This can make the game more interesting
    # random_delay = random.randint(0, 20)  # Adjust the range as needed
    # time.sleep(random_delay / 10)  # Adjust the divisor for desired speed variation

screen.exitonclick()
