# 📌 QUESTION:
# Extend the Doubly Linked List (DLL) to support:
# 1️⃣ Append → insert node at the end
# 2️⃣ Prepend → insert node at the beginning
# 3️⃣ Print (__str__)
# 4️⃣ Traverse → visit each node one by one

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes (Focus on Traverse)
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
        values = []
        temp = self.head
        while temp:
            values.append(str(temp.value))
            temp = temp.next
        return " <-> ".join(values)

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
    # ✅ Traverse Method
    # ------------------------------
    """
    Purpose:
    - Visit each node from head → tail
    - Print values one by one

    Example:
    DLL = [100 <-> 10 <-> 20 <-> 30]
    Output:
    100
    10
    20
    30

    🔗 Visualization:
    head → [100] → [10] → [20] → [30] → None

    ⏱️ Complexity:
    - Time: O(n) → must visit all nodes
    - Space: O(1) → only one pointer (current_node)
    """
    def traverse(self):
        current = self.head
        while current:
            print(current.value)
            current = current.next


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(10)     # [10]
DLL.append(20)     # [10 <-> 20]
DLL.append(30)     # [10 <-> 20 <-> 30]
DLL.prepend(100)   # [100 <-> 10 <-> 20 <-> 30]

print("DLL contents:", DLL)  
print("\nTraversing the DLL:")
DLL.traverse()
