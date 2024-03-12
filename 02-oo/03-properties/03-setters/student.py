# Write your code here
class Time:
    def __init__(self,hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds =seconds
    
    @property
    def hours(self):
        return self.__hours
    @property
    def minutes(self):
        return self.__minutes
    @property
    def seconds(self):
        return self.__seconds
    
    @hours.setter
    def hours(self, value):
        if value <0 or value > 23:
            raise ValueError("Hours must be between 0 and 23")
        else:
            self.__hours = value
    
    @minutes.setter
    def minutes(self,value):
        if value <0 or value > 59:
            raise ValueError("Minutes must be between 0 and 59")
        else:
            self.__minutes = value
    
    @seconds.setter
    def seconds(self,value):
        if value <0 or value > 59:
            raise ValueError("Seconds must be between 0 and 59")
        else:
            self.__seconds = value
    