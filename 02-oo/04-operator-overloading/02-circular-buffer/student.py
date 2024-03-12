class CircularBuffer:
    def __init__(self, n):
        self.n = n
        self.items = []
    
    def add(self, item):
        if len(self.items) ==self.n:
            self.items.pop(0)
            self.items.append(item)
        else:
            self.items.append(item)    
        
    def __getitem__(self,index):
        return self.items[index]
    def __len__(self):
        return len(self.items)