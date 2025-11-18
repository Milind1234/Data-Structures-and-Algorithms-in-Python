r"""
===============================================================================
📘 BinaryHeap_InsertNode_Notes.py — Insert node into Binary Heap (Min/Max)
===============================================================================

Purpose
-------
This file explains and demonstrates how to insert a node into an array-backed
Binary Heap (Min-Heap and Max-Heap). It contains:

  - A short theory and mapping reminders (array ↔ tree)
  - Step-by-step "bubble up" (percolate up) explanation with ASCII visuals
  - A compact, safe Heap class
  - heapifyTreeInsert() — "bubble up" implementation (works for Min & Max)
  - insertNode() — user-facing insertion API
  - Example runs for both Min and Max heaps (runnable)
  - Time / space complexity notes

Style
-----
- Array-backed heap uses 1-based indexing (index 0 unused) to simplify formulas:
      left  = 2 * i
      right = 2 * i + 1
      parent = i // 2
- For teaching clarity the docstring contains ASCII diagrams that show
  concrete numeric steps for insertion.

===============================================================================
Theory recap — array mapping (1-based)
===============================================================================
For node at index i:
    left_child_index  = 2 * i
    right_child_index = 2 * i + 1
    parent_index      = i // 2

We reserve index 0 unused. Root is at index 1.

Example array <-> tree:

Indices:   0   1   2   3   4   5   6   7
Array : [ X,  5, 10, 20, 30, 40, 50, 60 ]

Tree:
                 5 (index 1)
              /    \
          10 (2)   20 (3)
         /  \     /  \
    30(4) 40(5) 50(6) 60(7)

===============================================================================
Insertion algorithm (high level)
===============================================================================
1) If there is room, append new value at the next free array index:
       idx = heapSize + 1
       arr[idx] = value
       heapSize += 1

2) "Bubble up" (percolate up): while the new node violates the heap property
   with respect to its parent, swap it with the parent and continue from the
   parent index. Stop when either index == 1 (root) or heap property satisfied.

For Min-Heap: parent_value <= child_value  
For Max-Heap: parent_value >= child_value

This guarantees heap property and runs in O(log N) time.

-------------------------------------------------------------------------------
ASCII walkthrough (concrete example; Min-Heap)
-------------------------------------------------------------------------------
Start (before insert):
Array (1-based):
 index:  0  1  2  3  4  5  6  7
 values: X, 5,10,20,30,40,50,60

Tree:
                5
              /   \
            10     20
           / \     / \
         30 40   50  60

Insert value 1:
 Step A: place at next index 8
    array[8] = 1

Array now:
 index:  0  1  2  3  4  5  6  7  8
 values: X, 5,10,20,30,40,50,60, 1

 Tree (1 placed as left child of 30):
                    5
                  /   \
                10     20
               / \     / \
             30 40   50  60
            /
           1   <-- inserted

 Bubble-up steps (Min):

  - idx = 8 (value 1). parentIndex = 8 // 2 = 4 (value 30).
    1 < 30 → swap arr[8] and arr[4].

  After first swap:
    arr: X,5,10,20,1,40,50,60,30
    idx now = 4 (value 1). parentIndex = 4 // 2 = 2 (value 10).
    1 < 10 → swap arr[4] and arr[2].

  After second swap:
    arr: X,5,1,20,10,40,50,60,30
    idx now = 2 (value 1). parentIndex = 2 // 2 = 1 (value 5).
    1 < 5 → swap arr[2] and arr[1].

  After third swap:
    arr: X,1,5,20,10,40,50,60,30

  idx = 1 -> stop. Final heap root is 1 (valid Min-Heap).

Final Tree:
                1
              /   \
             5     20
           /  \    / \
         10  40  50 60
        /
      30

This is exactly the sequence illustrated in your notes.

-------------------------------------------------------------------------------
Complexity
-------------------------------------------------------------------------------
- Insertion time: O(log N) (bubble-up along path from leaf to root)
- Insertion space (extra): O(1) (in-place swaps)
- Create Heap: O(N) space to allocate array (we allocate capacity)
- Peek (root): O(1)
- Level-order traversal: O(N)

===============================================================================
Implementation (runnable)
===============================================================================
"""

