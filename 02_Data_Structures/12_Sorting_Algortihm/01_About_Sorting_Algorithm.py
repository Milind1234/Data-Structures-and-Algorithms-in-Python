"""
===============================================================================
📘 SORTING — THEORY NOTES (Python Style Documentation)
===============================================================================

Sorting:
--------
Sorting means arranging elements in a specific order — typically Ascending or
Descending.

Practical Uses:
---------------
1) Microsoft Excel → Sort columns (A→Z, Small→Large, Date sorting)
2) Online shopping (Amazon, Flipkart) → sort products by price, rating, reviews
3) Databases → ORDER BY uses sorting internally

===============================================================================
TYPES OF SORTING
===============================================================================
Sorting algorithms are classified based on:

1) Space Used
2) Stability

===============================================================================
1️⃣ SPACE USED
===============================================================================

A) **In-place Sorting**
-----------------------
• Sorting algorithms that do NOT require extra space  
• They modify the original array  
• Space Complexity → O(1)

Example:
    Bubble Sort  
    Selection Sort  
    Insertion Sort  

📌 Visualization:
Before → [70, 10, 80, 30, 20, 40, 60, 50, 90]
After  → [10, 20, 30, 40, 50, 60, 70, 80, 90]

---------------------------------------------------------------

B) **Out-place Sorting**
------------------------
• Requires EXTRA space for sorting  
• Space Complexity → O(n)

Example:
    Merge Sort  
    Bucket Sort

📌 Visualization:
Original: [70, 10, 80, 30, 20]
TempArr: [10, 20, 30, 70, 80]   ← extra space used

===============================================================================
2️⃣ STABILITY
===============================================================================

A) **Stable Sorting**
---------------------
• If identical elements maintain their relative order  
• Useful when sorting records with multiple keys

Example:
    Insertion Sort  
    Merge Sort  
    Bubble Sort  

📌 Example:
Unsorted → [40(green), 20, 40(red), 60]
Sorted   → [20, 40(green), 40(red), 60]  
Order preserved → Stable ✔️

---------------------------------------------------------------

B) **Unstable Sorting**
-----------------------
• Identical elements may change order  
• Faster sometimes, but loses original sequence

Example:
    Quick Sort  
    Heap Sort  
    Selection Sort  

📌 Example:
Unsorted → [40(green), 20, 40(red), 60]
Sorted   → [20, 40(red), 40(green), 60]  
Order changed → Unstable ❌

---------------------------------------------------------------
📌 REAL EXAMPLE (STABILITY)

Unsorted Data:
    (Renad, 7)
    (Nick, 6)
    (Richard, 6)
    (Parker, 7)
    (Sofia, 7)

Sorted by name:
    Nick, Parker, Renad, Richard, Sofia

Stable Sort by age:
    Nick(6), Richard(6), Parker(7), Renad(7), Sofia(7)  ← Order kept ✔️

Unstable Sort by age:
    Nick(6), Richard(6), Renad(7), Parker(7), Sofia(7) ← Order changed ❌


===============================================================================
SORTING TERMINOLOGY
===============================================================================
--------------------
1) Increasing Order:
--------------------

Definition:
A sequence is in increasing order if every element is strictly smaller than the element that follows it.

a[i] < a[i+1]
Example → 1, 3, 5, 7, 9
(Each element is strictly greater than the previous one.)

--------------------
2) Decreasing Order:
--------------------

Definition:
A sequence is in decreasing order if every element is strictly greater than the next element.

a[i] > a[i+1]
Example → 11, 9, 7, 5, 3, 1
(Each element is strictly smaller than the one before.)

------------------------
3) Non-Increasing Order:
------------------------

Definition:
A sequence is in non-increasing order if every element is greater than or equal to the next element.

Duplicates are allowed.
a[i] >= a[i+1]  (duplicates allowed)
Example → 11, 9, 7, 5, 5, 3, 1
(The equal pair “5, 5” is allowed.)

------------------------
4) Non-Decreasing Order:
------------------------

Definition:
A sequence is in non-decreasing order if every element is less than or equal to the next element.
Duplicates are allowed.

a[i] <= a[i+1]  (duplicates allowed)
Example → 1, 3, 5, 7, 7, 9, 11
(The equal pair “7, 7” is allowed.)

NOTE:
-----
“Non” means duplicates are allowed.

===============================================================================
LIST OF SORTING ALGORITHMS
===============================================================================

1) Bubble Sort         (Stable, In-place)
2) Selection Sort      (Unstable, In-place)
3) Insertion Sort      (Stable, In-place)
4) Bucket Sort         (Stable, Out-place)
5) Merge Sort          (Stable, Out-place)
6) Quick Sort          (Unstable, In-place)
7) Heap Sort           (Unstable, In-place)

===============================================================================
How to choose a sorting algorithm?
===============================================================================

Based on:

1) Stability required?
   • YES → Merge Sort, Insertion Sort  
   • NO  → Quick Sort, Heap Sort

2) Space Available?
   • Low memory → choose In-place (Quick Sort / Heap Sort / Selection Sort)
   • High memory → Merge Sort (very fast)

3) Time Efficient?
   • Merge Sort → O(n log n) guaranteed
   • Quick Sort → best average performer but worst case O(n²)

===============================================================================
END OF NOTES
===============================================================================
"""
"""
sorting_notes.py

Comprehensive Python notes for sorting algorithms.
Includes:
 - Definitions (increasing/decreasing/non-...)
 - ASCII visualizations for common sorting algorithms
 - Flowcharts (ASCII) for bubble, selection, insertion, quick, merge
 - Simple Python implementations (clean, commented)
 - Small helpers to print the ASCII diagrams

Usage: open this file and call any `print_*()` functions to see ASCII diagrams.

"""

