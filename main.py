import scoreboard
import turtle
import ball
import time
import bat

#Objects:
my_score = scoreboard.Score()
my_screen = turtle.Screen()
my_ball =  ball.Ball()
my_bat1 = bat.Bat(350)
my_bat2 = bat.Bat(-350)

#Screen Properties 
my_screen.screensize(600,600)
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
    if my_ball.xcor() >320 or my_ball.xcor() < -320:
        my_ball.snails_law_x()
    elif my_ball.ycor() >320 or my_ball.ycor() < -310:
        my_ball.snails_law_y()


        






#keep this in the end to exit the screen finally 
my_screen.exitonclick()