from typing import Optional

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

    def _debug(self) -> str:
        """Return a compact representation of indices and values (for teaching)."""
        indices = " ".join(f"{i:>3}" for i in range(self.maxSize))
        values = " ".join(f"{str(v) if v is not None else ' _':>3}" for v in self.customList)
        return f"Indices: {indices}\nValues : {values}"

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

# ----------------------------
# Bubble-up (heapify after insert)
# ----------------------------
def heapifyTreeInsert(rootnode: Heap, index: int, heapType: str):
    """
    - rootnode: an instance of Heap (with `customList` and `heapSize`)
    - index: the 1-based index of the node we want to bubble up
    - heapType: string "Min" or "Max" that selects the comparison direction

    Step-by-step reading of code
    --------------------------------

    1) `parentIndex = int(index/2)`
       - Integer division gives the parent index using 1-based indexing.
       - Example: index=8 → parentIndex=4, index=5 → parentIndex=2.

    2) `if index <= 1: return`
       - If index is 1 (root) or an invalid small value, there's nothing to do.
       - This is the base case for the recursion.

    3) `if heapType == "Min":`
       - Use Min-Heap rule: parent <= children
       - Inside this branch:

        a) `if rootnode.customList[index] < rootnode.customList[parentIndex]:`
           - Compare child value with parent value.
           - If child < parent, heap property is violated (for Min-Heap), so swap.

        b) The swap block:
           ```
           temp = rootnode.customList[index]
           rootnode.customList[index] = rootnode.customList[parentIndex]
           rootnode.customList[parentIndex] = temp
           ```
           - Standard 3-line swap to move the smaller value up and larger value down.
           - After swap, the node moved to `parentIndex` may still violate the heap
             property with its new parent, so we must continue bubbling.

        c) `heapifyTreeInsert(rootnode, parentIndex , heapType)`
           - Recurse on parent index (the new position of the inserted value).
           - Recursion continues until the root or until no swap is needed.

    4) `elif heapType == "Max":`
       - Symmetric logic for Max-Heap:
         - If child > parent → swap, then recurse on parent.

    """
    if not rootnode:
        raise ValueError("rootnode is required")

    parentIndex = int(index/2)
    if index <= 1:
        return  # already at root or invalid index
    if heapType == "Min" : # Min heap
        # If child < parent, swap
        if rootnode.customList[index] < rootnode.customList[parentIndex]:
            temp = rootnode.customList[index]
            rootnode.customList[index] = rootnode.customList[parentIndex]
            rootnode.customList[parentIndex] = temp
        heapifyTreeInsert(rootnode, parentIndex , heapType)
    elif heapType == "Max": # Max heap
        # If child > parent, swap
        if rootnode.customList[index] > rootnode.customList[parentIndex]:
            temp = rootnode.customList[index]
            rootnode.customList[index] = rootnode.customList[parentIndex]
            rootnode.customList[parentIndex] = temp
        heapifyTreeInsert(rootnode , parentIndex , heapType)

# ----------------------------
# Insert node
# ----------------------------
def insertNode(rootnode: Heap, node_value, heapType: str = "Min"):
    """
    Insert node_value into the heap and restore heap property using bubble-up.

    Returns:
      - Success message string, or raises exception on invalid input.
    Complexity: O(log N) time, O(1) extra space.
    """
    if rootnode.heapSize + 1 == rootnode.maxSize:
        return " The Binary Tree is Full"
    # Place at next free position (heap is 1-based)
    rootnode.customList[rootnode.heapSize + 1] = node_value
    rootnode.heapSize += 1
    # Restore heap property by bubbling up
    heapifyTreeInsert(rootnode , rootnode.heapSize , heapType)
    return f"The value {node_value} has been successfully inserted into {heapType} Heap"

