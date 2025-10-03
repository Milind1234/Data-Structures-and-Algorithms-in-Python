"""
📌 Reverse Method in Singly Linked List
---------------------------------------

🔹 Time Complexity: O(n) — we visit each node once.
🔹 Space Complexity: O(1) — only 3 extra pointers are used.

------------------------------------------------------------
📊 Step-by-Step Iteration Visualization
------------------------------------------------------------

Let’s reverse this list:

1 → 2 → 3 → 4 → None

Initial:
head → [1] → [2] → [3] → [4] → None
tail → [4]

Before start of loop:
prev_node = None
current_node = [1]

------------------------------------------------------------
Iteration 1
Before:
prev_node: None
current_node: [1] → [2]

Step-by-Step:
1. Save next node → next_node = [2]
2. Reverse pointer → [1].next = None
3. Move prev → prev_node = [1]
4. Move current → current_node = [2]

Diagram:
None ← [1]    [2] → [3] → [4] → None
prev          current

------------------------------------------------------------
Iteration 2
Before:
prev_node: [1] ← None
current_node: [2] → [3]

Step-by-Step:
1. Save → next_node = [3]
2. Reverse → [2].next = [1]
3. Move prev → prev_node = [2]
4. Move current → current_node = [3]

Diagram:
None ← [1] ← [2]    [3] → [4] → None
           prev     current

------------------------------------------------------------
Iteration 3
Before:
prev_node: [2] ← [1]
current_node: [3] → [4]

Step-by-Step:
1. Save → next_node = [4]
2. Reverse → [3].next = [2]
3. Move prev → prev_node = [3]
4. Move current → current_node = [4]

Diagram:
None ← [1] ← [2] ← [3]    [4] → None
                  prev    current

------------------------------------------------------------
Iteration 4
Before:
prev_node: [3] ← [2] ← [1]
current_node: [4] → None

Step-by-Step:
1. Save → next_node = None
2. Reverse → [4].next = [3]
3. Move prev → prev_node = [4]
4. Move current → current_node = None (loop ends)

Diagram:
None ← [1] ← [2] ← [3] ← [4]
                           prev

------------------------------------------------------------
✅ After Loop:
head = prev_node = [4]
tail = old head = [1]

Final List:
[4] → [3] → [2] → [1] → None
head                tail
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
        if not self.head:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def reverse(self):
        if self.length <= 1:
            return
        
        prev_node = None
        current_node = self.head
        self.tail = self.head  # Old head becomes new tail

        while current_node:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        self.head = prev_node

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
    ll.append(1)
    ll.append(2)
    ll.append(3)
    ll.append(4)
    print("Original:", ll)
    ll.reverse()
    print("Reversed:", ll)
