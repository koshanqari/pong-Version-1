from turtle import Turtle
class Bat(Turtle):

    def __init__(self, x):
        super().__init__()
        self.shape("square")
        self.penup()
        self.setheading(90)
        self.shapesize(stretch_len=5, stretch_wid= 1)
        self.goto(x,0)

    def up(self):
        self.fd(10)

    def down(self):
        self.bk(10)
        
    


