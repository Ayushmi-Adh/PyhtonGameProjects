from turtle import Turtle

positions = [(0, 0), (-20, 0), (-40, 0)]
MOVING_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:

    def __init__(self):
        self.snake_together = []
        self.create_snake()
        self.head = self.snake_together[0]

    def create_snake(self):
        for position in positions:
            self.add_segment(position)

    def add_segment(self, position):
        snakes = Turtle(shape="square")
        snakes.color("blue")
        snakes.penup()
        snakes.goto(position)
        self.snake_together.append(snakes)

    def extend_snake(self):
        self.add_segment(self.snake_together[-1].position())
    def move(self):
        for seg_num in range(len(self.snake_together) - 1, 0, -1):
            new_x = self.snake_together[seg_num - 1].xcor()
            new_y = self.snake_together[seg_num - 1].ycor()
            self.snake_together[seg_num].goto(new_x, new_y)
        self.head.forward(MOVING_DISTANCE)

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

    def reset(self):
        for seg in self.snake_together:
            seg.goto(1000, 1000)
        self.snake_together.clear()
        self.create_snake()
        self.head = self.snake_together[0]
