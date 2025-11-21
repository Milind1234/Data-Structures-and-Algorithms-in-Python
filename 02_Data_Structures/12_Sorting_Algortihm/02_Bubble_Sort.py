"""
==================================================================
                        BUBBLE SORT — NOTES
==================================================================

Bubble Sort (also called *Sinking Sort*) is the simplest sorting 
algorithm. It repeatedly compares **adjacent pairs** and swaps 
them if they are in the wrong order.

It keeps bubbling the largest element to the end in each round.
Eventually, the entire array becomes sorted.
==================================================================
"""

# ---------------------------------------------------------------
# 1) BASIC IDEA OF BUBBLE SORT
# ---------------------------------------------------------------
"""
Given a list:

    [5, 9, 3, 1, 2, 8, 4, 7, 6]

Bubble sort compares adjacent items:

    Compare A[i] and A[i+1]
    If A[i] > A[i+1], swap them

This process repeats (N-1) times.

Each full pass pushes the **largest element** to the right.
"""


# ---------------------------------------------------------------
# 2) ASCII VISUALIZATION OF ONE PASS
# ---------------------------------------------------------------
"""
Initial list:
    5  9  3  1  2  8  4  7  6

Pass 1 comparisons:

    [5, 9] → OK  
    [9, 3] → swap → 5 3 9 ...
    [9, 1] → swap
    [9, 2] → swap
    [9, 8] → swap
    [9, 4] → swap
    [9, 7] → swap
    [9, 6] → swap

After Pass 1:
    5  3  1  2  8  4  7  6 | 9  ← largest element sorted

After Pass 2:
    3  1  2  5  4  7  6 | 8 9

After Pass 3:
    1  2  3  4  5  6  7 | 8 9

After further passes, the list remains unchanged; bubble sort finishes.
"""


# ---------------------------------------------------------------
# 3) ASCII FLOWCHART OF BUBBLE SORT
# ---------------------------------------------------------------
"""
                ┌──────────────────────┐
                │      Start           │
                └──────────┬───────────┘
                           │
               ┌───────────▼────────────┐
               │  i = 0 to n-2 (loop)   │
               └───────────┬────────────┘
                           │
               ┌───────────▼────────────┐
               │ j = 0 to n-i-2 (loop)  │
               └───────────┬────────────┘
                           │
               ┌───────────▼────────────┐
               │ Compare A[j] , A[j+1]  │
               └───────────┬────────────┘
                           │
         ┌───────YES───────┘        NO ────────────────┐
         ▼                                               ▼
┌─────────────────┐                             ┌─────────────────┐
│ Swap elements    │                             │ Keep as is      │
└────────┬────────┘                             └────────┬────────┘
         │                                              │
         └───────────────► Continue inner loop ◄────────┘
                           (j loop)
                           │
                           ▼
               ┌──────────────────────┐
               │ Continue outer loop  │
               └──────────────────────┘
                           │
                           ▼
                ┌─────────────────────┐
                │        End          │
                └─────────────────────┘
"""


# ---------------------------------------------------------------
# 4) PYTHON IMPLEMENTATION
# ---------------------------------------------------------------
def bubbleSort(customList):
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]

    return customList


# Example:
CList = [5, 6, 7, 1, 3, 4, 8, 2]
print("Sorted:", bubbleSort(CList))


# ---------------------------------------------------------------
# 5) TIME COMPLEXITY ANALYSIS
# ---------------------------------------------------------------
"""
⚠ Bubble Sort has *nested loops*

Outer loop   → runs N-1 times  
Inner loop   → runs N-i-1 times  

Worst Case: O(N^2)  
Average Case: O(N^2)  
Best Case: O(N)         (only if optimized version used with a 'no swap' flag)

Space Complexity: O(1)
    - Bubble sort is an **in-place algorithm**
    - Requires NO additional array
"""

# ---------------------------------------------------------------
# 6) WHEN TO USE BUBBLE SORT?
# ---------------------------------------------------------------
"""
USE BUBBLE SORT WHEN:
    ✔ Input list is almost sorted  
    ✔ Space is extremely limited (in-place algo, O(1) space)  
    ✔ You need a simple brute-force method  
    ✔ Teaching / Demonstration purposes  

AVOID BUBBLE SORT WHEN:
    ✘ Performance matters  
    ✘ Input list is large  
    ✘ Real-time applications  

Better alternatives:
    Merge Sort, Quick Sort, Heap Sort, Timsort
"""

