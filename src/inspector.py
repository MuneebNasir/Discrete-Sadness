from workstation import *
from component import *
import numpy
from simpy.resources import container


import random
class Inspector:

    def __init__(self, env, tracking_vars, workstations, inspector_num):
        self.env = env
        self.tracking_vars = tracking_vars
        self.inspector_num = inspector_num
        
        self.workstations = []
        for workstation in workstations:
            self.workstations.append(workstation)

    def test(self):
        print("Inspector {} is running".format(self.inspector_num))
        print("Inspector {} is {}".format(self.inspector_num, self.calculate_service_time(2)))

    def run(self):
        print("Inspector {} is running".format(self.inspector_num))

        while True:
            service_time = self.calculate_service_time(component_num)
            if self.inspector_num == 1:
                self.inspector_one(service_time)
            else:
                self.inspector_two(service_time)            

    #function for inspector one
    def inspector_one(self, service_time):
        self.tracking_vars.add_inspector_service_time(service_time, 1)
        yield self.env.timeout(service_time)
        blocked_time = self.env.now
        
        if self.workstations[0].buffers[0].level <= self.workstations[1].buffers[0].level or self.workstations[0].buffers[0].level <= self.workstations[2].buffers[0].level:
            yield self.workstations[0].buffers[0].put(1)
            print("Added component 1 to workstation 1")
        elif self.workstations[1].buffers[0].level <= self.workstations[2].buffers[0].level:
            yield self.workstations[1].buffers[0].put(1)
            print("Added component 1 to workstation 2")
        else:
            yield self.workstations[2].buffers[0].put(1)
            print("Added component 1 to workstation 3")

        self.tracking_vars.add_inspector_blocked_time(self.env.now - blocked_time, 1)
    
    #function for inspector two
    def inspector_two(self, service_time):
        component_num = random.randint(2,3)
        self.tracking_vars.add_inspector_service_time(service_time, 20 + component_num)
        yield self.env.timeout(service_time)
        blocked_time = self.env.now
        yield self.workstations[component_num - 1].buffers[1].put(1) 
        self.tracking_vars.add_inspector_blocked_time(self.env.now - block_time, component_num)
        print("Added component {} to workstation {}".format(component_num))
        
    
    #opens the data files and calls the function to calcultate the proper value
    def calculate_service_time(self, component_num):
        if self.inspector_num == 1:
            file_name = "servinsp{}.dat".format(self.inspector_num)
        else:
            file_name = "servinsp{}{}.dat".format(self.inspector_num, component_num)
        
        data = open("../resources/{}".format(file_name)).read().splitlines()
        return self.calculate_rand_value(data)

    #finds the mean of the given data then returns a random value based on the numpy exponential function
    def calculate_rand_value(self, data):
        datatotal = 0
        for i in range(0,300):
            datatotal += float(data[i])
        mean = datatotal / 300
        return numpy.random.exponential(mean)*60
