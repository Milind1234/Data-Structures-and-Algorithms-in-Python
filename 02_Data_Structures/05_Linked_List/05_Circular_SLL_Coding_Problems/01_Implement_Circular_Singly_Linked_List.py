"""
📌 Question:
Implement a Circular Singly Linked List (CSLL).
The list should support the following operations:
1. Insert a new node at the beginning (prepend).
2. Insert a new node at the end (append).
3. Print the list (display all nodes in circular order).

---

📖 Explanation:
- A CSLL is similar to a singly linked list except that the tail node points back to the head.
- This circular property allows continuous traversal without a `None` terminator.
- Each node has:
    • value (data stored)
    • next (reference to next node)
- The list tracks:
    • head (first node)
    • tail (last node, whose next points to head)
    • length (total number of nodes)

Time Complexity:
- Append:   O(1)
- Prepend:  O(1)
- Print:    O(n)

Space Complexity:
- Overall: O(n) (for storing n nodes)
"""

# ============================================================
# Node Class
# ============================================================
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


# ============================================================
# Circular Singly Linked List (CSLL)
# ============================================================
class CSLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ------------------------------
    # Print representation
    # ------------------------------
    """
    Traverse nodes starting from head until we circle back.
    Example:
    [10 -> 20 -> 30 -> (back to head)]
    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def __str__(self):
        if self.head is None:
            return "Empty CSLL"
        temp = self.head
        result = []
        while True:
            result.append(str(temp.value))
            temp = temp.next
            if temp == self.head:
                break
        return " -> ".join(result)

    # ------------------------------
    # Append (insert at end)
    # ------------------------------
    """
    Steps:
    1. Create new node
    2. If list empty:
         - head = tail = new_node
         - new_node.next = new_node
    3. Else:
         - tail.next = new_node
         - new_node.next = head
         - tail = new_node
    4. length += 1

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
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
        return "Appended Successfully"

    # ------------------------------
    # Prepend (insert at beginning)
    # ------------------------------
    """
    Steps:
    1. Create new node
    2. If list empty:
         - head = tail = new_node
         - new_node.next = new_node
    3. Else:
         - new_node.next = head
         - head = new_node
         - tail.next = head
    4. length += 1

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1
        return "Prepended Successfully"


# ============================================================
# ▶️ Usage Example
# ============================================================
if __name__ == "__main__":
    csll = CSLinkedList()
    csll.append(10)
    csll.append(20)
    csll.append(30)
    print("After appending 10, 20, 30:", csll)   # 10 -> 20 -> 30

    csll.prepend(5)
    print("After prepending 5:", csll)           # 5 -> 10 -> 20 -> 30

    print("Head:", csll.head.value)              # 5
    print("Tail:", csll.tail.value)              # 30
    print("Tail.next (should point to head):", csll.tail.next.value)  # 5
