from Workstation import *
from Component import *

class Inspector:

    def __init__(self, workstation):
        self.workstation = workstation
        self.is_blocked = False
        self.component = None

    def set_component(self, component):
    	self.component = component

    def inspect_component(self):

        if self.component.name == "C1":
            print("Inspector 1: Inspecting Item {} ".format(self.component.name))
            if workstation.is_buffer_free("B1"):
                self.workstation.add_component(self.component, "B1")


        if self.component.name == "C2":
            print("Inspector 2: Inspecting Item {} ".format(self.component.name))
            if workstation.is_buffer_free("B2"):
                self.workstation.add_component(self.component, "B2")


        if self.component.name == "C3":
            print("Inspector 2: Inspecting Item {} ".format(self.component.name))
            if workstation.is_buffer_free("B2"):
                self.workstation.add_component(self.component, "B2")
    
    def retrieve_service_times(self, inspector_type, component_name):
        service_times_I1 = []
        service_times_I2 = []
        service_times_I3 = []

        file = None 
        if inspector_type == "I1":
            file = "../resources/servinsp1.dat"

        if inspector_type == "I2" or component_name =="C2":
            file = "../resources/servinsp22.dat"

        if inspector_type == "I2" or component_name =="C3":
            file = "../resources/servinsp23.dat"

        if file is not None: 
            if "servinsp1" in file:
                service_times_I1 = self.read_file(file)

            if "servinsp22" in file:
                service_times_I2 = self.read_file(file)

            if "servinsp23" in file:
                service_times_I3 = self.read_file(file)

    def read_file(self, file):
        time_values = []
        with open(file, "rt") as data:
            for time_value in data:
                if time_value.strip():
                    time_values.append(time_value.strip())


        return time_values



