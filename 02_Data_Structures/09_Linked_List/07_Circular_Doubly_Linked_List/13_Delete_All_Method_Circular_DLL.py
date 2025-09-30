# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: delete_all() → Remove All Nodes
# ------------------------------------------------------

# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    # Pointer to next node
        self.prev = None    # Pointer to previous node

    def __str__(self):
        return str(self.value)


# 🔷 Circular Doubly Linked List (CDLL) Structure
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None    # First node
        self.tail = None    # Last node
        self.length = 0     # Total number of nodes

    # 🔹 append(value): Inserts node at the end
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:   # Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:                  # Non-empty list
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    # 🔹 __str__(): String representation
    def __str__(self):
        if self.head is None:
            return "Empty CDLL"
        current_node = self.head
        result = ''
        while True:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += ' ◀——▶ '
        return result

    # ---------------------------------------------------------------
    # 1️⃣ delete_all() → Remove all nodes
    # ---------------------------------------------------------------
    def delete_all(self):
        """
        Purpose:
        Delete **all nodes** from the Circular Doubly Linked List (CDLL).

        Steps:
        1. Set head = None
        2. Set tail = None
        3. Reset length = 0
        4. Return None (list cleared)

        After this operation:
        - Entire CDLL is cleared.
        - All previous node references are lost → garbage collector frees memory.

        🔍 Visualization:

        Case 1: Non-Empty CDLL
        ----------------------
        Before:
        [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40] ◀──▶ [50]
         ↑head                                    ↑tail

        After delete_all():
        None
        head = None, tail = None, length = 0

        Case 2: Already Empty CDLL
        --------------------------
        Before:
        None
        After delete_all():
        None (no change)

        ⏱️ Time Complexity: O(1) → resets head, tail, length
        ⏱️ Space Complexity: O(1)
        """
        self.head = None
        self.tail = None
        self.length = 0
        return None


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    CDLL = CircularDoublyLinkedList()
    CDLL.append(10)
    CDLL.append(20)
    CDLL.append(30)
    CDLL.append(40)
    CDLL.append(50)

    print("Before delete_all:", CDLL)
    # Output: 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    print("delete_all() returned:", CDLL.delete_all())
    # Output: None

    print("After delete_all:", CDLL)
    # Output: Empty CDLL
