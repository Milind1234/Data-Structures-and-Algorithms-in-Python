"""
note.py - CSLL deletion notes (explicit vs unified)

This file contains two complete Circular Singly Linked List implementations:
  - CSLinkedListExplicit : explicit if/elif branches for each case
  - CSLinkedListUnified  : single traversal loop (prev=tail, curr=head)

Each delete_by_value has:
  1) a short line-by-line, human-friendly explanation
  2) dry-run examples for the main edge cases

Both classes use:
  - Node(value).value  -> stored data
  - Node(value).next   -> pointer to next node (circular)
  - head, tail, length stored on list object
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
# Version 1: Explicit branches
# ============================================================
class CSLinkedListExplicit:
    """
    Delete uses separate blocks for:
      - empty list
      - single-node list
      - head deletion
      - tail deletion
      - middle deletion
      - not found
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head is None:
            return "Empty CSLL"
        out = []
        node = self.head
        while True:
            out.append(str(node.value))
            node = node.next
            if node == self.head:
                break
        return " -> ".join(out) + " -> (back to head)"

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            # empty list: head and tail point to new node
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node  # circular link to itself
        else:
            # connect old tail to new node, make new tail point to head
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def delete_by_value(self, value):
        """
        Returns True if a node was deleted, False otherwise.

        Plain line-by-line explanation:
        --------------------------------
        1) if self.length == 0:
             - list empty -> nothing to do -> return False
        2) if self.length == 1:
             - only one node exists
             - if it matches: remove it by setting head and tail to None, length=0, return True
             - else return False (value not present)
        3) if self.head.value == value:
             - removing the head in a list of >=2 nodes:
             - move head forward to head.next
             - update tail.next to the new head to preserve circularity
             - decrement length and return True
        4) if self.tail.value == value:
             - removing tail:
             - find node just before tail (prev)
             - make prev.next point to head (closing circle)
             - update tail = prev
             - decrement length and return True
        5) middle nodes:
             - start prev = head, curr = head.next (we already checked head and tail)
             - scan until we return to head
             - if curr.value matches:
                 - unlink by prev.next = curr.next
                 - decrement length and return True
        6) if loop completes -> not found -> return False
        """

        # 1) Empty list
        if self.length == 0:
            return False

        # 2) Single-node list
        if self.length == 1:
            if self.head.value == value:
                # remove the only node
                self.head = None
                self.tail = None
                self.length = 0
                return True
            return False

        # 3) Head node (list has >= 2 nodes)
        if self.head.value == value:
            # move head forward and preserve circular link from tail
            self.head = self.head.next
            self.tail.next = self.head
            self.length -= 1
            return True

        # 4) Tail node (list has >= 2 nodes)
        if self.tail.value == value:
            prev = self.head
            # find node just before tail
            while prev.next is not self.tail:
                prev = prev.next
            # link prev to head and update tail
            prev.next = self.head
            self.tail = prev
            self.length -= 1
            return True

        # 5) Middle node (neither head nor tail)
        prev = self.head
        curr = self.head.next
        while curr != self.head:
            if curr.value == value:
                # unlink curr by skipping it
                prev.next = curr.next
                self.length -= 1
                return True
            prev = curr
            curr = curr.next

        # 6) Not found
        return False

    # ------------------------------
    # Dry-run examples for explicit version
    # ------------------------------
    """
    Dry-run: empty list
      - length == 0 -> function returns False immediately.

    Dry-run: single-node list, value present
      - length == 1 and head.value == value
      - set head=None, tail=None, length=0 -> return True

    Dry-run: single-node list, value absent
      - length == 1 and head.value != value -> return False

    Dry-run: delete head in [10 -> 20 -> 30]
      - head.value == 10 matches -> head becomes 20
      - tail.next updated to point to new head -> preserves circularity

    Dry-run: delete tail in [10 -> 20 -> 30]
      - tail.value == 30 matches -> find prev (20)
      - prev.next = head, tail = prev (20)

    Dry-run: delete middle (20) in [10 -> 20 -> 30]
      - prev=head(10), curr=20 -> match -> prev.next=30 -> length-- -> return True

    Dry-run: not found
      - loop completes -> return False (no change)
    """


