
# Import required library
import turtle
import os
import keyboard

wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Left paddle
paddle_l = turtle.Turtle()
paddle_l.shape("square")
paddle_l.color("white")
paddle_l.penup()
paddle_l.goto(-350, 0)
paddle_l.shapesize(5, 1)

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


def paddle_l_up():
    y = paddle_l.ycor()
    y += 20
    paddle_l.sety(y)

def paddle_l_down():
    y = paddle_l.ycor()
    y -= 20
    paddle_l.sety(y)

def paddle_r_up():
    y = paddle_r.ycor()
    y += 20
    paddle_r.sety(y)

def paddle_r_down():
    y = paddle_r.ycor()
    y -= 20
    paddle_r.sety(y)

# Keyboard binding
wn.listen()
wn.onkeypress(paddle_l_up, "w")
wn.onkeypress(paddle_l_down, "s")
wn.onkeypress(paddle_r_up, "Up")
wn.onkeypress(paddle_r_down, "Down")

times_lost = 0
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
            times_lost+=1
            wn.title("lost: " + str(times_lost))
            ball.goto(0,0)
            ball.dx *= -1 

    if ball.xcor() < -330:
        # Check if padel is behind the ball
        if (paddle_r.ycor()-50) <= ball.ycor() <= (paddle_r.ycor()+50):
            ball.setx(-330)
            ball.dx *= -1 
        else:
            times_lost+=1
            wn.title("lost: " + str(times_lost))
            ball.goto(0,0)
            ball.dx *= -1 


    # Exit on q key press
    keyboard.on_press_key("q", lambda _:wn.bye())




