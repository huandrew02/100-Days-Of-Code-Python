from turtle import Turtle
from random import randrange
import random
class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color(randrange(255), randrange(255), randrange(255))
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        self.color(randrange(255), randrange(255), randrange(255))
        randx = random.randint(-280, 280)
        randy = random.randint(-280, 280)
        self.goto(randx, randy) 

