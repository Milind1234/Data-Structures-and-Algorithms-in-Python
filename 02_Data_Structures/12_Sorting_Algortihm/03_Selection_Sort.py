"""
===============================================================================
📘 SelectionSort_Notes.py — Selection Sort (Notes, ASCII visuals, flowchart, dry-run)
===============================================================================

Purpose
-------
This single-file notes document mirrors the style of your Bubble Sort notes:
  - clear definition + when to use selection sort
  - exact selectionSort implementation (logic preserved)
  - detailed comments explaining each line
  - ASCII visualizations showing array before/after key steps
  - ASCII flowchart
  - verbose trace (per-iteration) and dry-run examples printed to terminal
  - helpful interview-style explanation of loops and complexity

Related uploaded file (for your reference / slides): 
  /mnt/data/WhatsApp Image 2025-11-21 at 18.57.41.jpeg

Run:
    python SelectionSort_Notes.py

===============================================================================
"""

from typing import List, Tuple
import textwrap

# -------------------------------------------------------------------------
# Quick summary / definition
# -------------------------------------------------------------------------
# Selection Sort:
#   - Divide the array into sorted prefix and unsorted suffix.
#   - Repeatedly find the minimum element from the unsorted suffix and
#     swap it with the first element of that suffix (i.e., place it at index i).
#
# Complexity:
#   - Time: O(n^2) best/avg/worst
#   - Space: O(1) (in-place)
#   - Stability: Not stable (standard implementation swaps.)
#
# Use when:
#   - Memory is very limited (in-place)
#   - List is small
#   - Simplicity/educational purposes
#
# Avoid when:
#   - Large inputs and time matters (prefer merge/quick/heap)
# -------------------------------------------------------------------------


# -------------------------------------------------------------------------
# ASCII FLOWCHART (high-level)
# -------------------------------------------------------------------------
FLOWCHART = """
Flowchart (ASCII): Selection Sort (high level)

   Start
     |
     v
  i = 0 .. n-1    <- outer loop
     |
     v
  min_index = i
     |
     v
  j = i+1 .. n-1  <- find minimum in unsorted suffix
     |
     v
  if A[j] < A[min_index]: min_index = j
     |
     v
  After scan: swap A[i] <-> A[min_index]
     |
     v
  i = i + 1 -> repeat until i == n-1
     |
     v
    End (array sorted)
"""

# -------------------------------------------------------------------------
# ASCII VISUALIZATION (small example)
# -------------------------------------------------------------------------
VISUAL_EXAMPLE = """
Example (visual):
Initial: [ 7  3  5  2 ]

i = 0: find min in [7,3,5,2] -> min=2 at index 3
  swap A[0] <-> A[3]   -> [ 2 | 3  5  7 ]  (2 is now in sorted prefix)

i = 1: find min in [3,5,7] -> min=3 at index 1
  swap A[1] <-> A[1] (no-op) -> [ 2  3 | 5  7 ]

i = 2: find min in [5,7] -> min=5
  swap A[2] <-> A[2] -> [ 2  3  5 | 7 ]

Done -> [2,3,5,7]
(Bar '|' marks boundary between sorted prefix and unsorted suffix)
"""


# -------------------------------------------------------------------------
# Utility: pretty print state with markers
# -------------------------------------------------------------------------
def visualize_array(arr: List[int], i: int, min_index: int, action: str = "") -> None:
    """Print array, indices, and sorted/unsorted boundary for this iteration."""
    n = len(arr)
    idx_row = "Idx : " + " ".join(f"{k:>3}" for k in range(n))
    val_row = "Arr : " + " ".join(f"{v:>3}" for v in arr)
    boundary = "      " + "".join((" S" if k < i+1 else " U") for k in range(n))
    print(idx_row)
    print(val_row)
    print(boundary + "   (S = sorted prefix, U = unsorted suffix)")
    print(f"i={i}  min_index={min_index}   {action}")
    print("-" * max(len(val_row), 60))


# -------------------------------------------------------------------------
# Core selection sort (preserve user's logic) + verbose trace
# -------------------------------------------------------------------------
def selectionSort(customList: List[int]) -> List[int]:
    """
    Selection sort (in-place). Logic preserved:
      for i in range(len(customList)):
          min_index = i
          for j in range(i+1, len(customList)):
              if customList[min_index] > customList[j]:
                  min_index = j
          customList[i], customList[min_index] = customList[min_index], customList[i]

    Returns sorted list (same object mutated).
    """
    n = len(customList)
    for i in range(n):
        min_index = i
        for j in range(i + 1, n):
            if customList[min_index] > customList[j]:
                min_index = j
        # swap (may be a no-op if min_index == i)
        customList[i], customList[min_index] = customList[min_index], customList[i]
    return customList


