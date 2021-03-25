import numpy

class Product:

    def __intit__(self, name, component=None):
        self.component = component
        self.component2 = None
        self.name = name

    def set_components(self, component, component2):
        self.component = component
        self.component2 = component2

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def get_product_components(self):
        return self.component, self.component2

    