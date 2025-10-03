# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: Get Node by Index
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
        if self.head is None:
            return "Empty CDLL"
        result = []
        current_node = self.head
        while True:
            result.append(str(current_node.value))
            current_node = current_node.next
            if current_node == self.head:
                break
        return " ◀——▶ ".join(result)

    # ---------------------------------------------------------------
    # 3️⃣ get_node(index) → Get node by index
    # ---------------------------------------------------------------
    def get_node(self, index):
        """
        Purpose:
        Retrieve the node present at a specific index (0-based).

        Steps:
        1. If index < 0 or index >= length → return None (invalid index).
        2. If index is in the **first half** of the list:
             - Start from head.
             - Move forward index times.
        3. If index is in the **second half** of the list:
             - Start from tail.
             - Move backward until index is reached.
        4. Return the node’s value with its index.

        🔍 Visualization:

        CDLL = [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40] ◀──▶ [50]

        get_node(1):
        - index=1 is in the first half (head → forward)
        - Traverse: head=10 → next=20
        - Return: "At index 1 Node 20 is present"

        get_node(4):
        - index=4 is in the second half (tail → backward)
        - Traverse: tail=50 (index=4) → found immediately
        - Return: "At index 4 Node 50 is present"

        ⏱️ Time Complexity:
        - Best: O(1) → index at head or tail
        - Average/Worst: O(n/2) → half traversal from closer end
        - Overall: O(n)

        ⏱️ Space Complexity:
        - O(1) → no extra memory used
        """
        if index < 0 or index >= self.length:
            return None

        current_node = None
        if index < self.length // 2:
            # Closer to head → move forward
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            # Closer to tail → move backward
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return f"At index {index} Node {current_node.value} is present"
    

# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    CDLL = CircularDoublyLinkedList()
    CDLL.append(10)
    CDLL.append(20)
    CDLL.append(30)
    CDLL.append(40)
    CDLL.append(50)

    print("CDLL:", CDLL)
    # Output: 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    print(CDLL.get_node(3))
    # Output: At index 3 Node 40 is present

    print(CDLL.get_node(0))
    # Output: At index 0 Node 10 is present

    print(CDLL.get_node(4))
    # Output: At index 4 Node 50 is present


    # ---------------------------------------------------------------
    # 3️⃣ get_node(index) → Get node by index return only node Object
    # ---------------------------------------------------------------
    
    def get_method(self , index):
        if index < 0 or index >= self.length:
            return None
        current_node = None
        if index < self.length // 2:
            # Closer to head → move forward
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            # Closer to tail → move backward
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node
    
# _______________________________________________________________________________________________________________________
# 📘 Visual Example — get_node(index) / get_value(index)
#
# Purpose:
# Retrieve a node (or its value) at a given 0-based index.
# The helper optimizes traversal by starting from head if index is in
# the first half, or from tail if index is in the second half.
#
# Behavior cases covered:
# - index out of range
# - index = 0 (head)
# - index = length - 1 (tail)
# - index in middle (closer to head)
# - index in middle (closer to tail)
# _______________________________________________________________________________________________________________________

# Case: Index Out of Range
# ------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head              ↑tail
#
# get_node(5) or get_value(5) -> index 5 >= length (3)
# Return: None (for get_node) or None (for get_value) / or "Index out of range" depending on API
#
# _______________________________________________________________________________________________________________________

# Case: Get Head (index 0)
# ------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head              ↑tail
#
# get_node(0):
# - index < length//2 → start at head
# - 0 steps needed → return head node ([10])
#
# get_value(0) -> 10
#
# _______________________________________________________________________________________________________________________

# Case: Get Tail (index = length - 1)
# -----------------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head              ↑tail
#
# get_node(2) (length=3):
# - index >= length//2 → start at tail
# - tail is already index 2 → return tail node ([30])
#
# get_value(2) -> 30
#
# _______________________________________________________________________________________________________________________

# Case: Get Middle (closer to head)
# ---------------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40] ◀——▶ [50]
#  ↑head                                 ↑tail
#
# get_node(1): index 1 < length//2 (5//2=2) → start at head
# - head (10) → next → 20 → return node [20]
#
# get_value(1) -> 20
#
# _______________________________________________________________________________________________________________________

# Case: Get Middle (closer to tail)
# ---------------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40] ◀——▶ [50]
#  ↑head                                 ↑tail
#
# get_node(4): index 4 >= length//2 → start at tail
# - tail (50) → already index 4 → return node [50]
#
# get_node(3):
# - start at tail (50) → prev → 40 → return node [40]
#
# get_value(3) -> 40
#
# _______________________________________________________________________________________________________________________
# Notes:
# - Time complexity: O(n) worst-case, O(n/2) average due to two-way traversal optimization.
# - Space complexity: O(1).
# _______________________________________________________________________________________________________________________
