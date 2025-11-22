"""
===============================================================================
📘 QuickSort — Concept, Visualization & Step-by-Step Walkthrough
===============================================================================

1) WHAT IS QUICKSORT?
---------------------
QuickSort is a divide-and-conquer sorting method.

It works by:
    • Picking a pivot (we pick the FIRST element)
    • Dividing the list into:
            - Values LESS than pivot       → left side
            - Values GREATER than pivot    → right side
    • Recursively repeating the process on each side
    • When a pivot reaches its final place, it becomes "ordered"

-------------------------------------------------------------------------------

2) STARTING EXAMPLE
-------------------
We sort:
        [3, 5, 0, 6, 2, 1, 4]

Pivot = FIRST element = 3

ASCII BAR VIEW:
    (Pink = Pivot, Blue = < pivot, Yellow = > pivot)

    ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
    │ 3 │ │ 5 │ │ 0 │ │ 6 │ │ 2 │ │ 1 │ │ 4 │
    └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘
     Pink  Yellow Blue Yellow Blue Blue Yellow

-------------------------------------------------------------------------------

3) CLASSIFICATION PHASE
-----------------------
Every element is compared with the pivot.

• 5 > 3 → mark Yellow  
• 0 < 3 → mark Blue  
• 6 > 3 → mark Yellow  
• 2 < 3 → mark Blue  
• 1 < 3 → mark Blue  
• 4 > 3 → mark Yellow  

ASCII classification:

    [ 3 | 5 0 6 2 1 4 ]
      │   │ │ │ │ │ │
      │   │ │ │ │ │ └─ Yellow (>3)
      │   │ │ │ │ └─── Blue (<3)
      │   │ │ │ └───── Blue (<3)
      │   │ │ └─────── Yellow (>3)
      │   │ └───────── Blue (<3)
      │   └─────────── Yellow (>3)
      └─────────────── Pivot

-------------------------------------------------------------------------------

4) SWAP PHASE (Grouping < pivot values to the left)
---------------------------------------------------
Whenever a smaller value is found, it moves to the left section.

SWAP STEPS VISUALIZED:

Step 1: 0 < 3  
Swap with first Yellow (5)

    Before:
        [3, 5, 0, 6, 2, 1, 4]

    After:
        [3, 0, 5, 6, 2, 1, 4]
              ↑ swapped

Bar view:
    ┌───┐ ┌───┐ ┌───┐ ...
    │ 3 │ │ 0 │ │ 5 │ ...

-----------------------------------

Step 2: 2 < 3  
Swap with next Yellow (5)

    [3, 0, 2, 6, 5, 1, 4]

-----------------------------------

Step 3: 1 < 3  
Swap with next Yellow (6)

    [3, 0, 2, 1, 5, 6, 4]

Now all < pivot values are grouped together.

ASCII segmented view:

    [ 3 | 0 2 1 | 5 6 4 ]
        BlueBlueBlue YellowYellowYellow

-------------------------------------------------------------------------------

5) FINAL PIVOT SWAP
-------------------
The pivot (3) is swapped with the **last Blue element (1)**.

Before:
    [3, 0, 2, 1, 5, 6, 4]

After:
    [1, 0, 2, 3, 5, 6, 4]
                ↑ pivot now in correct place

ASCII bar:

    ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
    │ 1 │ │ 0 │ │ 2 │ │ 3 │ │ 5 │ │ 6 │ │ 4 │
    └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘
      LHS sorted part   Pivot   RHS unsorted

Pivot “3” is now correctly placed.

-------------------------------------------------------------------------------

6) RESULTING SUBLISTS
---------------------
Left of pivot (must be sorted):
        [1, 0, 2]

Right of pivot (must be sorted):
        [5, 6, 4]

QuickSort now repeats the SAME PROCESS on each side.

-------------------------------------------------------------------------------

7) LEFT SIDE: [1,0,2]
----------------------
Pivot = 1

Bars:
    ┌───┐ ┌───┐ ┌───┐
    │ 1 │ │ 0 │ │ 2 │
    └───┘ └───┘ └───┘
     Pink  Blue Yellow

Swap smaller number (0) with pivot (1):

        [0, 1, 2]

1 is now ordered.

Both sides are size 1 → automatically sorted.

-------------------------------------------------------------------------------

8) RIGHT SIDE: [5,6,4]
----------------------
Pivot = 5

Bars:
    ┌───┐ ┌───┐ ┌───┐
    │ 5 │ │ 6 │ │ 4 │
    └───┘ └───┘ └───┘
    Pink Yellow Blue

Smaller element “4” swaps with first Yellow (6):

    [5, 4, 6]

Final pivot swap:
    [4, 5, 6]

Pivot = 5 positioned correctly.

Left & right of pivot are size 1 → done.

-------------------------------------------------------------------------------

9) FINAL SORTED LIST
--------------------
Combine all the segments:

    [0, 1, 2, 3, 4, 5, 6]

-------------------------------------------------------------------------------

10) QUICK SUMMARY
------------------
QuickSort steps:
    1) Choose pivot (first element)
    2) Move all < pivot to the left
    3) Move all > pivot to the right
    4) Put pivot in its final sorted position
    5) Recur on left sublist
    6) Recur on right sublist

Visual memory:
    Pink  → pivot  
    Blue  → smaller  
    Yellow→ greater  
    Grey  → pivot placed

===============================================================================
END OF QUICK SORT NOTES
===============================================================================
"""
