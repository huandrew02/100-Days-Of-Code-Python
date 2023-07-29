from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 22, "normal"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.write(f"Score: {self.score}", False, align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.clear()
        self.updateScoreboard()

    def gameover(self):
        self.goto(0,0)
        self.write("Game Over", False, align=ALIGNMENT, font=FONT)