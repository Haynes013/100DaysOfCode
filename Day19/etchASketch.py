from turtle import Turtle, Screen

mike = Turtle()
screen = Screen()

def move_forward():
    mike.forward(10)

def move_back():
    mike.backward(10)

def clear():
    mike.clear()
    mike.penup()
    mike.home()
    mike.pendown()

def turn_left():
    mike.left(10)

def turn_right():
    new_heading = mike.heading() - 10
    mike.setheading(new_heading)

screen.listen()
screen.onkey(key="w", fun=move_forward)
screen.onkey(key="s", fun=move_back)
screen.onkey(key="c", fun=clear)
screen.onkey(key="a", fun=turn_left)
screen.onkey(key="d", fun=turn_right)


















screen.exitonclick()




















