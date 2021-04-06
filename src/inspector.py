from workstation import *
from component import *
import numpy
import pathlib
from simpy.resources import container


import random
class Inspector:

    def __init__(self, env, tracking_vars, workstations, inspector_num, ALTERNATE_DESIGN):
        self.env = env
        self.tracking_vars = tracking_vars
        self.inspector_num = inspector_num
        
        self.workstations = []
        for workstation in workstations:
            self.workstations.append(workstation)
        self.action = env.process(self.run())

        self.design_num = ALTERNATE_DESIGN

    def run(self):
        print("Inspector {} is running".format(self.inspector_num))
        while True:
            if self.inspector_num == 1:
                service_time = self.calculate_service_time(1)
                self.tracking_vars.add_inspector_service_time(service_time, 1)
                yield self.env.timeout(service_time)
                blocked_time = self.env.now
                
                count = 0

                if self.design_num == 0:
                    if self.workstations[0].buffers[0].level <= self.workstations[1].buffers[0].level or self.workstations[0].buffers[0].level <= self.workstations[2].buffers[0].level:
                        yield self.workstations[0].buffers[0].put(1)
                        print("Added component 1 to workstation 1")
                    elif self.workstations[1].buffers[0].level <= self.workstations[2].buffers[0].level:
                        yield self.workstations[1].buffers[0].put(1)
                        print("Added component 1 to workstation 2")
                    else:
                        yield self.workstations[2].buffers[0].put(1)
                        print("Added component 1 to workstation 3")
                elif self.design_num == 1:
                    #alternative design - reverse priority
                    if self.workstations[2].buffers[0].level <= self.workstations[1].buffers[0].level or self.workstations[2].buffers[0].level <= self.workstations[0].buffers[0].level:
                        yield self.workstations[2].buffers[0].put(1)
                        print("Added component 1 to workstation 3")
                    elif self.workstations[1].buffers[0].level <= self.workstations[0].buffers[0].level:
                        yield self.workstations[1].buffers[0].put(1)
                        print("Added component 1 to workstation 2")
                    else:
                        yield self.workstations[0].buffers[0].put(1)
                        print("Added component 1 to workstation 1")
                elif self.design_num == 2:
                    #alternative design - random 
                    r = random.randint(0,2)
                    yield self.workstations[r].buffers[0].put(1)
                    print("Added component 1 to workstation {}".format(r))
                else:
                    #alternative design - circular design
                    if count == 0:
                        if self.workstations[0].buffers[0].level < 2:
                            yield self.workstations[0].buffers[0].put(1)
                            print("Added component 1 to workstation 1")

                        count += 1
                    if count == 1:
                        if self.workstations[1].buffers[0].level < 2:
                            yield self.workstations[1].buffers[0].put(1)
                            print("Added component 1 to workstation 2")
                        count += 1
                    if count == 2:
                        if self.workstations[2].buffers[0].level < 2:
                            yield self.workstations[2].buffers[0].put(1)
                            print("Added component 1 to workstation 3")
                        count = 0

                self.tracking_vars.add_inspector_blocked_time(self.env.now - blocked_time, 1)
                # Time Data Collected
                self.tracking_vars.add_batched_inspector_block_times(1, self.env.now)
            else:
                component_num = random.randint(2, 3)
                service_time = self.calculate_service_time(component_num)
                self.tracking_vars.add_inspector_service_time(service_time, 20 + component_num)
                yield self.env.timeout(service_time)
                blocked_time = self.env.now
                if component_num == 2:
                    index = 0
                else:
                    index = 1
                yield self.workstations[index].buffers[1].put(1)
                self.tracking_vars.add_inspector_blocked_time(self.env.now - blocked_time, component_num)
                # Time Data Collected
                self.tracking_vars.add_batched_inspector_block_times(component_num, self.env.now)
                print("Added component {} to workstation {}".format(component_num, component_num))            
        
    
    #opens the data files and calls the function to calcultate the proper value
    def calculate_service_time(self, component_num):
        path = pathlib.Path(__file__).parents[1].absolute()
        if self.inspector_num == 1:
            file_name = 'servinsp1.dat'
        else:
            file_name = 'servinsp{}{}.dat'.format(self.inspector_num, component_num)
        
        data = open('{}\\resources\\{}'.format(path, file_name)).read().splitlines()
        print("file was opened")
        return self.calculate_rand_value(data)

    #finds the mean of the given data then returns a random value based on the numpy exponential function
    def calculate_rand_value(self, data):
        datatotal = 0
        for i in range(0,300):
            datatotal += float(data[i])
        mean = datatotal / 300
        return numpy.random.exponential(mean)

