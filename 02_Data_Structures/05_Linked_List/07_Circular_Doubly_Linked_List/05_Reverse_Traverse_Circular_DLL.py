# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topics: Append | String Representation | Traverse | Reverse Traverse
# ------------------------------------------------------

# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # backward pointer for doubly linked

    def __str__(self):
        return str(self.value)


# 🔷 Circular Doubly Linked List (CDLL)
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0   # initially empty list has 0 length

    # ---------------------------------------------------------------
    # 1️⃣ Append() → Insert node at the end
    # ---------------------------------------------------------------
    def append(self, value):
        new_node = Node(value)
        # Case 1: Empty CDLL
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Case 2: Non-Empty CDLL
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        self.length += 1

    # ---------------------------------------------------------------
    # 2️⃣ __str__() → String Representation
    # ---------------------------------------------------------------
    def __str__(self):
        """
        Traverse the CDLL starting from head and collect values
        in a readable format with double links.

        Example:
        [10] ◀——▶ [20] ◀——▶ [30]
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

    # ---------------------------------------------------------------
    # 3️⃣ traverse() → Print all node values
    # ---------------------------------------------------------------
    def traverse(self):
        """
        Purpose:
        Print all nodes in **forward direction** starting from head.

        Steps:
        1. Start at head.
        2. Keep moving to next node.
        3. Stop when you circle back to head.

        Example CDLL: [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]

        traverse():
        → 10 → 20 → 30 → 40
        """
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    # ---------------------------------------------------------------
    # 4️⃣ reverse_traverse() → Print all node values in reverse
    # ---------------------------------------------------------------
    def reverse_traverse(self):
        """
        Purpose:
        Print all nodes in **reverse direction** starting from tail.

        Steps:
        1. Start at tail.
        2. Keep moving to prev node.
        3. Stop when you circle back to tail.

        🔍 Visualization:
        CDLL = [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]

        reverse_traverse():
        → 40 → 30 → 20 → 10

        ⏱️ Time: O(n) → visits all nodes once
        ⏱️ Space: O(1) → no extra structures
        """
        current_node = self.tail
        while current_node:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
CDLL = CircularDoublyLinkedList()
CDLL.append(10)
CDLL.append(20)
CDLL.append(30)
CDLL.append(40)

print("CDLL:", CDLL) 
# Output: 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40

print("\nTraverse Output:")
CDLL.traverse()
# Output:
# 10
# 20
# 30
# 40

print("\nReverse Traverse Output:")
CDLL.reverse_traverse()
# Output:
# 40
# 30
# 20
# 10

# _______________________________________________________________________________________________________________________
# 📘 Visual Example — reverse_traverse()
#
# Purpose:
# Visit every node in reverse direction starting from tail and process/print values.
#
# Cases covered:
# - empty list
# - single-node list
# - multi-node list
# _______________________________________________________________________________________________________________________

# Case: Reverse Traverse on Empty List
# ------------------------------------
# Before:
# None
#
# reverse_traverse() -> prints nothing (or indicates empty)
#
# _______________________________________________________________________________________________________________________

# Case: Reverse Traverse on Single-Node List
# ------------------------------------------
# Before:
# [10]
#  ↑head & tail
#
# reverse_traverse():
# → prints 10
#
# _______________________________________________________________________________________________________________________

# Case: Reverse Traverse on Multi-Node List
# -----------------------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]
#  ↑head                          ↑tail
#
# reverse_traverse():
# → prints 40
# → prints 30
# → prints 20
# → prints 10
# (stop when current becomes tail again)
#
# Complexity:
# - Time: O(n)
# - Space: O(1)
# _______________________________________________________________________________________________________________________
