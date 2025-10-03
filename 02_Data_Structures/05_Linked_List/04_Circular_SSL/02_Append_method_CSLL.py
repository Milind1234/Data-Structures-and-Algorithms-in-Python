# 📌 QUESTION:
# Create a class-based implementation of a Circular Singly Linked List (CSLL) in Python.
# Your implementation should include:
# ✅ A Node class with 'value' and 'next' attributes.
# ✅ A CircularSinglyLinkedList class with:
#    - head, tail, and length attributes.
#    - append(value) method to insert a node at the end while maintaining circularity.

# 🧠 Expected Behavior:
# - If the list is empty:
#     head = tail = new_node
#     new_node.next = new_node (circular link)
# - If list is not empty:
#     tail.next = new_node
#     new_node.next = head (to keep circular)
#     tail = new_node
# - Length increases by 1.

# ------------------------------------------------------
# 📘 Circular Singly Linked List (CSLL) - Notes
# ------------------------------------------------------

# ✅ Node class: Represents each element in the list
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.next = None       # Next pointer (circular links maintained later)

# ✅ CircularSinglyLinkedList class: Manages the CSLL
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None       # Start of the list
        self.tail = None       # End of the list
        self.length = 0        # Track length of the list
    
    # ✅ Append method: Inserts a new node at the end of the CSLL
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:                # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node        # Circular link to itself
        else:                               # Case 2: Non-empty list
            self.tail.next = new_node       # Old tail points to new node
            new_node.next = self.head       # New node points back to head
            self.tail = new_node            # Tail updated to new node
        self.length += 1

# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
csLinkedList = CircularSinglyLinkedList()
csLinkedList.append(10)   # First node → head=tail=10
csLinkedList.append(20)   # Append 20 → tail=20, circular link maintained

print("Head:", csLinkedList.head.value)   # 10
print("Tail:", csLinkedList.tail.value)   # 20
print("Tail.next:", csLinkedList.tail.next.value)  # 10 (circular back to head)
print("Length:", csLinkedList.length)     # 2

# ------------------------------------------------------
# 📌 Example Diagram
# ------------------------------------------------------
# After appending 10:
#   ┌──────────┐
#   ↓          │
# [10] ────────┘
#  ↑head
#  ↑tail
# length = 1
#
# After appending 20:
# [10] → [20]
#   ↑      ↓
#   └──────┘  (tail.next points back to head)
# head = 10
# tail = 20
# length = 2

# ------------------------------------------------------
# ⏱️ Complexity
# ------------------------------------------------------
# - append():
#   • Time: O(1) → inserting at the end only requires pointer updates
#   • Space: O(1) → no extra memory, just one new node created
