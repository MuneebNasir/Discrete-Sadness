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
    def add_insp_1_st(self, value):
        self.service_times["inspector_1"].append(value)

    def add_insp_22_st(self, value):
        self.service_times["inspector_22"].append(value)

    def add_insp_23_st(self, value):
        self.service_times["inspector_23"].append(value)

    #workstation service time
    def add_worskation_service_time(self, value, work_num):
        key = "workstation_" + work_num
        self.service_times[key].append(value)


    #blocked time
    def add_insp_1_bt(self, value):
        self.block_times[1].append(value)

    def add_insp_22_bt(self, value):
        self.block_times[2].append(value)

    def add_insp_23_bt(self, value):
        self.block_times[3].append(value)

    #idle time
    def add_workstation_idle_time(self, value, work_num):
        self.idle_times[work_num].append(value)

    #number of products
    def add_product(self, work_num):
        self.products[work_num] += 1

