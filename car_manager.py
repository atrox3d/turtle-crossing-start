from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
YLIMITS = -240, 240
XSTART = 300
CARS_PER_WAVE = 480 / 20
MAX_CARS = 60


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        # self.setheading(180)
        self.set_randomy()

    def set_randomy(self):
        # don't overlap in y axis
        randomy = random.randint(*YLIMITS)
        self.goto(XSTART, randomy)


class CarManager:
    def __init__(self):
        self.cars: list[Car] = []

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:
            car = Car()
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.backward(STARTING_MOVE_DISTANCE)
