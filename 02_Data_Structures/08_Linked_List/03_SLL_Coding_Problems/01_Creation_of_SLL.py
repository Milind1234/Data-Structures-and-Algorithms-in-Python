# 📌 QUESTION:
# Create a class-based implementation of a Singly Linked List (SLL) in Python.
# Your implementation should include:
# ✅ A Node class with 'value' and 'next' attributes.
# ✅ A LinkedList class with:
#    - head, tail, and length attributes.
#    - A constructor to initialize an empty SLL.

# 🧠 Expected Behavior:
# - head and tail should be None initially.
# - length should be initialized to 0.

# ----------------------------------------
# 📘 Singly Linked List (SLL) - Notes File
# ----------------------------------------

# ✅ Node class: Creates a node with a value and pointer to the next node
class Node:
    def __init__(self, value):
        self.value = value    # Data stored in the node
        self.next = None      # Points to the next node (None by default)

# ✅ LinkedList class: Manages the linked list structure
class LinkedList:
    def __init__(self, value):
        new_node = Node(value)   # Create the first node
        self.head = new_node     # Head points to first node
        self.tail = self.head    # Tail also points to first (only) node
        self.length = 1          # Initial length is 1

# 🧠 Summary:
# - A Node stores data (value) and a pointer (next).
# - LinkedList starts with a single node.
# - Both head and tail point to the same node initially.
# - Length helps track the number of nodes for efficient operations.

# 📌 Example Diagram After Initialization:
# [value] -> None
#  ↑head
#  ↑tail
