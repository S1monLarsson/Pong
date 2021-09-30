# Import required library
import turtle
from paddle import Paddle

# Gamescreen
wn = turtle.Screen()
wn.title("Pong")
wn.bgcolor("Black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Left paddle
paddle_l = Paddle("Player A", -350)

# Right paddle
paddle_r = Paddle("Player B", 350)

# Ball
ball = turtle.Turtle(shape="circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.15
ball.dy = 0.15

# Middle line
line = turtle.Turtle(shape="square")
line.color("white")
line.penup()
line.shapesize(30, 0.1)

# Score
score = turtle.Turtle()
score.penup()
score.color("white")
score.speed(0)
score.hideturtle()
score.goto(0, 250)
score.write("{}            {}".format(paddle_l.score, paddle_r.score), 
          align="center", font=("Courier", 24, "normal"))

# Keyboard binding, paddle moves on release
wn.listen()
wn.onkey(paddle_l.up, "w")
wn.onkey(paddle_l.down, "s")
wn.onkey(paddle_r.up, "Up")
wn.onkey(paddle_r.down, "Down")
wn.onkey(wn.bye, "q")


# Functions

# Write updated score
def update_score():
    score.clear()
    score.write("{}            {}".format(paddle_l.score, paddle_r.score), 
                align="center", font=("Courier", 24, "normal")) 

# Check if padel is behind the ball
def paddle_bounce(paddle, x):
    if (paddle.get_y()-50) <= ball.ycor() <= (paddle.get_y()+50):
        ball.setx(x)
        ball.dx *= -1 
        return True
    else:
        return False

# Update score and reset ball
def goal(paddle):
    paddle.score+=1
    ball.goto(0,0)
    ball.dx *= -1
    if paddle.score == 10:
        score.clear()
        score.write("{} won!  ".format(paddle.name), 
                    align="right", font=("Courier", 24, "normal"))
        wn.mainloop()
    else:
        update_score()
        

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
    
    # Ball has reached right edge, 
    # should be goal or paddle bounce
    if ball.xcor() > 330:
        if not paddle_bounce(paddle_r, 330):
            goal(paddle_l)

    # Ball has reached left edge, 
    # should be goal or paddle bounce
    if ball.xcor() < -330:
        if not paddle_bounce(paddle_l, -330):
            goal(paddle_r)

        




