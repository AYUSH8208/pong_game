from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, x, y):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.penup()

        self.goto(x, y)
        self.shapesize(stretch_len=1, stretch_wid=5)

    def up(self):
        new_y = self.ycor() + 40
        self.goto(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 40
        self.goto(self.xcor(), new_y)
