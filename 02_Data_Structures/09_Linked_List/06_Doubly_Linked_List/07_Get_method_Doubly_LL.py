# 📌 QUESTION:
# Extend the Doubly Linked List (DLL) to support:
# 1️⃣ Append → insert node at the end
# 2️⃣ Print (__str__)
# 3️⃣ Get Element by Index → retrieve value at a given position

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes (Focus on get_element)
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
    # ✅ Get Element by Index
    # ------------------------------
    """
    Purpose:
    - Retrieve the value at a specific index.

    Optimized Traversal:
    - If index is in the **first half**, start from head.
    - If index is in the **second half**, start from tail.
    (Because DLL allows backward traversal.)

    Steps:
    1. Validate index (0 <= index < length)
    2. If index < length//2 → traverse from head
    3. Else → traverse from tail
    4. Return node.value

    Example:
    DLL = [10 <-> 20 <-> 30 <-> 40]
    get_element(2) → 30

    🔗 Visualization:
    Indices:  0      1      2      3
            [10] <-> [20] <-> [30] <-> [40]
                          ↑
                        index=2

    ⏱️ Complexity:
    - Best Case: O(1) (first or last element)
    - Worst Case: O(n/2) ≈ O(n) (middle element)
    - Space: O(1)
    """
    def get_element(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        if index < self.length // 2:       # Search from head
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:                              # Search from tail
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return current_node.value


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(10)     # [10]
DLL.append(20)     # [10 <-> 20]
DLL.append(30)     # [10 <-> 20 <-> 30]
DLL.append(40)     # [10 <-> 20 <-> 30 <-> 40]

print("DLL contents:", DLL)
print("Element at index 2:", DLL.get_element(2))
print("Element at index 0:", DLL.get_element(0))
print("Element at index 3:", DLL.get_element(3))