# ---------------------------------------------------------------------------
# Definitions (short)
# ---------------------------------------------------------------------------
INCREASING = "a[i] < a[i+1]"
DECREASING = "a[i] > a[i+1]"
NON_INCREASING = "a[i] >= a[i+1]"
NON_DECREASING = "a[i] <= a[i+1]"

# ---------------------------------------------------------------------------
# ASCII Visualizations helpers
# ---------------------------------------------------------------------------

def _format_arr(arr):
    """Return a single-line boxed representation of the array."""
    return " ".join(f"[{x}]" for x in arr)


def print_step(title, arr):
    print(title)
    print(_format_arr(arr))
    print()

# ---------------------------------------------------------------------------
# Visual: Bubble Sort (example steps)
# ---------------------------------------------------------------------------

def ascii_bubble_example():
    """Show step-by-step array evolution for bubble sort (small example)."""
    arr = [70, 10, 80, 30, 20]
    print("BUBBLE SORT - example steps")
    print("Initial:")
    print_step("", arr)

    # pass 1
    if arr[0] > arr[1]: arr[0], arr[1] = arr[1], arr[0]
    print_step("After compare (0,1):", arr)
    if arr[1] > arr[2]: arr[1], arr[2] = arr[2], arr[1]
    print_step("After compare (1,2):", arr)
    if arr[2] > arr[3]: arr[2], arr[3] = arr[3], arr[2]
    print_step("After compare (2,3):", arr)
    if arr[3] > arr[4]: arr[3], arr[4] = arr[4], arr[3]
    print_step("After compare (3,4) -> end pass 1:", arr)

    # pass 2 (shortened)
    for i in range(3):
        if arr[i] > arr[i+1]: arr[i], arr[i+1] = arr[i+1], arr[i]
    print_step("After pass 2 (3 compares):", arr)

    # final pass
    arr.sort()
    print_step("Final (sorted):", arr)

# ASCII diagram (compact)
BUBBLE_ASCII = r'''
Bubble Sort (pairwise swaps, largest bubbles to end)

Initial: [70] [10] [80] [30] [20]
Compare 70 & 10 -> swap -> [10] [70] [80] [30] [20]
Compare 70 & 80 -> no swap -> [10] [70] [80] [30] [20]
Compare 80 & 30 -> swap -> [10] [70] [30] [80] [20]
Compare 80 & 20 -> swap -> [10] [70] [30] [20] [80]
(pass 1 complete: biggest element 80 at rightmost)
...continue passes until fully sorted
'''

# ---------------------------------------------------------------------------
# Visual: Selection Sort (example + ASCII)
# ---------------------------------------------------------------------------

def ascii_selection_example():
    arr = [64, 25, 12, 22, 11]
    print("SELECTION SORT - example steps")
    print_step("Initial:", arr)

    # select min for position 0
    mn_idx = arr.index(min(arr))
    arr[0], arr[mn_idx] = arr[mn_idx], arr[0]
    print_step("Place min at pos 0:", arr)

    # select min for position 1
    mn_idx = 1 + arr[1:].index(min(arr[1:]))
    arr[1], arr[mn_idx] = arr[mn_idx], arr[1]
    print_step("Place min at pos 1:", arr)

    # finish with builtin sort for brevity
    arr.sort()
    print_step("Final (sorted):", arr)

