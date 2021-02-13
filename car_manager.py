from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10
YLIMITS = -240, 240
XSTART = 300
MAX_CARS = 300


class Car(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=1, stretch_len=2)
        self.penup()
        self.color(random.choice(COLORS))
        self.setheading(180)
        self.set_randomy()

    def set_randomy(self):
        # don't overlap in y axis
        randomy = random.randrange(*YLIMITS, 20)
        self.goto(XSTART, randomy)


class CarManager:
    def __init__(self):
        self.cars = []

    def add_car(self):
        if len(self.cars) < MAX_CARS:
            car = Car()
            overlap = True
            while overlap:
                overlap = False
                for othercar in self.cars:
                    if car.ycor() == othercar.ycor():
                        overlap = True
                        print(f"overlap: {car.color()}:{car.ycor()}, {othercar.color()}:{car.ycor()}")
                        car.set_randomy()

            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
            if car.xcor() < -310:
                self.cars.remove(car)
                car.hideturtle()
                print(f"car clear; {car}")
