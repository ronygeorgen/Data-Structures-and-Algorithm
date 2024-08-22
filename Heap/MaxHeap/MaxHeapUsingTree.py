class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None

class MaxHeap:
    def __init__(self):
        self.root = None
        self.last = None
        self.size = 0

    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
            self.last = new_node
        else:
            parent = self._find_insert_parent()
            if not parent.left:
                parent.left = new_node
            else:
                parent.right = new_node
            new_node.parent = parent
            self.last = new_node
        self.size += 1
        self._heapify_up(new_node)
    
    def _find_insert_parent(self):
        if self.size == 1:
            return self.root
        queue = [self.root]
        while queue:
            node = queue.pop(0)
            if not node.left or not node.right:
                return node
            queue.append(node.left)
            queue.append(node.right)
    
    def _heapify_up(self, node):
        while node.parent and node.value > node.parent.value:
            node.value, node.parent.value = node.parent.value, node.value
            node = node.parent
    
    def extract_max(self):
        if not self.root:
            return None
        max_value = self.root.value
        if self.size == 1:
            self.root = None
            self.last = None
        else:
            self.root.value = self.last.value
            self._remove_last()
            self._heapify_down(self.root)
        self.size -= 1
        return max_value

    def _remove_last(self):
        if self.last == self.last.parent.left:
            self.last.parent.left = None
        else:
            self.last.parent.right = None
        self.last = self._find_new_last()
    
    def _find_new_last(self):
        if self.size == 2:
            return self.root
        queue = [self.root]
        last_node = None
        while queue:
            node = queue.pop(0)
            if node.left:
                last_node = node.left
                queue.append(node.left)
            if node.right:
                last_node = node.right
                queue.append(node.right)
        return last_node

    def _heapify_down(self, node):
        while True:
            largest = node
            if node.left and node.left.value > largest.value:
                largest = node.left
            if node.right and node.right.value > largest.value:
                largest = node.right
            if largest == node:
                break
            node.value, largest.value = largest.value, node.value
            node = largest
    
    def get_max(self):
        return self.root.value if self.root else None
    
    def is_empty(self):
        return self.size == 0
    
    def heap_size(self):
        return self.size


# Create a MinHeap object
max_heap = MaxHeap()

# Insert some elements
print("Inserting elements: 5, 3, 7, 1, 4, 2")
max_heap.insert(5)
max_heap.insert(3)
max_heap.insert(7)
max_heap.insert(1)
max_heap.insert(4)
max_heap.insert(2)

# Check the minimum element
print(f"Maximum element: {max_heap.get_max()}")

# Check the size of the heap
print(f"Heap size: {max_heap.heap_size()}")

# Extract the minimum element a few times
print("Extracting maximum elements:")
for _ in range(3):
    print(f"Extracted: {max_heap.extract_max()}")

# Check the new minimum element
print(f"New maximum element: {max_heap.get_max()}")

# Check if the heap is empty
print(f"Is the heap empty? {max_heap.is_empty()}")

# Insert more elements
print("Inserting elements: 6, 8")
max_heap.insert(6)
max_heap.insert(8)

# Final size check
print(f"Final heap size: {max_heap.heap_size()}")