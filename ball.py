from turtle import Turtle
import random

BALL_MOVEMENT = 15

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.pu()
        self.color('white')
        self.xmove = BALL_MOVEMENT
        self.ymove = BALL_MOVEMENT
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.xmove
        new_y = self.ycor() + self.ymove
        self.goto(new_x,new_y)

    def ybounce(self):
        # maintain angle laws with the horizontal collision
        self.ymove *= -1 

    def xbounce(self):
        # maintain angle laws with vertical (paddle) collision
        self.xmove *= -1
        self.move_speed *= 0.99

    def reset_position(self):
        self.goto(0,0)
        self.move_speed = 0.1
        self.xbounce()

    
