"""
📌 Problem: Implement pop_first() method in a Circular Singly Linked List (CSLL)

You need to extend the CSLL with a pop_first method that:
✅ Removes and returns the first node (head)
✅ Handles edge cases (empty list, single node, multiple nodes)
✅ Maintains circular property (tail.next → head)
✅ Updates head, tail, and length correctly
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
In a CSLL:
- The head points to the first node.
- The tail.next always points back to the head.

To remove the first node:
1. If the list is empty → return None
2. If the list has one node:
   - Store head in popped_node
   - Set head = None, tail = None
3. If the list has more than one node:
   - Store head in popped_node
   - Move head to head.next
   - Update tail.next to new head (preserve circular link)
   - Disconnect popped_node.next = None
4. Decrement length
5. Return popped_node
"""

# ---------------------------------------------------------------
# 📝 Algorithm (pop_first)
# ---------------------------------------------------------------
"""
pop_first():
1. If length == 0 → return None
2. Save current head as popped_node
3. If length == 1:
   - head = None, tail = None
4. Else:
   - head = head.next
   - tail.next = head
   - popped_node.next = None
5. length -= 1
6. Return popped_node
"""

# ---------------------------------------------------------------
# ✅ Code Implementation
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

    def __str__(self):
        if self.head is None:
            return "Empty CSLL"
        result = []
        node = self.head
        while True:
            result.append(str(node.value))
            node = node.next
            if node == self.head:
                break
        return "  -->  ".join(result)

    def pop_first(self):
        """Remove and return the first node in the CSLL."""
        if self.length == 0:          # Case 1: Empty list
            return None

        popped_node = self.head
        if self.length == 1:          # Case 2: Single node
            self.head = None
            self.tail = None
        else:                         # Case 3: Multiple nodes
            self.head = self.head.next
            self.tail.next = self.head
            popped_node.next = None   # detach popped node
        self.length -= 1
        return popped_node


# ---------------------------------------------------------------
# ▶️ Driver Code
# ---------------------------------------------------------------
if __name__ == "__main__":
    csLinkedList = CircularSinglyLinkedList()
    csLinkedList.append(10)
    csLinkedList.append(20)
    csLinkedList.append(30)
    csLinkedList.append(40)

    print("CSLL:", csLinkedList)  # 10 --> 20 --> 30 --> 40
    print("Popped:", csLinkedList.pop_first())  # 10
    print("After pop_first:", csLinkedList)     # 20 --> 30 --> 40
    print("Head:", csLinkedList.head.value)     # 20
    print("Tail:", csLinkedList.tail.value)     # 40
    print("Tail.next:", csLinkedList.tail.next.value)  # 20 (circular)

# ---------------------------------------------------------------
# 📊 Complexity
# ---------------------------------------------------------------
"""
- Time Complexity: O(1) (direct pointer updates)
- Space Complexity: O(1) extra
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
"""
Initial CSLL: [10  -->  20  -->  30  -->  40]
Indexes:       [ 0       1       2       3 ]

Case 1: pop_first() when list = [10 20 30 40]
- popped_node = head (10)
- head moves to 20
- tail.next points to 20 (new head)
- popped_node.next = None
- length = 3
- Return 10
Result: [20  -->  30  -->  40]

Case 2: pop_first() again on [20 30 40]
- popped_node = 20
- head moves to 30
- tail.next points to 30
- popped_node.next = None
- length = 2
- Return 20
Result: [30  -->  40]

Case 3: pop_first() on [30 40]
- popped_node = 30
- head moves to 40
- tail.next points to 40
- length = 1
- Return 30
Result: [40] (single node circular: tail.next = head)

Case 4: pop_first() on [40]
- popped_node = 40
- head = None, tail = None
- length = 0
- Return 40
Result: Empty CSLL

Case 5: pop_first() on Empty CSLL
- length = 0
- Return None
"""
