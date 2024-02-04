from turtle import Turtle


def load_score():
    with open("data.txt", mode="r") as file:
        return int(file.read())


class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score_point = 0
        self.high_score = load_score()
        self.color("green")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"SCORE: {self.score_point} HIGH SCORE: {self.high_score}", align="center", font=("TimesNewRoman", 11, "bold"))

    def reset(self):
        if self.score_point > self.high_score:
            self.high_score = self.score_point
            with open("data.txt", mode="w") as file:
                file.write(str(self.score_point))

        self.score_point = 0
        self.update_scoreboard()

    def update_points(self):
        self.score_point += 1
        self.update_scoreboard()

