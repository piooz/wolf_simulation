import sheep as s
import json
import csv
from wolf import Wolf
from point import Point


class Simulation(object):

    sheeps_collection = []
    dump_list = []
    csv_report = []

    def __init__(
            self,
            rounds,
            sheeps_number,
            init_pos_limit,
            sheep_move_dist,
            wolf_move_dist):
        self.rounds = rounds
        self.create_sheeps(sheeps_number, init_pos_limit, sheep_move_dist)
        self.wolf = Wolf(wolf_move_dist)

    def create_sheeps(
            self,
            sheeps_number,
            init_pos_limit,
            sheep_move_distance):
        for _ in range(sheeps_number):
            self.sheeps_collection.append(
                s.Sheep(init_pos_limit, sheep_move_distance))
        self.alives = sheeps_number

    def simulate_round(self):
        if self.alives == 0:
            return True

        self.simulate_sheeps()
        self.simulate_wolf()
        return False

    def simulate_wolf(self):
        sheep = self.attach_closest_sheep()
        if self.wolf.chase():
            sheep.isAlive = False
            self.alives -= 1

    def attach_closest_sheep(self):
        ab = -1
        index = 0
        for i, val in enumerate(self.sheeps_collection):
            if not val.isAlive:
                continue

            len = Point.distance(self.wolf, val)
            if ab == -1:
                ab = len
                index = i
            elif len < ab:
                ab = len
                index = i
        self.wolf.set_target(self.sheeps_collection[index])
        return self.sheeps_collection[index]

    def simulate_sheeps(self):
        for value in self.sheeps_collection:
            value.make_move()

    def start_simulation(self):
        for i in range(self.rounds):
            if self.simulate_round():
                break
            self.std_output_report(i + 1)
            self.update_dump(i + 1)
        self.json_dump()
        self.csv_dump()

    def update_dump(self, round: int):
        self.dump_list.append(
            {
                "round_no": round,
                "wolf_pos": (self.wolf.x, self.wolf.y),
                "sheeps_pos ": self.get_alive_sheeps_pos()
            }
        )
        self.csv_report.append([round, self.alives])

    def get_alive_sheeps_pos(self):
        list = []
        for val in self.sheeps_collection:
            if val.isAlive:
                list.append((val.x, val.y))
            else:
                list.append(None)
        return list

    def json_dump(self):
        with open("pos.json", "w") as output:
            json.dump(self.dump_list, output, indent='\t')

    def csv_dump(self):
        with open("alive.csv", "w") as target:
            writer = csv.writer(target)
            writer.writerows(self.csv_report)

    def std_output_report(self, round_nr):
        print(f"Round : {round_nr}")
        print(f"Sheeps alive : {self.alives}")
        print(
            f"Current Target : {self.sheeps_collection.index(self.wolf.target)}")
        print(f"Wolf : {self.wolf}")

        for i, val in enumerate(self.sheeps_collection):
            if val.isAlive:
                print(f"Sheep nr {i} : {self.sheeps_collection[i]}")
            else:
                print("None")
        print('---------------------')
