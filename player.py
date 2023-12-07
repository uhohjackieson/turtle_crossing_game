from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.left(90)
        self.starting_line()

    def finish_line(self):
        if self.ycor() > 290:
            return True
        else:
            return False

    def reset(self):
        self.clear()
        self.goto(STARTING_POSITION)

    def go_up(self):
        new_y = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - MOVE_DISTANCE
        self.goto(self.xcor(), new_y)

    def starting_line(self):
        self.goto(STARTING_POSITION)
