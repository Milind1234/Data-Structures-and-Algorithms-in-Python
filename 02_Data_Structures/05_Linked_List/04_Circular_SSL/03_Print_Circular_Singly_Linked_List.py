# 📌 QUESTION:
# Implement a Circular Singly Linked List (CSLL) in Python with:
# ✅ A Node class
# ✅ A CircularSinglyLinkedList class that supports:
#    - head, tail, and length attributes
#    - append(value): add a new node at the end of the CSLL
#    - __str__(): return a string representation of the list for easy printing

# 🧠 Expected Behavior:
# - When empty → head = None, tail = None, length = 0
# - append(value):
#   • If list empty → new node points to itself, head = tail = new_node
#   • If not empty → new node linked at tail, tail updated, tail.next points back to head
# - __str__():
#   • Traverse nodes until reaching head again (circular stop condition).
#   • Print values separated by arrows ("-->").
# - Length updates correctly after each append.

# ------------------------------------------------------
# 📘 Circular Singly Linked List (CSLL) - Notes
# ------------------------------------------------------

# ✅ Node class: represents each element
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.next = None       # Next pointer (circular links maintained in CSLL)


# ✅ CSLL class with append & print functionality
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None       # Start of the list
        self.tail = None       # End of the list
        self.length = 0        # Track length of the list
    
    # Append: add new node at the end while maintaining circular link
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:                # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node        # Node points to itself
        else:                               # Case 2: Non-empty list
            self.tail.next = new_node       # Old tail → new node
            new_node.next = self.head       # New node → head (circular link)
            self.tail = new_node            # Update tail
        self.length += 1

    # __str__: for printing the CSLL as "10 --> 20 --> 30"
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:      # Stop when circle completes
                break
            result += '  -->  '
        return result


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
csLinkedList = CircularSinglyLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
csLinkedList.append(30)
csLinkedList.append(40)
csLinkedList.append(50)

print("Head:", csLinkedList.head.value)       # 10
print("Tail:", csLinkedList.tail.value)       # 50
print("Tail.next:", csLinkedList.tail.next.value)  # 10 (circular back to head)
print("Length:", csLinkedList.length)         # 5
print(csLinkedList)                           # 10 --> 20 --> 30 --> 40 --> 50

# ------------------------------------------------------
# 📌 Example Diagram (after appending 10,20,30,40,50)
# ------------------------------------------------------
# [10] → [20] → [30] → [40] → [50]
#   ↑                           ↓
#   └───────────────────────────┘
# head = 10
# tail = 50
# tail.next = 10
# length = 5

# ------------------------------------------------------
# ⏱️ Complexity
# ------------------------------------------------------
# append():
#   • Time: O(1) → direct tail insertion, only updates pointers
#   • Space: O(1) → no extra space, just one new node created
#
# __str__():
#   • Time: O(n) → must traverse the entire list once
#   • Space: O(1) → only uses temp references, no extra storage
