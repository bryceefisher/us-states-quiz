from turtle import Turtle



class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.goto(-150, 300)

    def update_score(self):
        self.clear()