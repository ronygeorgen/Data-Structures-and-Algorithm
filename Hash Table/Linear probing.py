class LinearProbingHashTable:
    def __init__(self,initial_size):
        self.size = initial_size
        self.count=0
        self.table = [None] * self.size
        self.load_factor_threshold = 0.7
    
    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self, key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self.resize()
        index = self.hash_function(key)
        initial_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key,value)
                return
            index = (index + 1) % self.size
            if index == initial_index:
                raise Exception("Hash Table is full")
        self.table[index] = (key,value)
        self.count += 1
    
    def search(self,key):
        index = self.hash_function(key)
        initial_index = index
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (index + 1) % self.size
            if index == initial_index:
                break
        return None
    
    def resize(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        old_table = self.table
        self.size = new_size
        self.table = new_table
        self.count = 0
        
        for item in old_table:
            if item:
                self.insert(item[0],item[1])
    
    def delete(self,key):
        index = self.hash_function(key)
        initial_index = index

        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                self.rehash(index)
                return True
            
            index = (index + 1) % self.size
            if index == initial_index:
                break
        return False

    def rehash(self,start_index):
        index = start_index
        while True:
            index = (index + 1) % self.size
            if self.table[index] is None:
                break
            key, value = self.table[index]
            self.table[index] = None
            self.insert(key,value)
    
    def __str__(self):
        return str([item for item in self.table if item is not None])

ht = LinearProbingHashTable(7)
ht.insert(10,"value1")
ht.insert(17,"value2")
ht.insert(24,"value3")
ht.insert(31,"value4")
ht.insert(38,"value5")
ht.insert(45,"value7")

print("After insertion:", ht)
print("Search 17:",ht.search(17))
print("Search 45:",ht.search(45))
ht.delete(17)
print("After deletion 17:",ht)
print("Search 17 after deletion:",ht.search(17))
ht.insert(52,"value8")
print("After inserting 52:", ht)