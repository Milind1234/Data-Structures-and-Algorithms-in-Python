"""
======================================================
APPEND METHOD IN LINKED LIST
======================================================

------------------------------------------------------
WHAT IS COVERED IN THIS NOTE?
------------------------------------------------------
1) What is append in linked list?
2) Why tail pointer is important for O(1) append?
3) Full code implementation of Node & LinkedList classes.
4) Detailed working of append step by step.
5) Complexity Analysis.
6) ASCII visualization of append operation.
7) Common Interview Questions and Answers.
------------------------------------------------------
"""

# =====================================================
# 1) NODE CLASS → BASIC BUILDING BLOCK
# =====================================================
class Node:
    def __init__(self, value):
        self.value = value    # Stores actual data
        self.next = None      # Pointer to the next node


# =====================================================
# 2) LINKED LIST CLASS
# =====================================================
class LinkedList:
    def __init__(self):
        self.head = None      # Points to first node
        self.tail = None      # Points to last node
        self.length = 0       # Tracks size of linked list

    # -------------------------------------------------
    # APPEND METHOD → Add node at end of linked list
    # -------------------------------------------------
    def append(self, value):
        """
        Steps:
        1) Create a new node.
        2) If linked list is empty → new node becomes head & tail.
        3) Else → attach new node at end using tail pointer.
        4) Increase linked list length.
        """
        # Step 1: Create new node → O(1)
        new_node = Node(value)

        # Step 2: If linked list is empty
        if self.head is None:
            # Empty list → new node is both head & tail
            self.head = new_node
            self.tail = new_node
        else:
            # Step 3: Non-empty list → attach new node at end
            self.tail.next = new_node
            self.tail = new_node

        # Step 4: Increment length counter
        self.length += 1

    # -------------------------------------------------
    # PRINT LIST METHOD → For visualization
    # -------------------------------------------------
    def print_list(self):
        """
        Traverses from head to tail and prints node values.
        """
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")   # End of linked list


# =====================================================
# 3) USAGE EXAMPLE
# =====================================================
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)

print("Length:", new_linked_list.length)   # Output: 3
print("Elements:")
new_linked_list.print_list()               # Output: 10 -> 20 -> 30 -> None


# =====================================================
# 4) HOW APPEND WORKS (STEP-BY-STEP)
# =====================================================
"""
Case 1: Empty Linked List
-------------------------
Initial: head = None, tail = None
append(10):
    - Create new_node(10)
    - head = new_node
    - tail = new_node
    - length = 1

Case 2: Non-Empty Linked List
-----------------------------
Existing: head -> [10|•] -> None, tail -> [10]
append(20):
    - Create new_node(20)
    - tail.next = new_node
    - tail = new_node
    - length = 2

ASCII Visualization:
--------------------
Before:
head ──► [10|•] ──► None
tail ──► [10]

After append(20):
head ──► [10|•] ──► [20|None]
tail ──► [20]
length = 2
"""


# =====================================================
# 5) COMPLEXITY ANALYSIS
# =====================================================
"""
APPEND():
- Time Complexity: O(1) → direct insertion using tail pointer
- Space Complexity: O(1) → only one node created

PRINT_LIST():
- Time Complexity: O(n) → traverses all nodes
- Space Complexity: O(1) → no extra data structure
"""


# =====================================================
# 6) COMMON INTERVIEW QUESTIONS
# =====================================================
"""
Q1) Why is append O(1) for a linked list?
A1) Because we use a tail pointer that directly points to the last node,
    eliminating the need to traverse the entire list.

Q2) What happens if we don't maintain a tail pointer?
A2) Then append becomes O(n) because we need to traverse from head to last node.

Q3) Is memory allocation different from array append?
A3) Yes, linked list nodes are allocated dynamically and not stored contiguously
    like arrays.

Q4) Can we append multiple nodes efficiently?
A4) Yes, each append is O(1) if tail is maintained, so k appends take O(k).

Q5) How to verify append visually?
A5) By printing linked list using a helper function like print_list().
"""
