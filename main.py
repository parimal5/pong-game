from turtle import Screen
from ball import Ball
from paddle import Paddle
import time

screen = Screen()

screen.bgcolor("black")
screen.setup(height=600, width=800)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
ball = Ball()

screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")
screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

is_game_on = True

while is_game_on:
    screen.update()
    ball.move()
    time.sleep(0.1)

    # Detect Collision of ball and wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    # Detect Collision of ball with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    # Detect Ball Miss and add score
    if ball.xcor() > 380:
        ball.reset_position()
    if ball.xcor() < -380:
        ball.reset_position()

screen.exitonclick()
