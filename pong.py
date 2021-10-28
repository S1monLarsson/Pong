# Import required library
import turtle
import keyboard
import time
import random
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

# Number of players (1 or 2)
players = 0

# Winning threshold
winning_score = 10

# Variables to keep track of when computer player is allowed to move
move = False
startTime = time.time()

# Ball
ball = turtle.Turtle(shape="circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.default_speed = 0.50
# Set x and y speed, add some noice to y start speed
ball.dx = ball.default_speed
ball.dy = ball.default_speed + random.uniform(-0.1, 0.1)
# Increase ball speed every bounce, speed += ball.increase * speed
ball.increase = 0.05

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


# Functions

# Write updated score
def update_score():
    score.clear()
    score.write("{}            {}".format(paddle_l.score, paddle_r.score), 
                align="center", font=("Courier", 24, "normal")) 

# Check if padel is behind the ball
def paddle_bounce(paddle, x):
    # Increase ball speed and reverse direction
    if (paddle.get_y()-50) <= ball.ycor() <= (paddle.get_y()+50):
        ball.setx(x)
        ball.dx *= -1 
        print(ball.dy)
        ball.dx += ball.increase * ball.dx
        ball.dy += ball.increase * ball.dy
        return True
    else:
        return False

# Update score and reset ball
def goal(paddle):
    paddle.score+=1
    ball.goto(0,0)
    ball.dx *= -1
    if ball.dx > 0:
        ball.dx = ball.default_speed
    else: 
        ball.dx = -ball.default_speed
    ball.dy = ball.default_speed + random.uniform(-0.2, 0.2)
    if random.random() < 0.5:
        ball.dy *= -1
    ball.default_speed
    # Check if the player won
    if paddle.score == winning_score:
        score.clear()
        score.write("{} won!  ".format(paddle.name), 
                    align="right", font=("Courier", 24, "normal"))
        wn.mainloop()
    else:
        update_score()

# Computer actions
def move_c_paddle(paddle_y, ball_y):
    # Move paddle to be behind ball
    if paddle_y < ball_y:
        paddle_l.up()
    elif paddle_y > ball_y: 
        paddle_l.down()

# Make player choose number of players
players = wn.numinput("#Players", "Type number of players (1 or 2)", 
                      minval=1, maxval=2)

# Game loop
while True:
    wn.update()

    # Computer is allowed to move every other secound
    # This is to make it possible to beat the computer
    # Toggle the move variable to get this behaviour
    if time.time() - startTime > 2:
        move = False
        startTime = time.time()
    elif time.time() - startTime > 0.5:
        move = True

    # Check for keypresses
    if keyboard.is_pressed("Up"):
        paddle_r.up()

    if keyboard.is_pressed("Down"):
        paddle_r.down()

    if keyboard.is_pressed('w') and players == 2:
        paddle_l.up()

    if keyboard.is_pressed('s') and players == 2:
        paddle_l.down()

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check if 1-player mode and computer is allowed to move
    if players == 1 and move:
        # Calculate expected y coordinate at bounce
        # Don't consider wall bounce in order to send some false values
        # to the computer pad in order to make it beatable 
        y = ball.ycor() + ball.dy * (330 - abs(ball.xcor())) / abs(ball.dx)
        # Move to calculated y position
        move_c_paddle(paddle_l.get_y(), y)

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


        




