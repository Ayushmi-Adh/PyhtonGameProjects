import turtle
from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(500, 400)
the_bet = screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")
colors = ["red", "green", "orange", "yellow", "violet", "blue"]
y_cord = [-70, -40, -10, 20, 50, 80]
all_turtles_inRace = []

for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-250, y=y_cord[turtle_index])
    all_turtles_inRace.append(new_turtle)

if the_bet:
    is_race_on = True 

while is_race_on:
    for turtle in all_turtles_inRace:
        if turtle.xcor() > 250:
            is_race_on =False
            winning_color = turtle.pencolor()
            if winning_color == the_bet:
                print(f"You have won! The{winning_color} turtle is the winner. ")
            else:
                print(f"You have lost! The {winning_color} turtle is the winner.")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)

screen.exitonclick()
