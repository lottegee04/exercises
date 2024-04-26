class Book:
    def __init__(self,title,isbn):
        self.title = title
        self.isbn= isbn
        
    @property
    def title(self):
        return self.__title
    
    @property
    def isbn(self):
        return  self.__isbn
    
    @title.setter
    def title(self,new_title):
        if new_title is not None and new_title.replace(" ","") != "" :
            self.__title = new_title
        else:
            raise RuntimeError("title cannot be empty")

    @isbn.setter
    def isbn(self, new_isbn):
        digits = [int(digit) for digit in new_isbn if digit.isdigit()]
        if sum([digits[x] if x %2 == 0 else digits[x] * 3 for x in range(len(digits))]) % 10 == 0:
            self.__isbn = new_isbn
            
        else:
            raise RuntimeError("invalid isbn")
        


