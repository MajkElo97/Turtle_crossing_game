from turtle import Turtle

FONT = ("Courier", 24, "normal")
TEXT_POSITION = (-280, 260)


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(TEXT_POSITION)
        self.level = 0
        self.add_level()

    def add_level(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", font=FONT)

    def game_over(self):
        self.goto(x=0, y=0)
        self.write("GAME OVER", align="center", font=FONT)