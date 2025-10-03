# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: Append | __str__ | Pop_first | Pop_last
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
    # 4️⃣ Pop_last() → Remove last node
    # ---------------------------------------------------------------
    def Pop_last(self):
        """
        Purpose:
        Remove and return the **last node** (tail) of the CDLL.

        Steps:
        1. If list is empty → return None.
        2. Save popped_node = tail.
        3. If only 1 node:
             - head = tail = None
        4. Else:
             - tail = tail.prev
             - popped_node.next = popped_node.prev = None (isolate node)
             - tail.next = head
             - head.prev = tail
        5. Decrease length.
        6. Return popped_node.

        🔍 Visualization:

        Before:
        [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40]
         ↑head                        ↑tail

        Pop_last():
        popped_node = [40]
        After:
        [10] ◀──▶ [20] ◀──▶ [30]
         ↑head              ↑new tail
        (circular links preserved: head.prev = tail, tail.next = head)

        ⏱️ Time Complexity: O(1)
        ⏱️ Space Complexity: O(1)
        """
        if self.length == 0:
            return None

        popped_node = self.tail
        if self.length == 1:  # Only one node
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
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

    print("Popped First Node:", CDLL.Pop_first())
    # Output: Popped First Node: 10
    print("After Pop_first:", CDLL)
    # Output: 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    print("Popped Last Node:", CDLL.Pop_last())
    # Output: Popped Last Node: 50
    print("After Pop_last:", CDLL)
    # Output: 20 ◀——▶ 30 ◀——▶ 40


# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Pop_last on Empty List)
#             Before:
#             None
#
#             After Pop_last():
#             None
#             (List remains empty, return None)
# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Pop_last on Single-Node List)
#             Before:
#             [10]
#              ↑
#        head & tail
#
#             After Pop_last():
#             None
#             head = None, tail = None
#             (List becomes empty)
# _______________________________________________________________________________________________________________________
# 📘 Visual Example (Pop_last on Multi-Node List)
#             Before:
#             [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]
#              ↑                               ↑
#             head                            tail
#
#             After Pop_last():
#             [10] ◀——▶ [20] ◀——▶ [30]
#              ↑                       ↑
#             head                   new tail
#
# Note:
# - popped_node = 40 (isolated from list)
# - new tail = 30
# - head.prev = tail (30), tail.next = head (10) → circular links preserved
# _______________________________________________________________________________________________________________________
