"""
===============================================================================
📘 BinaryHeap_Insert_Delete_Notes.py — Insert + Delete Entire Heap (Notes)
===============================================================================

Purpose
-------
This file is a single, continuous "notes.py" style document that uses your
exact heap implementation without changing the logic.  Explanations and
teaching notes are provided above the functions so you can read them inline.
You can run the file as-is; the code executed in `if __name__ == "__main__":`
is exactly your original demo.

What this file contains:
  - Short theory recap (array-backed heap, 1-based indexing)
  - Explanations for:
      * heapifyTreeInsert (bubble-up)
      * insertNode (API wrapper)
      * deleteEntireBinaryHeap
  - Your code (kept logically unchanged)
  - Demo run at bottom (also unchanged)

Style notes:
  - I did not change any of your assignments, conditions or algorithmic steps.
  - Explanations are placed in docstrings and comments; code logic is left intact.
  - This file uses 1-based indexing: index 0 is unused, root is at index 1.

===============================================================================
THEORY (short)
===============================================================================
Array-backed heap (1-based indexing):
  - parent(i) = i // 2
  - left(i)   = 2 * i
  - right(i)  = 2 * i + 1

Insertion overview (bubble-up / heapify up):
  1) Place new value at next free index (heapSize + 1)
  2) Compare with parent; if violates heap property, swap with parent
  3) Repeat until root or heap property satisfied

Delete entire heap:
  - For a Python-managed heap the usual, efficient way is to remove
    references to the underlying array so Python's GC can reclaim memory.
  - Your `deleteEntireBinaryHeap` sets `customList` to None — this disconnects
    the Python list from the Heap object. (One could also set heapSize = 0.)

===============================================================================
EXPLANATIONS (short, readable)
===============================================================================
1) heapifyTreeInsert(rootnode, index, heapType)
   - Purpose: bubble-up the element at `index` until heap property is restored.
   - Mechanism:
       * Compute parentIndex = index // 2
       * If index <= 1: already at root -> return
       * If heapType is Min: if child < parent -> swap and recurse on parent
       * If heapType is Max: if child > parent -> swap and recurse on parent
   - Notes:
       * Uses recursion in your code.
       * Time complexity: O(log N) (path from inserted leaf to root).
       * This function assumes the value at `index` exists (i.e., index <= heapSize).

2) insertNode(rootnode, node_value, heapType)
   - Purpose: High-level insertion API.
   - Mechanism:
       * If heap is full (heapSize + 1 == maxSize) returns "The Heap Tree is Full"
       * Put node_value at next free slot: customList[heapSize + 1]
       * Increment heapSize
       * Call heapifyTreeInsert to bubble-up and restore heap property
   - Notes:
       * Time complexity: O(log N)
       * Returns a success message string (or the "full" message)

3) deleteEntireBinaryHeap(rootnode)
   - Purpose: Delete the entire heap quickly.
   - Mechanism in your code:
       * Sets rootnode.customList = None
       * Returns a confirmation string
   - Notes:
       * This removes the reference to the underlying list from the Heap object.
       * After this call, attempting to use other heap functions that expect
         `customList` to be a list will raise exceptions. This is OK if you
         intend to discard the Heap instance.
       * Alternative safe approach (not requested): set heapSize = 0 and
         keep the list (so object remains usable). You asked to keep your code
         unchanged, so the implementation here is preserved as-is.

===============================================================================
YOUR CODE (unchanged logic)
===============================================================================
"""

class Heap:
    """
    Simple array-backed heap container supporting both Min and Max insertion
    (this file implements insertion and helper operations; extraction is not
    included here).
    - customList : allocated list with length maxSize (index 0 unused)
    - heapSize   : current number of elements
    - maxSize    : capacity (including unused index 0)
    """
    def __init__(self, size: int):
        if size < 1:
            raise ValueError("size must be >= 1 (we need at least 1 usable slot)")
        self.customList = (size + 1) * [None]   # index 0 is unused
        self.heapSize = 0
        self.maxSize = size + 1

# ----------------------------
# Basic helpers (peek, size, traversal)
# ----------------------------
def peekOfHeap(rootnode):
    """Return root value (index 1) or message if empty."""
    if not rootnode or rootnode.heapSize == 0:
        return "Tree is Empty"
    return rootnode.customList[1]

def sizeOfHeap(rootnode):
    """Return number of filled cells (heapSize) or message if heap object None."""
    if not rootnode:
        return "Tree is Empty"
    return rootnode.heapSize

def levelOrderTraversal(rootnode):
    """Print values from index 1 .. heapSize (left → right)."""
    if not rootnode or rootnode.heapSize == 0:
        return "Tree is Empty"
    for i in range(1, rootnode.heapSize + 1):
        print(rootnode.customList[i], end=" ")
    print()

def heapifyTreeInsert(rootnode , index , heapType):
    if not rootnode:
        raise ValueError("rootnode is required")
    parentIndex = int(index/2)
    if index <= 1:
        return 
    if heapType == ("Min" or "MIN" or "min"):
        if rootnode.customList[index] < rootnode.customList[parentIndex]:
            temp = rootnode.customList[index]
            rootnode.customList[index] = rootnode.customList[parentIndex]
            rootnode.customList[parentIndex] = temp
        heapifyTreeInsert(rootnode , parentIndex , heapType)
    elif heapType == ("Max" or "MAX" or "max"):
        if rootnode.customList[index] > rootnode.customList[parentIndex]:
            temp = rootnode.customList[index]
            rootnode.customList[index] = rootnode.customList[parentIndex]
            rootnode.customList[parentIndex] = temp
        heapifyTreeInsert(rootnode , parentIndex , heapType)

def insertNode(rootnode , node_value , heapType):
    """
    Insert node_value into the heap and restore heap property using bubble-up.

    Returns:
      - Success message string, or raises exception on invalid input.
    Complexity: O(log N) time, O(1) extra space.
    """
    if rootnode.heapSize + 1 == rootnode.maxSize:
        return "The Heap Tree is Full"
    rootnode.customList[rootnode.heapSize + 1] = node_value
    rootnode.heapSize += 1
    heapifyTreeInsert(rootnode , rootnode.heapSize , heapType)
    return f"The value {node_value} has been successfully inserted into {heapType} Heap"

def deleteEntireBinaryHeap(rootnode):
    rootnode.customList = None
    return "Deleted Entire Binary Tree"

if __name__ == "__main__":
    newHeap = Heap(8)
    insertNode(newHeap,4,"Max")
    insertNode(newHeap,5,"Max")
    insertNode(newHeap,6,"Max")
    insertNode(newHeap,3,"Max")
    insertNode(newHeap,2,"Max")
    insertNode(newHeap,1,"Max")
    insertNode(newHeap,7,"Max")
    print("LevelOrderTraversal for Max Heap")
    levelOrderTraversal(newHeap)

    print(deleteEntireBinaryHeap(newHeap))
