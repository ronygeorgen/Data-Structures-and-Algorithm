class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None
    
    def push(self,item):
        new_node = Node(item)
        new_node.next = self.head
        self.head = new_node
    
    def pop(self):
        if self.head is None:
            print("Stack underflow")
            return
        item = self.head.data 
        self.head = self.head.next
        return item
    
    def traverse(self):
        if self.head is None:
            print('Stack is empty')
            return
        n = self.head
        while n is not None:
            print(n.data, end=' ')
            n = n.next
        print()
        
    def is_empty(self):
        return self.head is None

stack = Stack()
stack.push(1)
stack.push(2)
print(stack.pop())
print(stack.is_empty())