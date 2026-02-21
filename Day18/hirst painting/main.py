import turtle as t
import random
t.colormode(255)
tim = t.Turtle()
tim.speed("fastest")
tim.hideturtle()
# import colorgram
#
# rgb_colors = []
# colors = colorgram.extract('image.jpg', 10)
# print(colors)
#
# for color in colors:
#     r = color.rgb.r
#     g = color.rgb.g
#     b = color.rgb.b
#     rgb_colors.append((r,g,b))

color_list = [(147, 145, 140), (213, 208, 193), (139, 147, 141), (139, 146, 155), (165, 138, 144), (41, 107, 148), (164, 86, 47), (202, 147, 30), (148, 23, 14), (55, 17, 8)]
tim.setheading(225)
tim.penup()
tim.forward(300)
tim.setheading(0)
number_of_dots = 100

for d in range(1, number_of_dots + 1):
    tim.dot(20,random.choice(color_list))
    tim.forward(50)

    if d % 10 == 0:
        tim.setheading(90)
        tim.forward(50)
        tim.setheading(180)
        tim.forward(500)
        tim.setheading(0)




screen = t.Screen()
screen.exitonclick()