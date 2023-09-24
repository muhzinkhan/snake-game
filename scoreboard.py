import time
from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        try:
            with open("assets/data.txt") as data:
                self.high_score = int(data.read())
        except FileNotFoundError:
            self.high_score = 0

        self.color("white")
        self.penup()
        self.goto(0, 268)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score} High score : {self.high_score}", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("assets/data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_scoreboard()

    def display_game_over(self):
        # self.penup()
        # self.goto(0, 0)
        # self.pendown()
        # self.write("GAME OVER", align=ALIGNMENT, font=FONT)
        # self.penup()
        time.sleep(2)
        # self.clear()
        # self.goto(0, 268)
        self.update_scoreboard()

    def increase_score(self):
        self.score += 1
        self.update_scoreboard()
