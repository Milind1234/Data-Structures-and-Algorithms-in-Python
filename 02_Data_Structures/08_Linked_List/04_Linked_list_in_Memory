"""
====================================
 HOW LINKED LISTS ARE STORED IN MEMORY
====================================

------------------------------------
Arrays in Memory (Recap)
------------------------------------
- Arrays are stored **contiguously** in memory.
- Memory cells are adjacent and indexed.
- Direct access to any element:
    Access Time = O(1) using index
- Size must be fixed or defined initially.

ASCII Visualization:
---------------------
Index → 0    1    2    3    4
Value → [10][20][30][40][50]
Addr  → 100  104  108  112  116  (example)

------------------------------------
Linked Lists in Memory
------------------------------------
- Linked list nodes are stored **non-contiguously**.
- Each node contains:
    1) Data (value)
    2) Pointer/Reference to next node
- Nodes are connected dynamically via pointers.
- **Head** points to first node.
- **Tail** points to last node (its next pointer = NULL).

ASCII Visualization:
---------------------
Head → [1 | 111] → [2 | 222] → [4 | 333] → [5 | NULL]
Memory addresses (example):
Node1 @ 001 | Node2 @ 111 | Node3 @ 222 | Node4 @ 333

- When new node is created → allocated at **random location**.
- Linked list size = **dynamic** (no need to declare initially).

------------------------------------
Key Points (Interview Answers)
------------------------------------
Q1) Why are linked lists NOT contiguous?
A1) Because each node is allocated separately in heap memory 
    → no guarantee of continuous block availability.

Q2) How do we find an element in linked list?
A2) Must traverse from head → next → next until node is found.
    → Access Time = O(n).

Q3) Why use linked lists?
A3) 
  - Dynamic memory allocation (no fixed size)
  - Efficient insertion/deletion (O(1) if pointer to node known)
  - No memory wastage due to pre-allocation

Q4) Why arrays are faster for access?
A4) Arrays use index-based addressing (direct memory calculation),
    linked list requires traversal since memory addresses are random.

------------------------------------
Advantages of Linked List (Memory Perspective)
------------------------------------
1) No need to declare size at start.
2) Efficient memory utilization (allocate as required).
3) Insertion/Deletion is flexible (no shifting like arrays).

Disadvantages:
--------------
1) Extra memory for pointer in each node.
2) No direct access → must traverse nodes.
3) Cache-unfriendly due to non-contiguous memory allocation.

------------------------------------
Example:
--------
Want to access Node(3) = value '4':
- Must start from Head:
  Head → Node(1) → Node(2) → Node(3)
- Cannot compute address like array[index].

------------------------------------
Complexity Summary:
-------------------
Access Element : O(n)
Insert (known node) : O(1)
Delete (known node) : O(1)
Space : O(n) + pointer overhead

------------------------------------
ASCII Final Comparison:
-----------------------
ARRAY:            LINKED LIST:
[10][20][30]      [10|100] -> [20|200] -> [30|NULL]
Contiguous        Random allocation
Index-based       Pointer-based
"""
