from component import *
from variables import *
from simpy.resources import container
import simpy
import numpy

import random

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

    def test(self):
        print("Workstation {} is running".format(self.work_num))
        print(self.calculate_service_time())

    def run(self):
        print("Workstation {} is running".format(self.work_num))        

        while True:
            idle_timer = self.env.now
            #Workstation 1 has only one buffer, 2 and 3 have two buffers
            if self.work_num == 1:
                yield self.buffers[0].get(1)
            else:
                yield self.buffers[0].get(1) & self.buffers[1].get(1)

            self.tracking_vars.add_workstation_idle_time(value, self.work_num)
            service_time = calculate_service_time()
            self.tracking_vars.add_worskation_service_time()
            yield self.env.timeout(service_time)
            self.tracking_vars.add_product(work_num)
            print("Product {} has been created".format(self.work_num))

    def calculate_rand_value(self, data):
        datatotal = 0
        for i in range(0,300):
            datatotal += float(data[i])
        mean = datatotal / 300
        return numpy.random.exponential(mean)*60


    def calculate_service_time(self):
        file_name = "ws{}.dat".format(self.work_num)
        
        data = open("../resources/{}".format(file_name)).read().splitlines()
        #data = open("{}".format(file_name)).read.splitlines()
        return self.calculate_rand_value(data)


    
    # def add_to_buffer(self, index, num):
    #     self.buffers[index] = num
    
    # def assemble_product(self):
    #     print(self.is_busy)
    #     # W1
    #     if self.buffer2 is None:
    #         if not self.is_buffer_empty('B1') and not self.is_busy:
    #             is_busy = True
    #             print(self.buffer.pop(0).name)
    #         else:
    #             print('Nothing to do here.')
        
    #     else:
    #         if not self.is_buffer_empty('B1') and not self.is_buffer_empty('B2'):
    #             # W2
    #             if self.buffer2[0].name == 'C2' and not self.is_busy:
    #                 is_busy = True
    #                 print(self.buffer.pop(0).name)
    #                 print(self.buffer2.pop(0).name)
    #             # W3
    #             elif self.buffer2[0].name == 'C3' and not self.is_busy :
    #                 is_busy = True
    #                 print(self.buffer.pop(0).name)
    #                 print(self.buffer2.pop(0).name)



    # def is_buffer_free(self, buffer_type):
    #     if buffer_type == 'B1':
    #         return (len(self.buffer) >= 0 and len(self.buffer) < 2)
    #     if buffer_type == 'B2':
    #         return (len(self.buffer2) >= 0 and len(self.buffer2) < 2)
    
    
    # def is_buffer_empty(self, buffer_type):
    #     if buffer_type == 'B1':
    #         return (len(self.buffer) == 0)
    #     if buffer_type == 'B2':
    #         return (len(self.buffer2) == 0)

    # def add_component(self, component, buffer_type):
    #     if buffer_type == 'B1':
    #         self.buffer.append(component)
    #     if buffer_type == 'B2':
    #         self.buffer2.append(component)

    # def retrieve_process_times_ws1(self):
    #     file = "../resources/ws1.dat"
    #     return self.read_file(file)

    # def retrieve_process_times_ws2(self):
    #     file = "../resources/ws2.dat"
    #     return self.read_file(file)

    # def retrieve_process_times_ws3(self):
    #     file = "../resources/ws3.dat"
    #     return self.read_file(file)

    # def read_file(self, file):
    #     time_values = []
    #     with open(file, "rt") as data:
    #         for time_value in data:
    #             if time_value.strip():
    #                 time_values.append(time_value.strip())


    #     return time_values

