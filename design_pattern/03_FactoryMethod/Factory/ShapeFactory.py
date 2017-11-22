from shape import *


class ShapeFactory:
    
    shapes = {}

    def __init__(self):
        for shape in Shape.__subclasses__():
            ShapeFactory.shapes[shape.__name__] = shape.__class__


    def produce(self, shape_name):                
        module = __import__("shape." + shape_name)
        shape_class = getattr(module, shape_name)
        
        return shape_class()