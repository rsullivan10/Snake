import time
from turtle import Screen, Turtle

screen = Screen()
screen.setup(600,600)
screen.bgcolor("black")
screen.title("Snake")
screen.tracer(0)

x_start_points = (0,-20,-40)

# holds new segments for the sneak
segments = []

# create starting sneak parts
for point in x_start_points:
    segment = Turtle("square")
    segment.penup()
    segment.color("green")
    segment.goto(point, 0)
    segments.append(segment)

screen.update()

# Game loop
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)

# moves the sneaks segments all togather
    for seg_num in range(len(segments) - 1, 0, -1):
        new_x = segments[seg_num - 1].xcor()
        new_y = segments[seg_num - 1].ycor()
        segments[seg_num].goto(new_x, new_y)
    segments[0].forward(20)
    segments[0].left(90)


screen.exitonclick()

