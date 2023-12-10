# Repo:   https://github.com/rsullivan10/Snake.git
# Author: Roger Sullivan

import time
from turtle import Screen
from sneak import Sneak

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

sneak = Sneak()
screen.listen()
screen.onkey(sneak.up,"Up")
screen.onkey(sneak.down,"Down")
screen.onkey(sneak.left,"Left")
screen.onkey(sneak.right,"Right")


# Game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

    sneak.move()
screen.exitonclick()

