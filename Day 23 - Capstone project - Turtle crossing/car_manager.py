from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5


class CarManager:
    def __init__(self, scoreboard):
        self.all_cars = []
        self.scoreboard = scoreboard

    def create_car(self):
        level = self.scoreboard.level

        if random.randint(1, 12) <= level:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.goto(300, random.randint(-240, 240))
            new_car.color(random.choice(COLORS))
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(max(int(STARTING_MOVE_DISTANCE *
                         (self.scoreboard.level * 0.25)), STARTING_MOVE_DISTANCE))
