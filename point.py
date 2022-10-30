from math import sqrt
import math


class Point(object):
    x: float = 0
    y: float = 0

    @staticmethod
    def distance(a, b) -> float:
        return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    @staticmethod
    def get_direction_to(fr, to):
        len = Point.distance(fr, to)
        vx = to.x - fr.x
        vy = to.y - fr.y

        return vx / len, vy / len

    def __str__(self) -> str:
        return f"{round(self.x,3)},{round(self.y,3)}"
