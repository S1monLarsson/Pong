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

# 1 or 2 players
computer = True

# Ball
ball = turtle.Turtle(shape="circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.default_speed = 0.15
ball.dx = ball.default_speed
ball.dy = ball.default_speed
ball.increase = 0.01
loops = 0

# Ball position to make computer player
old_ball_x = 0
old_ball_y = 0

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

# Keyboard binding, paddle moves on release when 2 players
# Otherwise on push down
wn.listen()
if not computer:
    wn.onkey(paddle_l.up, "w")
    wn.onkey(paddle_l.down, "s")
    wn.onkey(paddle_r.up, "Up")
    wn.onkey(paddle_r.down, "Down")
else:
    wn.onkeypress(paddle_r.up, "Up")
    wn.onkeypress(paddle_r.down, "Down")
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
    ball.dx = ball.default_speed
    ball.dy = ball.default_speed
    ball.default_speed
    if paddle.score == 10:
        score.clear()
        score.write("{} won!  ".format(paddle.name), 
                    align="right", font=("Courier", 24, "normal"))
        wn.mainloop()
    else:
        update_score()

# Computer actions
def move_c_paddle(paddle_y, ball_y):
    if paddle_y+20 < ball_y:
        paddle_l.up()
    elif paddle_y-20 > ball_y: paddle_l.down()
        

# Game loop
while True:
    wn.update()


    # Set old ball coordinates
    old_ball_x = ball.xcor()
    old_ball_y = ball.ycor()

    # Increase speed of ball
    if loops == 600: # Change this to time
        print(ball.dx)
        ball.dx += ball.increase * ball.dx
        ball.dy += ball.increase * ball.dy
        loops = 0
    

    # Move ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Move computer player
    move_c_paddle(paddle_l.get_y(), ball.ycor())

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


    loops += 1
        




