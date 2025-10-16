from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 1
        self.penup()
        self.hideturtle()
        self.color("black")
        self.goto(-220, 260)
        self.write(f"Level:{self.level}",move=False,align="center",font=FONT)
    def update_score(self):
        self.clear()
        self.level += 1
        self.write(f"Level:{self.level}",move=False,align="center",font=FONT)
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER",move=False,align="center",font=FONT)