#!/bin/env python

import simulation
import argparse
import logging

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

BASE_FROMAT = '[%(name)s][%(levelname)-6s] %(message)s'
FILE_FORMAT = '[%(asctime)s]' + BASE_FROMAT

def setup_logging(level = logging.DEBUG):
    logger = logging.getLogger();
    logger.setLevel(level);

    file = logging.FileHandler('chase.log');
    file.setFormatter(logging.Formatter(FILE_FORMAT));
    file.setLevel(level);

    logger.addHandler(file);
    
    logger.warning('siema');
    return logger;

if __name__ == "__main__":
    logger = setup_logging();
    setup_args()
    print("hello world")
    sim = simulation.Simulation(3,10,10,3,4);
    sim.start_simulation()
