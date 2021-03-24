import random
from workstation import *
from component import *
from inspector import *

# ALQ - Arrival at Inspector Queue 
# ES - End Component Servcing 
# EP - End Product Processing
EVENTS = ["ALQ", "ES", "EP"]

# FEL To Track Events - ESTA Scheduling Algorithm 
future_event_list = []

c1 = Component("C1")
c11 = Component("C11")
w1 = Workstation([c1, c11])

w2 = Workstation([])
w2.set_buffers([])
w2.add_component("B1", c1)

w3 = Workstation([])
w3.set_buffers([])

c2 = Component("C2")
w3.add_component(c2, "B2")


w1.assemble_product()
w2.assemble_product()
w3.assemble_product()
i1 = Inspector(w1)
i2 = Inspector(w1)
i1.retrieve_service_times_nsp1()
w3.retrieve_process_times_ws1()

# Need to process the FEL 
i = 0 
while i < 10:
    i += 1
    # Creating the Component Using Random Number Generator 
    component_new = Component("C{}".format(random.randint(1, 3)))
    print(component_new.name)