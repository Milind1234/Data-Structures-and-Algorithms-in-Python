"""
===========================================
 NODE CLASS CONSTRUCTOR (Linked List Basics)
===========================================

-------------------------------------------
What is a Node?
-------------------------------------------
- A **Node** is the fundamental building block of a Linked List.
- Each Node consists of:
    1) **Value/Data** → stores the actual data (e.g., 10)
    2) **Pointer/Reference** → points to the next node

ASCII Visualization:
--------------------
[ Value | Next Pointer ]
Example:
[ 10 | 200 ] → [ 20 | 300 ] → [ 30 | NULL ]

- **Head** → reference to the first node
- **Tail** → reference to the last node

-------------------------------------------
Why Separate Node Class?
-------------------------------------------
- Nodes have their own **responsibility** (hold data + next pointer)
- Separation of concerns:
    - Node class → creates individual nodes
    - LinkedList class → manages structure & operations
- Makes code modular and reusable

-------------------------------------------
Python Node Class Implementation
-------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value  # store data
        self.next = None    # initially no link to next node

# Example Usage:
node1 = Node(10)
print(node1)  # <__main__.Node object at 0x...> (memory location)

-------------------------------------------
Key Points:
-------------------------------------------
1) Initially, `next` pointer = None (no neighbor yet)
2) Later LinkedList class updates `next` to link nodes
3) A Node object itself does not know entire list structure

-------------------------------------------
Time & Space Complexity:
-------------------------------------------
- **Time Complexity**:
    Constructor (__init__) → O(1) (simple attribute assignments)
- **Space Complexity**:
    Each node stores 2 attributes → O(1)

-------------------------------------------
Interview Q&A:
-------------------------------------------
Q1) Why do we need a Node class instead of dictionary?
A1) A class provides better encapsulation, 
    clear structure, and can be extended with methods.

Q2) What does `next = None` mean?
A2) It means initially the node has no link. 
    When connected in LinkedList, this pointer will be updated.

Q3) How much memory does each node require?
A3) Depends on data type stored + extra memory for reference 
    (in Python, memory is dynamically managed).

-------------------------------------------
Advantages:
-------------------------------------------
1) Reusable building block for all linked list types
2) Encapsulation (clean separation of data and links)
3) Easy to extend (e.g., add prev pointer for doubly linked list)

Disadvantages:
-------------------------------------------
1) Extra memory overhead (pointer for every node)
2) Slightly more complex to implement than using built-in lists

-------------------------------------------
Complexity Summary:
-------------------------------------------
Create Node → O(1)
Space per Node → O(1)
"""
