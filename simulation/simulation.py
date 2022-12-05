import json
import csv
import logging
from .sheep import Sheep
from .wolf import Wolf
from .point import Point


BASE_FROMAT = '[%(name)s][%(levelname)-6s][%(funcName)s] %(message)s'
FILE_FORMAT = '[%(asctime)s]' + BASE_FROMAT
LOG_FILE = 'chase.log'


class Simulation(object):

    sheeps_collection = []
    dump_list = []
    csv_report = []
    log_level = logging.DEBUG
    round = 0

    def __init__(
            self,
            rounds,
            sheeps_number,
            init_pos_limit,
            sheep_move_dist,
            wolf_move_dist,
            log_level):

        self.log_level = logging.getLevelName(log_level)
        self.logger = self.__setup_logging(self.log_level)
        self.rounds = rounds
        self.__create_sheeps(sheeps_number, init_pos_limit, sheep_move_dist)
        self.wolf = Wolf(wolf_move_dist)
        self.round = 0

    def __setup_logging(self, level):
        logger = logging.getLogger()
        logger.setLevel(level)

        file = logging.FileHandler(LOG_FILE)
        file.setFormatter(logging.Formatter(FILE_FORMAT))
        file.setLevel(level)

        logger.addHandler(file)
        logger.warning('siema')
        return logger

    def __create_sheeps(
            self,
            sheeps_number,
            init_pos_limit,
            sheep_move_distance):
        for _ in range(sheeps_number):
            self.sheeps_collection.append(
                Sheep(init_pos_limit, sheep_move_distance))

        self.alives = sheeps_number
        logging.debug("returning void")

    def simulate_round(self):
        self.round += 1

        self.__simulate_sheeps()
        self.__simulate_wolf()

        if self.alives == 0:
            logging.debug("returning True")
            return True

        logging.debug("returning False")
        return False

    def __simulate_wolf(self):
        sheep = self.__attach_closest_sheep()
        if self.wolf.chase():
            sheep.isAlive = False
            self.alives -= 1
        logging.debug("returning void")

    def __attach_closest_sheep(self):
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
        logging.debug(f"returning sheep {index} {self.sheeps_collection[index]}")
        return self.sheeps_collection[index]

    def __simulate_sheeps(self):
        for value in self.sheeps_collection:
            value.make_move()
        logging.debug("moved sheeps. returning void")

    def start_simulation(self):
        for i in range(self.rounds):
            if self.simulate_round():
                break
            self.std_output_report(i + 1)
            self.update_dump(i + 1)
        self.json_dump()
        self.csv_dump()
        logging.debug("returning void")

    def update_dump(self, round: int):
        self.dump_list.append(
            {
                "round_no": round,
                "wolf_pos": (self.wolf.x, self.wolf.y),
                "sheeps_pos ": self.__get_alive_sheeps_pos()
            }
        )
        self.csv_report.append([round, self.alives])
        logging.debug("append to file, return void")

    def __get_alive_sheeps_pos(self):
        list = []
        for val in self.sheeps_collection:
            if val.isAlive:
                list.append((val.x, val.y))
            else:
                list.append(None)
        logging.debug(f"returning {list}")
        return list

    def json_dump(self):
        with open("pos.json", "w") as output:
            json.dump(self.dump_list, output, indent='\t')
        logging.debug("return void")

    def csv_dump(self):
        with open("alive.csv", "w") as target:
            writer = csv.writer(target)
            writer.writerows(self.csv_report)
        logging.debug("return void")

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
        logging.debug("printed raprot return void")

    def get_raport(self):
        round = f"Round : {self.round}\n"
        sheeps_alive = f"Sheep Alive : {self.alives}\n"
        target = f"Current Target : {self.sheeps_collection.index(self.wolf.target)}\n"
        wolf = f"Wolf possition : {self.wolf}\n"
        sheeps = ""
        for i, val in enumerate(self.sheeps_collection):
            if val.isAlive:
                sheeps += f"Sheep nr {i} : {self.sheeps_collection[i]}\n"
            else:
                sheeps += "None\n"

        logging.debug(f"return {round.__class__}")
        return round + sheeps_alive + target + wolf + sheeps
