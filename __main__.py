#!/bin/env python

import simulation
import argparse
import configparser
import sys
import os

global rounds
global init_pos_limit
global sheep_move_dist
global wolf_move_dist

def setup_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-c', '--config', help='spec config file')
    parse.add_argument('-d', '--dir', help='spec directory')
    parse.add_argument('-l', '--level', help='spec debug level', choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])
    parse.add_argument('-r', '--rounds', help='spec rounds number', type=int)
    parse.add_argument('-s', '--sheeps', help='spec number of sheeps', type=int)
    parse.add_argument('-w', '--wait', help='pause simulatoin for each round', action='store_true')

    return parse.parse_args()

def process_arguments(args):
    if args.config:
        parse_config(args.config)
    if args.dir:
        try:
            os.chdir(args.dir)
        except:
            print("bad directory")
            print(sys.exc_info)
        os.chdir(args.dir)
        
def parse_config(filename):
    parser = configparser.ConfigParser()
    parser.read(filename)

    try:
        global wolf_move_dist
        wolf_move_dist = parser.getfloat('Movement', 'WolfMoveDist')
        if wolf_move_dist <= 0:
            raise Exception("move distance is lower than 0")
    except Exception as e:
        print(e)
        print("Setting default 1.0")
        wolf_move_dist = 1.0

    try:
        global sheep_move_dist
        sheep_move_dist = parser.getfloat('Movement', 'SheepMoveDist')
    except Exception as e:
        print(e)
        print("Setting default 0.5")
        sheep_move_dist = 0.5

    try:
        global init_pos_limit
        parser = parser.getfloat('Terrain', 'InitPosLimit')
    except Exception as e:
        print(e)
        print("Setting default 10.0")
        init_pos_limit = 10.0 

def set_defaults():
    global rounds
    global sheeps_number
    global init_pos_limit
    global sheep_move_dist
    global wolf_move_dist

    rounds = 10;
    sheeps_number = 5
    init_pos_limit = 10.0
    sheep_move_dist = 0.5
    wolf_move_dist = 1.0 

if __name__ == "__main__":
    set_defaults()
    args = setup_args()
    process_arguments(args);
    sim = simulation.Simulation(rounds, sheeps_number, init_pos_limit, sheep_move_dist, wolf_move_dist)
    sim.start_simulation()
