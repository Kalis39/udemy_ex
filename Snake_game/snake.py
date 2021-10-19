from turtle import Turtle
MOVE_DISTANCE = 20
STARTING_POSITION = [(0, 0), (-20, 0), (-40, 0)]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.squares = []
        self.create_snake()
        self.head = self.squares[0]

    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        new_square = Turtle(shape='square')
        new_square.up()
        new_square.color("white")
        new_square.goto(position)
        self.squares.append(new_square)

    def extend(self):
        self.add_segment(self.squares[-1].position())

    def move(self):
        for square in range(len(self.squares) - 1, 0, -1):
            new_x_position = self.squares[square - 1].xcor()
            new_y_position = self.squares[square - 1].ycor()
            self.squares[square].goto(new_x_position, new_y_position)
        self.head.forward(MOVE_DISTANCE)

    def reset(self):
        for square in self.squares:
            square.goto(1000, 1000)
        self.squares.clear()
        self.create_snake()
        self.head = self.squares[0]

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def reached_boundaries(self):
        if self.head.xcor() == -300 or self.head.xcor() == 300:
            return True
        elif self.head.ycor() == -300 or self.head.ycor() == 300:
            return True
