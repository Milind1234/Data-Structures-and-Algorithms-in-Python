# 📌 QUESTION:
# Create a class-based implementation of a Doubly Linked List (DLL) in Python.
# Show both:
# 1️⃣ How to create an Empty DLL
# 2️⃣ How to create a DLL with one node

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes
# ------------------------------------------------------

# ✅ Node class: Creates a node with a value, a pointer to the previous node, and a pointer to the next node
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Will point to the previous node
        self.next = None       # Will point to the next node

# ------------------------------------------------------
# 1️⃣ Empty DLL Implementation
# ------------------------------------------------------
class EmptyDoublyLinkedList:
    def __init__(self):
        self.head = None       # No head node
        self.tail = None       # No tail node
        self.length = 0        # Empty list has length 0

# 🧪 Example:
dll_empty = EmptyDoublyLinkedList()
print("Empty DLL -> Head:", dll_empty.head)       # None
print("Empty DLL -> Tail:", dll_empty.tail)       # None
print("Empty DLL -> Length:", dll_empty.length)   # 0

# 📌 Diagram:
# head = None
# tail = None
# length = 0

# ⏱️ Complexity:
# - Time: O(1) → only initializes three attributes (constant work).
# - Space: O(1) → only stores references for head, tail, and an integer length.


# ------------------------------------------------------
# 2️⃣ One-Node DLL Implementation
# ------------------------------------------------------
class OneNodeDoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)     # O(1) → creating one node
        self.head = new_node       # O(1)
        self.tail = new_node       # O(1)
        self.length = 1            # O(1)

# 🧪 Example:
dll_one = OneNodeDoublyLinkedList(10)
print("One-Node DLL -> Head:", dll_one.head.value)     # 10
print("One-Node DLL -> Tail:", dll_one.tail.value)     # 10
print("One-Node DLL -> Length:", dll_one.length)       # 1
print("One-Node DLL -> Head.prev:", dll_one.head.prev) # None
print("One-Node DLL -> Head.next:", dll_one.head.next) # None

# 📌 Diagram:
# None <- [10] -> None
#  ↑head
#  ↑tail
# length = 1

# ⏱️ Complexity:
# - Time: O(1) → constant steps to create one node and assign pointers.
# - Space: O(1) → stores only one node + three references (head, tail, length).
