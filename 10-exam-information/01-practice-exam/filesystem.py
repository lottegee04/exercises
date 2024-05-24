# Enter your code here:

from abc import ABC, abstractmethod
import re
class StorageDevice:
    def __init__(self, block_count, block_size):
        self.block_count = block_count
        self.__block_size = block_size
        self.__available_blocks = {number for number in range(block_count)}
        self.__used_blocks = set()
    
    @property
    def available_block_count(self):
        return len(self.__available_blocks)
    
    @property
    def used_block_count(self):
        return len(self.__used_blocks)
    
    @property
    def total_block_count(self):
        return len(self.__available_blocks) + len(self.__used_blocks)
    
    @property
    def block_size(self):
        return self.__block_size
    
    def allocate(self,block_count):
        if self.available_block_count < block_count:
            raise RuntimeError
        list_available_blocks = list(self.__available_blocks)
        for x in range(block_count):
            self.__used_blocks.add(list_available_blocks[x])
            self.__available_blocks.remove(list_available_blocks[x])
        return [list_available_blocks[x] for x in range(block_count)]
    
    def free(self, blocks):
        if len(set(blocks).difference(self.__used_blocks)) > 0:
            raise RuntimeError
        for block in blocks:
            self.__available_blocks.add(block)
            self.__used_blocks.remove(block)

class Entity(ABC):
    
    def __init__(self, storage,name):
        self.__storage = storage
        self.name =name
    @staticmethod
    def is_valid_name(name):
        return re.fullmatch(r'[a-z,0-9,\.]+',name.lower()) and len(name) <= 16
    
    @property
    def name(self):
        return self.__name
    
    @name.setter
    def name(self,value):
        if Entity.is_valid_name(value):
            self.__name = value
        else:
            raise RuntimeError
    
    @property
    def storage(self):
        return self.__storage
    
    @property
    @abstractmethod
    def size_in_blocks(self):
        pass
    
    @property
    def size_in_bytes(self):
        return self.size_in_blocks*self.storage.block_size
    
    @abstractmethod
    def clear(self):
        pass
    

class File(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__size_in_blocks =0
        self.__occupied_blocks = []
    
    @property
    def size_in_blocks(self):
        return self.__size_in_blocks
    
    def grow(self,block_count):
        self.__occupied_blocks.append(self.storage.allocate(block_count))
        
    def clear(self):
        self.storage.free([x for x in range(self.__occupied_blocks)])
        self.__size_in_blocks = 0
        self.__occupied_blocks = []

class Directory(Entity):
    def __init__(self, storage, name):
        super().__init__(storage, name)
        self.__children = []
    
    def add(self,entity):
        self.__children.append(entity)
    
    @property
    def size_in_blocks(self):
        return sum([child.size_in_blocks for child in self.__children])
    
    def clear(self):
        for child in self.__children:
            child.clear()
            self.__children.remove(child)
            
            
storage = StorageDevice(block_count = 100, block_size=5)
print(storage.block_size)
print(storage.available_block_count)
storage.allocate(15)
print(storage.available_block_count)
storage.allocate(5)
print(storage.available_block_count)
storage.free([0,1,2,3,4])
print(storage.available_block_count)
