import turtle
from turtle import Turtle
from car_manager import CarManager
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280


car = CarManager()

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)

    def move_turtle(self):
        self.forward(MOVE_DISTANCE)

    def to_start(self):
        self.penup()
        self.goto(STARTING_POSITION)

    def next_level(self, ):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False



