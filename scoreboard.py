from turtle import Turtle
FONT = ("Courier", 18, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-280, 250)

        self.level = 1

    def update_score(self):
        self.clear()
        self.write(f"LEVEL: {self.level}", font=FONT)

    def levelup(self):
        self.level += 1

    def gameover(self):
        self.goto(-50, 0)
        self.write("GAME OVER", font=FONT)

