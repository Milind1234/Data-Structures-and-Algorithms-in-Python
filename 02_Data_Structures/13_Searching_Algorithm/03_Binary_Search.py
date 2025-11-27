"""
===============================================================================
📘 Binary Search — Concept, Pseudocode, Implementation, Visualization, Dry Run
===============================================================================

Purpose
-------
Binary Search is an efficient search algorithm for sorted arrays. Instead of
checking elements one-by-one (linear search), binary search repeatedly divides
the search interval in half — discarding the half that cannot contain the target.

Key restriction:
    • The input array MUST be sorted (ascending or descending).
    • Most common: ascending order (small → large).

Complexity
----------
Time:
    • Worst / Average: O(log n)
    • Best (found at middle): O(1)
Space:
    • O(1) for iterative implementation (this file)
    • O(log n) stack depth for recursive version (if implemented recursively)

When to use
-----------
Use binary search when:
    • Your data is sorted, and
    • You need fast lookup on large datasets.

-------------------------------------------------------------------------------
1) PSEUDOCODE (iterative)
-------------------------------------------------------------------------------
FUNCTION binarySearch(array, target):
    start = 0
    end   = len(array) - 1

    WHILE start <= end:
        middle = floor((start + end) / 2)

        IF array[middle] == target:
            RETURN middle       # found

        ELSE IF target < array[middle]:
            end = middle - 1    # search left half

        ELSE:
            start = middle + 1  # search right half

    RETURN -1   # not found

-------------------------------------------------------------------------------
2) STEP-BY-STEP ALGORITHM (iterative)
-------------------------------------------------------------------------------
1. Initialize two pointers: start = 0, end = len(array)-1
2. While start <= end:
     a. Compute middle = floor((start + end) / 2)
     b. If array[middle] == target → done (return middle)
     c. If target < array[middle]   → end = middle - 1  (search left)
     d. Else                        → start = middle + 1 (search right)
3. If loop finishes → target not present → return -1

-------------------------------------------------------------------------------
3) CORRECT PYTHON IMPLEMENTATION (iterative)
-------------------------------------------------------------------------------
"""

import math
from typing import List, Union

def binarySearch(arr: List[int], target_value: int) -> Union[int, str]:
    """
    Iterative binary search on a sorted list (ascending).
    Returns index of target_value if present, otherwise returns "Not Present".

    Example:
        arr = [1,2,3,4,5,6,8,9,10,15,17,23,33]
        binarySearch(arr, 8)  -> 6
        binarySearch(arr, 7)  -> "Not Present"
    """
    start = 0
    end = len(arr) - 1

    # Loop while the search interval is valid
    while start <= end:
        middle = (start + end) // 2  # integer division (floor)

        # Found it
        if arr[middle] == target_value:
            return middle

        # Target is smaller → go left
        elif target_value < arr[middle]:
            end = middle - 1

        # Target is larger → go right
        else:
            start = middle + 1

    # Not found
    return "Not Present"


# -----------------------------------------------------------------------------
# 4) VISUALIZATION + DETAILED DRY-RUN (verbose style)
# -----------------------------------------------------------------------------
def _ascii_visual(arr: List[int], start: int, end: int, middle: int) -> str:
    """Return a compact ASCII visualization showing the current window & middle."""
    values = ' | '.join(str(x) for x in arr)
    # pointer line (mark start S, middle M, end E)
    pointers = ['   '] * len(arr)
    if 0 <= start < len(arr):
        pointers[start] = ' S '
    if 0 <= middle < len(arr):
        pointers[middle] = ' M '
    if 0 <= end < len(arr):
        pointers[end] = ' E '
    ptr_line = ''.join(ptr.center(len(str(arr[i])) + 3) for i, ptr in enumerate(pointers))
    return f"[{values}]\n{ptr_line}"


