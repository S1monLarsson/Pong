import turtle
import paddle

class Paddle:
    def __init__(self, name, x):
        self.x = x
        self.y = 0
        self.score = 0
        self.paddle = name

    def setup(self):
        # Init paddle
        self.paddle = turtle.Turtle()
        self.paddle.shape("square")
        self.paddle.color("white")
        self.paddle.penup()
        self.paddle.goto(self.x, 0)
        self.paddle.shapesize(5, 1)

    def get_x(self):
        return self.paddle.xcor()

    def get_y(self):
        return self.paddle.ycor()

    def set_y(self, y):
        self.paddle.sety(y)
        

        
