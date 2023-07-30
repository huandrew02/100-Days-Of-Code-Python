import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
screen.listen()
screen.onkeypress(player.go_up, "w")

scoreboard = Scoreboard()
carmanager = CarManager()

car_speed = 0.1

game_is_on = True
while game_is_on:
    time.sleep(car_speed)
    screen.update()

    carmanager.create_car()
    carmanager.move_cars()

    # Player reaches finish line
    if player.ycor() > 280:
        player.refresh()
        scoreboard.increase_score()
        car_speed *= 0.8

    for car in carmanager.all_cars:
        if player.distance(car) < 18:
            game_is_on = False
            scoreboard.gameover()


screen.exitonclick()