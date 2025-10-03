# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: Append | __str__ | Pop_first
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

    # ---------------------------------------------------------------
    # 1️⃣ append(value) → Insert node at the end
    # ---------------------------------------------------------------
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

    # ---------------------------------------------------------------
    # 2️⃣ __str__() → String Representation
    # ---------------------------------------------------------------
    def __str__(self):
        """
        Traverse the CDLL from head and build a string representation.

        Example:
        [10] ◀——▶ [20] ◀——▶ [30]
        """
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
    # 3️⃣ Pop_first() → Remove first node
    # ---------------------------------------------------------------
    def Pop_first(self):
        """
        Purpose:
        Remove and return the **first node** (head) of the CDLL.

        Steps:
        1. If list is empty → return None.
        2. Save popped_node = head.
        3. If only 1 node:
             - head = tail = None
        4. Else:
             - head = head.next
             - popped_node.next = popped_node.prev = None (isolate node)
             - head.prev = tail
             - tail.next = head
        5. Decrease length.
        6. Return popped_node.

        🔍 Visualization:

        Before:
        [10] ◀──▶ [20] ◀──▶ [30]
         ↑head              ↑tail

        Pop_first():
        popped_node = [10]
        After:
        [20] ◀──▶ [30]
         ↑head     ↑tail
        (circular links preserved: head.prev = tail, tail.next = head)

        ⏱️ Time Complexity: O(1)
        ⏱️ Space Complexity: O(1)
        """
        if self.length == 0:
            return None

        popped_node = self.head
        if self.length == 1:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.prev = None
            popped_node.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped_node


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

    print("Initial CDLL:", CDLL)
    # Output: 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    print("Popped Node:", CDLL.Pop_first())
    # Output: Popped Node: 10

    print("After popping First Node:", CDLL)
    # Output: 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Pop_first on Empty List)
#             Before:
#             None
#
#             After Pop_first():
#             None
#             (List remains empty, return None)
# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Pop_first on Single-Node List)
#             Before:
#             [10]
#              ↑
#        head & tail
#
#             After Pop_first():
#             None
#             head = None, tail = None
#             (List becomes empty)
# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Pop_first on Multi-Node List)
#             Before:
#             [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]
#              ↑                               ↑
#             head                            tail
#
#             After Pop_first():
#             [20] ◀——▶ [30] ◀——▶ [40]
#              ↑                       ↑
#            new head                 tail
#
# Note:
# - popped_node = 10 (isolated from list)
# - new head = 20
# - head.prev = tail (40), tail.next = head (20) → circular links preserved
# _______________________________________________________________________________________________________________________
