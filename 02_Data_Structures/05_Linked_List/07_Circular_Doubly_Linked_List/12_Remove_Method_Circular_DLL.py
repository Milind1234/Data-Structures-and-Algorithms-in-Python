# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: remove (using helper) | remove_direct (no helper)
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
    # append(value) → Insert node at the end
    # ---------------------------------------------------------------
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            self.head.prev = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    # ---------------------------------------------------------------
    # __str__() → String Representation
    # ---------------------------------------------------------------
    def __str__(self):
        if self.head is None:
            return "Empty CDLL"
        current_node = self.head
        parts = []
        while True:
            parts.append(str(current_node.value))
            current_node = current_node.next
            if current_node == self.head:
                break
        return " ◀——▶ ".join(parts)

    # ---------------------------------------------------------------
    # get(index) → Get node object by index (helper)
    # ---------------------------------------------------------------
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        return current

    # ---------------------------------------------------------------
    # Pop_first() → Remove first node (used by remove)
    # ---------------------------------------------------------------
    def Pop_first(self):
        if self.length == 0:
            return None
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped.prev = None
            popped.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped

    # ---------------------------------------------------------------
    # Pop_last() → Remove last node (used by remove)
    # ---------------------------------------------------------------
    def Pop_last(self):
        if self.length == 0:
            return None
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped.prev = None
            popped.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped

    # ---------------------------------------------------------------
    # remove(index) → Remove node by index using helper get()
    # ---------------------------------------------------------------
    def remove(self, index):
        """
        Purpose:
        Remove and return the node at `index` (0-based) using the helper get().

        Steps:
        1. If index invalid (<0 or >= length) -> return "Index out of Bound".
        2. If index == 0 -> use Pop_first() and return popped node.
        3. If index == length-1 -> use Pop_last() and return popped node.
        4. Else:
           - popped_node = get(index)
           - popped_node.prev.next = popped_node.next
           - popped_node.next.prev = popped_node.prev
           - isolate popped_node (popped_node.next = popped_node.prev = None)
           - decrease length and return popped_node.

        Visualization & edge-cases are shown in the test cases below.

        Complexity:
        - Time: O(n) worst-case, optimized by get() (O(n/2) average).
        - Space: O(1).
        """
        if index < 0 or index >= self.length:
            return "Index out of Bound"
        if index == 0:
            return self.Pop_first()
        if index == self.length - 1:
            return self.Pop_last()

        popped_node = self.get(index)
        # unlink popped_node
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node

    # ---------------------------------------------------------------
    # remove_direct(index) → Remove node by index without using helper
    # ---------------------------------------------------------------
    def remove_direct(self, index):
        """
        Purpose:
        Remove and return the node at `index` (0-based) without using helper methods.

        Steps & Cases:
        1. If index invalid -> return "Index out of Bound".
        2. If length == 1 -> remove single node and return it.
        3. If index == 0 -> remove head (update head, tail links).
        4. If index == length-1 -> remove tail (update tail, head links).
        5. Else:
           - Walk from head index steps to reach the node to remove.
           - unlink it (prev.next = next, next.prev = prev)
           - isolate node, decrement length, return node.

        Complexity:
        - Time: O(n) worst-case
        - Space: O(1)
        """
        # case 1 : invalid index
        if index < 0 or index >= self.length:
            return "Index out of Bound"

        # case 2 : single-node list
        if self.length == 1:
            popped_node = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            return popped_node

        # case 3 : remove head
        if index == 0:
            popped_node = self.head
            self.head = self.head.next
            popped_node.next = None
            popped_node.prev = None
            self.tail.next = self.head
            self.head.prev = self.tail
            self.length -= 1
            return popped_node

        # case 4 : remove tail
        if index == self.length - 1:
            popped_node = self.tail
            self.tail = self.tail.prev
            popped_node.prev = None
            popped_node.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
            self.length -= 1
            return popped_node

        # case 5 : remove middle node (walk from head)
        popped_node = self.head
        for _ in range(index):
            popped_node = popped_node.next
        popped_node.prev.next = popped_node.next
        popped_node.next.prev = popped_node.prev
        popped_node.next = None
        popped_node.prev = None
        self.length -= 1
        return popped_node


