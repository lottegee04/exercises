from abc import ABC, abstractmethod
from math import pi


class Shape(ABC):
    @property
    @abstractmethod
    def area(self):
        ...

    @property
    @abstractmethod
    def perimeter(self):
        ...

class Rectangle(Shape):
    def __init__(self, length, width):
        super().__init__()
        self.__length = length
        self.__width = width
        
    @property
    def length(self):
        return self.__length
    
    @property
    def width(self):
        return self.__width
    
    @property
    def perimeter(self):
        return 2*(self.__width +self.__length)
    
    @property
    def area(self):
        return self.width * self.length
    
    
class Square(Rectangle):
    def __init__(self, side):
        super().__init__(side, side)
        self.__side = side
    
    @property
    def side(self):
        return self.__side
    
    @property
    def perimeter(self):
        return 4*self.side
    

class Ellipse(Shape):
    def __init__(self, minor_radius,major_radius):
        super().__init__()
        self.__minor_radius = minor_radius
        self.__major_radius = major_radius
        
    @property
    def minor_radius(self):
        return self.__minor_radius
    
    @property
    def major_radius(self):
        return self.__major_radius
    
    @property
    def perimeter(self):
        raise NotImplementedError
    
    @property
    def area(self):
        return pi *self.minor_radius * self.major_radius
    
    
class Circle(Ellipse):
    def __init__(self, radius):
        super().__init__(radius,radius)
        self.__radius = radius
    
    @property
    def radius(self):
        return self.__radius
    
    @property
    def perimeter(self):
        return 2*pi*self.radius
    
    @property
    def area(self):
        return pi * self.radius **2    
    
        
        