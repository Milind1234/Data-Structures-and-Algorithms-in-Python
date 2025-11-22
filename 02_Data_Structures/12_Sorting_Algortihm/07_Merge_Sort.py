"""
===============================================================================
📘 MergeSort_Notes.py — Full Notes, ASCII Visualization, Flowchart & Dry Run
===============================================================================

Contents:
- What Merge Sort is
- Why it uses Divide & Conquer
- How merge() works (with ASCII explanation)
- Flowchart for Merge Sort
- Your exact merge() and mergeSort() functions
- Step-by-step dry run example
- Time & Space complexity
===============================================================================
"""

# -----------------------------------------------------------------------------
# THEORY — What is Merge Sort?
# -----------------------------------------------------------------------------
THEORY = """
Merge Sort — Concept
--------------------
Merge Sort is a Divide & Conquer sorting algorithm.

It works in 3 steps:

1) Divide  
   Split the array into two halves until every sub-array has only ONE element.

2) Conquer  
   Recursively sort the left half and right half.

3) Combine  
   Merge the two sorted halves into one sorted array.

Why is it fast?
---------------
Because merging two sorted halves is linear.

Merge Sort guarantees:
    • Worst case:   O(n log n)
    • Average case: O(n log n)
    • Best case:    O(n log n)
    • Stable sorting
"""

# -----------------------------------------------------------------------------
# ASCII VISUALIZATION — Divide Phase
# -----------------------------------------------------------------------------
VISUAL_SPLIT = """
Example Array:
    [2, 1, 4, 3]

Divide:
    [2, 1, 4, 3]
        /     \\
  [2, 1]       [4, 3]
    /  \\        /  \\
  [2] [1]    [4]  [3]   ← base case reached
"""

# -----------------------------------------------------------------------------
# ASCII VISUALIZATION — Merge Phase
# -----------------------------------------------------------------------------
VISUAL_MERGE = """
Merging Example:

Left  = [1, 4, 7]
Right = [2, 3, 6]

Compare 1 and 2 → pick 1
Compare 4 and 2 → pick 2
Compare 4 and 3 → pick 3
Compare 4 and 6 → pick 4
Compare 7 and 6 → pick 6
Pick leftover → 7

Final merged array:
    [1, 2, 3, 4, 6, 7]
"""

# -----------------------------------------------------------------------------
# FLOWCHART (ASCII)
# -----------------------------------------------------------------------------
FLOWCHART = """
                ┌──────────────┐
                │   mergeSort  │
                └───────┬──────┘
                        │
                if left < right
                        │
        ┌───────────────▼──────────────────┐
        │  middle = (left + right) // 2    │
        └───────────────┬──────────────────┘
                        │
        ┌───────────────▼───────────────┐
        │  mergeSort(left, middle)      │
        └───────────────┬───────────────┘
                        │
        ┌───────────────▼───────────────┐
        │  mergeSort(middle+1, right)   │
        └───────────────┬───────────────┘
                        │
        ┌───────────────▼───────────────┐
        │         merge()               │
        └───────────────────────────────┘
"""

