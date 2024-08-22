class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return self.items == []
    
    def push(self,item):
        self.items.append(item)
    
    def display(self):
        print(self.items)

    def pop(self):
        if not self.is_empty():
            return self.items.pop()
        else:
            print("stack is empty")
            return None
        
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            print("stack is empty")
            return None
        
    def size(self):
        return len(self.items)
    
stack = Stack()
stack.push(1)
stack.push(7)
# stack.display()
print(stack.peek())
print(stack.pop())
# stack.display()
print(stack.size())
print(stack.pop())
print(stack.size())