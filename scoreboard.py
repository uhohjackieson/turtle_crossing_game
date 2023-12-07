from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("black")
        self.penup()
        self.goto(-230, 250)
        self.score = 0
        self.write(f"Level: {self.score}", align="center", font=FONT)
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-230, 250)
        self.write(f"Level: {self.score}", align="center", font=FONT)

    def scored(self):
        self.score += 1
        self.update_score()

    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
