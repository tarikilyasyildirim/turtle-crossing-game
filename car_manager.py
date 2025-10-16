import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = 5


    def car_generator(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.color(random.choice(COLORS))
            new_car.penup()
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            random_y = random.randint(-250, 250)
            new_car.goto(x=300, y=random_y)
            self.all_cars.append(new_car)

    def car_move(self):
        for car in self.all_cars:
            car.backward(self.car_speed)
    def level_up(self):
        self.car_speed += MOVE_INCREMENT