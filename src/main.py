import numpy
import scipy
import random
import simpy
from simpy.resources import container
from workstation import *
from component import *
from inspector import *
from variables import *


ITERATIONS = 2


if __name__ == "__main__":
    outputs = []
    for i in range(0, ITERATIONS):

        print("Running iteration {}".format(i + 1))
        environment = simpy.Environment()
        tracking_vars = TrackingVariables()

        #Create the inspectors and workstations
        workstation_one = Workstation(environment, 1, tracking_vars, 1)
        workstation_two = Workstation(environment, 2, tracking_vars, 2)
        workstation_three = Workstation(environment, 2, tracking_vars, 3)
        print("Workstations setup complete")

        insepctor_one = Inspector(environment, tracking_vars, [workstation_one, workstation_two, workstation_three], 1)
        inspector_two = Inspector(environment, tracking_vars, [workstation_two, workstation_three], 2)
        print("Inspector setup complete")

        print("running simulation")
        environment.run(until=28000)

        outputs.append(tracking_vars)

    #end loop
    print("Simulation has ended")
    
    for data in outputs:
        for key, value in data.service_times.items():
            print("{} : {}".format(key, value))
        for key, value in data.idle_times.items():
            print("Idle {} : {}".format(key, value))
        for key, value in data.block_times.items():
            print("Block {} : {}".format(key, value))
        for key, value in data.products.items():
            print("Product {} : {}".format(key, value))

