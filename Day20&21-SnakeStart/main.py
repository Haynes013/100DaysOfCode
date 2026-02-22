from turtle import Screen
from snake import Snake
import time
from food import Food

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0) #stops from tracing all movement

snake = Snake()
food = Food()

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")

game_on = True
while game_on:
    screen.update()  # updates the screen every time the loop iterates
    time.sleep(0.1)  # Delays the refresh by .1 second
    snake.move()
    #Detect collision with food
    if snake.head.distance(food) < 15:
        food.refresh()

screen.exitonclick()













