#!/bin/env python

import simulation
import argparse
import configparser
import os


def setup_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-c', '--config', help='spec config file')
    parse.add_argument('-d', '--dir', help='spec directory')
    parse.add_argument('-l', '--level', help='spec debug level', choices=['DEBUG', 'INFO', 'WARNING', 'ERROR', 'CRITICAL'], default='DEBUG')
    parse.add_argument('-r', '--rounds', help='spec rounds number', type=int, default=10)
    parse.add_argument('-s', '--sheeps', help='spec number of sheeps', type=int, default=5)
    parse.add_argument('-w', '--wait', help='pause simulatoin for each round', action='store_true', default=False)

    return parse.parse_args()


def parse_config(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)

    try:
        wolf_move_dist = parser.getfloat('Movement', 'WolfMoveDist')
        if wolf_move_dist <= 0:
            raise Exception("move distance is lower than 0")
    except Exception as e:
        print(e)
        print("Setting default 1.0")
        wolf_move_dist = 1.0

    try:
        sheep_move_dist = parser.getfloat('Movement', 'SheepMoveDist')
    except Exception as e:
        print(e)
        print("Setting default 0.5")
        sheep_move_dist = 0.5

    try:
        init_pos_limit = parser.getfloat('Terrain', 'InitPosLimit')
    except Exception as e:
        print(e)
        print("Setting default 10.0")
        init_pos_limit = 10.0

    return init_pos_limit, sheep_move_dist, wolf_move_dist


if __name__ == "__main__":
    args = setup_args()
    if args.dir:
        os.chdir(args.dir)

    rounds = args.rounds
    sheeps_number = args.sheeps
    wait = args.wait
    log_level = args.level

    init_pos_limit = 10.0
    sheep_move_dist = 0.5
    wolf_move_dist = 1.0

    if args.config:
        init_pos_limit, sheep_move_dist, wolf_move_dist = parse_config(args.config)

    sim = simulation.Simulation(rounds, sheeps_number, init_pos_limit, sheep_move_dist, wolf_move_dist, log_level)
    sim.start_simulation()
