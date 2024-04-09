# simple Pong game

import turtle
import time
import tkinter

# windows screen
wd = turtle.Screen()
wd.title("Classic Pong")
wd.bgcolor("black")
wd.setup(width=800, height=600)
wd.tracer(0)  # Set the animation delay to 0 for manual updating

score_a = 0
score_b = 0
delay = 0.0001  # Set a small delay for smoother animation

# Paddle A
paddle_a = turtle.Turtle()
paddle_a.color("white")
paddle_a.speed(0)
paddle_a.shape("square")
paddle_a.shapesize(stretch_wid=5, stretch_len=1)
paddle_a.penup()
paddle_a.goto(-350, 0)

# Paddle B
paddle_b = turtle.Turtle()
paddle_b.color("white")
paddle_b.speed(0)
paddle_b.shape("square")
paddle_b.shapesize(stretch_wid=5, stretch_len=1)
paddle_b.penup()
paddle_b.goto(350, 0)

# Ball
ball = turtle.Turtle()
ball.color("white")
ball.speed(0)
ball.shape("square")
ball.penup()
ball.goto(0, 0)
ball.dx = 0.5
ball.dy = -0.5

# Pen
pen = turtle.Turtle()
pen.speed(0)
pen.color("red")
pen.penup()
pen.hideturtle()
pen.goto(0, 260)
pen.write(f"Player A score: {score_a}    Player B score: {score_b}", align="center", font=("Courier", 24, "normal"))

# Function key up for paddle_a
def paddle_a_up():
    y = paddle_a.ycor()
    y += 20
    paddle_a.sety(y)

def paddle_a_down():
    y = paddle_a.ycor()
    y -= 20
    paddle_a.sety(y)

def paddle_b_up():
    y = paddle_b.ycor()
    y += 20
    paddle_b.sety(y)

def paddle_b_down():
    y = paddle_b.ycor()
    y -= 20
    paddle_b.sety(y)

# Keyboard binding
wd.listen()
wd.onkeypress(paddle_a_up, "w")
wd.onkeypress(paddle_a_down, "s")
wd.onkeypress(paddle_b_up, "Up")
wd.onkeypress(paddle_b_down, "Down")

# Main loop
while True:
    try:
        wd.update()  # Update the screen manually

        # Ball move
        ball.setx(ball.xcor() + ball.dx)
        ball.sety(ball.ycor() + ball.dy)

        # Border checking
        if ball.ycor() > 290:
            ball.sety(290)
            ball.dy *= -1
        if ball.ycor() < -290:
            ball.sety(-290)
            ball.dy *= -1
        if ball.xcor() > 390:
            ball.goto(0, 0)
            ball.dx *= -1
        if ball.xcor() < -390:
            ball.goto(0, 0)
            ball.dx *= -1

        # Check for collisions with paddles
        if (ball.xcor() > 340 and ball.xcor() < 350) and (ball.ycor() < paddle_b.ycor() + 40 and ball.ycor() > paddle_b.ycor() - 40):
            ball.setx(340)
            ball.dx *= -1
            score_b += 1
            pen.clear()
            pen.write(f"Player A score: {score_a}    Player B score: {score_b}", align="center", font=("Courier", 24, "normal"))

        if (ball.xcor() < -340 and ball.xcor() > -350) and (ball.ycor() < paddle_a.ycor() + 40 and ball.ycor() > paddle_a.ycor() - 40):
            ball.setx(-340)
            ball.dx *= -1
            score_a += 1
            pen.clear()
            pen.write(f"Player A score: {score_a}    Player B score: {score_b}", align="center", font=("Courier", 24, "normal"))

        time.sleep(delay)
    except:
        break  # Break out of the loop if any exception occurs
