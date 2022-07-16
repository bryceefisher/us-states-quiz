import turtle
from score import Score
import pandas as pd
from turtle import Turtle, Screen
from state_name import StateName

state_turtle = Turtle()
screen = turtle.Screen()
screen.title("U.S. States Game")
score = Score()

image = "blank_states_img.gif"
screen.addshape(image)

turtle.shape(image)

df = pd.read_csv("50_states.csv")

guess_list = []
state_list = df["state"].tolist()
correct_guess = 0
missed_state_index = 0
missed_states = []

while correct_guess <= 50:

    if correct_guess == 50:
        print("You got them all!!")
        break

    score.write(f"Current Score: {correct_guess}/50", font=("Verdana", 30, "normal"))
    answer_state = screen.textinput(title="Guess the State", prompt="Name a State").title()



    state_name = StateName(answer_state)
    state_list_index = 0

    while state_list_index <= 49:
        if answer_state == state_list[state_list_index]:
            guess_x = (df[df["state"] == answer_state]["x"]).values
            guess_y = (df[df["state"] == answer_state]["y"]).values
            state_name.goto(guess_x[0], guess_y[0])
            state_name.write(answer_state, font=("Verdana", 12, "normal"))
            correct_guess += 1
            guess_list.append(answer_state)
            score.update_score()
        state_list_index += 1

    if answer_state == "Exit":
        missing_states = [states for states in state_list if states not in guess_list]
        print(guess_list)
        print(missing_states)
        break


