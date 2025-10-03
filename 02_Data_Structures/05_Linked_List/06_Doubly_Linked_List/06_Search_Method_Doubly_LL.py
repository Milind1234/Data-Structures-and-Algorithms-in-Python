# 📌 QUESTION:
# Extend the Doubly Linked List (DLL) to support:
# 1️⃣ Append → insert node at the end
# 2️⃣ Print (__str__)
# 3️⃣ Search Element → find the index of a target value

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes (Focus on Search)
# ------------------------------------------------------

# ✅ Node class
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Points to the previous node
        self.next = None       # Points to the next node


# ✅ DLL Implementation
class DoublyLinkedList:
    def __init__(self):
        self.head = None       # First node
        self.tail = None       # Last node
        self.length = 0        # Initially empty list

    # ------------------------------
    # __str__ → string representation
    # ------------------------------
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    # ------------------------------
    # Append → insert at the end
    # ------------------------------
    def append(self, value):
        new_node = Node(value)
        if self.head is None:           # Empty list
            self.head = new_node
            self.tail = new_node
        else:                           # Non-empty list
            self.tail.next = new_node   # old tail → new node
            new_node.prev = self.tail   # new node ← old tail
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # ✅ Search Element
    # ------------------------------
    """
    Purpose:
    - Find the index of the first occurrence of a given target value.

    Steps:
    1. Start from head node
    2. Keep a counter (index)
    3. Traverse until:
         - Found value → return index
         - Reached end → return "Element not found"

    Example:
    DLL = [10 <-> 20 <-> 30 <-> 40]
    search_element(30) → 2

    🔗 Visualization:
    head → [10] → [20] → [30] → [40]
             0      1      2      3

    ⏱️ Complexity:
    - Time: O(n) → may need to check all nodes
    - Space: O(1) → only one pointer + counter
    """
    def search_element(self, target):
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
        return "Element not found"


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(10)     # [10]
DLL.append(20)     # [10 <-> 20]
DLL.append(30)     # [10 <-> 20 <-> 30]
DLL.append(40)     # [10 <-> 20 <-> 30 <-> 40]

print("DLL contents:", DLL)  
print("Index of 30:", DLL.search_element(30))  
print("Index of 50:", DLL.search_element(50))  # Not in list
