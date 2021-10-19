from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
LIMIT = 280

class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape("turtle")
        self.goto(STARTING_POSITION)
        self.seth(90)
        self.move_speed = 0.1

    def move_turtle(self):
        self.fd(MOVE_DISTANCE)

    def reset_turtle(self):
        self.move_speed *= 0.9
        self.goto(STARTING_POSITION)
