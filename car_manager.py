from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.cars = []
        self.create_car()
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid=1, stretch_len=2)
        new_car.penup()
        y_pos = random.randint(-250, 250)
        new_car.setposition(320, y_pos)
        self.cars.append(new_car)

    def movement(self):
        for single_cars in self.cars[0::6]:
            single_cars.backward(self.car_speed)

    def speed_up(self):
        self.car_speed += MOVE_INCREMENT



