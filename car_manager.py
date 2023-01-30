from turtle import Turtle
from random import choice, randint

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
STRETCH_WIDTH_TURTLE = 1
STRETCH_HEIGHT_TURTLE = 2
X_AREA_LEFT = 0
X_AREA_RIGHT = 600
Y_AREA_LOW = -250
Y_AREA_HIGH = 270
NUMBER_OF_CARS = 20


class CarManager:
    def __init__(self):
        self.car = None
        self.cars = []
        self.generate_car(NUMBER_OF_CARS)

    def generate_car(self, number_of_cars):
        for car in range(0, number_of_cars):
            self.car = Turtle(shape="square")
            self.car.penup()
            self.car.color(choice(COLORS))
            self.car.turtlesize(stretch_wid=STRETCH_WIDTH_TURTLE, stretch_len=STRETCH_HEIGHT_TURTLE)
            self.car.goto(x=randint(X_AREA_LEFT, X_AREA_RIGHT), y=randint(Y_AREA_LOW, Y_AREA_HIGH))
            self.car.setheading(180)
            self.cars.append(self.car)

    def move(self, level):
        for car in range(len(self.cars)):
            self.cars[car].forward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT * (level - 1))
            if self.cars[car].xcor() <= -300:
                self.cars[car].goto(x=X_AREA_LEFT, y=self.cars[car].ycor())

    def add_car(self):
        self.car = Turtle(shape="square")
        self.car.penup()
        self.car.color(choice(COLORS))
        self.car.turtlesize(stretch_wid=STRETCH_WIDTH_TURTLE, stretch_len=STRETCH_HEIGHT_TURTLE)
        self.car.goto(x=randint(X_AREA_LEFT, X_AREA_RIGHT), y=randint(Y_AREA_LOW, Y_AREA_HIGH))
        self.car.setheading(180)
        self.cars.append(self.car)
