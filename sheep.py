import random as r
import point as p

class Sheep(p.Point):

    sheep_move_distance:float
    
    def __init__(self, init_pos_limit:float) -> None:
        self.rand_position(init_pos_limit)

    def rand_position(self, init_pos_limit:float):
        self.posX = r.uniform(-init_pos_limit, init_pos_limit)
        self.posY = r.uniform(-init_pos_limit, init_pos_limit)
    
    def make_move(self):
        dir = r.randint(0,3)
        self.move_self(dir)

    def move_self(self, direction:int):
        if(direction == 0):
            self.x += self.sheep_move_distance
        if(direction == 1):
            self.y += self.sheep_move_distance
        if(direction == 2):
            self.x -= self.sheep_move_distance
        if(direction == 3):
            self.y -= self.sheep_move_distance
