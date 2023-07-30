from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-280, 250)
        self.write(f"Level: {self.level}", align="left", font=FONT)

    def increase_score(self):
        self.level += 1
        self.update_scoreboard()

    def gameover(self):
        self.goto(0, 0)
        self.write("Game Over", False, align="center", font=FONT)


