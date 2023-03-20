import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

car = CarManager()
turtle = Player()
screen = Screen()
score = Scoreboard()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

screen.onkeypress(turtle.move_turtle, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.movement()

    for cares in car.cars:
        if cares.distance(turtle) < 20:
            score.game_over()
            game_is_on=False

    if turtle.next_level():
        turtle.to_start()
        car.speed_up()
        score.increase_score()












screen.exitonclick()