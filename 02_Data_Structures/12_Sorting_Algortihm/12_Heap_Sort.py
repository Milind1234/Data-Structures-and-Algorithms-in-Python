"""
===============================================================================
📘 HeapSort_Notes.py — Heapsort (min-heap variant in your code) — Notes + Code
===============================================================================

What this file contains (all explanations are in Python comment format):
- Clear algorithm overview (what heapify and heapSort do)
- The exact code you provided (unchanged logic)
- Line-by-line commented explanation inside functions
- ASCII / box visualizations for key steps (building heap, extraction)
- A detailed dry-run for the example list:
      cList = [2,1,7,6,5,3,4,9,8]
  showing the state after each important operation (heapify passes and after each extraction)
- Complexity, when to use, and summary

Run:
    python HeapSort_Notes.py

Notes:
- The implementation below builds a MIN-HEAP (smallest at root) using heapify,
  then repeatedly swaps root with last element and heapifies the reduced heap.
  Finally the list is reversed to produce ascending order.
===============================================================================
"""

# -----------------------------------------------------------------------------
# 1) ALGORITHM OVERVIEW (short)
# -----------------------------------------------------------------------------
# Heapsort (as implemented below) follows two main phases:
#
# Phase A — Build heap:
#    - Treat the array as a complete binary tree.
#    - Call heapify on all non-leaf nodes from right-to-left. This arranges
#      array into a valid heap (here: min-heap where parent <= children).
#
# Phase B — Extract elements:
#    - Repeatedly swap the root (smallest element in min-heap) with the last
#      element in the heap region.
#    - Reduce heap size by 1 and call heapify on root to re-heapify.
#    - Continue until heap size becomes 1.
#
# Final step:
#    - Because we used min-heap + extracted by swapping root to end, the array
#      becomes sorted in descending order; we reverse it at the end to get
#      ascending sorted array.
#
# Time Complexity:
#    - Building heap: O(n)
#    - Each extraction: O(log n), repeated n times -> O(n log n)
#    - Total: O(n log n)
#
# Space Complexity:
#    - In-place: O(1) extra space (ignoring recursion stack for heapify)
#
# When to use:
#    - Good worst-case O(n log n) guaranteed sort.
#    - In-place (no extra arrays).
#    - Not stable (relative order of equal elements is not preserved).
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 2) HELPER: heapify (min-heap)
# -----------------------------------------------------------------------------
def heapify(customList, n, i):
    """
    Make subtree rooted at index i satisfy min-heap property (parent <= children).

    Parameters:
      - customList : list being treated as binary tree (0-indexed)
      - n          : size of heap region (elements at indices 0..n-1 belong to heap)
      - i          : current root index to heapify

    Inside this function:
      1) Compute left child index l = 2*i + 1 and right child r = 2*i + 2.
      2) Find the smallest among customList[i], customList[l], customList[r].
      3) If the smallest is not i, swap parent with smallest child and recursively
         heapify the child subtree (because swap may violate heap property there).

    This implementation uses recursion; an iterative variant is also possible.
    """
    smallest = i
    l = 2 * i + 1
    r = 2 * i + 2

    # If left child exists and is smaller than current smallest, update
    if l < n and customList[l] < customList[smallest]:
        smallest = l

    # If right child exists and is smaller than current smallest, update
    if r < n and customList[r] < customList[smallest]:
        smallest = r

    # If smallest is not root, swap and continue heapifying downwards
    if smallest != i:
        customList[i], customList[smallest] = customList[smallest], customList[i]
        # Recursively heapify the affected subtree
        heapify(customList, n, smallest)


# -----------------------------------------------------------------------------
# 3) heapSort implementation (keeps your logic)
# -----------------------------------------------------------------------------
def heapSort(customList):
    """
    Sorts customList in-place using heap sort. Implementation details follow
    the code you provided exactly:
      1) Build min-heap by calling heapify from n//2 - 1 down to 0.
      2) For i from n-1 down to 1:
           - swap customList[i] with customList[0] (move smallest to end)
           - heapify the root with heap size i (exclude the sorted tail)
      3) After loop, reverse the list to obtain ascending order.
    """
    n = len(customList)

    # Build heap (min-heap) — start from last non-leaf node down to root
    # Explanation: nodes at indices >= n//2 are leaves (no children).
    for i in range(int(n / 2) - 1, -1, -1):
        heapify(customList, n, i)

    # Extraction phase:
    # Swap root with last element and reduce heap size by 1, then heapify root
    for i in range(n - 1, 0, -1):
        customList[i], customList[0] = customList[0], customList[i]
        heapify(customList, i, 0)

    # Because we used min-heap and moved smallest to the end each time,
    # the resulting array is in descending order. Reverse it to get ascending.
    customList.reverse()


