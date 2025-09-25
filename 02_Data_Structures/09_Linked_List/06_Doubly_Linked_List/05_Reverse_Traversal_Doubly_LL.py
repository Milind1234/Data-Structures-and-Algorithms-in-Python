# 📌 QUESTION:
# Extend the Doubly Linked List (DLL) to support:
# 1️⃣ Append → insert node at the end
# 2️⃣ Prepend → insert node at the beginning
# 3️⃣ Print (__str__)
# 4️⃣ Reverse Traverse → visit nodes from tail → head

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes (Focus on Reverse Traverse)
# ------------------------------------------------------

# ✅ Node class
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Points to the previous node
        self.next = None       # Points to the next node


# ✅ DLL Implementation
class DoublyLinkedList:
    def __init__(self):
        self.head = None       # First node of the list
        self.tail = None       # Last node of the list
        self.length = 0        # Initially empty list

    # ------------------------------
    # __str__ → string representation
    # ------------------------------
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    # ------------------------------
    # Append → insert at the end
    # ------------------------------
    def append(self, value):
        new_node = Node(value)
        if self.head is None:           # Empty list
            self.head = new_node
            self.tail = new_node
        else:                           # Non-empty list
            self.tail.next = new_node   # old tail → new node
            new_node.prev = self.tail   # new node ← old tail
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # Prepend → insert at the beginning
    # ------------------------------
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:           # Empty list
            self.head = new_node
            self.tail = new_node
        else:                           # Non-empty list
            new_node.next = self.head   # new node → old head
            self.head.prev = new_node   # old head ← new node
            self.head = new_node
        self.length += 1

    # ------------------------------
    # ✅ Reverse Traverse Method
    # ------------------------------
    """
    Purpose:
    - Visit each node starting from tail → head.
    - Useful when we want to explore the list backwards.

    Example:
    DLL = [10 <-> 20 <-> 30 <-> 40]
    Reverse Traverse Output:
    40
    30
    20
    10

    🔗 Visualization:
    tail → [40] ← [30] ← [20] ← [10] ← None

    ⏱️ Complexity:
    - Time: O(n) → must visit all nodes
    - Space: O(1) → uses one pointer (current_node)
    """
    def reverse_traverse(self):
        current = self.tail
        while current:
            print(current.value)
            current = current.prev


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(20)    # [20]
DLL.append(30)    # [20 <-> 30]
DLL.append(40)    # [20 <-> 30 <-> 40]
DLL.prepend(10)   # [10 <-> 20 <-> 30 <-> 40]

print("DLL contents:", DLL)  
print("\nReverse Traversing the DLL:")
DLL.reverse_traverse()