SELECTION_ASCII = r'''
Selection Sort (select min and put to front)

Initial: [64] [25] [12] [22] [11]
Find min(64..11) = 11 -> swap with index0 -> [11] [25] [12] [22] [64]
Find min(index1..end) = 12 -> swap with index1 -> [11] [12] [25] [22] [64]
...repeat
'''

# ---------------------------------------------------------------------------
# Visual: Insertion Sort (example + ASCII)
# ---------------------------------------------------------------------------

def ascii_insertion_example():
    arr = [70, 10, 80, 30]
    print("INSERTION SORT - example steps")
    print_step("Initial:", arr)

    # insert 10 into sorted [70]
    key = arr[1]
    j = 0
    while j >= 0 and arr[j] > key:
        arr[j+1] = arr[j]
        j -= 1
    arr[j+1] = key
    print_step("Insert 10 into sorted left:", arr)

    # insert 80 (already in place)
    print_step("Insert 80 (already in place):", arr)

    # insert 30
    # simplified using sort for remainder
    arr.sort()
    print_step("Final (sorted):", arr)

INSERTION_ASCII = r'''
Insertion Sort (builds sorted prefix)

Initial: [70] [10] [80] [30]
Take 10, insert into [70] -> [10] [70] [80] [30]
Take 80, insert -> stays -> [10] [70] [80] [30]
Take 30, insert -> [10] [30] [70] [80]
'''

# ---------------------------------------------------------------------------
# Visual: Merge Sort (ASCII + minimal depiction)
# ---------------------------------------------------------------------------

MERGE_ASCII = r'''
Merge Sort (divide & conquer)

Start: [38] [27] [43] [3] [9] [82] [10]
Split -> left: [38 27 43]    right: [3 9 82 10]
Split recursively until single elements
Merge back sorted pairs to get final sorted array
Example merge step:
  merge [27] and [38] -> [27 38]
  merge [3] and [9] -> [3 9]
  ...
'''

# Simple merge helper (not full trace)

def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    mid = len(arr) // 2
    left = merge_sort(arr[:mid])
    right = merge_sort(arr[mid:])
    # merge
    i = j = 0
    out = []
    while i < len(left) and j < len(right):
        if left[i] <= right[j]:
            out.append(left[i]); i += 1
        else:
            out.append(right[j]); j += 1
    out.extend(left[i:]); out.extend(right[j:])
    return out

# ---------------------------------------------------------------------------
# Visual: Quick Sort (ASCII + partition concept)
# ---------------------------------------------------------------------------

QUICK_ASCII = r'''
Quick Sort (pick pivot, partition around pivot)

Start: [10] [80] [30] [90] [40] [50] [70]
Choose pivot (e.g., last=70)
Partition -> elements <= 70 to left, >70 to right
After partition: [10 30 40 50] [70] [80 90]
Recursively quicksort left and right
'''

# ---------------------------------------------------------------------------
# Visual: Heap Sort (ASCII brief)
# ---------------------------------------------------------------------------

HEAP_ASCII = r'''
Heap Sort (build max heap, then extract max to end repeatedly)

Array -> build max-heap in-place
Max-heap example: root is largest element
Swap root with last element, reduce heap size, heapify
Repeat until sorted
'''

# ---------------------------------------------------------------------------
# ASCII Flowcharts (very compact) for requested algorithms
# ---------------------------------------------------------------------------

FLOW_BUBBLE = r'''
Bubble Sort Flowchart (compact ASCII)

+-------------------------------+
| start                         |
+-------------------------------+
           |
           v
+-------------------------------+
| for i in 0..n-1               |
+-------------------------------+
           |
           v
+-------------------------------+
| for j in 0..n-i-2             |
+-------------------------------+
           |
           v
+-------------------------------+
| if a[j] > a[j+1] then swap    |
+-------------------------------+
           |
           v
+-------------------------------+
| end inner loop                |
+-------------------------------+
           |
           v
+-------------------------------+
| end outer loop                |
+-------------------------------+
           |
           v
+-------------------------------+
| done (array sorted)           |
+-------------------------------+
'''

FLOW_SELECTION = r'''
Selection Sort Flowchart (compact ASCII)

+------------------+
| start            |
+------------------+
        |
        v
+------------------+
| for i in 0..n-2  |
+------------------+
        |
        v
+------------------+
| find min index k |
+------------------+
        |
        v
+------------------+
| swap a[i], a[k]  |
+------------------+
        |
        v
+------------------+
| end for          |
+------------------+
        |
        v
+------------------+
| done             |
+------------------+
'''