def selectionSort_verbose(customList: List[int]) -> List[int]:
    """
    Same logic but prints detailed per-iteration trace for learning.
    Shows:
      - min_index discovered
      - whether a swap occurred
      - array after swap and visualization
    """
    arr = customList  # operates in-place
    n = len(arr)
    print("\n=== Selection Sort — Verbose Trace ===")
    print("Initial array:", arr)
    for i in range(n):
        min_index = i
        # find min in unsorted suffix
        for j in range(i + 1, n):
            if arr[min_index] > arr[j]:
                min_index = j

        swapped = (min_index != i)
        if swapped:
            action = f"swap A[{i}] ({arr[i]}) <-> A[{min_index}] ({arr[min_index]})"
        else:
            action = "no swap (min already at position)"

        # perform swap
        arr[i], arr[min_index] = arr[min_index], arr[i]

        print(f"\nIteration i={i}:")
        print(f"  min_index found = {min_index} (value after swap if any -> {arr[i]})")
        print("  action:", action)
        visualize_array(arr, i, min_index, action)
    print("Final sorted array:", arr)
    return arr


# -------------------------------------------------------------------------
# Dry-run printed notes (step-by-step) for pedagogy
# -------------------------------------------------------------------------
def selection_sort_dry_run_example(example: List[int]) -> None:
    """
    Produce a detailed dry-run for the provided example list.
    Prints each outer iteration, inner comparisons and the effect (swap/no-swap).
    """
    print("\nDRY RUN — Example:", example)
    arr = example.copy()
    n = len(arr)
    print("\nInitial array:")
    print(arr)
    for i in range(n):
        print(f"\n== Iteration i={i} ==")
        min_index = i
        print(f"  Start: min_index={min_index} (value {arr[min_index]})")
        for j in range(i + 1, n):
            print(f"    compare arr[{j}]={arr[j]} with arr[{min_index}]={arr[min_index]}")
            if arr[j] < arr[min_index]:
                min_index = j
                print(f"      -> new min_index={min_index} (value {arr[min_index]})")
            else:
                print("      -> no change")
        # perform final swap for this iteration
        if min_index != i:
            print(f"  Swap A[{i}] ({arr[i]}) <-> A[{min_index}] ({arr[min_index]})")
            arr[i], arr[min_index] = arr[min_index], arr[i]
        else:
            print("  No swap needed (minimum already at i)")
        print("  After iteration:", arr)
    print("\nSorted result:", arr)


# -------------------------------------------------------------------------
# Interview-style explanation of loops (short & precise)
# -------------------------------------------------------------------------
LOOP_EXPLANATION = textwrap.dedent("""
Loop explanation (concise — interview-style):

Outer loop: for i in range(len(customList)):
  - 'i' points to the current position where we will place the smallest element
    from the remaining unsorted suffix.
  - After iteration i finishes, the prefix arr[0..i] is sorted and contains the
    smallest i+1 elements of the original array.

Inner loop: for j in range(i+1, len(customList)):
  - 'j' scans the unsorted suffix to find the smallest element.
  - We keep track of the index of the smallest element in min_index.

Swap step:
  - After inner loop, swap arr[i] and arr[min_index] (even if min_index == i,
    swap is a no-op). This places the smallest element into its final place.

Why ranges:
  - Outer needs only n iterations in Python (i from 0..n-1). After n-1 iterations
    the last element is already in place; the final loop does no harm but you
    can stop at n-1 if you prefer.
  - Inner goes from i+1 to n-1 because we only search the remaining unsorted part.
""")


# -------------------------------------------------------------------------
# Examples + demo (printed output like your bubble notes)
# -------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n" + "="*70)
    print("SELECTION SORT — NOTES (Python file)")
    print("="*70)

    # Print definition & flowchart
    print("\n1) DEFINITION & QUICK SUMMARY\n")
    print("Selection sort repeatedly picks the minimum element from the unsorted")
    print("portion and moves it to the sorted prefix (in-place).")
    print("\nFlowchart:")
    print(FLOWCHART)

    # Visual example
    print("\n2) SMALL VISUAL EXAMPLE\n")
    print(VISUAL_EXAMPLE)

    # Loop explanation
    print("\n3) LOOP EXPLANATION\n")
    print(LOOP_EXPLANATION)

    # Show original algorithm behavior
    print("\n" + "="*10 + " ORIGINAL FUNCTION DEMO " + "="*10)
    demo_list = [9, 2, 3, 1, 4, 6, 5, 7, 8]
    print("Input:", demo_list)
    sorted_result = selectionSort(demo_list.copy())
    print("Output:", sorted_result)

    # Verbose trace (iteration-wise)
    print("\n" + "="*10 + " VERBOSE TRACE " + "="*10)
    selectionSort_verbose([9, 2, 3, 1, 4, 6, 5, 7, 8])

    # Dry-run (step-by-step) for a small example
    print("\n" + "="*10 + " DETAILED DRY RUN " + "="*10)
    selection_sort_dry_run_example([7, 3, 5, 2])

    # Another dry-run for the user's last CList
    print("\n" + "="*10 + " DRY RUN FOR CList EXAMPLE " + "="*10)
    c_list = [9,2,3,1,4,6,5,7,8]
    selection_sort_dry_run_example(c_list)

    # Complexity summary
    print("\n" + "="*10 + " COMPLEXITY SUMMARY " + "="*10)
    print("Time complexity: O(n^2)  (best/avg/worst)")
    print("Space complexity: O(1)   (in-place)")
    print("Stability: Not stable by default (swaps change relative order of equal elements)")

    # End
    print("\nNotes saved as: SelectionSort_Notes.py (this script).")
    print("Related uploaded file path (for your slides/images):")
    print("/mnt/data/WhatsApp Image 2025-11-21 at 18.57.41.jpeg")
    print("\nDone.")
