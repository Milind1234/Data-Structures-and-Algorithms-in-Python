# ------------------------------------------------------
# 📘 Singly Linked List (SLL) - Notes File
# ✅ Topic: Insertion at the Beginning of a Linked List
# ------------------------------------------------------

# ❓ QUESTION:
# Write a function to insert a new element at the beginning of a singly linked list.
# You are given a LinkedList and Node class.
# Note: Function name must be 'prepend'.
# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# A node contains `value` and `next` (pointer to the next node)

# 🔷 LinkedList Structure
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

# The linked list maintains:
# - head: First node
# - tail: Last node
# - length: Total number of nodes

# 🔹 prepend(value): Inserts node at the beginning
    def prepend(self, value):
        new_node = Node(value)        # Step 1: Create a new node
        
        # 🔹 Case 1: Empty List
        if self.head is None:
            self.head = new_node      # Head and tail both point to the new node
            self.tail = new_node
        else:
            # 🔹 Case 2: Non-Empty List
            new_node.next = self.head # Link new node to the current head
            self.head = new_node      # Move head to point to new node

        self.length += 1              # Step 5: Increase list length

# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Prepend on Empty List)
#             Before:
#             None
#
#             After:
#             [10] → None
#              ↑
#            head & tail
# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Prepend on Non-Empty List)
#             Before:
#             [20] → [30] → [40]
#              ↑
#             head
#
#             After prepend(10):
#             [10] → [20] → [30] → [40]
#              ↑
#            new head
# _______________________________________________________________________________________________________________________

    # 🔹 __str__ Method for Easy Printing
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

# ✅ How to Use & Output
new_LinkedList = LinkedList()
new_LinkedList.prepend(40)
new_LinkedList.prepend(30)
new_LinkedList.prepend(20)
new_LinkedList.prepend(10)

print(new_LinkedList)
# Output: 10 -> 20 -> 30 -> 40

print(new_LinkedList.head.value)
# Output: 10 (new head)

print(new_LinkedList.tail.value)
# Output: 40 (unchanged tail)

# 📊 Complexity Analysis

# Time Complexity:
# - prepend() → O(1) → constant time insert at head

# Space Complexity:
# - O(1) → only one new node is allocated

# 🧠 Tips for Interviews
# - Always handle the empty list case separately
# - Understand head pointer movement clearly
# - Visualize the before/after state of `head` and `next`
# - Practice adding trace prints or diagrams when debugging
