"""
📌 Problem: Implement delete_all() in a Circular Singly Linked List (CSLL)

You need to extend the CSLL with a delete_all method that:
✅ Removes all nodes from the CSLL
✅ Sets head and tail to None
✅ Breaks circular references
✅ Resets length to 0
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
In a CSLL:
- Every node is linked, and the tail points back to head.
- To delete all nodes, we can simply:
  1. Break the circular link (tail.next = None).
  2. Set head = None and tail = None.
  3. Reset length to 0.
- Python's garbage collector will free all nodes.
"""

# ---------------------------------------------------------------
# 📝 Algorithm (delete_all)
# ---------------------------------------------------------------
"""
delete_all():
1. If list is empty -> just return
2. Break circular link: tail.next = None
3. head = None
4. tail = None
5. length = 0
"""

# ---------------------------------------------------------------
# ✅ Implementation
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
        """Append a new node at the end."""
        new_node = Node(value)
        if self.length == 0:                
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node        # circular
        else:                              
            self.tail.next = new_node       
            new_node.next = self.head      
            self.tail = new_node            
        self.length += 1

    def __str__(self):
        if not self.head:
            return "Empty CSLL"
        temp = self.head
        result = []
        while True:
            result.append(str(temp.value))
            temp = temp.next
            if temp == self.head:
                break
        return "  -->  ".join(result)

    def delete_all(self):
        """Delete all nodes in the CSLL."""
        if self.head is None:   # already empty
            return
        self.tail.next = None   # break circular link
        self.head = None
        self.tail = None
        self.length = 0


# ---------------------------------------------------------------
# ▶️ Driver Code / Dry Run
# ---------------------------------------------------------------
if __name__ == "__main__":
    csll = CircularSinglyLinkedList()
    csll.append(10)
    csll.append(20)
    csll.append(30)
    csll.append(40)

    print("CSLL before delete_all:", csll)   # 10 --> 20 --> 30 --> 40
    csll.delete_all()
    print("After delete_all:", csll)         # Empty CSLL
    print("Head:", csll.head)                # None
    print("Tail:", csll.tail)                # None
    print("Length:", csll.length)            # 0

# ---------------------------------------------------------------
# 📊 Complexity
# ---------------------------------------------------------------
"""
- Time Complexity: O(1) — just resets pointers and length
- Space Complexity: O(1) extra
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
"""
Initial CSLL: [10  -->  20  -->  30  -->  40]
Head = 10, Tail = 40, Length = 4

Step 1: delete_all() called
- Break circular link: tail.next = None
- head = None
- tail = None
- length = 0

Final CSLL: []
Head = None, Tail = None, Length = 0
"""
