import sheep as s
from wolf import Wolf
from point import Point

class Simulation(object):

    sheeps_collection = []

    def __init__(self, rounds, sheeps_number, init_pos_limit, sheep_move_dist, wolf_move_dist):
        self.rounds = rounds
        self.create_sheeps(sheeps_number, init_pos_limit, sheep_move_dist)
        self.wolf = Wolf(wolf_move_dist)
        
    def create_sheeps(self, sheeps_number, init_pos_limit, sheep_move_distance):
        for _ in range(sheeps_number):
            self.sheeps_collection.append(s.Sheep(init_pos_limit, sheep_move_distance))
        
    def simulate_round(self):
        self.simulate_sheeps()
        self.simulate_wolf()


    def simulate_wolf(self):
        sheep = self.attach_closest_sheep()
        if self.wolf.chase():
            sheep.isAlive = False

    def attach_closest_sheep(self) :
        sheep = self.sheeps_collection[0]
        min = Point.distance(self.wolf, sheep)

        for val in self.sheeps_collection:
            len = Point.distance(self.wolf, val)
            if len < min:
                min = len
                sheep = val

        self.wolf.set_target(sheep)
        return sheep

    def simulate_sheeps(self):
        for value in self.sheeps_collection:
            value.make_move()
    
    def start_simulation(self):
        for _ in range(self.rounds):
            self.simulate_round()
            self.report()


    def report(self):
        print(f"Wolf {self.wolf}")
        for i, val in enumerate(self.sheeps_collection):
            if val.isAlive:
                print(f"Sheep nr {i} {self.sheeps_collection[i]}")
            
        print('---------------------')
