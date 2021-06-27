from turtle import Turtle
import random
RANDOM_COLOR = ["green4", "blue", "red", "yellow", "green4", "green4"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color(random.choice(RANDOM_COLOR))
        self.speed("fastest")
        self.refresh()
        self.col = ""

    def refresh(self):
        self.color(random.choice(RANDOM_COLOR))
        random_x = random.randint(-240, 240)
        random_y = random.randint(-240, 240)
        self.goto(random_x, random_y)
