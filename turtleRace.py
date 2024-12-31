import turtle
import time
import random

WIDTH, HEIGHT = 500, 500
COLORS = ['red', 'green', 'blue', 'orange', 'yellow', 'black', 'purple', 'pink', 'brown', 'cyan']

def get_number_of_racers():
    racers = 0
    while True:
        racers = input("How many racers would you like to have (2 - 10)? ")
        if racers.isdigit():
            racers = int(racers)
        else:
            print("Please enter a valid number of racers between 2-10.")
            continue

        if 2 <= racers <= 10:
            return racers
        else:
            print("Please enter a number between 2 and 10!")

def create_turtles(colors):
    turtles = []
    for i, color in enumerate(colors):
        racer = turtle.Turtle()
        racer.color(color)
        racer.shape('turtle')
        racer.left(90)
        turtles.append(racer)

def init_turtle():
    screen = turtle.Screen()
    screen.setup(WIDTH, HEIGHT)
    screen.title('Turtle Racers 5000')

racers = get_number_of_racers()
init_turtle()
random.shuffle(COLORS)
colors = COLORS[:racers]
create_turtles(colors)


