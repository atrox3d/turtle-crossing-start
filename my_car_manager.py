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
        self.setheading(180)
        self.set_randomy()

    def set_randomy(self):
        # don't overlap in y axis
        randomy = random.randrange(*YLIMITS, 20)
        self.goto(XSTART, randomy)


class CarManager:
    def __init__(self):
        self.cars = []

    def repositiony(self, car):
        check = True
        while check:
            reposition = False
            for othercar in self.cars:
                if car is othercar:
                    # print(f"samecar: {car}:{othercar}")
                    pass
                # if car is not othercar and car.pos() == othercar.pos():
                elif car.distance(othercar) < 40:
                    # print(f"cary = {car.pos()} othercary = {othercar.pos()} -----> OVERLAP!")
                    print(f"car distance: {car.distance(othercar)}")
                    reposition = True
                    car.set_randomy()
                else:
                    # print(f"cary = {car.ycor()} othercary = {c.ycor()}")
                    pass
            print("-" * 80)
            if not reposition:
                check = False

    def add_car(self):
        if len(self.cars) < MAX_CARS:
            car = Car()
            self.repositiony(car)
            self.cars.append(car)

    def move_cars(self):
        for car in self.cars:
            car.forward(MOVE_INCREMENT)
            if car.xcor() < -310:
                #self.cars.remove(car)
                car.setx(XSTART)
                self.repositiony(car)
                # print(f"car reset; {car}")