FLOW_INSERTION = r'''
Insertion Sort Flowchart (compact ASCII)

+---------------+
| start         |
+---------------+
      |
      v
+---------------+
| for i in 1..n |
+---------------+
      |
      v
+---------------+
| key = a[i]    |
+---------------+
      |
      v
+---------------+
| j = i-1       |
+---------------+
      |
      v
+-------------------------------+
| while j>=0 and a[j] > key     |
|   a[j+1] = a[j]; j -= 1       |
+-------------------------------+
      |
      v
+---------------+
| a[j+1] = key  |
+---------------+
      |
      v
+---------------+
| end for       |
+---------------+
      |
      v
+---------------+
| done          |
+---------------+
'''

FLOW_MERGE = r'''
Merge Sort Flowchart (compact ASCII)

+----------------+
| start          |
+----------------+
      |
      v
+---------------------------+
| if len(a) <= 1 return a   |
+---------------------------+
      |
      v
+---------------------------+
| mid = n//2                |
| left = merge_sort(a[:mid])|
| right = merge_sort(a[mid:])|
+---------------------------+
      |
      v
+---------------------------+
| merge left and right      |
+---------------------------+
      |
      v
+----------------+
| return merged  |
+----------------+
'''

FLOW_QUICK = r'''
Quick Sort Flowchart (compact ASCII)

+----------------+
| start          |
+----------------+
      |
      v
+---------------------------+
| if len(a) <=1 return a    |
+---------------------------+
      |
      v
+---------------------------+
| pivot = choose_pivot(a)   |
| left = [x<=pivot]         |
| right = [x>pivot]         |
+---------------------------+
      |
      v
+---------------------------+
| return quick(left) + [pivot] + quick(right)
+---------------------------+
'''

# ---------------------------------------------------------------------------
# Compact implementations (for reference)
# ---------------------------------------------------------------------------

def bubble_sort(a):
    n = len(a)
    arr = a[:]  # copy
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
    return arr


def selection_sort(a):
    arr = a[:]
    n = len(arr)
    for i in range(n-1):
        min_idx = i
        for j in range(i+1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def insertion_sort(a):
    arr = a[:]
    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j+1] = arr[j]
            j -= 1
        arr[j+1] = key
    return arr


def quick_sort(a):
    if len(a) <= 1:
        return a[:]
    pivot = a[len(a)//2]
    left = [x for x in a if x < pivot]
    mid = [x for x in a if x == pivot]
    right = [x for x in a if x > pivot]
    return quick_sort(left) + mid + quick_sort(right)

# ---------------------------------------------------------------------------
# Print helpers to expose ASCII diagrams/flowcharts
# ---------------------------------------------------------------------------

def print_all_diagrams():
    print("--- ORDER DEFINITIONS ---")
    print(f"Increasing: {INCREASING}")
    print(f"Decreasing: {DECREASING}")
    print(f"Non-Increasing: {NON_INCREASING}")
    print(f"Non-Decreasing: {NON_DECREASING}")
    print()

    print("--- BUBBLE ASCII ---")
    print(BUBBLE_ASCII)
    print("--- SELECTION ASCII ---")
    print(SELECTION_ASCII)
    print("--- INSERTION ASCII ---")
    print(INSERTION_ASCII)
    print("--- MERGE ASCII ---")
    print(MERGE_ASCII)
    print("--- QUICK ASCII ---")
    print(QUICK_ASCII)
    print("--- HEAP ASCII ---")
    print(HEAP_ASCII)

    print("\n--- FLOWCHARTS ---\n")
    print(FLOW_BUBBLE)
    print(FLOW_SELECTION)
    print(FLOW_INSERTION)
    print(FLOW_MERGE)
    print(FLOW_QUICK)

# ---------------------------------------------------------------------------
# If executed directly, print a compact set of notes / diagrams
# ---------------------------------------------------------------------------
if __name__ == '__main__':
    print_all_diagrams()
    print('\n--- Example runs ---\n')
    print('Bubble example:')
    ascii_bubble_example()
    print('\nSelection example:')
    ascii_selection_example()
    print('\nInsertion example:')
    ascii_insertion_example()
    print('\nMerge sort demo: merge_sort([38,27,43,3,9,82,10]) ->')
    print(merge_sort([38,27,43,3,9,82,10]))
    print('\nQuick sort demo: quick_sort([10,80,30,90,40,50,70]) ->')
    print(quick_sort([10,80,30,90,40,50,70]))
