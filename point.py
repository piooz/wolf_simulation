from math import sqrt

class Point(object):
    x:float
    y:float

    @staticmethod
    def distance(a, b) -> float:
        return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)

    def __str__(self) -> str:
        return f"Point x:{self.x} y:{self.y}"
