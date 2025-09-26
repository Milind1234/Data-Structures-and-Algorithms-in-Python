# note.py
# ---------------------------------------------------------------
# 📌 Circular Doubly Linked List (CDLL) - Notes & Implementation
# ---------------------------------------------------------------
"""
CDLL (Circular Doubly Linked List):
- Each node contains data, a pointer to the next node, and a pointer to the previous node.
- The last node points back to the head (circular property).
- The head node’s prev pointer points to the tail.

This file shows:
1️⃣ Empty CDLL implementation
2️⃣ One-Node CDLL implementation
"""

# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # extra pointer for doubly linked

    def __str__(self):
        return str(self.value)


# ---------------------------------------------------------------
# 1️⃣ Empty Circular Doubly Linked List
# ---------------------------------------------------------------
class EmptyCircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0   # initially empty list has 0 length

# 🧪 Example:
cdll_empty = EmptyCircularDoublyLinkedList()
print("Empty CDLL -> Head:", cdll_empty.head)     # None
print("Empty CDLL -> Tail:", cdll_empty.tail)     # None
print("Empty CDLL -> Length:", cdll_empty.length) # 0

# 📌 Diagram:
# head = None
# tail = None
# length = 0

# ⏱️ Complexity:
# - Time: O(1) → initializes attributes only
# - Space: O(1) → stores 3 references (head, tail, length)


# ---------------------------------------------------------------
# 2️⃣ One-Node Circular Doubly Linked List
# ---------------------------------------------------------------
class OneNodeCircularDoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)   # O(1)
        new_node.next = new_node # circular forward
        new_node.prev = new_node # circular backward
        self.head = new_node
        self.tail = new_node
        self.length = 1

# 🧪 Example:
cdll_one = OneNodeCircularDoublyLinkedList(10)
print("One-Node CDLL -> Head:", cdll_one.head.value)        # 10
print("One-Node CDLL -> Tail:", cdll_one.tail.value)        # 10
print("One-Node CDLL -> Head.next:", cdll_one.head.next.value) # 10
print("One-Node CDLL -> Head.prev:", cdll_one.head.prev.value) # 10
print("One-Node CDLL -> Length:", cdll_one.length)          # 1

# 📌 Diagram:
#                          ┌─────┐
#                          ↓     │
#                   ———▶[10]◀──
#                  |       |
#                  |_______|
#
#                         ↑head 
#                         ↑tail
# length = 1

# ⏱️ Complexity:
# - Time: O(1) → creating and linking one node
# - Space: O(1) → one node + three references
