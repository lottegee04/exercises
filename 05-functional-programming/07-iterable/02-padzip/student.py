class PadZip:
    def __init__(self, iterable1, iterable2, padding=None):
        self.__iterleft = iter(iterable1)
        self.__iterright = iter(iterable2)
        self.__padding = padding
        
    
    def __iter__(self):
        return self
    
    def __next__(self):
        end_reached = 0
        try:
            left = next(self.__iterleft)
        except StopIteration:
            left = self.__padding
            end_reached+=1
        
        try:
            right = next(self.__iterright)
        except StopIteration:
            right = self.__padding
            end_reached +=1
        
        if end_reached == 2:
            raise StopIteration
        
        return (left,right)