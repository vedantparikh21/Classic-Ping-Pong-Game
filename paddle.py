from turtle import Turtle

PADDLE_SZ = 3
PADDLE_COLOR = 'white'
MOVE_DISTANCE = 20
UP = 90
DOWN = 270

class Paddle(Turtle):
    def __init__(self,xcord,ycord):
        super().__init__()
        self.create_paddle(xcord,ycord)

    def create_paddle(self,xcord,ycord):
        self.pu()
        self.color(PADDLE_COLOR)
        self.shape('square')
        self.shapesize(stretch_len=1,stretch_wid=5)
        self.speed('fastest')
        self.goto(xcord,ycord)

    def up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(),new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(),new_y)