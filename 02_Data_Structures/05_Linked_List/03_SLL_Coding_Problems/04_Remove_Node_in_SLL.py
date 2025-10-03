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

# 🔁 remove(index): Removes node at given index
    def remove(self, index):

        # 🔹 Case 1: Invalid Index
        if index < 0 or index >= self.length:
            return "Out of Range"
        # Handles out-of-bound access

            # 🔹 Case 2: Remove Head (index = 0)
        elif index == 0:
            popped_node = self.head

            # If only one node in the list
            if self.length == 1:
                self.head = None
                self.tail = None

            # If multiple nodes, shift head
            else:
                self.head = self.head.next

            popped_node.next = None
            self.length -= 1
            return popped_node.value
# _______________________________________________________________________________________________________________________
# """
#             Before:
#             [10] → [20] → [30]
#              ↑
#             head (index 0)
            
#             After:
#             [20] → [30]
#              ↑
#             new head
# """
# ___________________________________________________________________________________________________________________
    # 🔹 Case 3: Remove from Middle or Tail
        else:
            temp_node = self.head

            # Traverse to one node before the target
            for _ in range(index - 1):
                temp_node = temp_node.next

            popped_node = temp_node.next

            # If removing the tail
            if popped_node.next is None:
                self.tail = temp_node

            # Bypass popped_node
            temp_node.next = temp_node.next.next
            popped_node.next = None
            self.length -= 1
            return popped_node.value
# _________________________________________________________________________________________________________________________
# Visual Example (Middle)
#                               Before:
#                               [10] → [20] → [30] → [40]
#                                                   ↑
#                                             popped_node (index 2)

#                               After:
#                               [10] → [20] → [40]
# __________________________________________________________________________________________________________________________
# Visual Example (tail)
#                               Before:
#                               [10] → [20] → [30] → [40] → [50] → [60]
#                                                                      ↑
#                                                                 popped_node (tail)

#                               After:
#                               [10] → [20] → [30] → [40] → [50]
#                                                                ↑
#                                                              new tail
# _____________________________________________________________________________________________________________________  
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
    
    # 🔹 Append Method
    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
# ✅ How to Use & Output
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.append(50)
new_LinkedList.append(60)

print(new_LinkedList)
# Output: 10 -> 20 -> 30 -> 40 -> 50 -> 60

print(new_LinkedList.remove(5))
# Output: 60 (removed tail)

print(new_LinkedList)
# Output: 10 -> 20 -> 30 -> 40 -> 50

print(new_LinkedList.tail.value)
# Output: 50 (new tail)

# 📊 Complexity Analysis

# Time Complexity:
# - Best case: O(1) (head removal)
# - Worst case: O(n) (tail removal or middle)

# Space Complexity:
# - O(1) → Constant space, no extra structures used

# 🧠 Tips for Interviews
# - Always check for edge cases: head, tail, empty list
# - Be careful when updating tail pointer
# - Traverse to index-1 when removing from middle
# - Practice drawing pointer movements to solidify understanding

