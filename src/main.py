import numpy
import scipy
import random
import simpy
from simpy.resources import container
from workstation import *
from component import *
from inspector import *
from variables import *
import performance_metrics
import utils


SIMULATION_REPLICATION = 5
SIMULATION_TIME = 600000

if __name__ == "__main__":
    outputs = []
    for i in range(0, SIMULATION_REPLICATION):

        print("Running Replication {}".format(i + 1))
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
        # Simulates an Eight Hour Working day / LONG RUN 10K Minutes
        environment.run(until=SIMULATION_TIME)
        outputs.append(tracking_vars)

    #end loop
    print("Simulation has ended")

    print("\n==================== SIMULATION SUMMARY ====================\n")
    print("Total Number of Replications: {} \n".format(SIMULATION_REPLICATION))
    for index in range(0, len(outputs)):
        print("Simulation Replication Number: {} Summary".format(index + 1))

        # Inspector Blocked Time
        # for key, value in outputs[index].block_times.items():
        #     print("Blocked Time Inspector {} : {}".format(key, value))
        # utils.write_output('blocked_time', outputs[index], index + 1)
        # utils.write_output('batched_time', outputs[index], index + 1)
        utils.write_output('product', outputs[index], index + 1)

        performance_metrics.calculate_replication_average(outputs[index])
        print("========================================\n")

    print("================== Overall Simulation Summary  ======================\n")
    performance_metrics.calculate_average_across_replications(outputs)
    print("================== Overall Simulation Summary  ======================\n")



