from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
bet = screen.textinput(title="Make Your Bet", prompt="Which turtle will win the race? Pick a color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_positions = [-70,-40,-10,20,50,80]
turtles = []

for turtle_i in range(0,6):
    new_turtle = Turtle(shape='turtle')
    new_turtle.penup()
    new_turtle.color(colors[turtle_i])
    new_turtle.goto(-240, y_positions[turtle_i])
    turtles.append(new_turtle)

if bet:
    is_race_on = True

while is_race_on:
    for turtle in turtles:
        if turtle.xcor() > 220:
            winner = turtle.pencolor()
            is_race_on = False
            if bet == winner:
                print(f'You win! {winner} was the first to make it across!')
            else:
                print(f'You lose! {winner} was the first to make it across!')

        turtle.forward(random.randint(0, 20))














screen.exitonclick()
















screen.exitonclick()