# -----------------------------------------------------------------------------
# EXACT CODE YOU PROVIDED (kept unchanged)
# -----------------------------------------------------------------------------
"""
Merge Sort (annotated) — in-place sorting using temporary subarrays

This file contains the two functions you provided (merge and mergeSort)
but each function now includes detailed algorithm notes and code-level
explanations as Python comments and docstrings.

Usage:
    arr = [2,1,4,3,5,8,7,9,6,10]
    mergeSort(arr, 0, len(arr)-1)
    print(arr)   # arr is sorted in-place

Properties:
    - Stable sorting algorithm
    - Time complexity: O(n log n) for best/average/worst cases
    - Space complexity: O(n) due to temporary arrays created during merge
"""
# -----------------------------------------------------------------------------
def merge(customList, left, middle, right):
    """
    Merge two sorted subarrays of customList in-place.

    The two sorted subarrays are:
        customList[left : middle+1]     (length n1)
        customList[middle+1 : right+1]  (length n2)

    Postcondition:
        customList[left : right+1] will be sorted.

    Algorithm summary (merge step of merge sort):
      1. Copy the left half into a temporary array L and the right half into R.
      2. Maintain pointers i (L), j (R) and k (write position in customList).
      3. Repeatedly choose the smaller of L[i] and R[j] and write it to customList[k].
      4. When one temporary array is exhausted, copy remaining elements from the other.
    
    Complexity for this merge call:
      - Time: O(n1 + n2) = O(right - left + 1)
      - Space: O(n1 + n2) temporary extra space
    """

    # -------------------------
    # 1) Compute sizes of halves
    # -------------------------
    n1 = middle - left + 1      # size of left subarray
    n2 = right - middle         # size of right subarray

    # -------------------------
    # 2) Allocate temporary arrays
    # -------------------------
    # We copy to temporaries because we'll overwrite positions in customList
    # while merging. Using temporaries preserves read-sources.
    L = [0] * n1
    R = [0] * n2

    # -------------------------
    # 3) Copy data into temporaries
    # -------------------------
    # copy left half into L
    for i in range(n1):
        L[i] = customList[left + i]
    # copy right half into R
    for j in range(n2):
        R[j] = customList[middle + 1 + j]

    # -------------------------
    # 4) Merge loop: choose smaller element repeatedly
    # -------------------------
    i = 0       # pointer for L (next candidate to read)
    j = 0       # pointer for R (next candidate to read)
    k = left    # write pointer into customList

    # While both arrays have remaining elements:
    # compare L[i] and R[j], write the smaller and advance its pointer.
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            # L[i] is smaller (or equal => stable: take from L first)
            customList[k] = L[i]
            i += 1
        else:
            # R[j] is smaller
            customList[k] = R[j]
            j += 1
        k += 1

    # -------------------------
    # 5) Copy any remaining elements
    # -------------------------
    # One of the temporary arrays may still have elements left.
    # Copy them as-is (they are already sorted internally).
    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1

    # At this point customList[left:right+1] is merged and sorted.
    return None   # function mutates customList in-place


# -----------------------------------------------------------------------------
def mergeSort(customList, left, right):
    """
    Recursively sort customList[left:right+1] using merge sort.

    Algorithm (Divide & Conquer):
      - Base case: if the segment has 0 or 1 element (left >= right) it's already sorted.
      - Recursive case:
          1) Compute middle index
          2) Recursively sort left half: mergeSort(customList, left, middle)
          3) Recursively sort right half: mergeSort(customList, middle+1, right)
          4) Merge the two sorted halves with merge(...)

    Notes:
      - This implementation returns the list for convenience, but sorting is done in-place.
      - Recursion depth is O(log n). Each level performs O(n) merge work overall,
        which leads to O(n log n) time.
      - Additional memory is used by merge via temporary arrays (total O(n) across merges).

    Example:
      >>> arr = [3,1,4,2]
      >>> mergeSort(arr, 0, len(arr)-1)
      >>> print(arr)   # [1,2,3,4]
    """
    # Base case: a segment of length 0 or 1 is already sorted.
    if left < right:
        # Find middle safely using integer division
        middle = (left + right) // 2

        # Recursively sort the left half
        mergeSort(customList, left, middle)

        # Recursively sort the right half
        mergeSort(customList, middle + 1, right)

        # Merge the two sorted halves into a single sorted segment
        merge(customList, left, middle, right)

    # return the list (sorted in-place). Returning is optional.
    return customList



# -----------------------------------------------------------------------------
# DRY RUN FOR YOUR TEST CASE
# -----------------------------------------------------------------------------
def dry_run():
    arr = [2,1,4,3,5,8,7,9,6,10]
    print("\nInitial Array:", arr)

    print("\n--- DIVIDE PHASE ---")
    print("Splits happen like:")
    print("0-9 → 0-4 & 5-9")
    print("0-4 → 0-2 & 3-4")
    print("0-2 → 0-1 & 2")
    print("etc... until single elements\n")

    print("--- MERGE PHASE (key merging) ---")
    print("[2] & [1] → [1,2]")
    print("[4] & [3] → [3,4]")
    print("[1,2] & [3,4] → [1,2,3,4]")
    print("Then merges continue for the rest.\n")

    print("Final output:", mergeSort(arr, 0, len(arr)-1))


# -----------------------------------------------------------------------------
# COMPLEXITY
# -----------------------------------------------------------------------------
COMPLEXITY = """
Time Complexity of Merge Sort
-----------------------------
Divide step   → O(log n)
Merge step    → O(n)

Total time    → O(n log n)     ALWAYS (best/worst/average)

Space Complexity
----------------
O(n)
Because Merge Sort creates temporary left/right arrays during merging.
"""

# -----------------------------------------------------------------------------
# RUN (for notes demonstration)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print(THEORY)
    print(VISUAL_SPLIT)
    print(VISUAL_MERGE)
    print(FLOWCHART)
    dry_run()
    print(COMPLEXITY)
