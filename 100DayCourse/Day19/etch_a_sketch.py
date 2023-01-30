from turtle import Turtle, Screen

leo = Turtle()
leo.speed(10)
leo.pensize(3)


def move_forward():
    leo.forward(20)


def move_backward():
    leo.backward(20)


def rotate_left():
    leo.left(30)


def rotate_right():
    leo.right(30)


def clear_screen():
    leo.clear()
    leo.up()
    leo.home()
    leo.down()


screen = Screen()
screen.listen()
screen.onkey(key="Up", fun=move_forward)
screen.onkey(key="Down", fun=move_backward)
screen.onkey(key="Left", fun=rotate_left)
screen.onkey(key="Right", fun=rotate_right)
screen.onkey(key="c", fun=clear_screen)
screen.exitonclick()
