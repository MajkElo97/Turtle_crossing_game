from turtle import Turtle

STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.new_level()
        self.setheading(90)

    def move(self):
        self.forward(MOVE_DISTANCE)

    def new_level(self):
        self.goto(STARTING_POSITION)

    def collision_with_car(self, cars):
        for car in range(len(cars)):
            print(self.distance(cars[car]))
            if (self.ycor() <= (cars[car].ycor() - 10) and self.distance(cars[car]) < 20) or (
                    self.ycor() > (cars[car].ycor() - 10) and self.distance(cars[car]) < 30):
                return False
        return True
