class Queue:
    def __init__(self):
        self.queue_list = []
        
    def add(self,item):
        self.queue_list.append(item)
    
    def next(self):
        next_one = self.queue_list[0]
        self.queue_list.pop(0)
        return next_one
    
    def is_empty(self):
        return len(self.queue_list) == 0