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
