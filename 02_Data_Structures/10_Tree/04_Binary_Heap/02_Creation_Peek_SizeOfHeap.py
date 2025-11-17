"""
===============================================================================
📘 BinaryHeap_CommonOps_Notes.py — Notes + Array-based Implementation (Min Heap)
===============================================================================

Purpose
-------
This file documents common operations on a **Binary Heap** (array/list
implementation) and provides a small, runnable Python example.

What this file contains:
  - A compact, continuous lecture-style explanation of:
      * how a heap is stored in an array
      * why index-1 root simplifies formulas
      * common operations (create, peek, size, level-order traversal)
      * time & space complexity for each operation
  - A minimal `Heap` class and helper functions that match the lecture
    (creation, peek, size, level-order traversal)
  - Example usage showing how to create and inspect a heap

Style notes:
  - This is array-based heap (no pointer/tree nodes).
  - We reserve index 0 (unused) so parent/child formulas become:
        left  = 2 * i
        right = 2 * i + 1
        parent= i // 2
    where i is the 1-based index of a node in the underlying list.
===============================================================================

INTRO — how a heap is stored in memory (array/list)
---------------------------------------------------
Because a Binary Heap is a *complete binary tree*, it maps naturally to an
array/list. If we reserve index 0 (unused) and start the root at index 1:

    index:  0   1   2   3   4   5   6   7
    array: [X,  5, 10, 20, 30, 40, 50, 60]

Mapping rules (1-based):
    left_child_index  = 2 * i
    right_child_index = 2 * i + 1
    parent_index      = i // 2

Example tree (min-heap):

               5            <- index 1
             /   \
           10     20       <- indices 2,3
          /  \    / \
        30  40  50 60     <- indices 4,5,6,7

We keep a `heapSize` that tracks how many cells are filled (excluding index 0).

-------------------------------------------------------------------------------
COMMON OPERATIONS (this lecture)
-------------------------------------------------------------------------------
Operations covered in this file:
  1) Create Heap (array/list)
  2) Peek (return root)
  3) Size (number of filled cells)
  4) Level-order traversal (print all filled cells left→right)
  5) Complexity summary

-------------------------------------------------------------------------------
Complexities (summary)
-------------------------------------------------------------------------------
Create Heap:
  Time:  O(1)      (initialization constants)
  Space: O(N)      (allocates list of size N+1)

Peek (get root):
  Time:  O(1)
  Space: O(1)

Size:
  Time:  O(1)
  Space: O(1)

Level-order traversal:
  Time:  O(n)      (visits each filled cell once)
  Space: O(1)      (we only use loop variables; no extra DS)

Note: Insertion & extract-min/extract-max are covered in other lectures.
They are O(log N) time (because they percolate up/down) and O(1) extra memory.

===============================================================================
IMPLEMENTATION (array-based min-heap helpers)
===============================================================================
The example below implements the simple features discussed:
 - class Heap(size)        : create array (size+1) with zero heapSize
 - peekOfHeap(rootnode)    : return value at index 1 (root) or a message
 - sizeOfHeap(rootnode)    : return number of filled slots (heapSize)
 - levelOrderTraversal(rootnode) : print elements from index 1..heapSize

This is intentionally minimal teaching code (no insert/extract yet).
===============================================================================
"""

from typing import Optional

class Heap:
    """
    Simple array-backed heap container (min-heap oriented; no insert/extract here).
    We reserve index 0 (unused) so index arithmetic is simpler:
      left = 2 * i, right = 2 * i + 1, parent = i // 2
    Attributes:
      - customList : list with length = maxSize (size+1 when created)
      - heapSize   : number of filled cells (starts at 0)
      - maxSize    : total allocated cells in customList (includes index 0)
    """
    def __init__(self, size: int):
        # allocate array of (size + 1) and reserve index 0 (unused)
        self.customList = (size + 1) * [None]   # index 0 will remain unused
        self.heapSize = 0                       # number of filled nodes
        self.maxSize = size + 1                 # capacity including unused 0 index

    # small utility to show the internal array (for debugging/demonstration)
    def _debug_array(self) -> str:
        """Return short string showing indices and filled values (for teaching)."""
        # show indices and values up to maxSize-1
        indices = " ".join(f"{i:>3}" for i in range(self.maxSize))
        values = " ".join(f"{str(v) if v is not None else ' _':>3}" for v in self.customList)
        return f"Indices: {indices}\nValues : {values}"

def peekOfHeap(rootnode: Optional[Heap]):
    """
    Return the heap root (min value for min-heap) located at customList[1].
    Behaviour:
      - If heap object is None or heapSize == 0 -> return "Tree is Empty"
      - Otherwise return the value at index 1
    Complexity: O(1) time, O(1) space
    """
    if not rootnode or rootnode.heapSize == 0:
        return "Tree is Empty"
    return rootnode.customList[1]

def sizeOfHeap(rootnode: Optional[Heap]):
    """
    Return number of filled cells (heapSize).
    Complexity: O(1) time, O(1) space
    """
    if not rootnode:
        return "Tree is Empty"
    return rootnode.heapSize

def levelOrderTraversal(rootnode: Optional[Heap]):
    """
    Print heap elements in level-order (left → right) using the array indices.
    We iterate from 1..heapSize (index 0 is unused).
    Complexity: O(n) time (n = heapSize), O(1) additional space.
    """
    if not rootnode or rootnode.heapSize == 0:
        print("Tree is Empty")
        return

    for i in range(1, rootnode.heapSize + 1):
        print(rootnode.customList[i], end=" ")
    print()  # newline after printing all elements

# -----------------------------------------------------------------------------
# Example usage & demonstration (runnable)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Create a heap with capacity for 7 elements (we allocate size+1 internally)
    newBinaryHeap = Heap(7)

    # For demonstration only: manually fill the internal array (teaching code)
    # Normally you'd call an insert() method that percolates up; insert not included here.
    # We fill customList[1..7] with values matching the lecture example.
    demo_values = [5, 10, 20, 30, 40, 50, 60]  # 7 filled nodes
    if len(demo_values) > (newBinaryHeap.maxSize - 1):
        raise ValueError("Too many demo values for the heap capacity")

    # place demo values into heap array and update heapSize
    for idx, val in enumerate(demo_values, start=1):
        newBinaryHeap.customList[idx] = val
    newBinaryHeap.heapSize = len(demo_values)

    # show debug representation (indices + values)
    print("DEBUG: internal array representation")
    print(newBinaryHeap._debug_array())
    print()

    # 1) Size of heap
    print("Size of heap:", sizeOfHeap(newBinaryHeap))   # expected 7

    # 2) Peek root (min element for min-heap)
    print("Peek (root) of heap:", peekOfHeap(newBinaryHeap))  # expected 5

    # 3) Level-order traversal (prints values left→right)
    print("Level-order traversal of heap:")
    levelOrderTraversal(newBinaryHeap)  # expected: 5 10 20 30 40 50 60

    # Example: empty heap behavior
    emptyHeap = Heap(3)
    print("\nEmpty heap peek:", peekOfHeap(emptyHeap))      # "Tree is Empty"
    print("Empty heap level-order:")
    levelOrderTraversal(emptyHeap)                         # prints "Tree is Empty"

"""
===============================================================================
END — BinaryHeap_CommonOps_Notes.py
===============================================================================
"""
