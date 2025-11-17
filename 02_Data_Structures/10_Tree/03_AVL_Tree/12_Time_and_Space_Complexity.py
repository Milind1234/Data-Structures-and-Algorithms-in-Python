"""
===============================================================================
📘 AVL_Complexity_Notes.py — Time & Space Complexity of AVL Trees
===============================================================================

Purpose
-------
This note summarizes the time and space complexities of every major AVL Tree
operation, explains why each complexity holds, and compares AVL Trees with
Binary Search Trees (BST) in worst-case scenarios.

AVL Trees remain height-balanced (height = O(log N)), so almost every operation
benefits from logarithmic performance even in the worst case.

This file covers:
  - Creating an AVL Tree
  - Inserting a node (with rotations)
  - Traversing an AVL Tree
  - Searching for a node
  - Deleting a node (with rotations)
  - Deleting the entire tree
  - AVL vs. Binary Search Tree (worst-case comparison)

===============================================================================
1️⃣ Creating an AVL Tree
===============================================================================

Time Complexity: **O(1)**
Reason: Only one root node is created.

Space Complexity: **O(1)**
Reason: Only one node is allocated.

-------------------------------------------------------------------------------

===============================================================================
2️⃣ Insert a Node into AVL Tree
===============================================================================

Time Complexity: **O(log N)**
Reason:
- AVL tree is always height-balanced.
- Searching the correct position takes O(log N).
- At most one rotation (LL/LR/RR/RL) is applied.
- Rotations take **O(1)** time.

Space Complexity: **O(log N)**
Reason:
- Insertion uses recursion.
- Recursion stack depth = tree height = O(log N).

-------------------------------------------------------------------------------

===============================================================================
3️⃣ Traversing an AVL Tree (Inorder / Preorder / Postorder / Level-order)
===============================================================================

Time Complexity: **O(N)**
Reason:
- Every node must be visited exactly once.

Space Complexity:
- **O(N)** for DFS recursive traversals
- **O(N)** for BFS level-order traversal

Reason:
- DFS recursion stack may store multiple nodes.
- BFS queue may store nodes of the largest level.

-------------------------------------------------------------------------------

===============================================================================
4️⃣ Searching for a Node in AVL Tree
===============================================================================

Time Complexity: **O(log N)**
Reason:
- AVL height = O(log N)
- Each step moves left or right.

Space Complexity: **O(log N)**
Reason:
- Recursive search goes through tree levels.

-------------------------------------------------------------------------------

===============================================================================
5️⃣ Deleting a Node from AVL Tree
===============================================================================

Time Complexity: **O(log N)**
Reason:
- BST-style search takes O(log N)
- Node deletion (leaf / one-child / two-child) takes O(1)
- Rebalancing may require rotations (O(1))
- Total remains O(log N)

Space Complexity: **O(log N)**
Reason:
- Recursive deletion depth equals tree height.

-------------------------------------------------------------------------------

===============================================================================
6️⃣ Deleting Entire AVL Tree
===============================================================================

Two approaches exist:

✔ Recommended approach (Pythonic):
    root = None  
    → Allows garbage collector to reclaim all nodes  
    → **O(1)** time, **O(1)** space

✔ Original approach:
    root.data = None  
    root.leftchild = None  
    root.rightchild = None  
    → Leaves a dummy node, but child nodes become unreachable.

Time Complexity: **O(1)**  
Space Complexity: **O(1)**

-------------------------------------------------------------------------------

===============================================================================
7️⃣ AVL Tree vs Binary Search Tree — Worst-Case Comparison
===============================================================================

Operation               | BST Worst Case     | AVL Worst Case
----------------------- | ------------------ | ---------------
Create Tree             | O(1)               | O(1)
Insert Node             | **O(N)** (skewed)  | **O(log N)**
Search Node             | **O(N)** (skewed)  | **O(log N)**
Delete Node             | **O(N)** (skewed)  | **O(log N)**
Traverse Tree           | O(N)               | O(N)
Delete Entire Tree      | O(1)               | O(1)

### Why AVL outperforms BST in many cases?

A Binary Search Tree (BST) **can become skewed** (worst case):

    1
     \
      2
       \
        3
         \
          4

This degenerates into a **linked list**, giving **O(N)** time for:
- search
- insert
- delete

But an AVL Tree **never allows skewing**, because after each insertion/deletion,
it performs rotations to maintain height = **O(log N)**.

Thus AVL performance:
- Searching: **O(log N)**
- Insertion: **O(log N)**
- Deletion: **O(log N)**

AVL trees guarantee balanced performance at all times.

-------------------------------------------------------------------------------

===============================================================================
8️⃣ Summary Table (All AVL Operations)
===============================================================================

Operation                  | Time Complexity     | Space Complexity
-------------------------- | ------------------- | ----------------
Create AVL Tree            | O(1)                | O(1)
Insert Node                | O(log N)            | O(log N)
Traverse Tree              | O(N)                | O(N)
Search Node                | O(log N)            | O(log N)
Delete Node                | O(log N)            | O(log N)
Delete Entire Tree         | O(1)                | O(1)

-------------------------------------------------------------------------------

🎯 Final Thoughts
---------------
- AVL Trees guarantee logarithmic efficiency through strict balancing.
- They fix worst-case BST performance issues.
- They deliver reliable search times and consistent performance.
- Although they perform more rotations, the benefits outweigh the cost.

With this, you've completed the entire AVL Tree module.
Next section: **Binary Heaps** — let's continue!

===============================================================================
"""
