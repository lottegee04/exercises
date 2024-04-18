class Cycle:
    def __init__(self, iterable):
        self.__iterable = iterable
        self.__current = 0
    
    def __next__(self):
        if self.__current == len(self.__iterable):
            self.__current = 0
        result= self.__iterable[self.__current]
        self.__current +=1
        return result
    
    def __iter__(self):
        return self