# -----------------------------------------------------------------------------
# 4) ASCII VISUALIZATIONS & EXPLANATION OF STEPS
# -----------------------------------------------------------------------------
#
# Binary tree index mapping (0-indexed):
#    index:   0
#            / \
#          1     2
#         / \   / \
#        3  4  5  6
# and so on...
#
# Left child index = 2*i + 1
# Right child index = 2*i + 2
#
# Example array (tree view):
#   array = [2,1,7,6,5,3,4,9,8]
#   indices= 0 1 2 3 4 5 6 7 8
#
# As tree:
#               (2)
#            /      \
#          (1)      (7)
#         /  \     /  \
#       (6) (5) (3)  (4)
#       / \
#     (9) (8)
#
# The heapify step ensures every parent is <= its children (min-heap).
#
# We'll provide a dry-run below that shows:
#   - states after each heapify call while building heap
#   - after each swap+heapify during extraction
#
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 5) DETAILED DRY-RUN for cList = [2,1,7,6,5,3,4,9,8]
# -----------------------------------------------------------------------------
#
# We'll show the important states only (after each heapify when building heap,
# and after each swap + heapify during extraction). Indentation shows tree segments.
#
# Initial list:
#   [2, 1, 7, 6, 5, 3, 4, 9, 8]
#
# n = 9
# Last non-leaf node index = floor(n/2) - 1 = 4 - 1 = 3  (int(n/2)-1 -> 3)
#
# Build heap phase (call heapify from i = 3 down to 0)
# ---------------------------------------------------
#
# i = 3:
#   Subtree rooted at index 3 has children at indices 7 and 8:
#     - arr[3]=6, left=arr[7]=9, right=arr[8]=8
#   smallest among (6,9,8) is 6 -> already a min-heap here -> no change
#
# After i=3 (no change):
#   [2, 1, 7, 6, 5, 3, 4, 9, 8]
#
# i = 2:
#   Subtree root arr[2] = 7, children arr[5]=3, arr[6]=4
#   smallest among (7,3,4) is 3 at index 5 -> swap arr[2] and arr[5]
#   -> array becomes: [2, 1, 3, 6, 5, 7, 4, 9, 8]
#   After swap, call heapify at index 5: index 5 is leaf (no children) -> done
#
# After i=2:
#   [2, 1, 3, 6, 5, 7, 4, 9, 8]
#
# i = 1:
#   Subtree root arr[1] = 1, children arr[3]=6, arr[4]=5
#   smallest among (1,6,5) is 1 -> already ok -> no change
#
# After i=1:
#   [2, 1, 3, 6, 5, 7, 4, 9, 8]
#
# i = 0:
#   Subtree root arr[0] = 2, children arr[1]=1, arr[2]=3
#   smallest among (2,1,3) is 1 at index 1 -> swap arr[0] and arr[1]
#   -> array becomes: [1, 2, 3, 6, 5, 7, 4, 9, 8]
#   After swap, heapify at index 1:
#       index 1 has children arr[3]=6 and arr[4]=5 -> smallest is 2 (root), all OK
#   heapify returns -> final heap after build:
#
# Heap after build phase (min-heap property satisfied):
#   [1, 2, 3, 6, 5, 7, 4, 9, 8]
#
# (Visual tree after build)
#               (1)
#            /      \
#          (2)      (3)
#         /  \     /  \
#       (6) (5) (7)  (4)
#       / \
#     (9) (8)
#
# Extraction phase (move smallest to end, reduce heap size, re-heapify)
# --------------------------------------------------------------------
#
# We'll show each iteration: swap root with arr[i], then heapify root for heap size i
#
# i = 8 (swap root with arr[8]):
#   swap arr[8] and arr[0] -> swap 8 and 1
#   array becomes: [8, 2, 3, 6, 5, 7, 4, 9, 1]
#   heapify on root with n=8 (indices 0..7):
#     children: arr[1]=2, arr[2]=3 -> smallest is 2 at index1 -> swap root and index1
#     -> [2, 8, 3, 6, 5, 7, 4, 9, 1]
#     heapify at index1 (n=8):
#        children arr[3]=6, arr[4]=5 -> smallest is 5 at idx4? careful: arr[1]=8 vs children 6 and 5
#        smallest among (8,6,5) is 5 at index4 -> swap arr[1] and arr[4]
#        -> [2, 5, 3, 6, 8, 7, 4, 9, 1]
#        heapify at index4: index4 has no children in n=8 -> done
#   After heapify(0,n=8):
#     [2, 5, 3, 6, 8, 7, 4, 9, 1]
#
# i = 7 (swap root with arr[7]):
#   swap arr[7] and arr[0] -> swap 9 and 2
#   array -> [9, 5, 3, 6, 8, 7, 4, 2, 1]
#   heapify root with n=7 (0..6):
#     children arr[1]=5, arr[2]=3 -> smallest 3 at idx2 -> swap
#     -> [3, 5, 9, 6, 8, 7, 4, 2, 1]
#     heapify at idx2 (n=7):
#       children arr[5]=7, arr[6]=4 -> smallest 4 at idx6 -> swap
#       -> [3, 5, 4, 6, 8, 7, 9, 2, 1]
#       heapify at idx6: no children (n=7) -> done
#   After heapify:
#     [3, 5, 4, 6, 8, 7, 9, 2, 1]
#
# i = 6 (swap root with arr[6]):
#   swap arr[6] and arr[0] -> swap 9 and 3
#   array -> [9, 5, 4, 6, 8, 7, 3, 2, 1]
#   heapify root with n=6 (0..5):
#     children arr[1]=5, arr[2]=4 -> smallest 4 at idx2 -> swap
#     -> [4, 5, 9, 6, 8, 7, 3, 2, 1]
#     heapify idx2 (n=6):
#       children idx5 exists arr[5]=7 (idx5), right idx6 is outside n=6 -> smallest among (9,7) is 7 idx5
#       swap idx2 and idx5 -> [4, 5, 7, 6, 8, 9, 3, 2, 1]
#       heapify idx5: no children under n=6 -> done
#   After heapify:
#     [4, 5, 7, 6, 8, 9, 3, 2, 1]
#
# i = 5 (swap root with arr[5]):
#   swap arr[5] and arr[0] -> swap 9 and 4
#   array -> [9, 5, 7, 6, 8, 4, 3, 2, 1]
#   heapify root with n=5 (0..4):
#     children arr[1]=5, arr[2]=7 -> smallest 5 at idx1 -> swap
#     -> [5, 9, 7, 6, 8, 4, 3, 2, 1]
#     heapify idx1 (n=5):
#       children arr[3]=6, arr[4]=8 -> smallest is 6 at idx3 -> swap
#       -> [5, 6, 7, 9, 8, 4, 3, 2, 1]
#       heapify idx3: no children under n=5 -> done
#   After heapify:
#     [5, 6, 7, 9, 8, 4, 3, 2, 1]
#
# i = 4 (swap root with arr[4]):
#   swap arr[4] and arr[0] -> swap 8 and 5
#   array -> [8, 6, 7, 9, 5, 4, 3, 2, 1]
#   heapify root with n=4 (0..3):
#     children arr[1]=6, arr[2]=7 -> smallest 6 at idx1 -> swap
#     -> [6, 8, 7, 9, 5, 4, 3, 2, 1]
#     heapify idx1 (n=4): children arr[3]=9 (only) -> 8 <= 9 -> done
#   After heapify:
#     [6, 8, 7, 9, 5, 4, 3, 2, 1]
#
# i = 3 (swap root with arr[3]):
#   swap arr[3] and arr[0] -> swap 9 and 6
#   array -> [9, 8, 7, 6, 5, 4, 3, 2, 1]
#   heapify root with n=3 (0..2):
#     children arr[1]=8, arr[2]=7 -> smallest 7 idx2 -> swap
#     -> [7, 8, 9, 6, 5, 4, 3, 2, 1]
#     heapify idx2 (n=3): no children under n=3 -> done
#   After heapify:
#     [7, 8, 9, 6, 5, 4, 3, 2, 1]
#
# i = 2 (swap root with arr[2]):
#   swap arr[2] and arr[0] -> swap 9 and 7
#   array -> [9, 8, 7, 6, 5, 4, 3, 2, 1]
#   heapify root with n=2 (0..1):
#     children arr[1]=8 -> smallest between arr[0]=9 and 8 is 8 -> swap
#     -> [8, 9, 7, 6, 5, 4, 3, 2, 1]
#     heapify idx1: no children -> done
#   After heapify:
#     [8, 9, 7, 6, 5, 4, 3, 2, 1]
#
# i = 1 (swap root with arr[1]):
#   swap arr[1] and arr[0] -> swap 9 and 8
#   array -> [9, 8, 7, 6, 5, 4, 3, 2, 1]
#   heapify root with n=1 -> nothing to do
#
# End of extraction loop.
# Now reverse the array (because we used min-heap extraction to tail):
#   current array (descending): [9,8,7,6,5,4,3,2,1]
#   after reverse -> [1,2,3,4,5,6,7,8,9]
#
# Final sorted array:
#   [1, 2, 3, 4, 5, 6, 7, 8, 9]
#
# -----------------------------------------------------------------------------
# 6) SUMMARY / KEY POINTS
# -----------------------------------------------------------------------------
# - heapify ensures subtree obeys min-heap property by pushing the larger root
#   downwards if needed (swap with smallest child).
# - building heap is done bottom-up: start at last non-leaf and move to root.
# - extraction swaps root with last element in heap, then heapifies the root
#   in the reduced heap.
# - Because we used a min-heap and placed smallest at end repeatedly, final list
#   is descending; we reverse to get ascending.
# - Complexity: O(n log n) time, O(1) extra space.
# -----------------------------------------------------------------------------

# -----------------------------------------------------------------------------
# 7) RUN EXAMPLE (the same cList you provided)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    cList = [2, 1, 7, 6, 5, 3, 4, 9, 8]
    print("Input:", cList)
    heapSort(cList)
    print("Sorted:", cList)

    # OPTIONAL: show step-by-step by uncommenting smaller helper prints inside functions
    # (Note: printed dry-run above in comments describes each step exactly)
