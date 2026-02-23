from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = ScoreBoard()

screen.listen()
screen.onkeypress(r_paddle.paddle_up, "Up")
screen.onkeypress(r_paddle.paddle_down, "Down")
screen.onkeypress(l_paddle.paddle_up, "w")
screen.onkeypress(l_paddle.paddle_down, "s")

game_on = True
while game_on: # needs the loop to update, after every move
    time.sleep(ball.move_speed)  # Delays the refresh by .1 second
    screen.update()  # updates the screen every time the loop iterates
    ball.move()

    #Detect collision with the wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        #make the ball bounce
        ball.bounce_y()
    #Detect collision with paddles
    if ball.distance(r_paddle) < 50 and ball.xcor() > 325 or ball.distance(l_paddle) < 50 and ball.xcor() < -325:
        ball.bounce_x()
    #Detect right paddle miss
    if ball.xcor() > 380:
        scoreboard.l_point()
        ball.reset_position()
        if scoreboard.l_score >= 5:
            game_on = False
            scoreboard.game_over("Left Player Wins!")

    #Detect left paddle miss
    if ball.xcor() < -380:
        scoreboard.r_point()
        ball.reset_position()
        if scoreboard.r_score >= 5:
            game_on = False
            scoreboard.game_over("Right Player Wins!")


screen.exitonclick()