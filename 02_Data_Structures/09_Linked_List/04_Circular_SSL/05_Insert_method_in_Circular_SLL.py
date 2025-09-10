"""
📌 Problem: Implement insert method in a Circular Singly Linked List (CSLL)

You need to extend the CSLL with an insert method that:
✅ Allows inserting a new node at any position (0 .. length)
✅ Maintains circular connections (tail.next always points to head)
✅ Updates head, tail, and length correctly
✅ Raises IndexError for invalid indices
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
A CSLL is similar to a normal singly linked list, but the tail’s next 
always points back to the head.

For insertion:
1. If index == 0 → insert at head
2. If index == length → insert at tail (same as append)
3. Otherwise → traverse to index-1 and insert in the middle
4. If list is empty and index == 0 → new node becomes head and tail
"""

# ---------------------------------------------------------------
# 📝 Algorithm (Insert)
# ---------------------------------------------------------------
"""
insert(index, value):
1. If index < 0 or index > length → raise IndexError
2. Create a new node
3. If length == 0:
    - new_node.next = new_node
    - head = tail = new_node
4. Elif index == 0:
    - new_node.next = head
    - head = new_node
    - tail.next = new_node   (preserve circular link)
5. Elif index == length:
    - tail.next = new_node
    - new_node.next = head
    - tail = new_node
6. Else (middle):
    - Traverse to node at index-1 (prev)
    - new_node.next = prev.next
    - prev.next = new_node
7. Increment length
"""

# ---------------------------------------------------------------
# ✅ Code Implementation
# ---------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        """Helper: append at end using insert."""
        self.insert(self.length, value)

    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")

        new_node = Node(value)

        # Case A: empty list
        if self.length == 0:
            new_node.next = new_node
            self.head = new_node
            self.tail = new_node

        # Case B: insert at head
        elif index == 0:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = new_node

        # Case C: insert at tail
        elif index == self.length:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node

        # Case D: insert in middle
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next
            new_node.next = prev.next
            prev.next = new_node

        self.length += 1

    def __str__(self):
        if not self.head:
            return "Empty CSLL"
        result = []
        node = self.head
        while True:
            result.append(str(node.value))
            node = node.next
            if node == self.head:
                break
        return "  -->  ".join(result)


if __name__ == "__main__":
    # Create a CSLL
    csll = CircularSinglyLinkedList()

    # Insert nodes
    csll.insert(0, 10)   # [10]
    csll.insert(1, 20)   # [10 → 20]
    csll.insert(0, 5)    # [5 → 10 → 20]
    csll.insert(2, 15)   # [5 → 10 → 15 → 20]
    csll.insert(4, 25)   # [5 → 10 → 15 → 20 → 25]

    # Print results
    print("CSLL:", csll)
    print("Head:", csll.head.value)
    print("Tail:", csll.tail.value)
    print("Tail.next:", csll.tail.next.value)  # should point to head
    print("Length:", csll.length)

# ---------------------------------------------------------------
# 📊 Complexity
# ---------------------------------------------------------------
"""
- Time Complexity:
  • O(1) for insert at head or tail
  • O(n) for insert at middle (traverse required)
- Space Complexity: O(1) extra
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
"""
Start: []
insert(0, 10) → [10]
insert(1, 20) → [10 → 20]
insert(0, 5)  → [5 → 10 → 20]
insert(2, 15) → [5 → 10 → 15 → 20]
insert(4, 25) → [5 → 10 → 15 → 20 → 25]

Circular property:
tail.next always points back to head
"""
