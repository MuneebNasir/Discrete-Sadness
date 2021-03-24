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
    for inter in range(0, ITERATIONS):
        environment = simpy.Environment()
        tracking_vars = TrackingVariables()
        #Create the inspectors and workstations
        workstation_one = Workstation(environment, 1, tracking_vars, 1)
        workstation_two = Workstation(environment, 2, tracking_vars, 2)
        workstation_three = Workstation(environment, 2, tracking_vars, 3)

        insepctor_one = Inspector(environment, tracking_vars, [workstation_one, workstation_two, workstation_three], 1)
        inspector_two = Inspector(environment, tracking_vars, [workstation_two, workstation_three], 2)

        workstation_one.test()
        workstation_two.test()
        workstation_three.test()

        insepctor_one.test()
        inspector_two.test()
