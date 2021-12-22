from turtle import Turtle


class Score(Turtle):
    '''This blueprint(class) will make the object into scoreboard. It has only two methods
    1. score_up(): That will increase the score once called
    2. game_over(): This will display GAME OVER on the display'''

    def __init__(self,x,y):
        self.x = x
        self.y = y
        super().__init__()
        self.shape("square")
        self.hideturtle()
        self.penup()
        self.goto(-20,y/2)
        self.num = 0
        self.write(f'Score : {self.num}', font=('Arial', 12, 'normal'))

    
    def score_up(self):
        self.num += 1
        self.clear()
        self.write(f'Score : {self.num}', font=('Arial', 12, 'normal'))

    def game_over(self):
        self.goto(0,0)
        self.write(f'Game Over', align='center',font=('Arial', 12, 'normal'))
        self.goto(0,-20)
        self.write(f'Thanks for playing KQari\'s pong', align='center',font=('Arial', 12, 'normal'))

    def make_borders(self):
        self.pencolor('red')
        # self.hideturtle()
        self.speed("fastest")
        self.penup()
        self.goto(-self.x/2,-self.y/2)
        self.pendown()
        self.goto(self.x/2,-self.y/2)
        self.goto(self.x/2,self.y/2)
        self.goto(-self.x/2,self.y/2)
        self.goto(-self.x/2,-self.y/2)
