from time import sleep
from turtle import Turtle
class Bat(Turtle):

    def __init__(self, x,y, goto):
        self.x = x
        self.y = y
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid= 1)
        self.goto(goto,0)

    def up(self):
        if self.ycor() <= self.y/2-100:
            self.fd(50)

    def down(self):
        if self.ycor() >= -self.y/2+100:
            self.bk(50)
        
    


