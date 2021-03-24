class Component:

    def __init__(self, name):
        self.name = name

    def get_name(self):
    	return self.name 


if __name__ == "__main__":
    c = Component("Test Name")
    print(c.get_name())