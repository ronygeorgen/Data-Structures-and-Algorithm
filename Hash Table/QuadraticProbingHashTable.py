class QuadraticProbingHashTable:
    def __init__(self,initial_size):
        self.size = initial_size
        self.count = 0
        self.table = [None] * self.size
        self.load_factor_threshold = 0.5
    
    def hash_function(self,key):
        return hash(key) % self.size
    
    def insert(self,key, value):
        if self.count / self.size >= self.load_factor_threshold:
            self.resize()
        index = self.hash_function(key)
        initial_index = index
        i = 1
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = (key, value)
                return
            index = (initial_index + i**2) % self.size
            i += 1
            if i > self.size:
                raise Exception("Hash table is full")
        self.table[index] = (key,value)
        self.count += 1
    
    def search(self,key):
        index = self.hash_function(key)
        initial_index = index
        i = 1
        while self.table[index] is not None:
            if self.table[index][0] == key:
                return self.table[index][1]
            index = (initial_index + i**2) % self.size
            i += 1
            if i > self.size:
                break
        return None

    def delete(self, key):
        index = self.hash_function(key)
        initial_index = index
        i = 1
        while self.table[index] is not None:
            if self.table[index][0] == key:
                self.table[index] = None
                self.count -= 1
                self.rehash(index)
                return True
            index = (initial_index + i**2) % self.size
            i += 1
            if i > self.size:
                break
        return False
    
    def rehash(self,start_index):
        for i in range(self.size):
            index = (start_index + i) % self.size
            if self.table[index] is None:
                continue
            key, value = self.table[index]
            self.table[index] = None
            self.insert(key, value)
    
    def resize(self):
        new_size = self.size * 2
        new_table = [None] * new_size
        old_table = self.table
        self.size = new_size
        self.table = new_table
        self.count = 0

        for item in old_table:
            if item:
                self.insert(item[0], item[1])
    
    def __str__(self):
        return str([item for item in self.table if item is not None])


# Example Usage
hash_table = QuadraticProbingHashTable(7)
hash_table.insert(10, "Value1")
hash_table.insert(17, "Value2")
hash_table.insert(24, "Value3")
hash_table.insert(31, "Value4")
hash_table.insert(38, "Value5")

print("After insertions:", hash_table)
print("Search 17:", hash_table.search(17))
print("Search 25:", hash_table.search(25))

hash_table.delete(17)
print("After deleting 17:", hash_table)
print("Search 17 after deletion:", hash_table.search(17))

hash_table.insert(45, "Value6")
print("After inserting 45:", hash_table)