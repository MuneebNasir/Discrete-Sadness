import math
from component import *
from variables import *
from simpy.resources import container
import simpy
import numpy
import random
import pathlib

class Workstation:

    # is_busy = False

    #Constructor for a workstation
    #env is the simpy environment
    #num_buffers is the number of buffers the workstation has
    #tracking_vars is the refernce to the object tracking times
    #work_num is the workstation number
    def __init__(self, env, num_buffers, tracking_vars, work_num):
        self.env = env
        self.tracking_vars = tracking_vars
        self.work_num = work_num
        self.buffers = []
        for i in range(0, num_buffers):
            self.buffers.append(container.Container(self.env, 2))
        
        self.action = env.process(self.run())


    def run(self):
        print("Workstation {} is running".format(self.work_num))        

        while True:
            idle_timer = self.env.now
            #Workstation 1 has only one buffer, 2 and 3 have two buffers
            if self.work_num == 1:
                yield self.buffers[0].get(1)
            else:
                yield self.buffers[0].get(1) & self.buffers[1].get(1)

            self.tracking_vars.add_workstation_idle_time(self.env.now - idle_timer, self.work_num)
            service_time = self.calculate_service_time()
            self.tracking_vars.add_worskation_service_time(service_time, self.work_num)
            yield self.env.timeout(service_time)

            # Time Data Collected (Manual Analysis & Change) 4000 (Original) 500 (Alternate)
            # if self.env.now > 500:
            self.tracking_vars.add_product(self.work_num)

            self.tracking_vars.add_batched_inspector_block_times(self.work_num, self.env.now)
            print("Product {} has been created".format(self.work_num))


    def calculate_service_time(self):
        path = pathlib.Path(__file__).parents[1].absolute()
        file_name = "ws{}.dat".format(self.work_num)
        
        data = open("{}/resources/{}".format(path, file_name)).read().splitlines()
        return self.calculate_rand_value(data)

    def calculate_rand_value(self, data):
        datatotal = 0
        for i in range(0, 300):
            datatotal += float(data[i])
        mean = datatotal / 300
        return numpy.random.exponential(mean)

    def generate_random_number_ws2(self, mean):
        # Distribution Parameter for Exponential Distribution
        lambda_val = 1 / mean
        # Generating the random number in range [0,1]
        rand_number = numpy.random.uniform(low=0.0, high=1.0)
        rand_variate = (-1 / lambda_val) * math.log(rand_number)
        return rand_variate

    def collect_batch_results_ws(self):
        """
        Need to collect results after Every 500s
        :return:
        """

        return None