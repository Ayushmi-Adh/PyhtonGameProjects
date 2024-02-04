from turtle import Turtle
import random


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("red")
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.speed("fastest")
        self.new_location()

    def new_location(self):
        x_cord = random.randint(-280, 280)
        y_cord = random.randint(-280, 280)
        self.goto(x_cord, y_cord)

