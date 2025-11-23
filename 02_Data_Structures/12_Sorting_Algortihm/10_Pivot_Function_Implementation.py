"""
===============================================================================
📘 Pivot Function Notes — Concept, Logic, Visual Breakdown
===============================================================================

Purpose
-------
This notes file explains how the pivot function works in QuickSort and why the
swap() helper is required. The explanation follows the exact flow of the
demonstration with step-by-step visualizations and pointer movements.

===============================================================================
1) SWAP FUNCTION — WHY WE NEED IT
===============================================================================

The pivot function must swap values in two different situations:

    1. When a value smaller than the pivot is found during scanning
       → it is swapped into the “left” region

    2. After the scanning finishes
       → pivot is swapped with the final swap index
         (placing pivot into its correct sorted position)

Because swapping happens in multiple places, a separate helper is used.

Explanation of swap logic:

    temp = my_list[index1]
    my_list[index1] = my_list[index2]
    my_list[index2] = temp

Python’s shorter tuple-based swapping:

    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]

This swaps both values in a single step.


===============================================================================
2) PIVOT FUNCTION — OVERVIEW
===============================================================================

The pivot function receives:

    my_list     → the list to operate on
    pivot_index → index of the chosen pivot value
    end_index   → where scanning should stop

It rearranges numbers so that:
    • all smaller numbers appear to the LEFT of the pivot
    • all larger numbers appear to the RIGHT of the pivot
    • pivot is placed into its correct sorted position

Finally, it returns the final position of the pivot (swap_index).


===============================================================================
3) INITIAL SETUP (Pointers + Example)
===============================================================================

Example list:

    [3, 5, 0, 6, 2, 1, 4]

pivot_index = 0 → pivot value = 3  
swap_index = pivot_index → starts at 0  
i pointer scans from pivot_index + 1 → starts at 1

Visualization:

       pivot     swap,i
         ↓         ↓
    [ 3 | 5 | 0 | 6 | 2 | 1 | 4 ]
      0   1   2   3   4   5   6


===============================================================================
4) LOOP LOGIC (i SCANS THE ARRAY)
===============================================================================

For each index i from pivot_index+1 to end_index:

    • If my_list[i] < pivot_value:
            swap_index += 1
            swap(my_list, swap_index, i)

    • Otherwise:
            do nothing (value stays on “right” side)


===============================================================================
5) FULL VISUAL DRY RUN OF THE PIVOT PROCESS
===============================================================================

Start:
    pivot = 3
    swap_index = 0
    i = 1

---------------------------------------------------------------------------
STEP 1 — i=1 → value = 5
---------------------------------------------------------------------------
5 > 3 → no swap

    pivot  swap   i
      ↓     ↓     ↓
    [ 3 | 5 | 0 | 6 | 2 | 1 | 4 ]
      │     │     │
      │     └─────┴─ stays (greater)
      └ pivot


---------------------------------------------------------------------------
STEP 2 — i=2 → value = 0
---------------------------------------------------------------------------
0 < 3 → small → must move left

swap_index increments:
    swap_index = 1

Swap 5 ↔ 0:

Before:
    [ 3 | 5 | 0 | 6 | 2 | 1 | 4 ]
               ▲
               i

After:
    [ 3 | 0 | 5 | 6 | 2 | 1 | 4 ]

Pointers now:
       pivot     swap      i
         ↓         ↓        ↓
    [ 3 | 0 | 5 | 6 | 2 | 1 | 4 ]


---------------------------------------------------------------------------
STEP 3 — i=3 → value = 6
---------------------------------------------------------------------------
6 > pivot → no action

    [ 3 | 0 | 5 | 6 | 2 | 1 | 4 ]
                     ↑
                     i


---------------------------------------------------------------------------
STEP 4 — i=4 → value = 2
---------------------------------------------------------------------------
2 < 3 → small → must move left

swap_index increments:
    swap_index = 2

Swap 5 ↔ 2:

Before:
    [ 3 | 0 | 5 | 6 | 2 | 1 | 4 ]
                 ↑       ↑
              swap      i

After:
    [ 3 | 0 | 2 | 6 | 5 | 1 | 4 ]


---------------------------------------------------------------------------
STEP 5 — i=5 → value = 1
---------------------------------------------------------------------------
1 < 3 → small → must move left

swap_index increments:
    swap_index = 3

Swap 6 ↔ 1:

Before:
    [ 3 | 0 | 2 | 6 | 5 | 1 | 4 ]

After:
    [ 3 | 0 | 2 | 1 | 5 | 6 | 4 ]


---------------------------------------------------------------------------
STEP 6 — i=6 → value = 4
---------------------------------------------------------------------------
4 > pivot → do nothing

Loop ends.


===============================================================================
6) FINAL STEP — PLACE THE PIVOT IN ITS CORRECT POSITION
===============================================================================

swap_index = 3  
pivot_index = 0  

Swap pivot (3) with my_list[3]:

Before:
    [ 3 | 0 | 2 | 1 | 5 | 6 | 4 ]
      ↑              ↑
    pivot           swap

After:
    [ 1 | 0 | 2 | 3 | 5 | 6 | 4 ]
                    ↑
               pivot final index


===============================================================================
7) FINAL STATE AFTER PARTITION
===============================================================================

Left partition (< pivot):
    [1, 0, 2]

Pivot in center:
    [3]

Right partition (> pivot):
    [5, 6, 4]

Returned value:
    pivot’s final index → 3


===============================================================================
8) SUMMARY OF THE PIVOT FUNCTION BEHAVIOR
===============================================================================

• swap_index begins at pivot_index
• i scans through the remaining list
• whenever a value is smaller than the pivot:
        swap_index increases
        that value is swapped to the “left area”
• after scanning:
        pivot is swapped with my_list[swap_index]
• the pivot is now in its correct sorted position
• the function returns swap_index

This index is used by QuickSort to determine the boundaries for
recursive calls on the left and right sublists.

===============================================================================
"""
"""
===============================================================================
📘 PIVOT FUNCTION — DETAILED EXPLANATION (ALGORITHM + STEPS)
===============================================================================

This file explains step-by-step how the given pivot() function works internally.
All explanation is written as Python comments to match code-note format.
===============================================================================
"""

