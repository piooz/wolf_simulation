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

    return parse.parse_args()

def process_arguments(args):
    if args.config:
        pass
        

if __name__ == "__main__":
    args = setup_args()
    process_arguments(args);
    sim = simulation.Simulation(3,10,10,3,4);
    sim.start_simulation()
