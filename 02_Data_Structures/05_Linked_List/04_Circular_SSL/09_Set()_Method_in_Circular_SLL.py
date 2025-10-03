"""
📌 Problem: Implement set_value() method in a Circular Singly Linked List (CSLL)

You need to extend the CSLL with methods that:
✅ Update the value of a node at a given index
✅ Maintain proper index validation (0 .. length-1)
✅ Provide two approaches:
   1. set_value_no_get → Traverse manually
   2. set_value → Reuse get() method for cleaner design
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
A CSLL allows traversal from head to tail (and back to head). 
To update a node’s value at a given index:

1. Ensure the index is valid (0 ≤ index < length).
2. Traverse from head to the target index.
3. Replace the node’s value with the new value.
4. Return True to confirm the update.

We provide two approaches:
- Without get(): Direct traversal inside set_value_no_get.
- With get(): Reuse get() to avoid duplicate traversal code.
"""

# ---------------------------------------------------------------
# 📝 Algorithm (set_value_no_get)
# ---------------------------------------------------------------
"""
set_value_no_get(index, value):
1. If index < 0 or index >= length → raise IndexError
2. Start from head
3. Move `index` steps forward
4. Update node.value = new value
5. Return True
"""

# ---------------------------------------------------------------
# 📝 Algorithm (set_value with get)
# ---------------------------------------------------------------
"""
set_value(index, value):
1. Call get(index) to retrieve node
2. Update node.value = new value
3. Return True
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
            new_node.next = new_node        # circular link
        else:                              
            self.tail.next = new_node       
            new_node.next = self.head      
            self.tail = new_node            
        self.length += 1

    def __str__(self):
        if not self.head:
            return "Empty CSLL"
        result = []
        temp_node = self.head
        while True:
            result.append(str(temp_node.value))
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return "  -->  ".join(result)

    def get(self, index):
        """Return node at given index (0..length-1). 
        Special case: index = -1 → return tail node."""
        if index == -1:
            return self.tail
        if index < 0 or index >= self.length:
            raise IndexError("Index Out of Range")
        
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    # ---------------------------------------------------------------
    # Without get()
    # ---------------------------------------------------------------
    def set_value_no_get(self, index, value):
        """Update node value by traversing manually."""
        if index < 0 or index >= self.length:
            raise IndexError("Index Out of Range")
        temp_node = self.head
        for _ in range(index):
            temp_node = temp_node.next
        temp_node.value = value
        return True

    # ---------------------------------------------------------------
    # With get()
    # ---------------------------------------------------------------
    def set_value(self, index, value):
        """Update node value using get()."""
        node = self.get(index)
        node.value = value
        return True


# ---------------------------------------------------------------
# ▶️ Driver Code
# ---------------------------------------------------------------
if __name__ == "__main__":
    csLinkedList = CircularSinglyLinkedList()
    csLinkedList.append(10)   
    csLinkedList.append(20)
    csLinkedList.append(30)
    csLinkedList.append(40)   
    
    print("CSLL:", csLinkedList)            # 10 --> 20 --> 30 --> 40
    
    # Without get()
    csLinkedList.set_value_no_get(0, 100)
    print("After set_value_no_get(0, 100):", csLinkedList)
    print("Head:", csLinkedList.head.value)

    # With get()
    csLinkedList.set_value(3, 120)
    print("After set_value(3, 120):", csLinkedList)
    print("Tail:", csLinkedList.tail.value)

# ---------------------------------------------------------------
# 📊 Complexity
# ---------------------------------------------------------------
"""
- set_value_no_get → O(n) (manual traversal)
- set_value (with get) → O(n) (get internally traverses)
- Space Complexity: O(1) extra
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
"""
Initial CSLL after appending: [10  -->  20  -->  30  -->  40]
Indexes:                      [ 0       1       2       3 ]

Example 1: set_value_no_get(0, 100)
- index = 0 (head)
- Traverse: no movement, at node 10
- Update: 10 → 100
- Result: [100 --> 20 --> 30 --> 40]

Example 2: set_value_no_get(2, 300)
- index = 2
- Traverse:
  • Step 0 → start at 10
  • Step 1 → move to 20
  • Step 2 → move to 30 (target)
- Update: 30 → 300
- Result: [100 --> 20 --> 300 --> 40]

Example 3: set_value(3, 120)
- index = 3 (tail)
- get(3) does traversal:
  • Step 0 → start at 100
  • Step 1 → move to 20
  • Step 2 → move to 300
  • Step 3 → move to 40 (target)
- Update: 40 → 120
- Result: [100 --> 20 --> 300 --> 120]

Example 4: set_value(-1, X)
- Invalid: raises IndexError

Example 5: set_value(4, X) (out of range)
- Invalid: raises IndexError
"""