# ---------------------------------------------------------------
# ✅ Multi Test Cases Demonstrating remove() and remove_direct()
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("=== Test group A: remove() using helper get() ===")
    A = CircularDoublyLinkedList()
    for v in [10, 20, 30, 40, 50]:
        A.append(v)
    print("Start A:", A)                      # 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    # remove head (index 0)
    popped = A.remove(0)
    print("Removed index 0 ->", popped)      # 10
    print("After remove(0):", A)              # 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    # remove tail (index length-1)
    popped = A.remove(A.length - 1)
    print("Removed tail ->", popped)         # 50
    print("After removing tail:", A)         # 20 ◀——▶ 30 ◀——▶ 40

    # remove middle (index 1)
    popped = A.remove(1)
    print("Removed index 1 ->", popped)      # 30
    print("After remove(1):", A)             # 20 ◀——▶ 40

    # invalid index
    print("Remove invalid index ->", A.remove(10))  # "Index out of Bound"
    print("Final A:", A)                             # 20 ◀——▶ 40

    print("\n=== Test group B: remove_direct() without helper ===")
    B = CircularDoublyLinkedList()
    for v in [1, 2, 3, 4, 5]:
        B.append(v)
    print("Start B:", B)                      # 1 ◀——▶ 2 ◀——▶ 3 ◀——▶ 4 ◀——▶ 5

    # remove middle (index 2)
    popped = B.remove_direct(2)
    print("Removed index 2 (direct) ->", popped)   # 3
    print("After remove_direct(2):", B)            # 1 ◀——▶ 2 ◀——▶ 4 ◀——▶ 5

    # remove head (index 0)
    popped = B.remove_direct(0)
    print("Removed index 0 (direct) ->", popped)   # 1
    print("After remove_direct(0):", B)            # 2 ◀——▶ 4 ◀——▶ 5

    # remove tail (index length-1)
    popped = B.remove_direct(B.length - 1)
    print("Removed tail (direct) ->", popped)      # 5
    print("After removing tail direct:", B)        # 2 ◀——▶ 4

    # single-node removal scenario
    C = CircularDoublyLinkedList()
    C.append(99)
    print("\nStart C (single node):", C)           # 99
    popped = C.remove_direct(0)
    print("Removed from single-node list ->", popped)  # 99
    print("After remove_direct on single-node:", C)    # Empty CDLL

    # invalid index
    print("\nRemove invalid index from B ->", B.remove_direct(10))  # "Index out of Bound"
    print("Final B:", B)

# ---------------------------------------------------------------
# 📊 Complexity Summary
# ---------------------------------------------------------------
# remove(index) [uses get()]:
# - Time: O(n) worst-case (optimized average O(n/2) by get())
# - Space: O(1)
#
# remove_direct(index):
# - Time: O(n) worst-case
# - Space: O(1)
#
# Notes:
# - Both functions correctly maintain circular links: head.prev == tail and tail.next == head.
# - Both isolate popped nodes by clearing their next/prev references before returning.
# - API design: These functions return the popped Node object when successful, or a string "Index out of Bound" for invalid index (keeps with your original behaviour).
# ---------------------------------------------------------------


# _______________________________________________________________________________________________________________________
# 📘 Visual Example (remove by index using helper)
#
# Case 1: Remove at Head (index = 0)
# Before:
# [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]
#  ↑head                        ↑tail
#
# remove(0):
# popped_node = [10]
#
# After:
# [20] ◀——▶ [30] ◀——▶ [40]
#  ↑head                  ↑tail
#
# Notes:
# - new head = 20
# - head.prev = tail (40), tail.next = head (20)
# - popped_node [10] is isolated
# _______________________________________________________________________________________________________________________
#
# Case 2: Remove at Tail (index = length-1)
# Before:
# [20] ◀——▶ [30] ◀——▶ [40] ◀——▶ [50]
#  ↑head                        ↑tail
#
# remove(3):
# popped_node = [50]
#
# After:
# [20] ◀——▶ [30] ◀——▶ [40]
#  ↑head                  ↑tail
#
# Notes:
# - new tail = 40
# - head.prev = tail (40), tail.next = head (20)
# - popped_node [50] isolated
# _______________________________________________________________________________________________________________________
#
# Case 3: Remove at Middle (index = 2)
# Before:
# [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40] ◀——▶ [50]
#  ↑head                                    ↑tail
#
# remove(2):
# popped_node = [30]
#
# After:
# [10] ◀——▶ [20] ◀——▶ [40] ◀——▶ [50]
#  ↑head                              ↑tail
#
# Notes:
# - 20.next = 40
# - 40.prev = 20
# - circular links preserved (head.prev = tail, tail.next = head)
# - popped_node [30] isolated
# _______________________________________________________________________________________________________________________
#
# 📘 Visual Example (remove_direct without helper)
# (Logic and result are the same as remove, only traversal differs)
#
# Example: remove_direct(1)
# Before:
# [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head                  ↑tail
#
# After:
# [10] ◀——▶ [30]
#  ↑head      ↑tail
#
# Notes:
# - node [20] removed by walking from head
# - 10.next = 30, 30.prev = 10
# - circular links preserved
# _______________________________________________________________________________________________________________________
