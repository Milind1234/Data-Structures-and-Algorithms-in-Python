"""
📌 Question:
Implement a Circular Singly Linked List (CSLL) and provide a method `count_nodes()`
to count the number of nodes in the list.

---

📖 Explanation:
- A Circular Singly Linked List (CSLL) is similar to a singly linked list, but:
    • The last node (tail) points back to the first node (head).
    • This makes traversal circular, without a natural `None` terminator.
- To count nodes:
    • Start from `head`
    • Move through each node
    • Stop when we return to `head` again
    • Keep a counter of how many nodes were visited

Edge Cases:
1. Empty list → count = 0
2. List with 1 node → count = 1
3. Multi-node list → count = number of unique nodes before looping back to head

Time Complexity:
- count_nodes(): O(n)  (traverse each node once)
- append(): O(1)

Space Complexity:
- O(1) extra (only uses a few pointers and a counter)
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
    # String representation
    # ------------------------------
    """
    Traverse nodes from head until we circle back.
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
            if temp == self.head:   # stop when we circle back
                break
        return " -> ".join(result) + " -> (back to head)"

    # ------------------------------
    # Append (insert at end)
    # ------------------------------
    """
    Steps:
    1. Create new node
    2. If list empty:
         - head = tail = new_node
         - new_node.next = new_node (points to itself)
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
        if self.head is None:          # empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node   # circular link
        else:
            self.tail.next = new_node  # link old tail to new node
            new_node.next = self.head  # new node points to head
            self.tail = new_node       # update tail
        self.length += 1

    # ------------------------------
    # Count nodes
    # ------------------------------
    """
    Steps:
    1. If list empty → return 0
    2. Initialize count = 0, start = head
    3. Traverse until we come back to head
    4. Increment count at each step
    5. Return count

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def count_nodes(self):
        if self.head is None:
            return 0
        count = 0
        temp = self.head
        while True:
            count += 1
            temp = temp.next
            if temp == self.head:   # stop when loop completes
                break
        return count


# ============================================================
# ▶️ Usage Example
# ============================================================
if __name__ == "__main__":
    csll = CSLinkedList()
    print("Initial list:", csll)
    print("Node count:", csll.count_nodes())   # 0

    csll.append(10)
    print("After adding 10:", csll)
    print("Node count:", csll.count_nodes())   # 1

    csll.append(20)
    csll.append(30)
    print("After adding 20 and 30:", csll)     # 10 -> 20 -> 30 -> (back to head)
    print("Node count:", csll.count_nodes())   # 3