# ----------------------------
# Example demonstrations
# ----------------------------
if __name__ == "__main__":
    # Example 1: Insert into a Min Heap that matches your notes example.
    print("\n--- Demo: Min-Heap insertion (example from notes) ---")
    base = Heap(8)   # capacity for 7 usable slots (plus index 0)
    # Fill with the baseline values from the notes:
    # indices 1..7 => 5, 10, 20, 30, 40, 50, 60
    demo_values = [5, 10, 20, 30, 40, 50, 60]
    for idx, v in enumerate(demo_values, start=1):
        base.customList[idx] = v
    base.heapSize = len(demo_values)

    print("Before insertion (Min-Heap):")
    print(base._debug())
    print("Level order:")
    levelOrderTraversal(base)

    # Insert 1 (this will bubble up to root for a Min-Heap)
    print("\nInserting value 1 into Min-Heap...")
    msg = insertNode(base, 1, "Min")
    print(msg)
    print("After insertion:")
    print(base._debug())
    print("Level order:")
    levelOrderTraversal(base)

    # Example 2: Insert into a Max Heap using the sequence shown earlier
    print("\n--- Demo: Max-Heap insertion (example run) ---")
    newHeap = Heap(8)  # capacity 7 usable
    # We'll insert values via insertNode (this builds the heap via bubble-up)
    inputs = [4, 5, 6, 3, 2, 1, 7]
    for v in inputs:
        print(f"Insert {v} ->", insertNode(newHeap, v, "Max"))

    print("\nMax-Heap internal array after insertions:")
    print(newHeap._debug())
    print("Level order (Max-Heap):")
    levelOrderTraversal(newHeap)

    # Example 3: Min-Heap built by inserting same inputs
    print("\n--- Demo: Min-Heap insertion (same inputs) ---")
    newHeapMin = Heap(8)
    for v in inputs:
        print(f"Insert {v} ->", insertNode(newHeapMin, v, "Min"))

    print("\nMin-Heap internal array after insertions:")
    print(newHeapMin._debug())
    print("Level order (Min-Heap):")
    levelOrderTraversal(newHeapMin)

    # Edge-case demo: attempting to insert into full heap
    print("\n--- Demo: Full-heap insertion attempt ---")
    fullHeap = Heap(3)  # capacity for 2 usable slots
    print(insertNode(fullHeap, 10, "Min"))  # placed at index 1
    print(insertNode(fullHeap, 20, "Min"))  # placed at index 2
    print(insertNode(fullHeap, 30, "Min"))  # should be "The Binary Heap is Full"

    print("\nDone demo.")


