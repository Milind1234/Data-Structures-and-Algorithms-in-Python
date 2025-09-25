# 📌 QUESTION:
# Implement "insert at index" in a Doubly Linked List (DLL) in two ways:
# 1️⃣ insert_element → with helpers (prepend, append, get_value)
# 2️⃣ insert_element_direct → without any helpers

# ------------------------------------------------------
# ✅ Node class
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# ✅ DLL Implementation
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ------------------------------
    # __str__ → string representation
    # ------------------------------
    def __str__(self):
        result = []
        temp_node = self.head
        while temp_node:
            result.append(str(temp_node.value))
            temp_node = temp_node.next
        return " <-> ".join(result) if result else "Empty DLL"

    # ------------------------------
    # Append (O(1))
    # ------------------------------
    def append(self, value):
        new_node = Node(value)
        if self.head is None:           # Empty list
            self.head = self.tail = new_node
        else:                           # Non-empty list
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # Prepend (O(1))
    # ------------------------------
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:           # Empty list
            self.head = self.tail = new_node
        else:                           # Non-empty list
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1

    # ------------------------------
    # Get node by index (O(n))
    # ------------------------------
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:       # Search from head
            current = self.head
            for _ in range(index):
                current = current.next
        else:                              # Search from tail
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        return current

    # ------------------------------
    # ✅ Insert with helpers
    # ------------------------------
    """
    Uses:
    - prepend() if index == 0
    - append() if index == length
    - get_value(index-1) to find previous node

    Time: O(n) (because of get_value)
    Space: O(1)
    """
    def insert_element(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        if index == 0:                  # Insert at head
            self.prepend(value)
            return
        if index == self.length:        # Insert at tail
            self.append(value)
            return

        prev_node = self.get_value(index - 1)
        new_node = Node(value)
        next_node = prev_node.next

        # Connect new node in between
        new_node.prev = prev_node
        new_node.next = next_node
        prev_node.next = new_node
        if next_node:
            next_node.prev = new_node

        self.length += 1

    # ------------------------------
    # ✅ Insert without helpers
    # ------------------------------
    """
    Does not use prepend, append, or get_value.
    - Traverse manually if needed.
    - Handle head, tail, and middle insertions directly.

    Time: O(n) (must traverse to position)
    Space: O(1)
    """
    def insert_element_direct(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        new_node = Node(value)

        # Case 1: Insert at head
        if index == 0:
            if self.head is None:  # empty list
                self.head = self.tail = new_node
            else:
                new_node.next = self.head
                self.head.prev = new_node
                self.head = new_node
            self.length += 1
            return

        # Case 2: Insert at tail
        if index == self.length:
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
            self.length += 1
            return

        # Case 3: Insert in the middle
        # Choose traversal direction
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        prev_node = current.prev
        # Link new_node between prev_node and current
        new_node.prev = prev_node
        new_node.next = current
        prev_node.next = new_node
        current.prev = new_node

        self.length += 1


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(10)
DLL.append(20)
DLL.append(30)
DLL.append(40)

print("Initial DLL:", DLL)

# Using helper-based insert
DLL.insert_element(2, 25)   # [10 <-> 20 <-> 25 <-> 30 <-> 40]
print("After insert_element(2,25):", DLL)

# Using direct insert
DLL.insert_element_direct(0, 5)  # [5 <-> 10 <-> 20 <-> 25 <-> 30 <-> 40]
print("After insert_element_direct(0,5):", DLL)

DLL.insert_element_direct(6, 100)  # at tail
print("After insert_element_direct(6,100):", DLL)

DLL.insert_element_direct(8, 100)  # at tail
print("After insert_element_direct(7,100):", DLL)