# ------------------------------------------------------------------------------
# SWAP FUNCTION
# ------------------------------------------------------------------------------
# The swap() helper simply exchanges the values at index1 and index2.
# It is used by the pivot() function whenever we need to:
#   • move a smaller element to the "left" region
#   • move the pivot into its final position at the end
# Python's tuple unpacking lets us swap in one line.
# ------------------------------------------------------------------------------

def swap(my_list, index1, index2):
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


# ------------------------------------------------------------------------------
# PIVOT FUNCTION (PARTITION LOGIC)
# ------------------------------------------------------------------------------
# Goal of pivot():
#   Rearrange the list so that:
#       - all values smaller than pivot go to the LEFT
#       - all values greater stay on the RIGHT
#       - pivot ends in its correct sorted position
#
# Returns:
#   The final index of the pivot (called swap_index)
#
# Parameters:
#   my_list      → list to operate on
#   pivot_index  → index of pivot value (usually start of section)
#   end_index    → last index to check in this segment
# ------------------------------------------------------------------------------

def pivot(my_list, pivot_index, end_index):

    # --------------------------------------------------------------------------
    # STEP 1 — Initialize swap_index
    # --------------------------------------------------------------------------
    # swap_index starts at pivot_index.
    # It marks the boundary where smaller values will be placed.
    #
    # As we scan the list:
    #   Whenever we find a value < pivot:
    #       - we increase swap_index
    #       - swap the value at i into this new position
    #
    # At the end, swap_index becomes pivot's final sorted spot.
    # --------------------------------------------------------------------------
    swap_index = pivot_index

    # --------------------------------------------------------------------------
    # STEP 2 — Scan through the array using i
    # --------------------------------------------------------------------------
    # i moves from pivot_index + 1 to end_index.
    #
    # For each value:
    #   • If my_list[i] < pivot_value:
    #           swap_index += 1
    #           swap the element at i into position swap_index
    #
    #   • Else:
    #           do nothing (it stays on the "right side")
    #
    # This gradually builds the left region of smaller elements.
    # --------------------------------------------------------------------------
    for i in range(pivot_index + 1, end_index + 1):

        # Check if current value is smaller than pivot
        if my_list[i] < my_list[pivot_index]:

            # Move the boundary of "small values" to the right
            swap_index += 1

            # Swap the smaller element into the left region
            swap(my_list, swap_index, i)

    # --------------------------------------------------------------------------
    # STEP 3 — After scanning all elements:
    #          Put pivot into its correct sorted position
    # --------------------------------------------------------------------------
    # Swap the pivot with the value at swap_index.
    # After this:
    #   - Everything left of swap_index is < pivot
    #   - Everything right of swap_index is ≥ pivot
    # --------------------------------------------------------------------------
    swap(my_list, pivot_index, swap_index)

    # Return where the pivot finally landed
    return swap_index


# ------------------------------------------------------------------------------
# EXAMPLE USAGE
# ------------------------------------------------------------------------------
# Input list:
#   [3, 5, 0, 6, 2, 1, 4]
#
# Expected pivot position after partition:
#   -> 3 (index)
#
# Expected list after pivoting:
#   [1, 0, 2, 3, 5, 6, 4]
# ------------------------------------------------------------------------------

my_list = [3,5,0,6,2,1,4]
print(pivot(my_list, 0, 6))
print(my_list)
