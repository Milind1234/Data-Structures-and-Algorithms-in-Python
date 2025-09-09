# 📌 QUESTION:
# Create a class-based implementation of a Circular Singly Linked List (CSLL) in Python.
# Show both:
# 1️⃣ How to create an Empty CSLL
# 2️⃣ How to create a CSLL with one node

# ------------------------------------------------------
# 📘 Circular Singly Linked List (CSLL) - Notes
# ------------------------------------------------------

# ✅ Node class: Creates a node with a value and pointer to the next node
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.next = None       # Will point to next node (or itself in circular list)

# ------------------------------------------------------
# 1️⃣ Empty CSLL Implementation
# ------------------------------------------------------
class EmptyCircularSinglyLinkedList:
    def __init__(self):
        self.head = None       # No head node
        self.tail = None       # No tail node
        self.length = 0        # Empty list has length 0

# 🧪 Example:
csll_empty = EmptyCircularSinglyLinkedList()
print("Empty CSLL -> Head:", csll_empty.head)     # None
print("Empty CSLL -> Tail:", csll_empty.tail)     # None
print("Empty CSLL -> Length:", csll_empty.length) # 0

# 📌 Diagram:
# head = None
# tail = None
# length = 0


# ------------------------------------------------------
# 2️⃣ One-Node CSLL Implementation
# ------------------------------------------------------
class OneNodeCircularSinglyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        new_node.next = new_node   # Point back to itself (circular link)
        self.head = new_node       # Head points to this node
        self.tail = new_node       # Tail also points to this node
        self.length = 1            # One node → length = 1

# 🧪 Example:
csll_one = OneNodeCircularSinglyLinkedList(10)
print("One-Node CSLL -> Head:", csll_one.head.value)     # 10
print("One-Node CSLL -> Tail:", csll_one.tail.value)     # 10
print("One-Node CSLL -> Next of Head:", csll_one.head.next.value) # 10
print("One-Node CSLL -> Length:", csll_one.length)       # 1

# 📌 Diagram:
#   ┌──────────┐
#   ↓          │
# [10] ────────┘
#  ↑head
#  ↑tail
# length = 1
