import random as r
from .point import *


class Sheep(Point):

    sheep_move_distance: float
    isAlive: bool = True

    def __init__(self, init_pos_limit: float, sheep_move_distance) -> None:
        self.rand_position(init_pos_limit)
        self.sheep_move_distance = sheep_move_distance

    def rand_position(self, init_pos_limit: float):
        self.x = r.uniform(-init_pos_limit, init_pos_limit)
        self.y = r.uniform(-init_pos_limit, init_pos_limit)

    def make_move(self):
        if self.isAlive:
            dir = r.randint(0, 3)
            self.move_self(dir)

    def move_self(self, direction: int):
        if (direction == 0):
            self.x += self.sheep_move_distance
        if (direction == 1):
            self.y += self.sheep_move_distance
        if (direction == 2):
            self.x -= self.sheep_move_distance
        if (direction == 3):
            self.y -= self.sheep_move_distance
