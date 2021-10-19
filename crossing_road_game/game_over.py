from turtle import Turtle

class Text(Turtle):
    def __init__(self):
        super().__init__()
        self.ht()
        self.up()
        self.goto(0, 0)
        self.write("GAME OVER", align='center', font=('Courier', 30, 'normal'))
