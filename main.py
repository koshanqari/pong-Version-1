import scoreboard
import turtle
import ball
import time
import bat
#Constants
XCOR = 1000
YCOR = 600

#Objects initialization:
my_score = scoreboard.Score(XCOR,YCOR)
my_ball =  ball.Ball()
my_border = scoreboard.Score(XCOR, YCOR)
my_bat1 = bat.Bat(XCOR, YCOR, XCOR/2+10)
my_bat2 = bat.Bat(XCOR, YCOR,-(XCOR/2+10))

#Object Attibutes and Methods:
my_screen = turtle.Screen()
my_border.make_borders()


#Screen Properties 
my_screen.screensize(XCOR,YCOR)
my_screen.title("K.Qari's Pong")
my_screen.listen()



#screen listening
my_screen.onkey(my_bat1.up, "Up")
my_screen.onkey(my_bat1.down, "Down")
my_screen.onkey(my_bat2.up, "w")
my_screen.onkey(my_bat2.down, "s")


#Game Loop
start = True
while start == True:
    time.sleep(.01)
    
    my_ball.move()
    if my_ball.xcor() >XCOR/2-14 or my_ball.xcor() < -XCOR/2+14:
        my_ball.snails_law_x()
    elif my_ball.ycor() >YCOR/2-14 or my_ball.ycor() < -YCOR/2+14:
        my_ball.snails_law_y()


        






#keep this in the end to exit the screen finally 
my_screen.exitonclick()
