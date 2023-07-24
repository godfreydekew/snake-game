from turtle import Turtle


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()

    def update_score(self, score):
        self.penup()
        self.color("white")
        self.hideturtle()
        self.goto(0, 280)
        self.write(f"score : {score}", False, align="center", font=('Arial', 15, 'normal'))
        # self.goto(50, 280)
        # self.write(score, False, align="center", font=('Arial', 15, 'normal'))

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align="center", font=('Arial', 15, 'normal'))
