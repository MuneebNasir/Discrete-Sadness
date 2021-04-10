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


class SimulationModel(object):

    def __init__(self):
        self.SIMULATION_REPLICATION = 5
        self.SIMULATION_TIME = None
        self.ALTERNATE_DESIGN = 0

    def validate_user_input(self):
        if self.ALTERNATE_DESIGN > 2:
            print("Invalid Selection: {} - Setting ALTERNATE_DESIGN Option To Default".format(self.ALTERNATE_DESIGN))
            self.ALTERNATE_DESIGN = 0

    def run_simulation(self):
        outputs = []

        # Simulation variables
        print("Enter Time For Simulation in Seconds (Default - 28,000)")
        self.SIMULATION_TIME = int(input("Enter time: ") or "28000")
        self.SIMULATION_REPLICATION = int(input("Enter Replications: ") or "70")
        print("Choose from the design that you would like to use")
        print("0: Normal Design")
        print("1: Cyclic Distribution")
        # print("2: Reverse Priority")
        self.ALTERNATE_DESIGN = int(input("Enter Design Number: ") or "0")
        self.validate_user_input()

        for i in range(0, self.SIMULATION_REPLICATION):
            print("Running Replication {}".format(i + 1))
            environment = simpy.Environment()
            tracking_vars = TrackingVariables()

            # Create the inspectors and workstations
            workstation_one = Workstation(environment, 1, tracking_vars, 1)
            workstation_two = Workstation(environment, 2, tracking_vars, 2)
            workstation_three = Workstation(environment, 2, tracking_vars, 3)
            print("Workstations setup complete")

            inspector_one = Inspector(environment, tracking_vars, [workstation_one, workstation_two, workstation_three],
                                      1, self.ALTERNATE_DESIGN)
            inspector_two = Inspector(environment, tracking_vars, [workstation_two, workstation_three], 2, 0)
            print("Inspector setup complete")

            print("running simulation")
            # Simulates an Eight Hour Working day / LONG RUN 10K Minutes
            environment.run(until=self.SIMULATION_TIME)
            outputs.append(tracking_vars)

        # end loop
        print("Simulation has ended")

        print("\n==================== SIMULATION SUMMARY ====================\n")
        print("Total Number of Replications: {} \n".format(self.SIMULATION_REPLICATION))
        for index in range(0, len(outputs)):
            print("Simulation Replication Number: {} Summary".format(index + 1))
            utils.write_output('product', outputs[index], index + 1)

            performance_metrics.calculate_replication_average(outputs[index])
            print("========================================\n")

        print("================== Overall Simulation Summary  ======================\n")
        performance_metrics.calculate_average_across_replications(outputs)
        print("================== Overall Simulation Summary  ======================\n")


if __name__ == "__main__":
    model = SimulationModel()
    SimulationModel.run_simulation(model)