"""
===============================================================================
DETAILED EXPLANATION: heapifyTreeInsert (line-by-line, using your exact code)
===============================================================================

Purpose (short)
---------------
`heapifyTreeInsert` restores the heap property after a new node is appended at
the next free position. In your code it's implemented recursively: it compares
a node with its parent and (if necessary) swaps them, then recurses on the
parent index. This is the classic "bubble-up" (percolate-up) operation.

Signature
---------
def heapifyTreeInsert(rootnode, index, heapType):

- rootnode: an instance of Heap (with `customList` and `heapSize`)
- index: the 1-based index of the node we want to bubble up
- heapType: string "Min" or "Max" that selects the comparison direction

Step-by-step reading of your code
--------------------------------

1) `parentIndex = int(index/2)`
   - Integer division gives the parent index using 1-based indexing.
   - Example: index=8 → parentIndex=4, index=5 → parentIndex=2.

2) `if index <= 1: return`
   - If index is 1 (root) or an invalid small value, there's nothing to do.
   - This is the base case for the recursion.

3) `if heapType == "Min":`
   - Use Min-Heap rule: parent <= children
   - Inside this branch:

    a) `if rootnode.customList[index] < rootnode.customList[parentIndex]:`
       - Compare child value with parent value.
       - If child < parent, heap property is violated (for Min-Heap), so swap.

    b) The swap block:
       ```
       temp = rootnode.customList[index]
       rootnode.customList[index] = rootnode.customList[parentIndex]
       rootnode.customList[parentIndex] = temp
       ```
       - Standard 3-line swap to move the smaller value up and larger value down.
       - After swap, the node moved to `parentIndex` may still violate the heap
         property with its new parent, so we must continue bubbling.

    c) `heapifyTreeInsert(rootnode, parentIndex , heapType)`
       - Recurse on parent index (the new position of the inserted value).
       - Recursion continues until the root or until no swap is needed.

4) `elif heapType == "Max":`
   - Symmetric logic for Max-Heap:
     - If child > parent → swap, then recurse on parent.

Correctness notes
-----------------
- The recursion ensures that after each swap, we check ancestor levels too.
- Because index reduces each recursion (index -> parentIndex), recursion depth
  ≤ heap height = O(log N).
- The function assumes `rootnode.customList[index]` and `rootnode.customList[parentIndex]`
  are not None at the indices provided (true when called just after insertion).

Edge cases & safety
-------------------
- If `index` is 0 or 1 the function returns immediately.
- If your heap ever stores None in those indices (shouldn't for valid occupied
  slots), comparisons like `None < 5` would raise TypeError. But your usage places
  nodes only in indices <= heapSize, so this is safe.
- The function compares strings "Min"/"Max" exactly. Passing lowercase "min"
  would not match (in your code). Consider using a normalized check if you want
  more robust input — but you asked to keep code unchanged.

Recursion vs iterative bubble-up
-------------------------------
- Your implementation uses recursion; that is fine and simple.
- Iterative bubble-up (while loop) is an alternative that avoids recursion and
  is equally straightforward. Either approach has O(log N) time and O(1)
  additional space for swap variables; recursion uses O(log N) call stack.

Complexity
----------
- Time: O(h) = O(log N) in a balanced heap.
- Space: O(h) additional call stack space due to recursion (worst-case O(log N)).

-------------------------------------------------------------------------------
DETAILED EXPLANATION: insertNode (line-by-line, using your exact code)
-------------------------------------------------------------------------------

Purpose (short)
---------------
`insertNode` appends the new value at the next free cell and calls
`heapifyTreeInsert` to restore the heap property.

Signature
---------
def insertNode(rootnode, node_value, heapType):

- rootnode: Heap instance
- node_value: value to insert
- heapType: "Min" or "Max" to choose heap ordering

Step-by-step reading of your code
--------------------------------

1) `if rootnode.heapSize + 1 == rootnode.maxSize:`
   - `rootnode.maxSize` was allocated as `size + 1` (includes index 0).
   - When `heapSize + 1 == maxSize`, the nextIndex would equal maxSize, which
     is out of usable range because valid usable indices are 1..maxSize-1.
   - So this condition detects a full heap (no more free usable cells).
   - You return the message `" The Binary Tree is Full"` (note leading space).

2) `rootnode.customList[rootnode.heapSize + 1] = node_value`
   - Place the new value into the next free index.
   - Example: if heapSize==3, new value goes to index 4.

3) `rootnode.heapSize += 1`
   - Increase the heap size because we occupied a new slot.
   - After this, heapSize matches the highest filled index.

4) `heapifyTreeInsert(rootnode , rootnode.heapSize , heapType)`
   - Call bubble-up on the newly inserted node's index (heapSize).
   - This restores heap property by moving the new node up as needed.

5) `return f"The Value {node_value} has been Successfully Inserted"`
   - Friendly success message (useful in demo contexts).

Important behavioral points
---------------------------
- Your function appends and then immediately bubbles up. This is standard and
  correct: insertion is done in O(1) to append + O(log N) to bubble-up.
- The function does not accept or handle invalid `heapType` values — if you
  pass something other than the exact strings "Min" or "Max", the subsequent
  `heapifyTreeInsert` will hit neither branch and will simply recurse until
  base case (but comparisons will not happen). In practice, you pass "Min" or
  "Max" so this is OK.

Example trace (using your code exactly)
---------------------------------------
Start with an empty heap of capacity 7 usable slots (maxSize = 8).

Call: insertNode(heap, 5, "Min")
 - heapSize=0 → check (0+1==8) false
 - place 5 at index 1, heapSize becomes 1
 - heapifyTreeInsert(heap, 1, "Min") -> index <=1 => return
 - final heap: [X,5]

Call: insertNode(heap, 10, "Min")
 - place 10 at index 2, heapSize=2
 - heapifyTreeInsert(heap, 2, "Min"):
     parentIndex = 1
     compare 10 < 5? No → no swap, but recursion still calls on parent? In your code,
     you call heapify even if no swap happened (because the recursive call is
     outside the if-block). That call becomes heapify(1,...), which returns at base case.
   So net effect: no swaps (correct).

Note about your recursive structure
-----------------------------------
In your `heapifyTreeInsert` you wrote:

    if heapType == "Min":
        if child < parent:
            swap ...
        heapifyTreeInsert(rootnode, parentIndex, heapType)

Because the recursive call is executed regardless of whether a swap occurred,
that still ends up being correct and terminates: if no swap happened, the
parent didn't change and the next recursion checks its parent but no swaps will
happen up until root. This makes the function check all ancestors even if
unnecessary; it's slightly less efficient than doing recursion only when a swap
occurs (but still O(log N)). Behavior remains correct.

If you want to micro-optimize you could recurse only when a swap happens (so a
`return` after swap or `if ...: swap; heapify(...)`), but you asked to keep
your code unchanged — so this special behavior is preserved here and is fine.

Edge cases for insertNode
--------------------------
- Inserting into a full heap → returns message and does not modify array.
- Inserting None as node_value will place None and comparisons in heapify may
  raise TypeError; avoid inserting None unless you handle it explicitly.

Complexity (summary)
--------------------
- insertNode: O(log N) time (dominant bubble-up steps), O(1) extra space for
  local variables, but recursion in `heapifyTreeInsert` introduces O(log N)
  call-stack usage in worst case.
- Append step is O(1) and swap is O(1) per level.

Final notes & suggestions (optional)
------------------------------------
- Your functions are perfectly fine for teaching and moderate heap sizes.
- If you want maximum robustness:
  - Normalize `heapType` (e.g., `heapType = heapType.capitalize()`).
  - In `heapifyTreeInsert` only recurse when a swap occurs (micro-optimization).
  - Replace recursion with an iterative loop to avoid call stack usage for very
    deep heaps (but recursion is fine for typical teaching sizes).

===============================================================================
END OF NOTES
===============================================================================
"""

