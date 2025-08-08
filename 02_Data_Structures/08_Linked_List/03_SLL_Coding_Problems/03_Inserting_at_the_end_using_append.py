"""
📌 Append Method in Singly Linked List
---------------------------------------

🔹 Time Complexity: O(1) — we always add the new node at the tail in constant time.  
🔹 Space Complexity: O(1) — we use no extra data structures, only a single new node.

------------------------------------------------------------
📊 Step-by-Step Iteration Visualization
------------------------------------------------------------

We will append values: 10, then later more nodes.

Initial (empty list):
head → None  
tail → None  
length = 0  

------------------------------------------------------------
Appending 10:
1. Create new node: [10] → None
2. Check if list is empty (head and tail are None) → True
3. Set head = new_node ([10])
4. Set tail = new_node ([10])
5. Increase length → length = 1

Diagram:
head → [10] → None  
tail └───────────^

------------------------------------------------------------
Appending another value (example: 20):
Before append:
head → [10] → None  
tail → [10]  
length = 1

Step-by-Step:
1. Create new node: [20] → None
2. Since head is NOT None, set tail.next = new_node
   → [10] → [20] → None
3. Move tail pointer to [20]
4. Increase length → length = 2

Diagram:
head → [10] → [20] → None  
tail └───────────────^

------------------------------------------------------------
✅ Summary:
- First append sets both head and tail to the new node.
- All subsequent appends add node at tail in O(1) time.
- No traversal is needed.

------------------------------------------------------------
"""

# ============================================================
#  CODE IMPLEMENTATION
# ============================================================

class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None and self.tail is None:  # Empty list
            self.head = new_node
            self.tail = new_node
        else:  # Non-empty list
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        temp = self.head
        result = ""
        while temp:
            result += f"[{temp.value}]"
            if temp.next:
                result += " → "
            temp = temp.next
        return result

# Example Run
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    print("After appending 10:", ll)
    ll.append(20)
    print("After appending 20:", ll)
    ll.append(30)
    print("After appending 30:", ll)
