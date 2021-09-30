import turtle
import paddle

# A class used to represent a player
class Paddle:
    def __init__(self, name, x):
        self.score = 0
        self.name = name
        self._paddle = turtle.Turtle(shape="square")
        self._paddle.color("white")
        self._paddle.penup()
        self._paddle.goto(x, 0)
        self._paddle.shapesize(5, 1)


    def get_x(self):
        return self._paddle.xcor()

    def get_y(self):
        return self._paddle.ycor()

    def set_y(self, y):
        self._paddle.sety(y)

    def up(self):
        y = self.get_y();
        if y <= 230:
            y += 20
        else:
            y = 250
        self.set_y(y)

    def down(self):
        y = self.get_y()
        if y >= -230:
            y -= 20
        else:
            y = -250
        self.set_y(y)
        

        
