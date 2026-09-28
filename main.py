from turtle import Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time

SCREEN_H = 600
SCREEN_L = 800
SCREEN_COLOR = 'black'

screen = Screen()
screen.setup(width=SCREEN_L,height=SCREEN_H)
screen.bgcolor(SCREEN_COLOR)
screen.tracer(0)
screen.title('The Ping Pong Game!')
screen.listen()

paddle_r = Paddle(350,0)
paddle_l = Paddle(-350,0)
# screen.update()
screen.onkeypress(paddle_r.up,'Up') # adding paranthesis after function name wont work in cases of user input as while interpreting the code, the function executes at that very moment
screen.onkeypress(paddle_r.down,'Down')
screen.onkeypress(paddle_l.up,'w') # adding paranthesis after function name wont work in cases of user input as while interpreting the code, the function executes at that very moment
screen.onkeypress(paddle_l.down,'s')

ball = Ball()
score = Scoreboard()

game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(ball.move_speed)
    ball.move()

    # detect wall collision
    if ball.ycor() > 290 or ball.ycor() < -290:
        ball.ybounce()

    # detect right paddle collsion
    if ball.xcor() > 330 and ball.xcor() < 350 and ball.distance(paddle_r) < 50:
        ball.xbounce()
    elif ball.xcor() < -330 and ball.xcor() > -350 and ball.distance(paddle_l) < 50:
        ball.xbounce()

    # out of bound detection
    if ball.xcor() > 400:
        score.l_point()
        ball.reset_position()
    elif ball.xcor() < -400:
        score.r_point()
        ball.reset_position()

    # game over 
    if score.r_score >= 10 or score.l_score >= 10:
        score.game_over()
        game_is_on = False
screen.exitonclick()
