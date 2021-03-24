class TrackingVariables:

    def __init__(self):
        self.service_times = {
            "inspector_1": [],
            "inspector_22": [],
            "inspector_23": [],
            "workstation_1": [],
            "workstation_2": [],
            "workstation_3": [],
        }
        self.idle_times = {
            1: [],
            2: [],
            3: [],
        }
        self.block_times = {
            1: [],
            2: [],
            3: []
        }
        self.products = {
            1: 0,
            2: 0,
            3: 0,
        }

    #inspector 1 service time
    def add_inspector_service_time(self, value, inspector_num):
        key = "inspector_{}".format(inspector_num)
        self.service_times[key].append(value)

    #workstation service time
    def add_worskation_service_time(self, value, work_num):
        key = "workstation_" + work_num
        self.service_times[key].append(value)

    #blocked time
    def add_inspector_blocked_time(self, value, inspector_num):
        index = inspector_num - 1
        self.block_times[index].append(value)

    #idle time
    def add_workstation_idle_time(self, value, work_num):
        index = work_num - 1
        self.idle_times[index].append(value)

    #number of products
    def add_product(self, work_num):
        index = work_num - 1
        self.products[index] += 1

