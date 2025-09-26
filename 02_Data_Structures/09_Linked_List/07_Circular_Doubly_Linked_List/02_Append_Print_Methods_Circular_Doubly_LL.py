# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: Append at the End of a Circular Doubly Linked List
# ------------------------------------------------------

# ❓ QUESTION:
# Write a function to insert a new element at the end of a circular doubly linked list.
# You are given a Node and CircularDoublyLinkedList class.
# Function name must be 'append'.

# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    # Pointer to next node
        self.prev = None    # Pointer to previous node

    def __str__(self):
        return str(self.value)

# A node contains:
# - value → data stored
# - next  → link to next node
# - prev  → link to previous node


# 🔷 Circular Doubly Linked List (CDLL) Structure
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None    # First node
        self.tail = None    # Last node
        self.length = 0     # Total number of nodes

    # 🔹 append(value): Inserts node at the end
    def append(self, value):
        """
        Insert a new node at the end of the CDLL.
        Cases:
        1. Empty list → new node points to itself (next & prev)
        2. Non-empty list → adjust head.prev, tail.next, and update tail
        """
        new_node = Node(value)        # Step 1: Create a new node

        # 🔹 Case 1: Empty List
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # circular → points to itself
            new_node.prev = new_node
        else:
            # 🔹 Case 2: Non-Empty List
            self.tail.next = new_node # old tail → new node
            self.head.prev = new_node # head.prev updated
            new_node.prev = self.tail # new node back link → old tail
            new_node.next = self.head # new node forward link → head
            self.tail = new_node      # update tail to new node

        self.length += 1              # Step 5: Increase list length

    # 🔹 __str__ Method for Easy Printing
    def __str__(self):
        """
        Traverse the list starting from head and print values
        in both circular and doubly-linked style.
        Example: 10 ◀——▶ 20 ◀——▶ 30
        """
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += ' ◀——▶ '
        return result


# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Append on Empty List)
#             Before:
#             None
#
#             After append(10):
#             [10]
#              ↑
#        head & tail (points to itself both ways)
# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Append on Non-Empty List)
#             Before:
#             [10] ◀——▶ [20] ◀——▶ [30]
#              ↑                  ↑
#             head               tail
#
#             After append(40):
#             [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]
#              ↑                               ↑
#             head                            new tail
#
# Note: head.prev = 40, tail.next = 10 (circular links maintained)
# _______________________________________________________________________________________________________________________


# ✅ How to Use & Output
CDLL = CircularDoublyLinkedList()
CDLL.append(10)
CDLL.append(20)
CDLL.append(30)
CDLL.append(40)
CDLL.append(50)

print(CDLL)
# Output: 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

print("Head.prev:", CDLL.head.prev.value)
# Output: 50

print("Tail.next:", CDLL.tail.next.value)
# Output: 10

# 📊 Complexity Analysis

# Time Complexity:
# - append() → O(1) → direct tail insertion
# - __str__() → O(n) → traversal for display

# Space Complexity:
# - O(1) per append (only one new node created)
# - O(n) for string representation when printing

# 🧠 Tips for Interviews
# - Always handle the empty list separately
# - Remember: in CDLL → tail.next = head, head.prev = tail
# - Visualize circular links clearly to avoid infinite loops
# - Use __str__ to debug connections easily
