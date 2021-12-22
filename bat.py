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
        print(self.ycor())
        if self.ycor() <= 250:
            self.fd(50)

    def down(self):
        print(self.ycor())
        if self.ycor() >= -250:
            self.bk(50)
        
    


