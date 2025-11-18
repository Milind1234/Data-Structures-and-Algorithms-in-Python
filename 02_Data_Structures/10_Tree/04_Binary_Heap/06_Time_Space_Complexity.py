"""
===============================================================================
📘 Binary Heap — Time & Space Complexity Notes (Python Style)
===============================================================================

This file summarizes the **time and space complexity** of all operations performed on
a Binary Heap (array-based, 1-indexed, Min/Max supported).

These notes match the lecture explanation you provided — rewritten cleanly and
formatted for your DSA notes collection.

===============================================================================
1️⃣ CREATE BINARY HEAP
===============================================================================
Operation:
    newHeap = Heap(size)

Explanation:
    - We only allocate a Python list of size (n + 1).
    - No looping, no heapifying → O(1) time.
    - But the list occupies contiguous memory → O(n) space.

Time Complexity:   O(1)
Space Complexity:  O(n)

-------------------------------------------------------------------------------
2️⃣ PEEK OF HEAP  (get root value)
===============================================================================
Operation:
    rootnode.customList[1]

Explanation:
    - Accessing an index in a Python list is O(1).
    - No extra memory is used.

Time Complexity:   O(1)
Space Complexity:  O(1)

-------------------------------------------------------------------------------
3️⃣ SIZE OF HEAP
===============================================================================
Operation:
    return rootnode.heapSize

Explanation:
    - Direct property access.
    - No loops, no recursion.

Time Complexity:   O(1)
Space Complexity:  O(1)

-------------------------------------------------------------------------------
4️⃣ LEVEL ORDER TRAVERSAL (traverse heap)
===============================================================================
Operation:
    for i in range(1, heapSize + 1):
        print(customList[i])

Explanation:
    - Must visit all elements → O(n)
    - No recursion, no extra structures → O(1) space

Time Complexity:   O(n)
Space Complexity:  O(1)

-------------------------------------------------------------------------------
5️⃣ INSERT NODE ( + heapify up )
===============================================================================
Operation:
    insertNode(...)
    → heapifyTreeInsert()

Explanation:
    - Insert element at bottom → O(1)
    - Bubble-up (heapify up) follows parent chain.
    - Height of heap = O(log n)
    - Worst case: swap all the way to root.

Time Complexity:   O(log n)
Space Complexity:  O(log n)   (because heapify uses recursion)

-------------------------------------------------------------------------------
6️⃣ EXTRACT NODE ( + heapify down )
===============================================================================
Operation:
    extractNode(...)
    → heapifyTreeExtract()

Explanation:
    - Replace root with last element → O(1)
    - Heapify down restores order.
    - Recurses until leaf → depth O(log n)

Time Complexity:   O(log n)
Space Complexity:  O(log n)   (recursive heapify down)

-------------------------------------------------------------------------------
7️⃣ DELETE ENTIRE BINARY HEAP
===============================================================================
Operation:
    rootnode.customList = None

Explanation:
    - Only dropping the reference to the array.
    - No traversal, no recursion → O(1)
    - No additional memory used.

Time Complexity:   O(1)
Space Complexity:  O(1)

===============================================================================
📘 SUMMARY TABLE
===============================================================================
Operation                     Time Complexity      Space Complexity
-------------------------------------------------------------------
Create Heap                       O(1)                   O(n)
Peek of Heap                      O(1)                   O(1)
Size of Heap                      O(1)                   O(1)
Level Order Traversal             O(n)                   O(1)
Insert Node                       O(log n)               O(log n)
Extract Node                      O(log n)               O(log n)
Delete Entire Heap                O(1)                   O(1)
===============================================================================

End of Binary Heap Section ✔  
Next topic in DSA: **Trie Data Structure**
===============================================================================
"""
