"""
📌 Problem: Implement pop_last() method in a Circular Singly Linked List (CSLL)

You need to extend the CSLL with a pop_last method that:
✅ Removes and returns the last node (tail)
✅ Handles edge cases (empty list, single node, multiple nodes)
✅ Maintains circular property (tail.next → head)
✅ Updates head, tail, and length correctly
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
In a CSLL:
- The tail is the last node and points back to the head.
- To remove the last node, we need to locate the node before tail.

Steps:
1. If the list is empty → return None
2. If the list has one node:
   - Save tail as popped_node
   - Set head = None, tail = None
3. If the list has multiple nodes:
   - Traverse until reaching the node just before tail
   - Save tail as popped_node
   - Update new tail = prev
   - Point new tail.next = head (circular link preserved)
   - Disconnect popped_node.next = None
4. Decrement length
5. Return popped_node
"""

# ---------------------------------------------------------------
# 📝 Algorithm (pop_last)
# ---------------------------------------------------------------
"""
pop_last():
1. If length == 0 → return None
2. Save tail as popped_node
3. If length == 1:
   - head = None, tail = None
4. Else:
   - prev = head
   - Traverse while prev.next != tail
   - prev becomes new tail
   - prev.next = head
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
        if self.length == 0:                 # empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:                                # non-empty
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1

    def __str__(self):
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

    def pop_last(self):
        """Remove and return the last node (tail)."""
        if self.length == 0:          # Case 1: Empty list
            return None

        popped_node = self.tail
        if self.length == 1:          # Case 2: Single node
            self.head = None
            self.tail = None
        else:                         # Case 3: Multiple nodes
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            prev.next = self.head
            self.tail = prev
            popped_node.next = None
        self.length -= 1
        return popped_node


# ---------------------------------------------------------------
# ▶️ Driver Code
# ---------------------------------------------------------------
if __name__ == "__main__":
    csll = CircularSinglyLinkedList()
    csll.append(10)
    csll.append(20)
    csll.append(30)
    csll.append(40)

    print("CSLL:", csll)                   # 10 --> 20 --> 30 --> 40
    print("Popped:", csll.pop_last())      # 40
    print("After pop_last:", csll)         # 10 --> 20 --> 30
    print("Head:", csll.head.value)        # 10
    print("Tail:", csll.tail.value)        # 30
    print("Tail.next:", csll.tail.next.value)  # 10 (circular)

# ---------------------------------------------------------------
# 📊 Complexity
# ---------------------------------------------------------------
"""
- Time Complexity:
  • O(1) for empty/single node case
  • O(n) for multiple nodes (traverse to find node before tail)
- Space Complexity: O(1) extra
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
"""
Initial CSLL: [10  -->  20  -->  30  -->  40]
Indexes:       [ 0       1       2       3 ]

Case 1: pop_last() on [10 20 30 40]
- popped_node = tail (40)
- Traverse: prev = head(10) → 20 → 30 (stop at node before tail)
- tail = 30
- prev.next = head (10)
- popped_node.next = None
- length = 3
Result: [10  -->  20  -->  30]
Return: 40

Case 2: pop_last() on [10 20 30]
- popped_node = 30
- Traverse: prev = 10 → 20
- tail = 20
- prev.next = head (10)
- popped_node.next = None
- length = 2
Result: [10  -->  20]
Return: 30

Case 3: pop_last() on [10 20]
- popped_node = 20
- Traverse: prev = 10
- tail = 10
- tail.next = head (10)
- popped_node.next = None
- length = 1
Result: [10] (single node circular)
Return: 20

Case 4: pop_last() on [10]
- popped_node = 10
- head = None, tail = None
- length = 0
Result: []
Return: 10

Case 5: pop_last() on empty list
- length = 0
- Return: None
"""
