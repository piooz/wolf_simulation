import sheep as s
import json
from wolf import Wolf
from point import Point

class Simulation(object):

    sheeps_collection = []
    dump_list = []

    def __init__(self, rounds, sheeps_number, init_pos_limit, sheep_move_dist, wolf_move_dist):
        self.rounds = rounds
        self.create_sheeps(sheeps_number, init_pos_limit, sheep_move_dist)
        self.wolf = Wolf(wolf_move_dist)
        
    def create_sheeps(self, sheeps_number, init_pos_limit, sheep_move_distance):
        for _ in range(sheeps_number):
            self.sheeps_collection.append(s.Sheep(init_pos_limit, sheep_move_distance))
        self.alives = sheeps_number
        
    def simulate_round(self):
        self.simulate_sheeps()
        self.simulate_wolf()


    def simulate_wolf(self):
        sheep = self.attach_closest_sheep()
        if self.wolf.chase():
            sheep.isAlive = False
            self.alives -= 1

    def attach_closest_sheep(self) :
        sheep = self.sheeps_collection[0]
        min = Point.distance(self.wolf, sheep)

        for val in self.sheeps_collection:
            if val.isAlive == False:
                continue
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
        for i in range(self.rounds):
            self.simulate_round()
            self.report(i+1)
            self.update_dump(i+1)
        self.json_dump()

    def update_dump(self,round:int):
        self.dump_list.append(
            {
                "round_no" : round, 
                "wolf_pos" : (self.wolf.x, self.wolf.y),
                "sheeps_pos ": [(val.x, val.y) for val in self.sheeps_collection]
            }
        )

    def json_dump(self):
        with open("pos.json","w") as output:
            json.dump(self.dump_list, output,indent='\t')
        


    def report(self, round_nr):
        print(f"Round : {round_nr}")
        print(f"Sheeps alive : {self.alives}")
        print(f"Current Target : {self.sheeps_collection.index(self.wolf.target)}")
        print(f"Wolf : {self.wolf}")

        for i, val in enumerate(self.sheeps_collection):
            if val.isAlive:
                print(f"Sheep nr {i} : {self.sheeps_collection[i]}")
            else:
                print("None")
            
        print('---------------------')
