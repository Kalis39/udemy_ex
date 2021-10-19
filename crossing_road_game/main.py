from turtle import Screen
from player import Player
from cars_menu import Car
from level_board import Level
from game_over import Text
import math
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

arty = Player()
level_board = Level()
cars = []

for i in range(20):
    cars.append(Car())

screen.onkey(fun=arty.move_turtle, key="Up")

game_is_on = True
while game_is_on:
    time.sleep(arty.move_speed)
    screen.update()

    for car in cars:
        if math.fabs(arty.ycor() - car.ycor()) < 22 and math.fabs(arty.xcor() - car.xcor()) < 25:
            game_over = Text()
            game_is_on = False
        else:
            if car.xcor() < -320:
                car.reset_car()
            else:
                car.move_car()

    if arty.ycor() > 280:
        arty.reset_turtle()
        level_board.level_up()
        cars.append(Car())


screen.exitonclick()
