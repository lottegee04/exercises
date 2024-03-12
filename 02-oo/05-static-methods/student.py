class Duration:
    def __init__(self, seconds):
        self.__seconds = seconds
        self.__minutes = self.__seconds /60
        self.__hours = self.__minutes /60
        
    
    @property
    def seconds(self):
        return self.__seconds
    @property 
    def minutes(self):
        return self.__minutes
    @property 
    def hours(self):
        return self.__hours
    
    
    @staticmethod
    def from_seconds(amount):
        duration = Duration(amount)
        return duration
    
    @staticmethod
    def from_minutes(amount):
        duration = Duration(amount*60)
        return duration
    
    @staticmethod
    def from_hours(amount):
        return Duration(amount*3600)