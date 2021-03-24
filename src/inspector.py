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


    def run(self):
        print("Inspector {} is running".format(self.inspector_num))

        while True:
            service_time = random.randint(1,10)
            self.tracking_vars.add_insp_1_st(service_time)







    # def set_component(self, component):
    # 	self.component = component

    # def inspect_component(self):

    #     if self.component.name == "C1":
    #         print("Inspector 1: Inspecting Item {} ".format(self.component.name))
    #         if self.workstation.is_buffer_free("B1"):
    #             self.workstation.add_component(self.component, "B1")


    #     if self.component.name == "C2":
    #         print("Inspector 2: Inspecting Item {} ".format(self.component.name))
    #         if self.workstation.is_buffer_free("B2"):
    #             self.workstation.add_component(self.component, "B2")


    #     if self.component.name == "C3":
    #         print("Inspector 2: Inspecting Item {} ".format(self.component.name))
    #         if self.workstation.is_buffer_free("B2"):
    #             self.workstation.add_component(self.component, "B2")
    
    # def retrieve_service_times_nsp1(self):
    #     file = "../resources/servinsp1.dat"
    #     return self.read_file(file)

    # def retrieve_service_times_nsp2(self):
    #     file = "../resources/servinsp22.dat"
    #     return self.read_file(file)

    # def retrieve_service_times_nsp3(self):
    #     file = "../resources/servinsp23.dat"
    #     return self.read_file(file)
    
    # def read_file(self, file):
    #     time_values = []
    #     with open(file, "rt") as data:
    #         for time_value in data:
    #             if time_value.strip():
    #                 time_values.append(time_value.strip())


    #     return time_values
