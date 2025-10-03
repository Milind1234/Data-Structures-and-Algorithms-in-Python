"""
note_split.py - CSLL split notes (in-place vs copy)

This file contains two approaches to splitting a Circular Singly Linked List (CSLL)
into two halves (first half gets the extra node when length is odd):

  - CSLinkedListInplace : re-links existing nodes (O(n) time, O(1) extra space)
  - CSLinkedListCopy    : builds two new lists by copying values (O(n) time, O(n) extra space)

Each split method includes:
  1) a plain, line-by-line explanation of what it does
  2) dry-run examples for edge cases (empty, single-node, even, odd, two-node)

Both classes share Node and basic append/str helpers.
"""

# ============================================================
# Node (shared)
# ============================================================
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
    def __str__(self):
        return str(self.value)


# ============================================================
# Version A — In-place pointer-surgery (destructive)
# ============================================================
class CSLinkedListInplace:
    """
    Split in-place:
      - Uses slow/fast pointers to find midpoint.
      - Re-links existing nodes to form two circular lists.
      - Returns two CSLinkedListInplace objects (first_half, second_half).
      - Complexity: O(n) time, O(1) extra space.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ------------------------------
    # Helpers
    # ------------------------------
    def __str__(self):
        if self.head is None:
            return "Empty"
        out = []
        cur = self.head
        while True:
            out.append(str(cur.value))
            cur = cur.next
            if cur == self.head:
                break
        return " -> ".join(out)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # split_inplace: plain explanation
    # ------------------------------
    """
    Plain, line-by-line explanation:
    --------------------------------
    1) If the list is empty:
         - return two empty lists (None-head objects are returned as empty CSLinkedList objects).

    2) If the list has a single node:
         - first half receives that node (circular),
         - second half is empty.
         - return (first_list, empty_list).

    3) Initialize pointers:
         - slow = head
         - fast = head

    4) Move pointers to find midpoint:
         - while fast.next != head and fast.next.next != head:
             - slow = slow.next        # moves 1 step
             - fast = fast.next.next   # moves 2 steps
         - Loop stops when fast is one or two steps away from head.
         - After loop:
             - slow points to last node of first half (even n) or to the middle node (odd n).

    5) Identify heads of halves:
         - head1 = head
         - head2 = slow.next

    6) Close first half:
         - slow.next = head1
         - tail1 = slow

    7) Determine tail2 and close second half:
         - if fast.next == head:
             - odd length -> tail2 = fast
           else:
             - even length -> tail2 = fast.next
         - tail2.next = head2

    8) Compute sizes:
         - size1 = n//2 + n%2  (first gets extra if odd)
         - size2 = n - size1

    9) Construct two CSLinkedListInplace objects using existing nodes:
         - set list1.head = head1, list1.tail = tail1, list1.length = size1
         - set list2.head = head2, list2.tail = tail2, list2.length = size2

    10) Return (list1, list2).
    """

    def split_inplace(self):
        # 1) empty
        if self.head is None:
            return CSLinkedListInplace(), CSLinkedListInplace()

        # 2) single node
        if self.head.next == self.head:
            l1 = CSLinkedListInplace()
            l1.head = self.head
            l1.tail = self.head
            l1.length = 1
            l1.tail.next = l1.head
            return l1, CSLinkedListInplace()

        # 3) init pointers
        slow = self.head
        fast = self.head

        # 4) find midpoint (stop when fast is 1 or 2 steps away from head)
        while fast.next != self.head and fast.next.next != self.head:
            slow = slow.next
            fast = fast.next.next

        # 5) split heads
        head1 = self.head
        head2 = slow.next

        # 6) close first half
        slow.next = head1
        tail1 = slow

        # 7) find tail2 and close second half
        if fast.next == self.head:
            tail2 = fast
        else:
            tail2 = fast.next
        tail2.next = head2

        # 8) sizes
        n = self.length
        size1 = (n // 2) + (n % 2)
        size2 = n - size1

        # 9) build list objects (reusing nodes)
        list1 = CSLinkedListInplace()
        list1.head = head1
        list1.tail = tail1
        list1.length = size1
        list1.tail.next = list1.head

        list2 = CSLinkedListInplace()
        list2.head = head2
        list2.tail = tail2
        list2.length = size2
        if list2.length > 0:
            list2.tail.next = list2.head

        return list1, list2

    # ------------------------------
    # Dry-run examples (inplace)
    # ------------------------------
    """
    Example: even 4 nodes [A,B,C,D]
      - slow/fast walk leads slow->B, fast->C; loop stops because fast.next.next == head
      - head1 = A, head2 = C
      - slow.next = head1 (B.next -> A)  => first: A->B
      - tail2 = fast.next (D); tail2.next = head2 (D.next -> C) => second: C->D

    Example: odd 5 nodes [A,B,C,D,E]
      - slow->C, fast->E; fast.next == head so odd case
      - head1 = A, head2 = D
      - slow.next = head1 (C.next -> A) => first: A->B->C
      - tail2 = fast (E); tail2.next = head2 (E.next -> D) => second: D->E

    Edge: single node -> first gets node, second empty
    Edge: empty -> both empty
    """


# ============================================================
# Version B — Copying approach (non-destructive)
# ============================================================
class CSLinkedListCopy:
    """
    Split by copying node values into two new lists:
      - Simpler and safe (original list unchanged).
      - Complexity: O(n) time, O(n) extra memory.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ------------------------------
    # Helpers
    # ------------------------------
    def __str__(self):
        if self.head is None:
            return "Empty"
        out = []
        cur = self.head
        while True:
            out.append(str(cur.value))
            cur = cur.next
            if cur == self.head:
                break
        return " -> ".join(out)

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        return new_node

    # ------------------------------
    # split_copy: plain explanation
    # ------------------------------
    """
    Plain, line-by-line explanation:
    --------------------------------
    1) If self.head is None:
         - return two empty CSLinkedListCopy objects.

    2) Compute mid count:
         - n = self.length
         - mid = (n + 1) // 2  # first half gets extra when odd

    3) Iterate through the original list once:
         - For the first mid nodes: append values to first_list
         - For remaining nodes: append values to second_list

    4) Return (first_list, second_list).

    Notes:
     - Each append builds brand-new Node objects and sets tail.next to head for the new lists.
     - Original list is unchanged.
    """

    def split_copy(self):
        if self.head is None:
            return CSLinkedListCopy(), CSLinkedListCopy()

        # mid count
        n = self.length
        mid = (n + 1) // 2

        first = CSLinkedListCopy()
        second = CSLinkedListCopy()

        cur = self.head
        i = 0
        # copy first mid values
        while i < mid:
            first.append(cur.value)
            cur = cur.next
            i += 1
        # copy remaining values
        while cur != self.head:
            second.append(cur.value)
            cur = cur.next

        return first, second

    # ------------------------------
    # Dry-run examples (copy)
    # ------------------------------
    """
    Example: [A,B,C,D] (even)
      - n=4, mid=2
      - first gets A,B; second gets C,D
      - original list unchanged

    Example: [A,B,C,D,E] (odd)
      - n=5, mid=3
      - first gets A,B,C; second gets D,E

    Edge: single node -> first gets node; second empty
    Edge: empty -> both empty
    """

# ============================================================
# ▶️ Combined usage example exercising both versions
# ============================================================
if __name__ == "__main__":
    def run_tests(values):
        print("Original values:", values)

        # In-place test
        L = CSLinkedListInplace()
        for v in values:
            L.append(v)
        print("Inplace original:", L, "| length =", L.length)
        a, b = L.split_inplace()
        print(" -> Inplace first :", a, "| length =", a.length)
        print(" -> Inplace second:", b, "| length =", b.length)

        # Copy test (original preserved)
        C = CSLinkedListCopy()
        for v in values:
            C.append(v)
        print("Copy original:", C, "| length =", C.length)
        x, y = C.split_copy()
        print(" -> Copy first :", x, "| length =", x.length)
        print(" -> Copy second:", y, "| length =", y.length)

        print("-" * 40)

    run_tests([])                # empty
    run_tests([1])               # single
    run_tests([1, 2])            # two nodes
    run_tests([1, 2, 3, 4])      # even
    run_tests([1, 2, 3, 4, 5])   # odd
