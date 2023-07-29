from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong Game")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))

ball = Ball()
scoreboard = Scoreboard()
screen.listen()
screen.onkeypress(r_paddle.go_up, "Up")
screen.onkeypress(r_paddle.go_down, "Down")

screen.onkeypress(l_paddle.go_up, "w")
screen.onkeypress(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Top and bottom wall collision 
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()
    
    # Paddle collision
    if ball.check_collision(r_paddle) or ball.check_collision(l_paddle):
        ball.bounce_x()

    # right and left paddle missed ball
    if ball.xcor() > 380:
        ball.refresh()
        scoreboard.increase_l_score()
    if ball.xcor() < -380:
        ball.refresh()
        scoreboard.increase_r_score()

screen.exitonclick()
