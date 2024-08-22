class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def traverse(self):
        if self.head is None:
            print("Linked List is empty")
        else:
            n = self.head 
            while n is not None:
                print(n.data,end=" ")
                n = n.next
            print("\n")
    
    def add_begin(self,data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node
    
    def add_end(self,data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            n = self.head
            while n.next is not None:
                n = n.next
            n.next = new_node
    def add_after(self, data, x):
        if self.head is None:
            print("Linked list is empty")
            return
        else:
            n = self.head
            while n is not None:
                if n.data == x:
                    break
                n = n.next
            if n is None:
                print("Node not found")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
    def add_before(self,data,x):
        if self.head is None:
            print("Linked List is empty")
            return
        elif self.head.data == x:
            new_node = Node(data)
            new_node.next = self.head
            self.head = new_node
            return
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n.next is None:
                print("Node not found")
            else:
                new_node = Node(data)
                new_node.next = n.next
                n.next = new_node
    def remove_first(self):
        if self.head is None:
            print("Linked list is none")
            return
        if self.head.next is None:
            self.head = None
        else:
            self.head = self.head.next
    def remove_end(self):
        if self.head is None:
            print("Linekd list is none")
            return
        if self.head.next is None:
            self.head = None
        else:
            n = self.head
            while n.next.next is not None:
                n = n.next
            n.next = None
    def remove_any(self,x):
        if self.head is None:
            print("Linked List is none")
            return
        if self.head.data == x:
            self.head = self.head.next
            return
        else:
            n = self.head
            while n.next is not None:
                if n.next.data == x:
                    break
                n = n.next
            if n.next is None:
                print("Node not found")
            else:
                n.next = n.next.next
    
    # Display sum of the linked list
    def display_sum(self):
        sum = 0
        if self.head is None:
            print('Linked List is empty')
            return
        else:
            n = self.head
            while n is not None:
                sum += n.data
                n = n.next
        return sum
    def reverse_LL(self):
        if self.head is None:
            print("Linked List is none")
        else:
            current_node = self.head
            next_node = self.head
            prev_node = None
            while next_node is not None:
                next_node = next_node.next
                current_node.next = prev_node
                prev_node = current_node
                current_node = next_node
            self.head = prev_node
    def min_max(self):
        if self.head is None:
            print("Linked list is none")
            return
        else:
            n = self.head
            max = n.data
            min = n.data
            while n is not None:
                if max < n.data:
                    max = n.data
                if min > n.data:
                    min = n.data
                n = n.next
        return min, max
    
    def mid(self):
        a=self.head

        b=self.head
        while b is not None and b.next is not None:            
            a=a.next
            b=b.next.next
        print(a.data,end= ' is mid',)
        print("\n")
    
    def midelement_delete(self):
        if self.head is None:
            print("Llinked List is none")
            return
        if self.head.next is None:
            self.head = None
            return
        slow_ptr = self.head
        fast_ptr = self.head
        prev_ptr = None
        while fast_ptr is not None and fast_ptr.next is not None:
            prev_ptr = slow_ptr
            slow_ptr = slow_ptr.next
            fast_ptr = fast_ptr.next.next
        prev_ptr.next = slow_ptr.next
        slow_ptr.next = None
    
    def merge_linked_list(self,list1,list2):
        if list1.head is None:
            return list2
        if list2.head is None:
            return list2
        last_node = list1.head
        while last_node.next is not None:
            last_node = last_node.next
        last_node.next = list2.head
        return list1.head
    
    def sort(self):
        self.head = self._merge_sort(self.head)

    def _merge_sort(self, head):
        if head is None or head.next is None:
            return head
        
        # Get the middle of the list
        middle = self._get_middle(head)
        next_to_middle = middle.next
        
        # Split the list into two halves
        middle.next = None
        
        # Apply _merge_sort on the left half
        left = self._merge_sort(head)
        
        # Apply _merge_sort on the right half
        right = self._merge_sort(next_to_middle)
        
        # Merge the sorted halves
        sorted_list = self._sorted_merge(left, right)
        return sorted_list
    
    def _get_middle(self, head):
        if head is None:
            return head
        
        slow = head
        fast = head
        
        while fast.next is not None and fast.next.next is not None:
            slow = slow.next
            fast = fast.next.next
        
        return slow
    
    def _sorted_merge(self, a, b):
        result = None
        
        if a is None:
            return b
        if b is None:
            return a
        
        if a.data <= b.data:
            result = a
            result.next = self._sorted_merge(a.next, b)
        else:
            result = b
            result.next = self._sorted_merge(a, b.next)
        
        return result
    
    
    #below code for merge two LL on the basis of sorting
    def merge_two_sorted_lists(self, list1, list2):
        # Create a new dummy node to form the new sorted list
        dummy = Node(0)
        tail = dummy
        
        while list1 is not None and list2 is not None:
            if list1.data <= list2.data:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            tail = tail.next
        
        # Attach the remaining elements
        if list1 is not None:
            tail.next = list1
        if list2 is not None:
            tail.next = list2
        
        # The head of the new list is the next node of the dummy
        return dummy.next


    

obj = LinkedList()
# obj.add_begin(55)
# obj.add_begin(6)
# obj.add_end(44)
# obj.add_end(1)
# obj.add_end(2)
# obj.add_end(3)
# obj.add_end(4)
# obj.add_end(5)
# obj.add_end(3)
# obj.add_end(0)
# obj.add_after(33,44)
# obj.add_before(12,6)
# obj.traverse()
# obj.mid()
# obj.midelement_delete()

#below array and loop is to convert array into a linked list
# arr = [5,9,7,56,98]
# for i in arr:
#     obj.add_end(i)
# obj.traverse()
#============================================================#
# obj.remove_first()
# obj.remove_end()
# obj.remove_any(33)
# obj.reverse_LL()
# print(obj.display_sum())
# x, y= obj.min_max()
# print(f"maximum = {y}, Minimum = {x}")
# obj.traverse()
obj.add_end(44)
obj.add_end(1)
obj.add_end(2)
obj.add_end(3)
obj.add_end(4)
obj.add_end(5)
obj.add_end(3)
obj.traverse()
obj.sort()
obj.traverse()

obj2 = LinkedList()
obj2.add_end(1)
obj2.add_end(33)
obj2.add_end(21)
obj2.add_end(90)
obj2.traverse()

merged_list = LinkedList()
merged_list.head = merged_list.merge_linked_list(obj,obj2)
merged_list.traverse()