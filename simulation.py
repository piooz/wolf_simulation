import sheep as s

class Simulation(object):

    sheeps_collection = []

    def __init__(self, rounds, sheeps_number, init_pos_limit, sheep_move_dist, wolf_move_dist):
        self.rounds = rounds
        self.create_sheeps(sheeps_number, init_pos_limit, sheep_move_dist)
        
    def create_sheeps(self, sheeps_number, init_pos_limit, sheep_move_distance):
        for _ in range(sheeps_number):
            self.sheeps_collection.append(s.Sheep(init_pos_limit, sheep_move_distance))
        
    def simulate_round(self):
        for value in self.sheeps_collection:
            value.make_move()
    
    def report(self):
        for i in range(len(self.sheeps_collection)):
            print(f"Sheep nr {i} {self.sheeps_collection[i]}")
            
        print('---------------------')

    def start_simulation(self):
        for _ in range(self.rounds):
            self.simulate_round()
            self.report();
