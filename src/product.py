class Product:

	self.name = None 

    def __init__(self, component=None, name):
        self.component = component
        self.component2 = None
        self.name = name

    def set_components(self, component, component2):
    	self.component = component
        self.component2 = component2

    def get_name(self):
        return name

    def set_name(self, name):
        self.name = name

    def get_product_components(self):
        return component, component2


    