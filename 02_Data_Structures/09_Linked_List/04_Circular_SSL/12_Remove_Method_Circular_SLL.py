"""
📌 Problem: Implement remove(index) in a Circular Singly Linked List (CSLL)

This file provides a clean implementation of a CSLL and a standalone `remove(index)` method
that **does not** rely on helper methods (no pop_first, pop_last, get). The method:
✅ Removes and returns the node at `index` (valid indices: 0 .. length-1)
✅ Correctly handles edge cases:
   - empty list (raises IndexError)
   - single-node list
   - removing head
   - removing tail
   - removing a middle node
✅ Preserves the circular property: tail.next → head
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
A CSLL maintains a circular link: tail.next points back to head.
To remove a node at index:
- Validate index (0 ≤ index < length).
- If list has one node -> clear head & tail.
- If removing head -> move head to head.next and update tail.next.
- If removing tail -> traverse to node before tail, update tail to it and link to head.
- If removing middle -> traverse to node at index-1 and relink to skip the removed node.
Always decrement length and return the removed node (with its next detached).
"""

# ---------------------------------------------------------------
# 📝 Algorithm (remove without helpers)
# ---------------------------------------------------------------
"""
remove(index):
1. If index < 0 or index >= length -> raise IndexError
2. If length == 1:
     - popped = head; head = tail = None; length -= 1; return popped
3. If index == 0:                # remove head
     - popped = head
     - head = head.next
     - tail.next = head
     - popped.next = None
     - length -= 1
     - return popped
4. If index == length - 1:       # remove tail
     - prev = head
     - while prev.next != tail: prev = prev.next
     - popped = tail
     - prev.next = head
     - tail = prev
     - popped.next = None
     - length -= 1
     - return popped
5. Else:                         # remove middle
     - prev = head
     - for _ in range(index - 1): prev = prev.next
     - popped = prev.next
     - prev.next = popped.next
     - popped.next = None
     - length -= 1
     - return popped
"""

