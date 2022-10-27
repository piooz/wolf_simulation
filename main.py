#!/bin/env python

import simulation

if __name__ == "__main__":
    print("hello world");
    sim = simulation.Simulation(20, 5, 10, 1, 1);
    sim.start_simulation();
