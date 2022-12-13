from .point import Point


class Wolf(Point):
    wolf_move_dist: float

    def __init__(self, wolf_move_dist):
        self.wolf_move_dist = wolf_move_dist

    def set_target(self, point: Point):
        self.target = point

    def chase(self) -> bool:
        if Point.distance(self, self.target) < self.wolf_move_dist:
            return True
        else:
            self.move_self()
        return False

    def move_self(self):
        vx, vy = Point.get_direction_to(self, self.target)
        vx *= self.wolf_move_dist
        vy *= self.wolf_move_dist

        self.x += vx
        self.y += vy
