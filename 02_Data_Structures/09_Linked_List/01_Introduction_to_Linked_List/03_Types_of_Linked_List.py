"""
====================================
      TYPES OF LINKED LISTS
====================================

Overview:
---------
Linked Lists are of 4 types:
1) Singly Linked List
2) Circular Singly Linked List
3) Doubly Linked List
4) Circular Doubly Linked List

------------------------------------
1) Singly Linked List
------------------------------------
Definition:
- Each node stores:
    - Data (value)
    - Reference to next node only
- Last node points to NULL

ASCII Representation:
----------------------
Head → [1|001] → [2|111] → [4|222] → [5|333] → NULL

Advantages:
-----------
1) Simple structure, easy to implement
2) Dynamic size allocation (memory efficient for unknown sizes)
3) Easy insertion/deletion at any position (O(1) if node reference known)

Disadvantages:
--------------
1) No backward traversal
2) Cannot directly access elements by index (O(n) search)
3) Extra memory for pointer (compared to arrays)

Use Cases:
----------
- Stack/Queue implementation
- Basic dynamic data structure

------------------------------------
2) Circular Singly Linked List
------------------------------------
Definition:
- Same as Singly Linked List, but **last node points to first node**
- Forms a circular connection

ASCII Representation:
----------------------
Head → [1|001] → [2|111] → [4|222] → [5|333] ┐
       └─────────────────────────────────────┘

Advantages:
-----------
1) Continuous traversal from last node to first node
2) Efficient for applications that require cycling (e.g., round-robin)

Disadvantages:
--------------
1) Slightly more complex to implement than singly list
2) Infinite loop risk if traversal conditions are not handled carefully

Use Cases:
----------
- Multiplayer games turn management
- Circular buffer

Example:
--------
4-player chess game turns:
Player1 → Player2 → Player3 → Player4 → Player1 (cycle repeats)

------------------------------------
3) Doubly Linked List
------------------------------------
Definition:
- Each node has two references:
    - Previous node
    - Next node
- Traversal possible in both directions

ASCII Representation:
----------------------
NULL ← [S1|001] ↔ [S2|111] ↔ [S3|222] ↔ [S4|333] → NULL

Advantages:
-----------
1) Can traverse forward and backward
2) Easier to delete a given node if pointer to node is known (O(1))
3) No need to traverse from head to find previous node

Disadvantages:
--------------
1) Extra memory for previous pointer
2) More complex node insertion/deletion logic than singly list

Use Cases:
----------
- Music playlist navigation (Next/Previous)
- Undo/Redo operations

Example:
--------
Music Player:
NULL ← Song1 ↔ Song2 ↔ Song3 ↔ Song4 → NULL

------------------------------------
4) Circular Doubly Linked List
------------------------------------
Definition:
- Doubly linked list where:
    - First node's prev points to last node
    - Last node's next points to first node
- Forms a circular connection with bidirectional traversal

ASCII Representation:
----------------------
[APP1|001] ⇆ [APP2|111] ⇆ [APP3|222] ⇆ [APP4|333]
   ↑--------------------------------------------↓

Advantages:
-----------
1) Traverse endlessly in both directions
2) Efficient insertion/deletion at both ends
3) Good for applications needing continuous forward & backward looping

Disadvantages:
--------------
1) Highest memory usage (two pointers + circular links)
2) Complex implementation

Use Cases:
----------
- Application switchers (Mac Cmd+Shift+Tab)
- Continuous image/video carousel

Example:
--------
Cmd+Shift+Tab (Mac):
APP1 ⇆ APP2 ⇆ APP3 ⇆ APP4 (loops infinitely)

------------------------------------
Quick Comparison Table
------------------------------------
| Type                    | Next Ptr | Prev Ptr | Circular | Traversal |
|-------------------------|----------|----------|----------|-----------|
| Singly Linked List      | Yes      | No       | No       | Forward   |
| Circular Singly Linked  | Yes      | No       | Yes      | Forward   |
| Doubly Linked List      | Yes      | Yes      | No       | Both ways |
| Circular Doubly Linked  | Yes      | Yes      | Yes      | Both ways |

------------------------------------
Complexity Summary:
------------------------------------
Traversal: O(n) for all
Insertion (known node): O(1)
Deletion (known node): O(1)
"""
