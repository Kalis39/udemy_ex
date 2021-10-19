from turtle import Turtle
from random import choice, randint
COLORS = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']

class Car(Turtle):

    def __init__(self):
        super().__init__()
        self.up()
        self.shape('square')
        self.color(choice(COLORS))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.x_cor = randint(-300, 300)
        self.y_cor = randint(-250, 250)
        self.move_car()

    def move_car(self):
        self.goto(self.x_cor, self.y_cor)
        self.x_cor -= 5

    def reset_car(self):
        self.color(choice(COLORS))
        self.x_cor = 320
        self.y_cor = randint(-250, 250)
        self.goto(self.x_cor, self.y_cor)
        self.move_car()
