"""
note_insert_sorted_csll.py - Insert into a Sorted Circular Singly Linked List (CSLL)

📌 Question:
Implement a function to insert a new node into a sorted circular singly linked list (CSLL).
Assume the list is *non-rotated* (i.e. head always points to the smallest element).

---

📖 Explanation:
- A CSLL is sorted in ascending order if nodes are in non-decreasing order, starting at head.
- To insert a new value correctly, we must handle four cases:
  1. Empty list:
       - Create a single-node circular list (node.next points to itself).
  2. New value ≤ head.data:
       - Insert before the head.
       - Update head pointer to this new node.
  3. New value between two nodes:
       - Traverse until `temp.next.data >= value` or we return to head.
       - Insert node between `temp` and `temp.next`.
  4. New value greater than all existing values:
       - Insert at the end (before head), effectively updating the tail.

- Special note on duplicates:
  • If new value equals `head.data`, the new node becomes the new head (inserted before).
  • If new value equals a middle node’s data, the new node is inserted before the first occurrence.

---

Time Complexity:
- O(n) in the worst case (must traverse to the correct insertion point).
- O(1) for empty list or head insertion.

Space Complexity:
- O(1), only one new node is allocated.
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
# Circular Singly Linked List
# ============================================================
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        """Utility: append at end (not sorted insert)."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            self.head.next = new_node
        else:
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def prepend(self, data):
        """Utility: prepend at beginning (used by sorted insert)."""
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            self.head = new_node

    def insert_into_sorted(self, data):
        """
        Insert into a non-rotated sorted CSLL.

        Step-by-step:
        1) If list empty:
             - Create single-node CSLL.
        2) If new value ≤ head.data:
             - Use prepend (insert before head, update head).
        3) Otherwise:
             - Traverse list while (temp.next != head and temp.next.data < new value).
             - Insert node between temp and temp.next.
        4) If loop ends at tail:
             - Append new node before head (tail insertion).
        """
        new_node = Node(data)
        if not self.head:
            # Case 1: empty list
            self.head = new_node
            new_node.next = new_node
        elif data <= self.head.data:
            # Case 2: new value smaller than or equal to head
            self.prepend(data)
        else:
            # Case 3 and 4: insert in middle or at end
            temp = self.head
            while temp.next != self.head and temp.next.data < data:
                temp = temp.next
            new_node.next = temp.next
            temp.next = new_node


# ============================================================
# ▶️ Dry-run examples
# ============================================================
"""
Dry-run 1: Empty list, insert 5
    head=None → new node(5).next=itself → head=5 → [5]

Dry-run 2: Insert 0 into [1->2->3->(back to head)]
    0 <= head(1).data → prepend
    new node=0, linked before 1, head updated to 0
    → [0->1->2->3->(back to head)]

Dry-run 3: Insert 3 into [1->2->4->5->(back to head)]
    head=1, value=3 > head
    traverse: 1<3, 2<3, next=4≥3 → insert before 4
    → [1->2->3->4->5]

Dry-run 4: Insert 6 into [1->2->4->5->(back to head)]
    traverse all nodes until temp.next==head
    insert before head
    → [1->2->4->5->6]

Dry-run 5: Insert duplicate 2 into [1->2->2->3]
    while loop uses `<` (not ≤)
    stops at first 2 (because 2 is not < 2)
    → inserts before first 2
    → [1->2->2->2->3]
"""
