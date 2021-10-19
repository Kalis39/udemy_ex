from turtle import Turtle
from random import randint
ANGLE = [10, 20, 30, 40, 50, 60, 70, 80, 90]


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape('circle')
        self.color("white")
        self.goto(0, 0)
        self.x_cor = randint(4, 10)
        self.y_cor = randint(4, 10)
        self.move_speed = 0.1

    def move_ball(self):
        newx_coordinate = self.xcor() + self.x_cor
        newy_coordinate = self.ycor() + self.y_cor
        self.goto(newx_coordinate, newy_coordinate)

    def bounce_y(self):
        self.y_cor *= -1

    def bounce_x(self):
        self.x_cor *= -1
        self.move_speed *= 0.9

    def reset_pos(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()
