# note.py
# ---------------------------------------------------------------------
# Doubly Linked List (DLL) — Combined helper-based implementation
# Methods included:
#  append, __str__, prepend, traverse, reverse_traverse,
#  search_element, get_node, set_value,
#  insert_element, pop_first, pop_last, remove_element, remove_by_value
#
# This file intentionally excludes the "direct" (no-helper) versions.
# Only one helper is provided: get_node (returns a Node).
# ---------------------------------------------------------------------

class Node:
    """Doubly linked list node."""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node({self.value!r})"


class DoublyLinkedList:
    """Doubly Linked List — helper-based implementations only."""

    def __init__(self, iterable=None):
        """Initialize empty list (optionally fill from iterable)."""
        self.head = None
        self.tail = None
        self.length = 0
        if iterable:
            for x in iterable:
                self.append(x)

    # ------------------------------
    # Representation
    # ------------------------------
    def __str__(self):
        """Return values as: '10 <-> 20 <-> 30' or 'Empty DLL'."""
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.value))
            cur = cur.next
        return " <-> ".join(vals) if vals else "Empty DLL"

    # ------------------------------
    # Basic modifications
    # ------------------------------
    def append(self, value):
        """
        Append value at the end.
        Time: O(1), Space: O(1)
        """
        new_node = Node(value)
        if self.head is None:           # empty list
            self.head = self.tail = new_node
        else:                           # non-empty
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1
        return True

    def prepend(self, value):
        """
        Insert value at the beginning.
        Time: O(1), Space: O(1)
        """
        new_node = Node(value)
        if self.head is None:           # empty list
            self.head = self.tail = new_node
        else:
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1
        return True

    # ------------------------------
    # Traversal helpers
    # ------------------------------
    def traverse(self):
        """Yield values from head -> tail (use: for v in dll.traverse())."""
        cur = self.head
        while cur:
            yield cur.value
            cur = cur.next

    def reverse_traverse(self):
        """Yield values from tail -> head."""
        cur = self.tail
        while cur:
            yield cur.value
            cur = cur.prev

    # ------------------------------
    # Search / access helper (single helper only)
    # ------------------------------
    def search_element(self, target):
        """
        Return index of the first occurrence of target, or -1 if not found.
        Time: O(n), Space: O(1)
        """
        cur = self.head
        idx = 0
        while cur:
            if cur.value == target:
                return idx
            cur = cur.next
            idx += 1
        return -1

    def get_node(self, index):
        """
        Helper: return Node at index, or None if index invalid.
        Optimized traversal: start from head or tail depending on index.
        Time: O(min(index, n-index)), Space: O(1)
        """
        if index < 0 or index >= self.length:
            return None

        # traverse from head if closer to head
        if index < self.length // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
            return cur

        # traverse from tail if closer to tail
        cur = self.tail
        for _ in range(self.length - 1, index, -1):
            cur = cur.prev
        return cur

    # ------------------------------
    # Set using helper
    # ------------------------------
    def set_value(self, index, value):
        """
        Update node.value at index using get_node helper.
        Returns True if successful, False if index invalid.
        """
        node = self.get_node(index)
        if node is None:
            return False
        node.value = value
        return True

    # ------------------------------
    # Insert using helpers
    # ------------------------------
    def insert_element(self, index, value):
        """
        Insert value at position index using helpers:
          - if index == 0 -> prepend
          - if index == length -> append
          - else use get_node(index-1) to place between nodes
        Raises IndexError for index < 0 or index > length.
        Time: O(n), Space: O(1)
        """
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)

        prev_node = self.get_node(index - 1)
        # prev_node must exist because index in (0, length-1)
        new_node = Node(value)
        next_node = prev_node.next

        # link new_node between prev_node and next_node
        prev_node.next = new_node
        new_node.prev = prev_node

        new_node.next = next_node
        if next_node:
            next_node.prev = new_node

        self.length += 1
        return True

    # ------------------------------
    # Pop helpers
    # ------------------------------
    def pop_first(self):
        """
        Remove and return head value. Return None if empty.
        Time: O(1), Space: O(1)
        """
        if self.head is None:
            return None
        removed = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = removed.next
            self.head.prev = None
            removed.next = None
        self.length -= 1
        return removed.value

    def pop_last(self):
        """
        Remove and return tail value. Return None if empty.
        Time: O(1), Space: O(1)
        """
        if self.tail is None:
            return None
        removed = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = removed.prev
            self.tail.next = None
            removed.prev = None
        self.length -= 1
        return removed.value

    # --------------------------------------------------
    # 1️⃣ Remove by Index (with helper functions)
    # --------------------------------------------------
    def remove_element(self, index):
        """
        Remove node at index and return its value.
        Uses helper functions: pop_first, pop_last, get_node.
        Returns None for invalid index.
        Time: O(n), Space: O(1)
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()

        # use get_node (returns the Node object)
        popped = self.get_node(index)
        # unlink popped node from its neighbors
        popped.prev.next = popped.next
        popped.next.prev = popped.prev
        # fully disconnect popped node
        popped.prev = None
        popped.next = None
        self.length -= 1
        return popped.value

    # ------------------------------
    # Remove by value (helper-based)
    # ------------------------------
    def remove_by_value(self, value):
        """
        Remove first node with given value.
        Uses traversal and remove_element helper for head/tail/middle.
        Returns True if removed, False if not found.
        Time: O(n), Space: O(1)
        """
        idx = self.search_element(value)
        if idx == -1:
            return False
        # reuse remove_element (helper-based) which handles all cases
        self.remove_element(idx)
        return True

    # ------------------------------
    # Utility helpers
    # ------------------------------
    def to_list(self):
        """Return Python list of values head -> tail."""
        return list(self.traverse())

    def clear(self):
        """Clear list memory and reset length."""
        cur = self.head
        while cur:
            nxt = cur.next
            cur.prev = None
            cur.next = None
            cur = nxt
        self.head = None
        self.tail = None
        self.length = 0


# ---------------------------------------------------------------------
# Quick self-check examples (run this file directly)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)
    dll.prepend(5)
    print("Initial:", dll)                 # 5 <-> 10 <-> 20 <-> 30
    print("Traverse:", list(dll.traverse()))
    print("Reverse:", list(dll.reverse_traverse()))

    print("Search 20 ->", dll.search_element(20))   # 2
    node = dll.get_node(1)
    print("Get index 1 ->", node.value if node else None)  # 10

    dll.set_value(2, 21)                           # change 20 -> 21
    print("After set_value(2,21):", dll)           # 5 <-> 10 <-> 21 <-> 30

    dll.insert_element(2, 15)
    print("After insert_element(2,15):", dll)      # 5 <-> 10 <-> 15 <-> 21 <-> 30

    print("pop_first ->", dll.pop_first())         # 5
    print("pop_last  ->", dll.pop_last())          # 30
    print("After pops:", dll)                      # 10 <-> 15 <-> 21

    print("remove_element(index=1) ->", dll.remove_element(1))  # removes 15
    print("After remove_element:", dll)             # 10 <-> 21

    dll.append(99)
    print("Before remove_by_value(21):", dll)
    print("remove_by_value(21) ->", dll.remove_by_value(21))    # True
    print("After remove_by_value:", dll)

    print("Final list as python list:", dll.to_list())
    dll.clear()
    print("Cleared ->", dll, "Length:", dll.length)