# ---------------------------------------------------------------
# END OF BUBBLE SORT NOTES
# ---------------------------------------------------------------

"""
===============================================================================
📘 BubbleSort_Notes.py — Bubble Sort explanation, ASCII visuals, flowchart, and dry-run
===============================================================================

What you'll find in this file
----------------------------
- A short theory recap of Bubble Sort
- Clear explanation of the outer (i) and inner (j) loops
- An ASCII step-by-step animation function (runnable)
- An annotated dry-run for example lists (printed when running)
- A simple flowchart (ASCII)
- The exact bubbleSort implementation you provided (kept unchanged) plus a verbose
  version that prints internal state per comparison/swap

Run this file with:  python BubbleSort_Notes.py

===============================================================================
"""

from typing import List
import time

# -----------------------------------------------------------------------------
# Your original bubble sort (unchanged behavior)
# -----------------------------------------------------------------------------
def bubbleSort(customList: List[int]) -> List[int]:
    for i in range(len(customList) - 1):
        for j in range(len(customList) - i - 1):
            if customList[j] > customList[j+1]:
                customList[j], customList[j+1] = customList[j+1], customList[j]
    return customList

# -----------------------------------------------------------------------------
# Verbose variant: prints comparisons, swaps and ASCII visualization per pass
# -----------------------------------------------------------------------------

def bubbleSort_verbose(customList: List[int], delay: float = 0.0) -> List[int]:
    """
    Same algorithm but prints a human-friendly trace per pass.

    Parameters
    ----------
    customList : List[int]
        The list to sort in-place. (It will be mutated.)
    delay : float
        Seconds to wait between printed steps (0.0 for no pause).
    """
    n = len(customList)
    print("Starting bubble sort (verbose) on:", customList)
    print()

    for i in range(n - 1):
        print(f"PASS {i} (i = {i}) — working range: 0..{n - i - 1}")
        for j in range(n - i - 1):
            a, b = customList[j], customList[j+1]
            # show comparison
            print(f"  compare j={j}: {a} ? {b}", end='')
            if a > b:
                # swap and show
                customList[j], customList[j+1] = b, a
                print(f"  → swap → {customList}")
            else:
                print("  → ok (no swap)")
            if delay > 0:
                time.sleep(delay)

        # after each pass, show which element bubbled to its final position
        print(f"After PASS {i}: {customList} (element at index {n-i-1} is final)")
        print(_ascii_visual(customList, final_index=n-i-1))
        print('-' * 60)
    print("Final sorted list:", customList)
    return customList

# -----------------------------------------------------------------------------
# Small helper to produce an ASCII visualization of the list and mark final zone
# -----------------------------------------------------------------------------

def _ascii_visual(arr: List[int], final_index: int = None) -> str:
    """Return an ASCII representation of arr with a bracket showing "final" elements.

    Example output:
      [ 3  4  2  5  8 ]
       ^^^^^^^^^^^^^^^
       ^^^^^ final ===>
    """
    if not arr:
        return "[]"
    line = "[ " + "  ".join(str(x) for x in arr) + " ]"
    if final_index is None:
        return line
    # caret line with final region marked
    n = len(arr)
    markers = []
    # compute cell widths approximately to align carets (simple approach)
    # This will produce a compact visual, not pixel-perfect.
    for x in arr:
        markers.append('^' * len(str(x)))
    left = 0
    # build a marker string where indices <= final_index are marked
    marker_line = "  "
    for idx, m in enumerate(markers):
        # add spacing used above: each value printed as str(x) plus 2 spaces
        marker_line += (' ' * 0) + (m + '  ' if idx != len(markers)-1 else m)
    # show hint
    hint = f"(elements at positions >= {final_index} are final)"
    return line + "\n" + marker_line + "\n" + hint

# -----------------------------------------------------------------------------
# Flowchart (ASCII) — a compact representation for bubble sort
# -----------------------------------------------------------------------------

