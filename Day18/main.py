import random
import turtle as t
# import heroes
# print(heroes.gen())
t.colormode(255)

timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("dark red")
timmy.speed("fastest")


# Make a square with the turtle
# for _ in range(4):
#     timmy.fd(100)
#     timmy.right(90)
#
#
# dotted line
# for _ in range(15):
#     timmy.fd(10)
#     timmy.penup()
#     timmy.fd(10)
#     timmy.pendown()

#Draw multiple shapes with random colors
# colors = ["red", "blue", "DarkSeaGreen4", "DarkRed", "DarkViolet", "burlywood4", "DeepPink4", "brown", "black", "gray"]
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.right(angle)
#
# for shape_side in range(3,11):
#     timmy.color(random.choice(colors))
#     draw_shape(shape_side)

def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color

#Random Walk
# directions = [0, 90, 180, 270]
# size = 1
# timmy.speed('fast')
# for _ in range(200):
#     timmy.pensize(size)
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))
#     size += 1

#Coloful Spiral
def draw_spiral(gap_size):
    for _ in range(int(360 / gap_size)):
        timmy.color(random_color())
        timmy.circle(100)
        timmy.setheading(timmy.heading() + gap_size)

draw_spiral(5)












screen = t.Screen()
screen.exitonclick()