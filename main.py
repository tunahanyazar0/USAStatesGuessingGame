import turtle
import pandas
from turtle import Turtle,Screen,colormode
import time
import datetime

colormode(256)

screen = Screen()
screen.title("Usa State Game")

image = "blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

tuna = Turtle()
tuna.speed(0)
tuna.hideturtle()
tuna.penup()

score  = 0
tuna2 = Turtle()
tuna2.speed(0)
tuna2.hideturtle()
tuna2.penup()
tuna2.goto(260,275)
tuna2.write(arg=f"Score : {score}/50",align="center",font=("Arial",24,"normal"))

def update_score():
    global score
    tuna2.clear()
    score += 1
    tuna2.goto(260, 275)
    tuna2.write(arg=f"Score : {score}/50", align="center", font=("Arial", 24, "normal"))

data = pandas.read_csv("50_states.csv")

guessed_states = []
unguessed_states = []

game_is_on = True
while game_is_on:

    respond = screen.textinput("USA STATE GAME","Enter a state : ")

    if respond == "exit":
        data_dict = {
            "Unguessed States" : states
        }
        data_dict_table = pandas.DataFrame(data_dict)
        data_dict_table.to_csv("unguessed_states.csv")
        game_is_on = False

    for i in data.state:
        if respond.title() == i:
            state = data[data.state == i]
            tuna.goto(float(state.x), float(state.y))
            tuna.write(arg=respond.title(),align="center",font = ("Arial",12,"normal"))
            update_score()
            guessed_states.append(respond.title())

    states = data["state"].to_list()
    for i in guessed_states:
        states.remove(i)



screen.exitonclick()
