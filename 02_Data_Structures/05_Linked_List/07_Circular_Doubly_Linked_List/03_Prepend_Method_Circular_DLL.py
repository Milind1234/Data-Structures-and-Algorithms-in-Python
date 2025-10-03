# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topics: Empty CDLL | Append | Prepend | String Representation
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
    # 2️⃣ Prepend() → Insert node at the beginning
    # ---------------------------------------------------------------
    def prepend(self, value):
        """
        Purpose:
        Insert a new node at the **beginning** of the Circular Doubly Linked List (CDLL).

        Steps:
        1. Create a new node.
        2. If list empty:
             - head = tail = new_node
             - new_node.next = new_node.prev = new_node (points to itself)
        3. Else:
             - new_node.next = head
             - new_node.prev = tail
             - head.prev = new_node
             - tail.next = new_node
             - head = new_node
        4. Increase length

        🔍 Visualization:

        Case 1: Empty CDLL
        ------------------
        Before: head = None, tail = None
        After prepend(100):

            [100] ◀──▶ [100]
              ↑head
              ↑tail

        Case 2: Non-Empty CDLL
        ----------------------
        Before (head=10, tail=30):
            [10] ◀──▶ [20] ◀──▶ [30]
             ↑head              ↑tail
            (circular links: head.prev=30, tail.next=10)

        Prepend(100):
            Step 1: new_node = [100]
            Step 2: new_node.next = head   (100.next → 10)
            Step 3: new_node.prev = tail   (100.prev → 30)
            Step 4: head.prev = new_node   (10.prev → 100)
            Step 5: tail.next = new_node   (30.next → 100)
            Step 6: head = new_node        (head → 100)

        After:
            [100] ◀──▶ [10] ◀──▶ [20] ◀──▶ [30]
              ↑head                        ↑tail
            (circular links: head.prev=30, tail.next=100)

        🔗 Pointer changes:
        - new_node.next → old head (10)
        - new_node.prev → tail (30)
        - old head.prev → new_node (100)
        - old tail.next → new_node (100)
        - head → new_node (100)

        ⏱️ Time: O(1) → constant pointer updates
        ⏱️ Space: O(1) → no extra structures
        """
        new_node = Node(value)

        if self.length == 0:
            # Case 1: Empty CDLL
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Case 2: Non-Empty CDLL
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

        self.length += 1

    # ---------------------------------------------------------------
    # 3️⃣ __str__() → String Representation
    # ---------------------------------------------------------------
    def __str__(self):
        """
        Traverse the CDLL starting from head and print values
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
# ✅ How to Use & Test
# ---------------------------------------------------------------
CDLL = CircularDoublyLinkedList()
CDLL.append(10)
CDLL.append(20)
CDLL.append(30)
CDLL.append(40)
print(CDLL)
print("Head:", CDLL.head.value)
print("Head.next:", CDLL.head.next.value)
print("Head.prev:", CDLL.head.prev.value)
print("Tail:", CDLL.tail.value)
print("Tail.prev:", CDLL.tail.prev.value)
print("Tail.next:", CDLL.tail.next.value)

CDLL.prepend(100)
print("After Prepend :" ,CDLL)
# Output: 100 ◀——▶ 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40
print("Head:", CDLL.head.value)
print("Head.next:", CDLL.head.next.value)
print("Head.prev:", CDLL.head.prev.value)
print("Tail:", CDLL.tail.value)
print("Tail.prev:", CDLL.tail.prev.value)
print("Tail.next:", CDLL.tail.next.value)

# _______________________________________________________________________________________________________________________
# 📘 Visual Example — prepend(value)
#
# Purpose:
# Insert a new node at the **beginning** (head) of the CDLL.
#
# Cases covered:
# - empty list
# - single-node list
# - multi-node list
# _______________________________________________________________________________________________________________________

# Case: Prepend on Empty List
# ---------------------------
# Before:
# None
#
# After prepend(10):
# [10]
#  ↑
# head & tail (points to itself both ways)
#
# _______________________________________________________________________________________________________________________

# Case: Prepend on Single-Node List
# ---------------------------------
# Before:
# [10]
#  ↑head & tail
#
# After prepend(5):
# [5] ◀——▶ [10]
#  ↑head     ↑tail
#
# Note:
# - new head = 5
# - head.prev = tail (10), tail.next = head (5) → circular links preserved
#
# _______________________________________________________________________________________________________________________

# Case: Prepend on Multi-Node List
# --------------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head              ↑tail
#
# After prepend(5):
# [5] ◀——▶ [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head                         ↑tail
#
# Pointer changes:
# - new_node.next → old head (10)
# - new_node.prev → tail (30)
# - old head.prev → new_node (5)
# - tail.next → new_node (5)
#
# Complexity:
# - Time: O(1)
# - Space: O(1)
# _______________________________________________________________________________________________________________________
