from turtle import Turtle
import random

# make the class - Food inherited from Turtle class
class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.color('red')
        self.penup()
        self.speed('fastest')
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.random_position()

    # randomly place the food on screen
    def random_position(self):
        x = random.randint(-280,280)
        y = random.randint(-280,280)
        self.goto(x,y)