class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None
    
    def is_empty(self):
        return self.front is None
    
    def enqueue(self,item):
        new_node = Node(item)
        if self.front is None:
            self.front = self.rear = new_node
            return
        self.rear.next = new_node
        self.rear = new_node
    
    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
            return
        temp = self.front
        self.front = temp.next
        if self.front is None:
            self.rear = None
        return temp.data
    
    def traverse(self):
        if self.front is None:
            print('Queue is empty')
            return
        n = self.front
        while n is not None:
            print(n.data,end=' ')
            n = n.next
        print()

queue = Queue()
queue.enqueue(1)
queue.enqueue(2)
print(queue.dequeue())