# ============================================================
# Version 2: Unified single-loop
# ============================================================
class CSLinkedListUnified:
    """
    Delete uses a single pass with prev = tail, curr = head.
    Handles head/tail/middle inside the loop; stops when we return to head.
    """

    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        if self.head is None:
            return "Empty CSLL"
        out = []
        node = self.head
        while True:
            out.append(str(node.value))
            node = node.next
            if node == self.head:
                break
        return " -> ".join(out) + " -> (back to head)"

    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def delete_by_value(self, value):
        """
        Returns True if removed, False if not found.

        Line-by-line simple explanation:
        --------------------------------
        1) If length == 0 -> empty -> return False
        2) If length == 1:
             - if head matches: clear head/tail, length=0 -> return True
             - else return False
        3) For length > 1:
             - set prev = tail, curr = head (we keep prev behind curr)
             - loop indefinitely:
                 a) if curr.value == value:
                       - remove curr by prev.next = curr.next
                       - if curr is head: move head forward
                       - if curr is tail: set tail = prev
                       - always ensure tail.next points to head (preserve circularity)
                       - decrement length and return True
                 b) move prev = curr, curr = curr.next
                 c) if curr loops back to head -> not found -> return False
        """

        # 1) empty
        if self.length == 0:
            return False

        # 2) single-node
        if self.length == 1:
            if self.head.value == value:
                self.head = None
                self.tail = None
                self.length = 0
                return True
            return False

        # 3) general case (length > 1)
        prev = self.tail
        curr = self.head

        while True:
            if curr.value == value:
                # unlink curr
                prev.next = curr.next

                # if curr is head, advance head
                if curr is self.head:
                    self.head = curr.next

                # if curr is tail, move tail back to prev
                if curr is self.tail:
                    self.tail = prev

                # maintain circularity: tail.next must point to head
                self.tail.next = self.head

                self.length -= 1
                return True

            # move forward one step
            prev = curr
            curr = curr.next

            # full circle -> not found
            if curr == self.head:
                return False

    # ------------------------------
    # Dry-run examples for unified version
    # ------------------------------
    """
    Dry-run: empty list
      - length == 0 -> return False

    Dry-run: single-node list, value present
      - length == 1 and head matches -> clear head/tail, length=0 -> return True

    Dry-run: delete head in [10 -> 20 -> 30]
      - prev = tail(30), curr = head(10)
      - curr matches -> prev.next = curr.next (30.next -> 20)
      - head = curr.next (head becomes 20)
      - tail remains 30, then tail.next = head (30.next -> 20)
      - length--, return True

    Dry-run: delete tail in [10 -> 20 -> 30]
      - traversal: curr=10(no) -> prev=10; curr=20(no) -> prev=20; curr=30(yes)
      - prev.next = curr.next -> 20.next = 10 (head)
      - curr is tail -> tail = prev (20)
      - tail.next = head (20.next -> 10)
      - length--, return True

    Dry-run: delete middle (20) in [10 -> 20 -> 30]
      - prev=10, curr=20 -> match -> prev.next = curr.next (10.next -> 30)
      - head/tail unaffected, tail.next still points to head
      - length--, return True

    Dry-run: not found
      - loop moves curr forward; when curr returns to head -> return False
    """

# ============================================================
# ▶️ Combined usage example that exercises both versions
# ============================================================
if __name__ == "__main__":
    print("=== Explicit version tests ===")
    e = CSLinkedListExplicit()
    print("Empty delete:", e.delete_by_value(1))  # False
    e.append(5)
    print("Single non-match delete:", e.delete_by_value(999))  # False
    e.append(5)  # now list has [5,5] just to test duplication handling
    # reset to single-node properly
    e = CSLinkedListExplicit()
    e.append(10)
    print("Before single delete:", e)
    print("Single match delete:", e.delete_by_value(10))  # True
    print("After single delete:", e)

    # multi-node tests
    for v in (10, 20, 30):
        e.append(v)
    print("Before deletions:", e)
    print("Delete head (10):", e.delete_by_value(10), "->", e)
    print("Delete tail (30):", e.delete_by_value(30), "->", e)
    print("Delete middle (20):", e.delete_by_value(20), "->", e)
    print("Delete not-present (999):", e.delete_by_value(999), "->", e)

    print("\n=== Unified version tests ===")
    u = CSLinkedListUnified()
    print("Empty delete:", u.delete_by_value(1))  # False
    u.append(7)
    print("Single non-match delete:", u.delete_by_value(999))  # False
    print("Single match delete:", u.delete_by_value(7))  # True

    for v in (10, 20, 30):
        u.append(v)
    print("Before deletions:", u)
    print("Delete middle (20):", u.delete_by_value(20), "->", u)
    print("Delete head (10):", u.delete_by_value(10), "->", u)
    print("Delete tail (30):", u.delete_by_value(30), "->", u)
    print("Delete not-present (999):", u.delete_by_value(999), "->", u)
