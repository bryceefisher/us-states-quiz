from turtle import Turtle


class StateName(Turtle):
    def __init__(self, answer_state):
        super().__init__()
        self.hideturtle()
        self.answer_state = answer_state
        self.penup()
        self.color("black")

    def go_to_state(self, guess_x, guess_y):
        self.goto(guess_x, guess_y)
