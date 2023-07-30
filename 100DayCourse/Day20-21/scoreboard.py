from turtle import Turtle

ALIGNMENT = "center"
FONT = "Courier", 22, "normal"
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.highscore = int(data.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.updateScoreboard()
        self.hideturtle()

    def updateScoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High Score: {self.highscore}", False, align=ALIGNMENT, font=FONT)

    def increaseScore(self):
        self.score += 1
        self.updateScoreboard()

    def reset(self):
        if self.score > self.highscore:
            self.highscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(str(self.highscore))
        self.score = 0
        self.updateScoreboard()