# ---------------------------------------------------------------
# ✅ Implementation (pretty & commented)
# ---------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # -------------------------
    # Basic operations
    # -------------------------
    def append(self, value):
        """Append a node with `value` to the end of the CSLL."""
        new_node = Node(value)
        if self.length == 0:            # empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node    # circular self-loop
        else:                           # non-empty list
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def __str__(self):
        """Readable representation (stops after full circle)."""
        if not self.head:
            return "Empty CSLL"
        values = []
        node = self.head
        while True:
            values.append(str(node.value))
            node = node.next
            if node == self.head:
                break
        return "  -->  ".join(values)
    
    def get(self, index):
        """
        Return node at index (0..length-1).
        Special case: index = -1 -> return tail.
        """
        if index == -1:
            return self.tail
        if index < 0 or index >= self.length:
            raise IndexError("Index Out of Range")

        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def pop_first(self):
        """Remove and return the first node (head)."""
        if self.length == 0:
            return None

        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None
        self.length -= 1
        return popped_node

    def pop_last(self):
        """Remove and return the last node (tail)."""
        if self.length == 0:
            return None

        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev = self.head
            # stop at node before tail
            while prev.next != self.tail:
                prev = prev.next
            prev.next = self.head
            self.tail = prev
            popped_node.next = None
        self.length -= 1
        return popped_node

    def remove_with_helpers(self, index):
        """
        Remove and return node at `index`.
        Valid indices: 0 .. length-1
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of Range")

        # Remove first
        if index == 0:
            return self.pop_first()

        # Remove last
        if index == self.length - 1:
            return self.pop_last()

        # Remove in middle
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        popped_node.next = None
        self.length -= 1
        return popped_node

    # -------------------------
    # Standalone remove(index)
    # -------------------------
    def remove_no_helpers(self, index):
        """
        Remove and return the node at `index` without using other helpers.
        Valid indices: 0 .. length-1

        Returns:
            Node: the removed node (its .next is set to None)
        Raises:
            IndexError: if index out of range
        """
        if index < 0 or index >= self.length:
            raise IndexError("Index out of Range")

        # Case A: only one node in the list
        if self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            popped.next = None
            return popped

        # Case B: remove head (index == 0)
        if index == 0:
            popped = self.head
            self.head = self.head.next
            self.tail.next = self.head    # maintain circular link
            popped.next = None            # detach node
            self.length -= 1
            return popped

        # Case C: remove tail (index == length - 1)
        if index == self.length - 1:
            prev = self.head
            # traverse to node before tail
            while prev.next != self.tail:
                prev = prev.next
            popped = self.tail
            prev.next = self.head
            self.tail = prev
            popped.next = None
            self.length -= 1
            return popped

        # Case D: remove middle node
        prev = self.head
        for _ in range(index - 1):   # stop one before the target
            prev = prev.next
        popped = prev.next
        prev.next = popped.next      # bypass popped node
        popped.next = None           # detach
        self.length -= 1
        return popped


# ---------------------------------------------------------------
# ▶️ Driver / big dry-run examples (both methods)
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Build initial list: [10, 20, 30, 40, 50]
    csll = CircularSinglyLinkedList()
    for v in (10, 20, 30, 40, 50):
        csll.append(v)

    print("Initial CSLL:", csll)   # 10 --> 20 --> 30 --> 40 --> 50
    print("Length:", csll.length)
    print()

    # ----- Using remove_with_helpers -----
    print("=== remove_with_helpers Examples ===")
    # Example WH1: remove head (index 0)
    removed = csll.remove_with_helpers(0)
    print("Removed (index 0):", removed)   # 10
    print("After:", csll)                  # 20 --> 30 --> 40 --> 50
    print("Length:", csll.length)
    print()

    # Example WH2: remove middle (index 1 -> removes 30 from [20,30,40,50])
    removed = csll.remove_with_helpers(1)
    print("Removed (index 1):", removed)   # 30
    print("After:", csll)                  # 20 --> 40 --> 50
    print("Length:", csll.length)
    print()

    # Example WH3: remove tail (index length-1)
    removed = csll.remove_with_helpers(csll.length - 1)
    print("Removed (tail):", removed)      # 50
    print("After:", csll)                  # 20 --> 40
    print("Head:", csll.head.value, "Tail:", csll.tail.value, "Tail.next:", csll.tail.next.value)
    print("Length:", csll.length)
    print()

    # Continue to empty using helper-based removes
    _ = csll.remove_with_helpers(1)  # removes 40
    _ = csll.remove_with_helpers(0)  # removes 20
    print("After removing all (helpers):", csll, "Length:", csll.length)
    print()

    # Rebuild for no-helper tests
    for v in (100, 200, 300, 400):
        csll.append(v)
    print("Rebuilt CSLL:", csll)  # 100 --> 200 --> 300 --> 400
    print("Length:", csll.length)
    print()

    # ----- Using remove_no_helpers -----
    print("=== remove_no_helpers Examples ===")
    # NH1: remove tail (index length-1)
    removed = csll.remove_no_helpers(csll.length - 1)
    print("Removed (tail):", removed)   # 400
    print("After:", csll)               # 100 --> 200 --> 300
    print("Length:", csll.length)
    print()

    # NH2: remove middle (index 1 -> removes 200)
    removed = csll.remove_no_helpers(1)
    print("Removed (index 1):", removed) # 200
    print("After:", csll)               # 100 --> 300
    print("Length:", csll.length)
    print()

    # NH3: remove head (index 0)
    removed = csll.remove_no_helpers(0)
    print("Removed (index 0):", removed) # 100
    print("After:", csll)               # 300
    print("Head/Tail:", csll.head.value, csll.tail.value)
    print("Length:", csll.length)
    print()

    # NH4: remove last remaining node
    removed = csll.remove_no_helpers(0)
    print("Removed (only node):", removed)   # 300
    print("After:", csll)                    # Empty CSLL
    print("Length:", csll.length)
    print()

# ---------------------------------------------------------------
# 📊 Complexity
# ---------------------------------------------------------------
"""
- Time Complexity:
  • O(1) for single-node remove or head remove (constant pointer ops)
  • O(n) for tail or middle remove (traversal needed)
- Space Complexity: O(1)
"""