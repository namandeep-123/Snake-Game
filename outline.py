from turtle import Turtle

COLOR = "White"
OUTLINE_DISTANCE = 500
RIGHT_MOVE = 90


class Outline(Turtle):

    def __init__(self):
        super().__init__()
        self.setheading(225)
        self.penup()
        self.hideturtle()
        self.forward(350)
        self.setheading(RIGHT_MOVE)
        self.color(COLOR)
        self.pendown()
        self.outline()

    def outline(self):
        for _ in range(4):
            self.forward(OUTLINE_DISTANCE)
            self.right(RIGHT_MOVE)
