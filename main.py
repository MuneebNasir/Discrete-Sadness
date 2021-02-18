from workstation import *
from component import *


c1 = Component("C1")
c11 = Component("C11")
w1 = Workstation([c1, c11])

w2 = Workstation()
w2.set_buffers([], [])

w3 = Workstation()
w3.set_buffers([],[])


w1.assemble_product()
w2.assemble_product()
w3.assemble_product()