def bubble_sort_flowchart() -> str:
    return """
Flowchart (ASCII): Bubble Sort (high level)

 START
   |
   v
 [i = 0..n-2] <- outer loop
   |
   v
  [j = 0..n-i-2] <- inner loop
   |
   v
 [compare a[j] and a[j+1]]
   |
  / \ 
 /   \ 
<=    >
 |     |
 v     v
 no   swap
 op   a[j],a[j+1]=a[j+1],a[j]
  \   /
   \ /
    v
  continue inner
    |
    v
 end inner -> i++ -> repeat
    |
    v
  sorted -> END
"""

# -----------------------------------------------------------------------------
# Dry-run example: step-by-step table printed as comments and output
# -----------------------------------------------------------------------------

def bubble_sort_dry_run_example(example: List[int]):
    """
    Produce a detailed dry-run for the provided example list. Prints every
    pass, every j, and resulting array after each swap — formatted like notes.
    """
    print("\nDRY RUN — Example:", example)
    arr = example.copy()
    n = len(arr)

    # Header
    print('\nInitial array:')
    print(arr)

    for i in range(n - 1):
        print(f"\n== PASS {i} (i = {i}) — inner j from 0 to {n - i - 2} ==")
        for j in range(n - i - 1):
            print(f"  j={j}: compare arr[{j}]={arr[j]} and arr[{j+1}]={arr[j+1]}")
            if arr[j] > arr[j+1]:
                print(f"    → swap because {arr[j]} > {arr[j+1]}")
                arr[j], arr[j+1] = arr[j+1], arr[j]
                print(f"    result: {arr}")
            else:
                print(f"    → no swap (order OK)")
        print(f"After PASS {i}: {arr}")
    print('\nFinal sorted array:', arr)

# -----------------------------------------------------------------------------
# A short explanation block about why outer and inner loops have those ranges
# -----------------------------------------------------------------------------

EXPLANATION = '''
Loop logic explained (compact, interview-style):

for i in range(len(customList) - 1):
    # i counts completed passes. After pass i, the largest i+1 elements are at the
    # end of the array in their final (sorted) positions.

    for j in range(len(customList) - i - 1):
        # j goes from 0 to the last unsorted index.
        # We compare a[j] and a[j+1]. If a[j] > a[j+1], swap them.
        # Because the rightmost i elements are already final, we don't iterate
        # into them; that's why we subtract i.

Why "len(customList) - 1" for outer loop?
  - If length is n, we only need n-1 passes max to fully sort (after n-1 passes
    every element will have bubbled into place).

Why inner bound is "len(customList) - i - 1"?
  - Each pass places one new element into its final position at the right end;
    so the next pass can ignore the last sorted elements, reducing work.
'''

# -----------------------------------------------------------------------------
# If run as a script, show everything: flowchart, concise explanation, verbose run
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print(__doc__)

    # flowchart
    print('\n' + '='*30 + ' FLOWCHART ' + '='*30)
    print(bubble_sort_flowchart())

    # concise explanation
    print('\n' + '='*30 + ' LOOP EXPLANATION ' + '='*30)
    print(EXPLANATION)

    # show original implementation result
    print('\n' + '='*30 + ' ORIGINAL FUNCTION DEMO ' + '='*30)
    demo_list = [5, 3, 8, 4, 2]
    print('Input:', demo_list)
    sorted_out = bubbleSort(demo_list.copy())
    print('Output:', sorted_out)

    # verbose animation (no delay by default — set delay>0 to watch)
    print('\n' + '='*30 + ' VERBOSE TRACE (animation-like) ' + '='*30)
    bubbleSort_verbose([5, 3, 8, 4, 2], delay=0.0)

    # dry-run printed notes
    print('\n' + '='*30 + ' DETAILED DRY RUN ' + '='*30)
    bubble_sort_dry_run_example([5, 3, 8, 4, 2])

    # alternative example (the list you used earlier in conversation)
    print('\n' + '='*30 + ' DRY RUN FOR CList EXAMPLE ' + '='*30)
    c_list = [5,6,7,1,3,4,8,2]
    bubble_sort_dry_run_example(c_list)

    print('\nDone.')
