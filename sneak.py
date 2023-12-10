from turtle import Turtle
X_STARTING_POINTS = (0,-20,-40)
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Sneak:
    def __init__(self):
        self.segments = []
        self.create_sneak()
        self.head = self.segments[0]
    def create_sneak(self):
        for point in X_STARTING_POINTS:
            segment = Turtle("square")
            segment.penup()
            segment.color("green")
            segment.goto(point, 0)
            self.segments.append(segment)

    def move(self):
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
