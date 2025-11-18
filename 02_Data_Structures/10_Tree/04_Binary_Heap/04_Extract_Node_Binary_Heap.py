"""
===============================================================================
📘 BinaryHeap_Extract_Notes.py — Extract Node from Binary Heap (Min / Max Heap)
===============================================================================

Purpose
-------
This file explains **how extraction works in a Binary Heap**, using your own
(original) code unchanged.

This note contains:
  ✔ High-level idea of extraction  
  ✔ ASCII diagrams based on your images  
  ✔ Deep explanation of heapifyTreeExtract()  
  ✔ Explanation of extractNode()  
  ✔ Your exact code (NO CHANGES)  
  ✔ Example run included at bottom  

Style / convention
------------------
- This uses 1-based indexing for the heap array. Index 0 is unused.
- Left child of i is 2*i, right child is 2*i + 1, parent is i // 2.

-------------------------------------------------------------------------------
🌳 What is Extraction?
-------------------------------------------------------------------------------
Extraction ALWAYS removes the **root** of the heap:

For Min-Heap → removes the **minimum**  
For Max-Heap → removes the **maximum**

Because root must always contain:
  - Minimum (Min-Heap)
  - Maximum (Max-Heap)

But after removal, heap property breaks.

So extraction has 3 fixed steps:

1️⃣ **Store the root (the answer)**  
2️⃣ **Move the last node → root position**  
3️⃣ **heapify-down (heapifyTreeExtract)**  
      → Compare root with its children  
      → Swap with correct child (min/max)  
      → Continue down until property restored  

-------------------------------------------------------------------------------
📌 IMPORTANT (1-based indexing)
-------------------------------------------------------------------------------
Your heap uses:
    Index 1 = root  
    Index 2 = root.left  
    Index 3 = root.right  
    ...

Index 0 is unused.

-------------------------------------------------------------------------------
📘 EXTRACTION VISUAL (based on your screenshots)
-------------------------------------------------------------------------------

Initial Min-Heap:

                5
              /    \
            10      20
           / \      / \
         30  40   50  60
        /
      80

Array (1-based):
    X  5  10  20  30  40  50  60  80
    0  1   2   3   4   5   6   7   8

Step 1: Remove 5  
Step 2: Move LAST node (80) to ROOT

                80
              /    \
            10      20
           / \      / \
         30  40   50  60

Array:
    X  80  10  20  30  40  50  60

Step 3: Heapify DOWN (swap with smallest child each time)

                10             ← 10 < 80
              /     \
           80        20

                10
              /     \
            30       20     ← next smallest child = 20
           / \      /  \
         80  40   50   60

DONE.

-------------------------------------------------------------------------------
📘 Why heapifyTreeExtract works?
-------------------------------------------------------------------------------
Because it always performs:

1️⃣ Check if left child exists  
2️⃣ If only left exists → swap if needed  
3️⃣ If both exist:
      - choose correct child (min or max)
      - compare parent with chosen child
      - swap if heap property violated
4️⃣ Recursively push the node DOWN

This is exactly how a Heap should fix itself after extraction.

-------------------------------------------------------------------------------
Now the actual CODE (Your Code — unmodified!)
-------------------------------------------------------------------------------
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
def peekOfHeap(rootnode: Optional[Heap]):
    """Return root value (index 1) or message if empty."""
    if not rootnode or rootnode.heapSize == 0:
        return "Tree is Empty"
    return rootnode.customList[1]

def sizeOfHeap(rootnode: Optional[Heap]):
    """Return number of filled cells (heapSize) or message if heap object None."""
    if not rootnode:
        return "Tree is Empty"
    return rootnode.heapSize

def levelOrderTraversal(rootnode: Optional[Heap]):
    """Print values from index 1 .. heapSize (left → right)."""
    if not rootnode or rootnode.heapSize == 0:
        print("Tree is Empty")
        return
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


"""
===============================================================================
📘 heapifyTreeExtract(rootnode, index, heapType)
===============================================================================

This is the MOST IMPORTANT part of extraction.

Its purpose:
------------
    Move the misplaced node DOWN until the heap property is restored.

How it works:
-------------
1️⃣ Compute left and right child indices  
2️⃣ If NO children → stop  
3️⃣ If ONLY left child exists:
        Compare parent ↔ left  
        Swap if needed  
4️⃣ If BOTH children exist:
        For Min-Heap → choose smaller child
        For Max-Heap → choose larger child
        Compare parent ↔ chosen child
        Swap if needed  
5️⃣ Recursively continue down

