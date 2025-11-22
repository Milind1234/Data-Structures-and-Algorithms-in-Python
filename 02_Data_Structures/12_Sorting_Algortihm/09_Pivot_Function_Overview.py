"""
===============================================================================
📘 Pivot Function — Concept + Visualization (QuickSort Helper)
===============================================================================

Goal
----
The pivot function rearranges the list so that:

    - all values smaller than the pivot are moved to the left
    - all values greater than the pivot are moved to the right

After rearranging, the pivot is placed into its correct sorted position,
and the function returns the index of that pivot.


===============================================================================
🔹 STARTING EXAMPLE
===============================================================================

Array:
    [3, 5, 0, 6, 2, 1, 4]

We choose the first element as the pivot:

    pivot_value = 3

Visualization:

    ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐ ┌───┐
    │ 3 │ │ 5 │ │ 0 │ │ 6 │ │ 2 │ │ 1 │ │ 4 │
    └───┘ └───┘ └───┘ └───┘ └───┘ └───┘ └───┘
      ↑
    pivot


===============================================================================
🔹 INITIAL POINTER SETUP
===============================================================================

The process uses two pointers:

1) i      → moves through the list (one step each loop)
2) swap   → marks where the next "less than pivot" number should go

Initial state:

    i starts at index 1 (first element after pivot)  
    swap starts at index 1 as well

Visualization:

    pivot     swap,i
      ↓         ↓
    [ 3 | 5 | 0 | 6 | 2 | 1 | 4 ]
      0   1   2   3   4   5   6


===============================================================================
🔹 LOOP & COLOR LOGIC (Concept)
===============================================================================

During scanning from left→right:

    • If arr[i] > pivot  → leave it on the right side temporarily (mark yellow)
    • If arr[i] < pivot  → swap it with arr[swap] and move swap pointer forward
                            (small numbers shift left / marked blue)

Visually:
    yellow = greater than pivot
    blue   = less than pivot
    red    = pivot


===============================================================================
🔹 STEP-BY-STEP VISUAL WALKTHROUGH
===============================================================================

STEP 1 — Compare 5 with pivot 3
--------------------------------
5 > 3 → leave it, color yellow

    [ 3 | 5 | 0 | 6 | 2 | 1 | 4 ]
      ↑    ↑
    pivot  i,swap stays


STEP 2 — Compare 0 with pivot 3
--------------------------------
0 < 3 → this belongs on the left  
Swap arr[i] with arr[swap]

Before swap:

    pivot   swap   i
      ↓      ↓     ↓
    [ 3 | 5 | 0 | 6 | 2 | 1 | 4 ]
          yellow   blue

Swap 5 and 0:

    [ 3 | 0 | 5 | 6 | 2 | 1 | 4 ]
      ↑    ↑
    pivot  swap moves → 2

swap pointer moves to next index:

    swap = 2
    i moves to 3


STEP 3 — Compare 6 with pivot 3
--------------------------------
6 > 3 → leave it yellow

    [ 3 | 0 | 5 | 6 | 2 | 1 | 4 ]
      ↑            ↑
    pivot          i


STEP 4 — Compare 2 with pivot 3
--------------------------------
2 < 3 → small → must move left

swap index currently at 2

Before swap:

      pivot  swap   i
       ↓      ↓     ↓
    [ 3 | 0 | 5 | 6 | 2 | 1 | 4 ]

Swap 5 and 2:

    [ 3 | 0 | 2 | 6 | 5 | 1 | 4 ]

swap → swap + 1 = 3  
i    → i + 1 = 5


STEP 5 — Compare 1 with pivot 3
--------------------------------
1 < 3 → again small → swap with arr[swap]

Before swap:

      pivot       swap   i
       ↓          ↓      ↓
    [ 3 | 0 | 2 | 6 | 5 | 1 | 4 ]

Swap 6 and 1:

    [ 3 | 0 | 2 | 1 | 5 | 6 | 4 ]

swap → 4  
i    → 6


STEP 6 — Compare 4 with pivot 3
--------------------------------
4 > pivot → yellow

No swap.



===============================================================================
🔹 FINAL SWAP — PUT PIVOT IN CORRECT POSITION
===============================================================================

Now the loop is finished.

Final step:
Swap pivot (index 0) with element at swap index.

Current state before final swap:

    pivot index = 0
    swap index  = 3

    [ 3 | 0 | 2 | 1 | 5 | 6 | 4 ]
      ↑              ↑
    pivot           swap

Swap pivot with arr[swap]:

    [ 1 | 0 | 2 | 3 | 5 | 6 | 4 ]
                    ↑
                  pivot's final position


===============================================================================
🔹 FINAL RESULT OF PARTITION
===============================================================================

Left side (< pivot):
    [ 1, 0, 2 ]

Pivot:
    [ 3 ]  ← now in correct sorted position

Right side (> pivot):
    [ 5, 6, 4 ]

Combined:

    [ 1, 0, 2, 3, 5, 6, 4 ]

The pivot function returns:
    swap index (in this example → 3)


===============================================================================
🔹 SUMMARY
===============================================================================

• pivot = first element  
• i scans the list  
• swap tracks the boundary where "smaller than pivot" elements should be placed  
• each time arr[i] < pivot:
        swap elements → move swap right  
• after loop, swap pivot with arr[swap]  
• return swap index

This index splits the array into:
    left  → values < pivot  
    pivot → correct sorted position  
    right → values > pivot

===============================================================================
"""
