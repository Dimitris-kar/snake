from turtle import Turtle
import random

food_colors = ['blue', 'red', 'orange', 'yellow', 'green', 'white', 'pink', 'brown']


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.color("blue")
        self.speed("fastest")
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.refresh()

    def refresh(self):
        self.color(random.choice(food_colors))
        self.goto(random.randint(-280, 280), random.randint(-280, 280))

