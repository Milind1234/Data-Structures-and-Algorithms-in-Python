"""
note_is_sorted.py - Check if a Circular Singly Linked List (CSLL) is Sorted

This file demonstrates how to check if a CSLL is sorted in ascending order
(strict check: every node <= its next node, including tail->head).

---

📌 Question:
Implement a function `is_sorted()` in a Circular Singly Linked List that
returns True if the list is sorted in ascending order, False otherwise.

---

📖 Explanation:
- A CSLL is sorted in ascending order if, starting from the head and traversing
  the list until back to head, each node's data <= its next node's data.
- Special cases:
  • Empty list: sorted by definition (True)
  • Single-node list: sorted by definition (True)
- General case:
  Traverse all nodes; if you ever find current.data > current.next.data, 
  return False. If you complete the cycle, return True.

Time Complexity:
- O(n), because we may check all nodes once.
Space Complexity:
- O(1), only a few pointers.
"""

# ============================================================
# Node
# ============================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# ============================================================
# Circular Singly Linked List (CSLL)
# ============================================================
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """
        Append a node at the end of the CSLL.
        Steps:
        1. If list is empty:
             - set head = new_node
             - point new_node.next to itself (circular link)
        2. Else:
             - traverse until the tail (where next == head)
             - link tail.next to new_node
             - new_node.next = head
        """
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = self.head
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def print_list(self):
        """
        Traverse CSLL once and print values in order.
        """
        nodes = []
        temp = self.head
        while temp:
            nodes.append(str(temp.data))
            temp = temp.next
            if temp == self.head:
                break
        print(" -> ".join(nodes))

    def is_sorted(self):
        """
        Return True if CSLL is sorted in ascending order (strict check).

        Step-by-step:
        1) If empty or single-node -> return True
        2) Start at head and traverse until tail:
             - If any current.data > current.next.data -> return False
        3) If traversal completes with no violation -> return True
        """
        if self.head is None or self.head.next == self.head:
            return True

        temp = self.head
        while temp.next != self.head:
            if temp.data > temp.next.data:
                return False
            temp = temp.next
        return True


# ============================================================
# ▶️ Dry-run examples
# ============================================================
"""
Dry-run 1: Empty list
    head = None
    -> directly return True

Dry-run 2: Single-node [10]
    head.next == head
    -> return True

Dry-run 3: [1 -> 2 -> 3 -> (back to head)]
    Compare 1<=2, 2<=3, 3<=head(1)
    - Last comparison fails (3 > 1), so return False

Dry-run 4: [1 -> 2 -> 2 -> (back to head)]
    Compare 1<=2, 2<=2, 2<=head(1)
    - Last comparison fails (2 > 1), so return False

Dry-run 5: [1 -> 2 -> 3 -> 4 -> (back to head)]
    1<=2, 2<=3, 3<=4, 4<=1 fails
    - Strict check says False
    - (If rotated-sorted definition used, [3,4,1,2] could be True)
"""
