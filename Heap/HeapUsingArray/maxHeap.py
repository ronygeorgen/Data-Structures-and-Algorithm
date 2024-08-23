class MaxHeap:
    def __init__(self):
        self.heap = []
    
    def parent(self,index):
        return (index - 1) // 2
    
    def lchild(self,index):
        return 2 * index + 1
    
    def rchild(self,index):
        return 2 * index + 2

    def insert(self,element):
        self.heap.append(element)
        self.heapify_up(len(self.heap)-1)
    
    def heapify_up(self,index):
        while index > 0 and self.heap[self.parent(index)] < self.heap[index]:
            self.swap(index,self.parent(index))
            index = self.parent(index)
    
    def swap(self,i,j):
        self.heap[i], self.heap[j] = self.heap[j], self.heap[i]
    
    def extract(self):
        if len(self.heap) == 0:
            return None
        if len(self.heap) == 1:
            return self.heap.pop()
        max_value = self.heap[0]
        self.heap[0] = self.heap.pop()
        self.heapify_down(0)
        return max_value
    
    def heapify_down(self,index):
        largest = index
        left  = self.lchild(index)
        right = self.rchild(index)
        if left < len(self.heap) and self.heap[left] > self.heap[largest]:
            largest = left
        if right < len(self.heap) and self.heap[right] > self.heap[largest]:
            largest = right
        if largest != index:
            self.swap(index,largest)
            self.heapify_down(largest)
    
    def get_max(self):
        if len(self.heap) == 0:
            return None
        return self.heap[0]
    
obj = MaxHeap()
obj.insert(4)
obj.insert(400)
obj.insert(90)
obj.insert(42)
obj.insert(3)
print(obj.parent(3))
print(obj.lchild(3))
print(obj.rchild(3))
# print(obj.extract())