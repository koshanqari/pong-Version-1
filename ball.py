
from turtle import Turtle
import random




class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.setheading(random.randint(-45,45))


    def move(self):
        self.fd(10)

    def snails_law_y(self):
        self.setheading(360-self.heading())
    def snails_law_x(self):
        self.setheading(180-self.heading())






    
        