Time Complexity: O(log N)
Space Complexity: O(log N) due to recursion

ASCII EXAMPLE:
--------------
For Min-Heap extract:

             80
           /    \
         10      20
        / \      
      30  40     

heapifyTreeExtract moves 80 → down → down → down
until heap property restored.
===============================================================================
"""
def heapifyTreeExtract(rootnode , index , heapType):
    leftIndex = index * 2
    rightIndex = (index * 2) + 1
    swapchild = 0

    # No children → STOP
    if rootnode.heapSize < leftIndex:
        return 
    
    # ONLY left child exists
    elif rootnode.heapSize == leftIndex:
        if heapType == ("Min" or " MIN" or "min"):
            if rootnode.customList[index] > rootnode.customList[leftIndex]:
                temp = rootnode.customList[index]
                rootnode.customList[index] = rootnode.customList[leftIndex]
                rootnode.customList[leftIndex] = temp
            return
        else: 
            if rootnode.customList[index] < rootnode.customList[leftIndex]:
                temp = rootnode.customList[index]
                rootnode.customList[index] = rootnode.customList[leftIndex]
                rootnode.customList[leftIndex] = temp
            return 
    
    # BOTH children exist
    else:
        if heapType == ("Min" or "MIN" or "min"):
            # choose smaller child
            if rootnode.customList[leftIndex] < rootnode.customList[rightIndex]:
                swapchild = leftIndex
            else:
                swapchild = rightIndex

            if rootnode.customList[index] > rootnode.customList[swapchild]:
                temp = rootnode.customList[index]
                rootnode.customList[index] = rootnode.customList[swapchild]
                rootnode.customList[swapchild] = temp

        else: 
            # choose larger child
            if rootnode.customList[leftIndex] > rootnode.customList[rightIndex]:
                swapchild = leftIndex
            else:
                swapchild = rightIndex

            if rootnode.customList[index] < rootnode.customList[swapchild]:
                temp = rootnode.customList[index]
                rootnode.customList[index] = rootnode.customList[swapchild]
                rootnode.customList[swapchild] = temp

    # continue heapifying down
    heapifyTreeExtract(rootnode , swapchild , heapType)


"""
===============================================================================
📘 extractNode(rootnode, heapType)
===============================================================================

Extraction steps:
-----------------
1️⃣ Save ROOT value (this is output)  
2️⃣ Move LAST element → ROOT  
3️⃣ Remove last element  
4️⃣ heapifyTreeExtract(root, 1, heapType)

This ensures:
  ✔ heap structure maintained  
  ✔ heap order restored  

Time Complexity:  O(log N)
Space Complexity: O(log N) (recursion)
===============================================================================
"""
def extractNode(rootnode , heapType):
    if rootnode.heapSize == 0:
        return 
    else:
        extractNode = rootnode.customList[1]     # Step 1: remove root
        rootnode.customList[1] = rootnode.customList[rootnode.heapSize]  # Step 2
        rootnode.customList[rootnode.heapSize] = None                    # Step 3
        rootnode.heapSize -= 1
        heapifyTreeExtract(rootnode , 1 , heapType)                      # Step 4
        return extractNode
                

# -----------------------------
# DEMO
# -----------------------------
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

    print("Extracted Node: " ,extractNode(newHeap ,"Max"))
    levelOrderTraversal(newHeap)



"""
===============================================================================
SHORT EXPLANATIONS (as requested — small sentences)
===============================================================================

heapifyTreeExtract:
- Purpose (one sentence): Heapify-down (percolate down) from the given index:
  pick the appropriate child (min-child for Min-heap or max-child for Max-heap),
  swap if the parent violates the heap property, then recurse into the swapped
  child until the subtree satisfies the heap property.
- Effect: restores the heap property after the root (or any internal node) has
  been replaced by a lower-level node (i.e., after extract or a swap).

extractNode:
- Purpose (one sentence): Remove and return the root: replace root with the
  last element, reduce heapSize, and call heapify-down (heapifyTreeExtract)
  from index 1 to restore the heap invariant.
- Effect: returns the extracted root value and keeps the heap valid in O(log N).

===============================================================================
Complexity (short)
- extractNode: O(log N) time (heapify-down along root→leaf path), O(1) extra
  space for variables; recursion in heapifyTreeExtract uses O(log N) call-stack.
- heapifyTreeExtract: O(log N) time worst-case, recursion depth ≤ heap height.

===============================================================================
End of BinaryHeap_ExtractNode_Notes.py
===============================================================================
"""