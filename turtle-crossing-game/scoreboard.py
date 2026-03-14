from turtle import Turtle

FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.hideturtle()
        self.penup()
        self.goto(-230,250)
        self.write_level()

    def write_level(self):
        self.write(f"Level:{self.level}", align="center", font=FONT)

    def increase_level(self):
        self.level += 1
        self.clear()
        self.write_level()

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write(f"GAME OVER, YOU REACHED LEVEL {self.level}!", align="center", font=FONT)