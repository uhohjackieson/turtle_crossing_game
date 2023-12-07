from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.all_cars = []

    def new_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 1:

            car = Turtle("square")
            car.shapesize(stretch_wid=1, stretch_len=2)
            car.penup()
            # make random color
            car.color(random.choice(COLORS))
            # go to random position
            car.goto(300, random.randint(-250, 250))
            self.all_cars.append(car)

    def move(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE)

    def increase_speed(self):
        for car in self.all_cars:
            car.backward(STARTING_MOVE_DISTANCE + MOVE_INCREMENT)
