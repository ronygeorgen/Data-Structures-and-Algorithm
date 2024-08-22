class BST:
    def __init__(self,key=None):
        self.key = key
        self.lchild = None
        self.rchild = None
    
    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return
        if self.key > data:
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
                self.rchild.insert(data)
            else:
                self.rchild = BST(data)
    
    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key:
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not present in the tree")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not present in the tree")

    def preorder(self):
        print(self.key, end=" ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()

    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key,end=" ")
        if self.rchild:
            self.rchild.inorder()
    
    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key,end=" ")

    def delete(self,data):
        if self.key is None:
            print("Tree is empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data)
            else:
                print("Given node is not present in the tree")
        elif data > self.key:
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given node is not present in the tree")
        else:
            if self.lchild is None:
                temp = self.rchild
                self = None
                return temp
            if self.rchild is None:
                temp = self.lchild
                self = None
                return temp
            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key)
        return self
    
    def min(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("Minimum node = ", current.key)

    def max(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Maximum node = ", current.key)

def count(node):
    if node is None:
        return 0
    return 1+count(node.lchild)+count(node.rchild)

    
root = BST()
root.insert(23)
list1 = [3,4,65,23,5]
for i in list1:
    root.insert(i)
root.search(6)
print("preorder")
root.preorder()
print("\nInorder")
root.inorder()
print()
if count(root) > 1:
    root.delete(10)
else:
    ("We can't perform deletion operation")
print("\npostorder")
root.postorder()
print()
root.inorder()
print()
root.min()
root.max()