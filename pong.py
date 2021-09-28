# Import required library
import turtle
import keyboard
from paddle import Paddle

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Score
score_l = 0
score_r = 0

# Left paddle
paddle_l = Paddle("paddle_l", -350)
paddle_l.setup()
#paddle_l.shape("square")
#paddle_l.color("white")
#paddle_l.penup()
#paddle_l.goto(-350, 0)
#paddle_l.shapesize(5, 1)

# Right paddle
paddle_r = turtle.Turtle()
paddle_r.shape("square")
paddle_r.color("white")
paddle_r.penup()
paddle_r.goto(350, 0)
paddle_r.shapesize(5, 1)

# Ball
ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Middle line
line = turtle.Turtle()
line.shape("square")
line.color("white")
line.penup()
line.shapesize(30, 0.1)

# Pen
pen = turtle.Turtle()
pen.penup()
pen.color("white")
pen.speed(0)
pen.hideturtle()
pen.goto(0, 250)
pen.write("{}            {}".format(score_l, score_r), 
          align="center", font=("Courier", 24, "normal"))


def paddle_l_up():
    y = paddle_l.get_y()
    if y <= 230:
        y += 20
    else:
        y = 250
    paddle_l.set_y(y)

def paddle_l_down():
    y = paddle_l.get_y()
    if y >= -230:
        y -= 20
    else:
        y = -250
    paddle_l.set_y(y)

def paddle_r_up():
    y = paddle_r.ycor()
    if y <= 230:
        y += 20
    else:
        y = 250
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    if y >= -230:
        y -= 20
    else:
        y = -250
    paddle_r.sety(y)

def update_score():
    pen.clear()
    pen.write("{}            {}".format(score_l, score_r), 
                align="center", font=("Courier", 24, "normal")) 

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")


# Game loop
while True:
    wn.update()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Border checking
    if ball.ycor() > 290:
        ball.sety(290)
        ball.dy *= -1 

    if ball.ycor() < -290:
        ball.sety(-290)
        ball.dy *= -1 
    
    if ball.xcor() > 330:
        # Check if padel is behind the ball
        if (paddle_r.ycor()-50) <= ball.ycor() <= (paddle_r.ycor()+50):
            ball.setx(330)
            ball.dx *= -1 
        else:
            score_l+=1
            ball.goto(0,0)
            ball.dx *= -1 
            update_score()

    if ball.xcor() < -330:
        # Check if padel is behind the ball
        if (paddle_l.ycor()-50) <= ball.ycor() <= (paddle_l.ycor()+50):
            ball.setx(-330)
            ball.dx *= -1 
        else:
            score_r+=1
            ball.goto(0,0)
            ball.dx *= -1
            update_score()


    # Exit on q key press
    keyboard.on_press_key("q", lambda _:wn.bye())




