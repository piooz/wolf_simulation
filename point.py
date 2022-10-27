from math import sqrt

class Point(object):
    x:float = 0
    y:float = 0

    @staticmethod
    def distance(a, b) -> float:
        return sqrt((a.x - b.x)**2 + (a.y - b.y)**2)
