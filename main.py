#!/bin/env python

import simulation
import argparse

def setup_args():
    parse = argparse.ArgumentParser()
    parse.add_argument('-c', '--config', help='spec config file')
    parse.add_argument('-d', '--dir', help='spec directory')
    parse.add_argument('-l', '--level', help='spec debug level', choices=['DEBUG','INFO','WARNING','ERROR','CRITICAL'])
    parse.add_argument('-r', '--rounds', help='spec rounds number', type=int)
    parse.add_argument('-s', '--sheeps', help='spec number of sheeps', type=int)
    parse.add_argument('-w', '--wait', help='pause simulatoin for each round', action='store_true')

    args = parse.parse_args()
    pass


if __name__ == "__main__":
    setup_args()
    print("hello world")
    sim = simulation.Simulation(20, 10, 10, 1, 1)
    sim.start_simulation()
