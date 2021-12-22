import scoreboard
import turtle
import ball
import time
import bat
#Constants
XCOR = 600
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

    my_bat1.pos_update()
    my_bat2.pos_update()

    # print(my_bat1.bat_pos)
    # print(my_bat2.bat_pos)
    my_ball.move()
    print(my_ball.position())
    print(my_bat1.bat_pos[0])
    # for i in range(5): 
    if my_ball.distance(my_bat1.bat_pos[0]) < 30 or my_ball.distance(my_bat1.bat_pos[1]) < 30 or my_ball.distance(my_bat1.bat_pos[2]) < 30 or my_ball.distance(my_bat1.bat_pos[3]) < 30 or my_ball.distance(my_bat1.bat_pos[4]) < 30 or my_ball.distance(my_bat2.bat_pos[0]) < 30 or my_ball.distance(my_bat2.bat_pos[1]) < 30 or my_ball.distance(my_bat2.bat_pos[2]) < 30 or my_ball.distance(my_bat2.bat_pos[3]) < 30 or my_ball.distance(my_bat2.bat_pos[4]) < 30:
        my_ball.snails_law_x()
        my_score.score_up()
    elif my_ball.xcor() >XCOR/2 or my_ball.xcor() < -XCOR/2:
        # my_score.score_up()
        # my_ball.snails_law_x()
        my_score.game_over()
        start = False
    elif my_ball.ycor() >YCOR/2-14 or my_ball.ycor() < -YCOR/2+14:
        my_ball.snails_law_y()


        






#keep this in the end to exit the screen finally 
my_screen.exitonclick()
