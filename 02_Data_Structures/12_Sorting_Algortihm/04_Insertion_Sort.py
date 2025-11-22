"""
===============================================================================
📘 InsertionSort_Notes.py — Insertion Sort (Theory + ASCII visuals + Flowchart + Dry Runs)
===============================================================================

This file follows the exact same style as:
    - BubbleSort_Notes.py
    - SelectionSort_Notes.py

What this file includes:
------------------------
✔ Clear explanation of Insertion Sort  
✔ Real-world analogy  
✔ ASCII visualization of how elements shift  
✔ Flowchart (ASCII)  
✔ Your insertionSort() logic (unchanged)  
✔ Verbose version printing each movement  
✔ Detailed dry-run generator  
✔ Loop breakdown (interview-style)  
✔ Time/space complexity  
✔ When to use & when to avoid  

===============================================================================
"""

from typing import List
import textwrap

# -----------------------------------------------------------------------------
# 1) THEORY — WHAT IS INSERTION SORT?
# -----------------------------------------------------------------------------
THEORY = """
Insertion Sort — Simple Definition
----------------------------------
Insertion Sort divides the array into two parts:
    1) Sorted part (left side)
    2) Unsorted part (right side)

Then repeatedly:
    - Take the FIRST element from unsorted part
    - Insert it into the CORRECT position of sorted part
    - Shift elements right until the correct spot is found

This is exactly how you sort playing cards in your hand.

Key Operation:
--------------
We "shift" elements instead of swapping every time.
"""


# -----------------------------------------------------------------------------
# 2) ASCII VISUALIZATION
# -----------------------------------------------------------------------------
VISUAL = """
Example:
--------
Initial array:
    [5, 3, 4, 1]

Step-by-step:

Take 3 → insert into sorted region [5]
    3 < 5 → shift 5 right
    [3, 5 | 4, 1]

Take 4 → insert into sorted region [3, 5]
    4 < 5 → shift 5 right
    4 > 3 → stop
    [3, 4, 5 | 1]

Take 1 → insert into sorted region [3,4,5]
    shift 5 → [3,4,_,5]
    shift 4 → [3,_,4,5]
    shift 3 → [_,3,4,5]
    insert 1 at start
Final:
    [1, 3, 4, 5]
"""


# -----------------------------------------------------------------------------
# 3) ASCII FLOWCHART
# -----------------------------------------------------------------------------
FLOWCHART = """
Insertion Sort — Flowchart (ASCII)
----------------------------------

        START
          |
          v
  i = 1 to n-1
          |
          v
      key = A[i]
      j = i-1
          |
          v
  while j>=0 AND A[j] > key
          |
     shift A[j] → A[j+1]
          |
         j--
          |
          v
  place key at A[j+1]
          |
          v
       repeat i
          |
          v
        END
"""


# -----------------------------------------------------------------------------
# 4) YOUR ORIGINAL IMPLEMENTATION (UNCHANGED)
# -----------------------------------------------------------------------------
def insertionSort(customList: List[int]) -> List[int]:
    for i in range(1, len(customList)):
        key = customList[i]
        j = i - 1
        while j >= 0 and key < customList[j]:
            customList[j+1] = customList[j]
            j -= 1
        customList[j+1] = key
    return customList


# -----------------------------------------------------------------------------
# 5) VERBOSE VERSION — Step-by-step shifts + ASCII visualization
# -----------------------------------------------------------------------------
def insertionSort_verbose(customList: List[int]) -> List[int]:
    arr = customList
    print("\n=== INSERTION SORT — VERBOSE TRACE ===")
    print("Initial array:", arr)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        print(f"\n--- i = {i} | key = {key} ---")
        print("Start comparing and shifting...")

        while j >= 0 and key < arr[j]:
            print(f"  key={key} < arr[{j}]={arr[j]} → shift {arr[j]} right")
            arr[j+1] = arr[j]
            j -= 1
            print("  array:", arr)

        print(f"Insert key={key} at position {j+1}")
        arr[j+1] = key
        print("After insertion:", arr)
        print("-" * 50)

    print("Final sorted array:", arr)
    return arr


# -----------------------------------------------------------------------------
# 6) DRY-RUN GENERATOR (printed like notebook notes)
# -----------------------------------------------------------------------------
def insertionSort_dry_run(example: List[int]):
    arr = example.copy()
    print("\n=== DETAILED DRY RUN ===")
    print("Initial:", arr)

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1

        print(f"\nIteration i = {i}")
        print(f"  key = {key}")
        print(f"  Compare key with sorted part:", arr[:i])

        while j >= 0 and key < arr[j]:
            print(f"    key={key} < arr[{j}]={arr[j]} → shift arr[{j}] to arr[{j+1}]")
            arr[j+1] = arr[j]
            j -= 1
            print("    array now:", arr)

        print(f"  Insert key={key} at index {j+1}")
        arr[j+1] = key
        print("  After inserting:", arr)

    print("\nFinal sorted result:", arr)


# -----------------------------------------------------------------------------
# 7) LOOP EXPLANATION (INTERVIEW STYLE)
# -----------------------------------------------------------------------------
LOOP_EXPLANATION = textwrap.dedent("""
Loop Logic Explanation (Interview Style)
----------------------------------------

for i in range(1, n):
    - i starts at 1 because A[0] is trivially sorted
    - key = arr[i] is the element we want to insert into the sorted region A[0..i-1]

j = i - 1
    - j walks BACKWARDS through the sorted region

while j >= 0 and key < arr[j]:
    - SHIFT arr[j] one step right
    - This is the key difference from selection sort: we shift, not swap repeatedly

Finally:
    arr[j+1] = key
    - insert key in the correct position

Time Complexity:
    Worst:  O(n^2)
    Average: O(n^2)
    Best:    O(n)  (when array is almost sorted)

Space Complexity: O(1)  (in-place)
Stability: Stable (shifting keeps relative order)
""")


# -----------------------------------------------------------------------------
# 8) MAIN — Demo Runs
# -----------------------------------------------------------------------------
if __name__ == "__main__":
    print("\n" + "="*70)
    print("INSERTION SORT — FULL NOTES")
    print("="*70)

    # Print Theory + Visuals
    print(THEORY)
    print(VISUAL)
    print(FLOWCHART)

    # Loop Explanation
    print("\n" + "="*70)
    print("LOOP EXPLANATION")
    print("="*70)
    print(LOOP_EXPLANATION)

    # Demo: Original function
    print("\n" + "="*70)
    print("DEMO: ORIGINAL FUNCTION")
    print("="*70)
    demo = [2, 3, 1, 6, 5, 8]
    print("Input: ", demo)
    print("Output:", insertionSort(demo.copy()))

    # Demo: Verbose trace
    print("\n" + "="*70)
    print("DEMO: VERBOSE TRACE")
    print("="*70)
    insertionSort_verbose([2, 3, 1, 6, 5, 8])

    # Demo: Dry Run
    print("\n" + "="*70)
    print("DEMO: DETAILED DRY RUN")
    print("="*70)
    insertionSort_dry_run([2, 3, 1, 6, 5, 8])

    print("\nNotes file execution finished.")
