
from turtle import *
from random import *
import time

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.shapesize(0.6,0.6)
        self.color("Blue")
        self.penup()
        self.refresh()

    def refresh(self):
        self.x_cor = randint(-280,280)
        self.y_cor = randint(-280,260)
        self.goto(self.x_cor,self.y_cor)



