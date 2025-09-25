class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Points to the previous node
        self.next = None       # Points to the next node


# ------------------------------------------------------
# 📌 DLL Implementation
# ------------------------------------------------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None       # First node of the list
        self.tail = None       # Last node of the list
        self.length = 0        # Initially list is empty

    # ------------------------------
    # ✅ __str__ Method
    # ------------------------------
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    # ------------------------------
    # ✅ Append Method
    # ------------------------------
    def append(self, value):
        new_node = Node(value)
        if self.head is None:          # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
        else:                          # Case 2: Non-empty list
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # ✅ Prepend Method
    # ------------------------------
    
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:          # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
        else:                          # Case 2: Non-empty list
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
    
    def Reverse_Traverse(self):
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            

DLL = DoublyLinkedList()
DLL.append(20)     # [10]
DLL.append(30)     # [10 <-> 20]
DLL.append(40)     # [10 <-> 20 <-> 30]
DLL.prepend(10)   # [100 <-> 10 <-> 20 <-> 30]
print(DLL)
print("Reverse Traversing the Doubly LinkedList") 
DLL.Reverse_Traverse()