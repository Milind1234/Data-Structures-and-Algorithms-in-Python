# 📌 QUESTION:
# Implement Doubly Linked List (DLL) with two versions of set_value:
# 1️⃣ set_value → updates node using helper function get_value()
# 2️⃣ set_value_direct → updates node directly (without helper)

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes
# ------------------------------------------------------
# ✅ Node class
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Points to previous node
        self.next = None       # Points to next node

    def __repr__(self):
        return f"Node({self.value})"


# ✅ DLL Implementation
class DoublyLinkedList:
    def __init__(self):
        """Initialize an empty Doubly Linked List."""
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """Return human-friendly representation: 10 <-> 20 <-> 30"""
        values = []
        node = self.head
        while node:
            values.append(str(node.value))
            node = node.next
        return " <-> ".join(values)

    # ------------------------------
    # Append → insert at the end
    # ------------------------------
    def append(self, value):
        """Append value at the end (O(1))."""
        new_node = Node(value)
        if self.head is None:           # empty list
            self.head = new_node
            self.tail = new_node
        else:                           # non-empty
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # ✅ Get node by index (helper)
    # ------------------------------
    """
    Purpose:
    - Return the Node object at a given index.
    - Returns None if index is invalid.

    Optimization:
    - If index in first half → traverse from head
    - If index in second half → traverse from tail

    ⏱️ Time: O(min(index, n-index)) ≈ O(n)
    ⏱️ Space: O(1)
    """
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None

        if index < self.length // 2:     # closer to head
            node = self.head
            for _ in range(index):
                node = node.next
        else:                            # closer to tail
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.prev
        return node

    # ------------------------------
    # ✅ Set value (with helper)
    # ------------------------------
    """
    Purpose:
    - Update the value of the node at a given index.
    - Uses get_value() to locate the node.

    Steps:
    1. Find node using get_value()
    2. If node exists → update node.value
    3. Return True if successful, False otherwise
    """
    def set_value(self, index, value):
        node = self.get_value(index)
        if node is None:
            return False
        node.value = value
        return True

    # ------------------------------
    # ✅ Set value (without helper)
    # ------------------------------
    """
    Purpose:
    - Same as set_value, but performs traversal itself instead of calling get_value().

    Steps:
    1. Validate index
    2. If index in first half → start from head
    3. If index in second half → start from tail
    4. Traverse until correct index, update node.value
    5. Return True if successful, False otherwise
    """
    def set_value_direct(self, index, value):
        if index < 0 or index >= self.length:
            return False

        if index < self.length // 2:     # closer to head
            node = self.head
            for _ in range(index):
                node = node.next
        else:                            # closer to tail
            node = self.tail
            for _ in range(self.length - 1, index, -1):
                node = node.prev

        node.value = value
        return True


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.append(40)

    print("Before:", dll)                     # 10 <-> 20 <-> 30 <-> 40

    # Using helper-based set_value
    success = dll.set_value(2, 100)           # update index 2 (30 → 100)
    print("set_value returned:", success)     # True
    print("After set_value:", dll)            # 10 <-> 20 <-> 100 <-> 40

    # Using direct set_value (no helper)
    success2 = dll.set_value_direct(3, 200)   # update index 3 (40 → 200)
    print("set_value_direct returned:", success2)  # True
    print("After set_value_direct:", dll)     # 10 <-> 20 <-> 100 <-> 200
