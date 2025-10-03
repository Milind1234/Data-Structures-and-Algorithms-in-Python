"""
📌 Problem: Implement Search in a Circular Singly Linked List (CSLL)

You need to extend the CSLL with a search method that:
✅ Returns the index of the first occurrence of the target value
✅ Returns -1 if the value does not exist
✅ Correctly handles the circular nature (stops when back at head)
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
- Start from the head node.
- Traverse the list while maintaining an index counter.
- If current node’s value == target → return index.
- If traversal completes a full circle (back to head) → stop search.
- If not found → return -1.
"""

# ---------------------------------------------------------------
# 📝 Algorithm (Search)
# ---------------------------------------------------------------
"""
search(target):
1. If list is empty (head == None) → return -1
2. Initialize:
   - index = 0
   - current = head
3. While True:
   - If current.value == target → return index
   - Move to next node, index += 1
   - If current == head → break (full circle completed)
4. Return -1 (not found)
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
        new_node = Node(value)
        if self.length == 0:   # Empty list
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:                  # Non-empty
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
            if node == self.head:   # Stop after full circle
                break
        return "  -->  ".join(result)

    def search(self, target):
        if self.head is None:
            return -1  # Empty list
        index = 0
        current = self.head
        while True:
            if current.value == target:
                return index
            current = current.next
            index += 1
            if current == self.head:  # Completed full circle
                break
        return -1  # Not found


# ---------------------------------------------------------------
# 📊 Complexity
# ---------------------------------------------------------------
"""
- Time Complexity: O(n) → may visit all nodes in worst case
- Space Complexity: O(1) → only index and pointer variables
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
"""
CSLL: [10 → 20 → 30 → 40]  (circular back to head)

Search(30):
- index=0, current=10 → not match
- index=1, current=20 → not match
- index=2, current=30 → match → return 2

Search(50):
- index=0..3 check all nodes
- back to head → stop, return -1
"""

# ---------------------------------------------------------------
# 🧪 Example Usage
# ---------------------------------------------------------------
if __name__ == "__main__":
    csll = CircularSinglyLinkedList()
    csll.append(10)
    csll.append(20)
    csll.append(30)
    csll.append(40)

    print("CSLL:", csll)

    target = 30
    idx = csll.search(target)
    print(f"Search({target}) → Index:", idx)  # 2

    target = 50
    idx = csll.search(target)
    print(f"Search({target}) → Index:", idx)  # -1