def binary_search_verbose(arr: List[int], target_value: int) -> Union[int, str]:
    """
    Verbose dry-run: prints each iteration's pointers and decisions, then returns result.
    Useful for learning / debugging.
    """
    start = 0
    end = len(arr) - 1
    step = 0

    print("\nBINARY SEARCH DRY-RUN")
    print(f"Array: {arr}")
    print(f"Searching for: {target_value}\n")

    while start <= end:
        middle = (start + end) // 2
        step += 1
        print(f"Step {step}: start={start}, middle={middle}, end={end}")
        print(_ascii_visual(arr, start, end, middle))
        print(f" -> arr[middle] = {arr[middle]}")

        if arr[middle] == target_value:
            print(f" -> Found: arr[{middle}] == {target_value}\n")
            return middle

        elif target_value < arr[middle]:
            print(f" -> Target {target_value} < {arr[middle]}: move end to middle-1 ({middle-1})\n")
            end = middle - 1

        else:
            print(f" -> Target {target_value} > {arr[middle]}: move start to middle+1 ({middle+1})\n")
            start = middle + 1

    print(" -> Loop finished: Target not found\n")
    return "Not Present"


# -----------------------------------------------------------------------------
# 5) DRY RUN EXAMPLES (explicit step-by-step)
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    # Example 1: target present
    arr1 = [1,2,3,4,5,6,8,9,10,15,17,23,33]
    print("Example 1 (target present):")
    print("Result index:", binarySearch(arr1, 8))          # expected 6
    print()
    binary_search_verbose(arr1, 8)                         # verbose trace

    # Example 2: target not present
    print("Example 2 (target NOT present):")
    print("Result index:", binarySearch(arr1, 7))          # expected "Not Present"
    print()
    binary_search_verbose(arr1, 7)                         # verbose trace

    # Example 3: target not present
    print("Example 3 (target present):")
    print("Result index:", binarySearch(arr1, 17))          # expected "10"
    print()
    binary_search_verbose(arr1, 17)                         # verbose trace


"""
-------------------------------------------------------------------------------
6) DRY-RUN WALKTHROUGH (compact textual steps for arr1 -> target = 8)
-------------------------------------------------------------------------------

Initial:
    arr = [1,2,3,4,5,6,8,9,10,15,17,23,33]
    start = 0
    end   = 12
Step A:
    middle = (0 + 12)//2 = 6
    arr[6] = 8 → equals target → found at index 6 → STOP

If target were 15:
    1) start=0, end=12, middle=6  → arr[6] = 8  → 15 > 8 → start = 7
    2) start=7, end=12, middle=9  → arr[9] = 15 → found at index 9 → STOP

If target were 2:
    1) start=0, end=12, middle=6  → arr[6] = 8  → 2 < 8 → end = 5
    2) start=0, end=5,  middle=2  → arr[2] = 3  → 2 < 3 → end = 1
    3) start=0, end=1,  middle=0  → arr[0] = 1  → 2 > 1 → start = 1
    4) start=1, end=1,  middle=1  → arr[1] = 2  → FOUND index 1

-------------------------------------------------------------------------------
7) NOTES & COMMON PITFALLS
-------------------------------------------------------------------------------
• Always ensure array is sorted (ascending) before calling binarySearch.
• Use start <= end as loop condition. Using start < end can miss single-element case.
• Middle index computed as (start + end)//2 is safe for Python ints.
  In languages with fixed int size, use start + (end - start) // 2 to avoid overflow.
• When updating start/end, ensure you use middle + 1 / middle - 1 (NOT middle),
  otherwise the loop may not shrink and you can create an infinite loop.

-------------------------------------------------------------------------------
8) SUMMARY
-------------------------------------------------------------------------------
• Binary search reduces the search space by half every iteration → O(log n).
• Works only on sorted arrays.
• Iterative version is simple and uses O(1) extra memory.
• Verbose trace helps you follow pointer movement & understand correctness.

===============================================================================
End of Binary Search notes (Python-comment format)
===============================================================================
"""
