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

def merge(customList , left , middle , right):
    n1 = middle - left + 1
    n2 = right - middle

    L = [0] * (n1)
    R = [0] * (n2)

    for i in range(0 , n1):
        L[i] = customList[left+i]

    for j in range(0 , n2):
        R[j] = customList[middle+1+j]

    i = 0
    j = 0   
    k = left
    
    while i < n1 and j < n2:
        if L[i] <= R[j]:
            customList[k] = L[i]
            i += 1
        else:
            customList[k] = R[j]
            j += 1
        k += 1

    while i < n1:
        customList[k] = L[i]
        i += 1
        k += 1

    while j < n2:
        customList[k] = R[j]
        j += 1
        k += 1


def mergeSort(customList , left , right):
    if left < right:
        middle = (left + right) // 2
        mergeSort(customList , left , middle)
        mergeSort(customList , middle + 1, right)
        merge(customList,left , middle , right)
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
