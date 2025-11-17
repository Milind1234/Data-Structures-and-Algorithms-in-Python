"""
===============================================================================
📘 BinaryHeap_Notes.py — Complete Notes on Binary Heap (Min Heap & Max Heap)
===============================================================================

Purpose
-------
This note explains Binary Heap in a clean and structured way, suitable for you. It covers:

  - What is a Binary Heap?
  - Why we need a Binary Heap
  - Properties of Binary Heap
  - Types of Heap (Min Heap and Max Heap)
  - Why Binary Heap is ideal for array implementation
  - Summary of time complexities
  - Real-world uses (Priority Queue, Heap Sort, Prim’s, Dijkstra)

===============================================================================
1️⃣ What is a Binary Heap?
===============================================================================

A Binary Heap is a Binary Tree with two special properties:

1) Heap Property:
   A heap is either:
     - Min Heap → parent ≤ children
     - Max Heap → parent ≥ children
   This must be true for **every node**, recursively.

2) Complete Tree Property:
   - All levels must be completely filled,
   - Except possibly the last level,
   - And the last level must be filled **from left to right**.

-------------------------------------------------------------------------------

Example of a Binary Heap (Min Heap):

                 5
               /   \
             10     20
            / \     / \
          30  40  50  60
         / \
       70  80

- All levels except last are full.
- Last level is filled from left side.
- Parent values are less than their children → Min Heap.

-------------------------------------------------------------------------------

===============================================================================
2️⃣ Why do we need a Binary Heap?
===============================================================================

We want a data structure where:

✔ Finding minimum/maximum takes O(1)  
✔ Inserting new numbers takes O(log N)  
✔ Extracting min/max takes O(log N)

Let’s analyze possible solutions:

-------------------------------------------------------------------------------

❌ Option 1: Sorted Array

Example:
    [10, 20, 30, 40, 50]

Find minimum → O(1)  
Insert new number at the front → O(n) (shift all elements)

Fails the requirement → NOT acceptable.

-------------------------------------------------------------------------------

❌ Option 2: Sorted Linked List

Example:
    Head → 1 → 2 → 3 → null

To insert 4, you must traverse → O(n)

Fails the requirement → NOT acceptable.

-------------------------------------------------------------------------------

✅ The Best Option: Binary Heap

Binary Heap guarantees:

Operation                   | Time
--------------------------- | ------------
Find min/max                | O(1)
Insert node                 | O(log N)
Extract min/max             | O(log N)

This is why Binary Heaps are used in:

- Priority Queue
- Heap Sort
- Prim’s Algorithm
- Dijkstra’s Algorithm

Binary Heap is the core of all these problems.

-------------------------------------------------------------------------------

===============================================================================
3️⃣ Properties of Binary Heap
===============================================================================

There are two essential properties:

-------------------------------------------------------------------------------
(A) Heap Property

1) Min Heap  
   parent ≤ children  

   Example:

                5
               / \
             10   20

   (valid min heap)

2) Max Heap  
   parent ≥ children  

   Example:

                80
               /  \
             70    60

   (valid max heap)

-------------------------------------------------------------------------------
(B) Complete Tree Property

A complete tree must be filled like this:

Level 0 → 1 node  
Level 1 → 2 nodes  
Level 2 → 4 nodes  
Level 3 → fill from left to right

Example:

                5
              /   \
            10     20
           / \     /
         30  40  50

This structure makes heap ideal for array representation.

-------------------------------------------------------------------------------

===============================================================================
4️⃣ Types of Binary Heap
===============================================================================

There are two types: **Min Heap** and **Max Heap**

-------------------------------------------------------------------------------
⭐ Min Heap

Rule:  
    parent ≤ children

Example:

                 5
               /   \
             10     20
            / \     / \
          30  40  50  60
         / \
       70  80

-------------------------------------------------------------------------------
⭐ Max Heap

Rule:  
    parent ≥ children

Example:

                 80
               /     \
             70       60
            / \      /  \
          50  40   30   20
         / \
        5  10

-------------------------------------------------------------------------------

===============================================================================
5️⃣ Why Binary Heap Works Well With Arrays?
===============================================================================

Because it is a complete binary tree, we can calculate relationships using indices:

If a node is at index *i*:

- Left child index  = 2*i + 1
- Right child index = 2*i + 2
- Parent index      = (i - 1) // 2

No pointers needed → saves memory and is fast.

-------------------------------------------------------------------------------

===============================================================================
6️⃣ Real-World Uses of Binary Heap
===============================================================================

Binary Heaps are used in:

- Priority Queue (most important application)
- Dijkstra’s Algorithm (graph shortest paths)
- Prim’s Algorithm (minimum spanning tree)
- Heap Sort
- Task Scheduling
- Event-driven simulations

-------------------------------------------------------------------------------

===============================================================================
7️⃣ Summary Table of Time Complexities
===============================================================================

Operation                     | Time Complexity
----------------------------- | --------------------
Get Min/Max (root)            | O(1)
Insert Node                   | O(log N)
Extract Min/Max               | O(log N)
Search (not typical)          | O(N)
Build Heap (heapify array)    | O(N)
Space Complexity              | O(N)

-------------------------------------------------------------------------------

🎯 Final Thoughts
----------------
- Binary Heap is a complete binary tree with a special ordering.
- Min Heap is useful for priority-based tasks.
- Max Heap is useful when the maximum must be accessed fast.
- It is faster than sorted arrays and linked lists for insert/extract operations.
- It is heavily used in advanced algorithms and data structures.

In the next Note, we will study:
**Insertion and Extraction operations in Binary Heap**.

===============================================================================
"""
