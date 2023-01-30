from turtle import Turtle
STARTING_POS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.bodies = []
        self.create_snake()
        self.head = self.bodies[0]
        self.move()
        self.up()
        self.down()
        self.left()
        self.right()

    def create_snake(self):
        for i in STARTING_POS:
            body = Turtle(shape="square")
            body.penup()
            body.color("white")
            body.goto(i)
            self.bodies.append(body)

    def move(self):
        for body_num in range(len(self.bodies) - 1, 0, -1):
            # gets previous body location
            new_x = self.bodies[body_num - 1].xcor()
            new_y = self.bodies[body_num - 1].ycor()
            self.bodies[body_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
