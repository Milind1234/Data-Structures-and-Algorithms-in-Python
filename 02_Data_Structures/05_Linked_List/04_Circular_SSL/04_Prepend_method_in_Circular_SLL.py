# 📌 QUESTION:
# Extend the Circular Singly Linked List (CSLL) to support:
# ✅ append(value): add a node at the end
# ✅ prepend(value): add a node at the beginning
# ✅ __str__(): visualize the CSLL

# 🧠 Expected Behavior:
# - append(value):
#   • If empty → head = tail = new_node, new_node.next = new_node
#   • Else → link new_node after tail, new_node.next = head, tail = new_node
#
# - prepend(value):
#   • If empty → head = tail = new_node, new_node.next = new_node
#   • Else → new_node.next = head, update head = new_node, and update tail.next to new head
#
# - __str__(): traverse from head until circle completes, printing values separated by arrows.

# ------------------------------------------------------
# 📘 Circular Singly Linked List (CSLL) - Notes
# ------------------------------------------------------

# ✅ Node class
class Node:
    def __init__(self, value):
        self.value = value     # Node data
        self.next = None       # Next pointer


# ✅ CSLL class with append + prepend
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # Append at the end
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:                 # Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:                                # Non-empty
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    # Prepend at the beginning
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:                 # Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:                                # Non-empty
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node        # Maintain circular link
        self.length += 1

    # String representation for visualization
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            temp_node = temp_node.next
            if temp_node == self.head:       # Stop when cycle completes
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
csLinkedList.prepend(100)

print("Head:", csLinkedList.head.value)        # 100
print("Tail:", csLinkedList.tail.value)        # 50
print("Tail.next:", csLinkedList.tail.next.value)  # 100 (circular back to head)
print("Length:", csLinkedList.length)          # 6
print(csLinkedList)                            # 100 --> 10 --> 20 --> 30 --> 40 --> 50

# ------------------------------------------------------
# 📌 Example Diagram
# ------------------------------------------------------
# After append(10,20,30,40,50) and prepend(100):
#
# [100] → [10] → [20] → [30] → [40] → [50]
#   ↑                                     ↓
#   └─────────────────────────────────────┘
#
# head = 100
# tail = 50
# tail.next = 100
# length = 6

# ------------------------------------------------------
# ⏱️ Complexity
# ------------------------------------------------------
# append():
#   • Time: O(1) → constant pointer updates
#   • Space: O(1)
#
# prepend():
#   • Time: O(1) → constant pointer updates
#   • Space: O(1)
#
# __str__():
#   • Time: O(n) → must traverse n nodes
#   • Space: O(1)
