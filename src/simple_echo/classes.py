
from math import pi as π, e as e, tau as τ
class A_Shape:

    def get_area(self):
        raise NotImplementedError("I don't know how to calculate the area of this shape.")

    def get_circumference(self):
        raise NotImplementedError("I don't know how to calculate the circumference of this shape.")


    def __str__(self):
        return f"{self.__class__.__name__}"

class Circle(A_Shape):
    def __init__(self,radius):
        self.radius = radius

    def get_area(self):
        return π * self.radius**2
    
    def get_circumference(self):
        return π * self.radius