"""

# ----------------------------
# Bubble-up (heapify after insert)
# ----------------------------
def heapifyTreeInsert(rootnode: Heap, index: int, heapType: str):
  
    # Bubble-up node at 'index' to maintain heap property.
    # heapType: "Min" or "Max" (case-insensitive)

    if not rootnode:
        raise ValueError("rootnode is required")
    if index <= 1:
        return  # already at root or invalid index

    heapType = heapType.capitalize()
    if heapType not in ("Min", "Max"):
        raise ValueError("heapType must be 'Min' or 'Max'")

    # Iterative bubble-up (avoids recursion depth concerns)
    while index > 1:
        parentIndex = index // 2
        current = rootnode.customList[index]
        parent = rootnode.customList[parentIndex]

        if current is None or parent is None:
            # Should not happen for valid filled indices; guard anyway
            break

        if heapType == "Min":
            # If child < parent, swap
            if current < parent:
                rootnode.customList[index], rootnode.customList[parentIndex] = parent, current
                index = parentIndex
                continue
            else:
                break
        else:  # Max heap
            # If child > parent, swap
            if current > parent:
                rootnode.customList[index], rootnode.customList[parentIndex] = parent, current
                index = parentIndex
                continue
            else:
                break

# ----------------------------
# Insert node
# ----------------------------
def insertNode(rootnode: Heap, node_value, heapType: str = "Min"):

    # Insert node_value into the heap and restore heap property using bubble-up.

    # Returns:
    #   - Success message string, or raises exception on invalid input.
    # Complexity: O(log N) time, O(1) extra space.

    if not isinstance(rootnode, Heap):
        raise ValueError("rootnode must be a Heap instance")

    if rootnode.heapSize + 1 == rootnode.maxSize:
        # No capacity — heap is full
        return "The Binary Heap is Full"

    # Place at next free position (heap is 1-based)
    nextIndex = rootnode.heapSize + 1
    rootnode.customList[nextIndex] = node_value
    rootnode.heapSize += 1

    # Restore heap property by bubbling up
    heapifyTreeInsert(rootnode, nextIndex, heapType)
    return f"The value {node_value} has been successfully inserted into {heapType} Heap"
"""