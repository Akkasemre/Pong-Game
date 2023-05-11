from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import Scoreboard


#Main screen
screen = Screen()
screen.bgcolor("black")
screen.screensize(canvwidth=800, canvheight=600)
screen.title("Pong ")
screen.tracer(0)
scoreboard = Scoreboard()


#Paddle's movement's
r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
screen.listen()
screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


#Creating a ball
ball = Ball()



game_is_on =True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

#Detect collision with ball
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()


#Detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()


# Detect R paddle misses ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

# Detect L paddle misses ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
