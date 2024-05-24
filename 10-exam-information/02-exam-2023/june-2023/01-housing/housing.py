# enter your code here to solve the housing assignment
# voer hier je code in om de huisvestingsvraag op te lossen
from abc import ABC, abstractmethod
import re
class Person:
    @staticmethod
    def is_valid_name(name):
        return re.fullmatch(r'/[a-zA-Z]+ [a-zA-Z]+( [a-zA-Z]+)*',name)
    
    def  __init__(self, id, name, is_a_student):
        self.id = id
        self.name = name
        self.is_a_student = is_a_student
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if Person.is_valid_name(value):
            self.__name = value
        else:
            raise ValueError
        

class Residence(ABC):
    def __init__(self, address, area, number_of_rooms):
        self.address = address
        self.area = area
        self.number_of_rooms = number_of_rooms
        self.__occupants = {}
        
    @property
    def number_of_occupants(self):
        return len(self.__occupants)
    
    @property
    def maximum_occupants(self):
        return min([self.area // 20,self.number_of_rooms*2])
        
    def register_resident(self,person):
        if not person.id in self.__occupants:
            if self.number_of_occupants < self.maximum_occupants:
                self.__occupants[person.id] = person
        else:
            raise RuntimeError
    
    def unregister_resident(self,id):
        if id in self.__occupants.keys():
            del self.__occupants[id]
        
    @property
    def resident_names(self):
        return [person.name for person in self.__occupants.values()]
    
    @abstractmethod
    def calculate_value(self):
        pass
    

class Villa(Residence):
    def __init__(self, address, area, number_of_rooms, garage_capacity):
        super().__init__(address, area, number_of_rooms)
        self.garage_capacity =garage_capacity
    
    def calculate_value(self):
        return (25000*self.number_of_rooms) + (2100 * self.area)+(10000*self.garage_capacity)


class StudentKot(Residence):
    
    def __init__(self, address, area):
        super().__init__(address, area, 1)
    
    def register_resident(self, person):
        if person.is_a_student:
            return super().register_resident(person)
        else:
            raise RuntimeError #blijkbaar mag "raise BlablaError" niet na een if, dus die moet na een else (niet zeker van maar iem had hier een probleem mee; uitproberen ??)
    def calculate_value(self):
        return 150000 +(750*self.area)


