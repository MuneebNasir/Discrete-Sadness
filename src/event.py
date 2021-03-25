class Event:

    def __init__(self, end_time, event_type, component_name):
        self.end_time = end_time
        self.event_type = event_type
        self.component_name = component_name

    def get_end_time(self):
        return self.end_time

    def get_event_type(self):
        return self.event_type

    def get_component_name(self):
        return self.component_name