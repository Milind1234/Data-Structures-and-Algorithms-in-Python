"""
===============================================================================
QuickSort_Notes.py — QuickSort (code, explanation, ASCII visuals, verbose dry-run)

Includes:
 - The original quickSort implementation (unchanged logic)
 - Detailed commented explanation (algorithm + steps)
 - ASCII/bar visualizations for each pivot partition
 - A verbose dry-run helper that prints each pivot step, pointer movements
 - Final demonstration run that prints iteration-by-iteration outputs

Run this file with: python QuickSort_Notes.py

NOTE: The verbose helpers are for learning / debugging and are separate from the
pure quickSort() function shown above.
===============================================================================
"""

from typing import List
import copy

# -----------------------------------------------------------------------------
# Original swap / pivot / quickSort implementation (logic preserved)
# -----------------------------------------------------------------------------

def swap(my_list, index1, index2):
    """Swap two values in-place using Python tuple unpacking.

    Kept identical in behaviour to the provided code.
    """
    my_list[index1], my_list[index2] = my_list[index2], my_list[index1]


def pivot(my_list, pivot_index, end_index):
    """Partition (Lomuto-style) around my_list[pivot_index].

    Algorithm summary (code exactly follows this):
      - swap_index starts at pivot_index and grows when we find values < pivot
      - i scans from pivot_index+1 .. end_index
      - when my_list[i] < pivot_value: increment swap_index and swap(my_list, swap_index, i)
      - after scan swap pivot into swap_index and return swap_index

    This function mutates my_list and returns the final pivot index.
    """
    swap_index = pivot_index
    for i in range(pivot_index + 1, end_index + 1):
        if my_list[i] < my_list[pivot_index]:
            swap_index += 1
            swap(my_list, swap_index, i)
    swap(my_list, pivot_index, swap_index)
    return swap_index


def quickSort_helper(my_list, left, right):
    """Recursive helper that sorts in-place between indices left..right.

    If left < right:
      - partition using pivot()
      - recurse on left segment and right segment

    Returns the list for convenience (same mutated list is returned).
    """
    if left < right:
        pivot_index = pivot(my_list, left, right)
        quickSort_helper(my_list, left, pivot_index - 1)
        quickSort_helper(my_list, pivot_index + 1, right)
    return my_list


def quickSort(my_list: List[int]) -> List[int]:
    """Public quickSort function (returns the sorted list).

    It uses quickSort_helper to perform an in-place quick sort and returns
    the same list reference for convenience.
    """
    return quickSort_helper(my_list, 0, len(my_list) - 1)


# -----------------------------------------------------------------------------
# Visualization helpers (ASCII bars + pointer display)
# -----------------------------------------------------------------------------

def _bar_visual(arr: List[int], lo: int, hi: int, pivot_idx: int = None, swap_idx: int = None, i_idx: int = None) -> str:
    """Return a compact ASCII bar + pointer visualization for indices lo..hi.

    Example output:
      [ 3| 5| 0| 6| 2| 1| 4 ]
        p        s  i
    where p= pivot_idx, s=swap_idx, i=i_idx (only within lo..hi region)
    """
    # compact line of numbers
    seg = arr[lo:hi+1]
    vals = ' | '.join(str(x) for x in seg)
    line1 = f"[{vals}]"

    # build pointer line aligned below values
    pointers = ['   '] * len(seg)  # placeholders
    def set_ptr(idx, ch):
        if lo <= idx <= hi:
            pointers[idx - lo] = f' {ch} '

    if pivot_idx is not None:
        set_ptr(pivot_idx, 'p')
    if swap_idx is not None:
        set_ptr(swap_idx, 's')
    if i_idx is not None:
        set_ptr(i_idx, 'i')

    # create pointer string with spacing to roughly line up with values
    pointer_line = ''.join(ptr.center(len(str(seg[j])) + 3) for j, ptr in enumerate(pointers))
    return line1 + '\n' + pointer_line


# -----------------------------------------------------------------------------
# Verbose / dry-run instrumented quicksort (does not change original functions)
# -----------------------------------------------------------------------------

def partition_trace(my_list: List[int], lo: int, hi: int, step_prefix: str = '') -> (int, List[str]):
    """Run pivot partition on a copy of the list and return debug frames.

    Returns (pivot_final_index, frames) where frames is a list of strings
    describing each micro-step (pointer positions, swaps, array snapshots).
    """
    arr = my_list
    frames = []
    pivot_idx = lo
    pivot_val = arr[pivot_idx]
    swap_index = pivot_idx

    frames.append(f"{step_prefix}START partition lo={lo} hi={hi} pivot_val={pivot_val} -> {arr}")
    frames.append(_bar_visual(arr, lo, hi, pivot_idx, swap_index, None))

    for i in range(pivot_idx + 1, hi + 1):
        frames.append(f"{step_prefix}i={i}: inspecting arr[{i}]={arr[i]}")
        frames.append(_bar_visual(arr, lo, hi, pivot_idx, swap_index, i))
        if arr[i] < pivot_val:
            swap_index += 1
            frames.append(f"{step_prefix} -> arr[{i}] < pivot ({arr[i]} < {pivot_val}) -> increment swap_index -> {swap_index}")
            swap(arr, swap_index, i)
            frames.append(f"{step_prefix}swap arr[{swap_index}] and arr[{i}] -> {arr}")
            frames.append(_bar_visual(arr, lo, hi, pivot_idx, swap_index, i))
        else:
            frames.append(f"{step_prefix} -> arr[{i}] >= pivot -> no swap")

    # final pivot placement
    frames.append(f"{step_prefix}FINAL: swap pivot arr[{pivot_idx}] and arr[{swap_index}] -> place pivot at {swap_index}")
    swap(arr, pivot_idx, swap_index)
    frames.append(f"{step_prefix}After final swap: {arr}")
    frames.append(_bar_visual(arr, lo, hi, swap_index, swap_index, None))

    return swap_index, frames


def quicksort_verbose_run(original: List[int]):
    """Run a verbose, step-by-step quicksort on a copy and print dry-run frames.

    This helper simulates recursion in a readable order and prints each partition
    step (micro-steps included) so you can follow pointer movements and swaps.
    """
    arr = original.copy()
    stack = [(0, len(arr)-1, 0)]  # manual stack for deterministic printing (lo, hi, depth)

    print('\nVERBOSE QUICK SORT DRY-RUN\n')
    # We'll process partitions in a DFS manner to simulate recursion order
    while stack:
        lo, hi, depth = stack.pop()
        indent = '  ' * depth
        if lo < hi:
            print(f"{indent}--- Partition lo={lo}, hi={hi} (depth={depth}) ---")
            pivot_final, frames = partition_trace(arr, lo, hi, step_prefix=indent)
            for f in frames:
                print(indent + f)
            # push right and left partitions onto stack (right first so left processed next)
            stack.append((pivot_final + 1, hi, depth + 1))
            stack.append((lo, pivot_final - 1, depth + 1))
        else:
            print(f"{indent}(segment lo={lo} hi={hi} is trivially sorted)")
    print('\nFinal sorted array:', arr)
    return arr


# -----------------------------------------------------------------------------
# Demonstration: run both the concise quickSort (original) and verbose dry-run
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    # original code list
    my_list = [3,5,0,6,2,1,4]

    print('\n--- ORIGINAL quickSort() OUTPUT ---')
    q_input = my_list.copy()
    print('Input:', q_input)
    print('Output:', quickSort(q_input))

    # verbose dry-run (step-by-step)
    quicksort_verbose_run(my_list)


# =========================
# DETAILED DRY-RUN / NOTES
# =========================
#
# The following block is a complete, step-by-step dry-run explanation of the code
# above for the example list [3, 5, 0, 6, 2, 1, 4].
# All steps are shown as comments (so they do not affect program execution).
#
# Read through the comments to understand:
#  - how 'pivot' partitions the array,
#  - how swap_index / i / pivot_index move,
#  - what swaps happen at each iteration,
#  - how quickSort recurses after partitioning.
#
# ------------------------------------------------------------------------
# Example:
#   initial array: [3, 5, 0, 6, 2, 1, 4]
#   call pivot(my_list, pivot_index=0, end_index=6)
#
# Notation used below:
#   - Pivot value = value at pivot_index (initially index 0 → value 3)
#   - swap_index (s) starts at pivot_index and moves right whenever we find
#     a value < pivot
#   - i scans from pivot_index+1 to end_index
#   - When my_list[i] < pivot_value:
#        swap_index += 1
#        swap(my_list, swap_index, i)
#   - After finishing the i-loop, swap(my_list, pivot_index, swap_index)
#     places the pivot in its final index (swap_index).
#
# For clarity each step prints (as a comment) the array BEFORE and AFTER each swap,
# along with the pointer positions and reason for swap/no-swap.
#
# ------------------------------------------------------------------------
#
# INITIAL STATE (before partitioning)
# ----------------------------------
# array = [3, 5, 0, 6, 2, 1, 4]
# indices:  0  1  2  3  4  5  6
# pivot_index = 0, pivot_value = 3
# swap_index = pivot_index = 0
# i will iterate 1..6
#
# Visual hint (arrow positions):
#   pivot -> index 0 (value 3)
#   swap_index (s) -> index 0
#   i -> starts at index 1
#
# Representation style used below:
#   [ a | b | c | d | e | f | g ]
#    0   1   2   3   4   5   6
#    p   s   i    etc.   (p=pivot, s=swap_index, i=current i)
#
# ------------------------------------------------------------------------
# STEP-BY-STEP PARTITION (pivot at index 0, value 3)
# ------------------------------------------------------------------------
#
# Start:
# array = [3, 5, 0, 6, 2, 1, 4]
# pivot_value = 3
# swap_index = 0
#
# i = 1 -> array[1] = 5
#    Compare 5 < 3 ?  No -> no change
#    swap_index remains 0
#    array unchanged: [3, 5, 0, 6, 2, 1, 4]
#
# i = 2 -> array[2] = 0
#    Compare 0 < 3 ? Yes
#    swap_index was 0 -> increment -> swap_index = 1
#    swap positions swap_index(1) and i(2): swap 5 and 0
#    After swap:
#      array = [3, 0, 5, 6, 2, 1, 4]
#    Explanation: Now index 1 holds a value < pivot (0). Values > pivot (like 5)
#                 have been pushed right.
#
# i = 3 -> array[3] = 6
#    Compare 6 < 3 ? No -> do nothing
#    array stays: [3, 0, 5, 6, 2, 1, 4]
#    swap_index remains 1
#
# i = 4 -> array[4] = 2
#    Compare 2 < 3 ? Yes
#    swap_index was 1 -> increment -> swap_index = 2
#    swap positions swap_index(2) and i(4): swap 5 and 2
#    After swap:
#      array = [3, 0, 2, 6, 5, 1, 4]
#    Explanation: index 2 now holds 2 (< pivot). The >pivot elements get shifted right.
#
# i = 5 -> array[5] = 1
#    Compare 1 < 3 ? Yes
#    swap_index was 2 -> increment -> swap_index = 3
#    swap positions swap_index(3) and i(5): swap 6 and 1
#    After swap:
#      array = [3, 0, 2, 1, 5, 6, 4]
#    Explanation: index 3 now holds 1 (< pivot). Larger values (6) move right.
#
# i = 6 -> array[6] = 4
#    Compare 4 < 3 ? No -> do nothing
#    array remains: [3, 0, 2, 1, 5, 6, 4]
#    swap_index is 3
#
# End of i-loop.
#
# Final pivot placement:
#   swap(my_list, pivot_index, swap_index) => swap indices 0 and 3 (swap 3 and 1)
#   After swap:
#     array = [1, 0, 2, 3, 5, 6, 4]
#   The pivot (3) is now at index 3 (swap_index). This is its correct sorted position.
#
# Partition result:
#   left partition  (indices 0..2):  [1, 0, 2]  (all < 3)
#   pivot final pos (index 3)    :  [3]
#   right partition (indices 4..6):  [5, 6, 4]  (all >= 3)
#
# pivot() returns 3 (pivot final index)
#
# ------------------------------------------------------------------------
# Now quickSort_helper recursively sorts the left and right partitions.
# ------------------------------------------------------------------------
#
# Left recursion: quickSort_helper(array, left=0, right=2)
#   working subarray = [1, 0, 2] (indices relative to full array: 0..2)
#
#   Call pivot(my_list, pivot_index=0, end_index=2)
#
#   Start:
#     array segment = [1, 0, 2]
#     pivot_value = 1 (index 0)
#     swap_index = 0
#
#   i = 1 -> array[1] = 0
#     0 < 1 ? Yes
#     swap_index -> 1
#     swap positions 1 and 1 (swap 0 with itself) -> array remains [1, 0, 2]
#     (this action effectively places 0 into the left region)
#
#   i = 2 -> array[2] = 2
#     2 < 1 ? No -> do nothing
#
#   After loop: swap pivot (index 0) with swap_index (index 1)
#     swap(0,1) -> swap 1 and 0
#     array becomes: [0, 1, 2]
#
#   pivot returns index 1 (pivot 1 now at array[1])
#
#   Now left-subrecursions for this segment:
#     quickSort_helper(array, left=0, right=0) -> segment of size 1 -> trivially sorted
#     quickSort_helper(array, left=2, right=2) -> trivially sorted
#
#   Result after left branch: the left part (indices 0..2) is now [0, 1, 2]
#
# ------------------------------------------------------------------------
# Right recursion of the top-level partition:
# quickSort_helper(array, left=4, right=6)
#   working subarray (indices 4..6) = [5, 6, 4]
#
#   Call pivot(my_list, pivot_index=4, end_index=6)
#   (Remember pivot_index is relative to full array indices)
#
#   pivot_value = array[4] = 5
#   swap_index = 4
#
#   i = 5 -> array[5] = 6
#     6 < 5 ? No -> do nothing
#
#   i = 6 -> array[6] = 4
#     4 < 5 ? Yes
#     swap_index -> 5
#     swap positions 5 and 6 -> swap 6 and 4
#     array becomes (full array indices):
#       [0, 1, 2, 3, 5, 4, 6]
#     Explanation for local view (indices 4..6): we now have [5, 4, 6]
#
#   End of i-loop: swap pivot (index 4) with swap_index (index 5)
#     swap indices 4 and 5 -> swap 5 and 4
#     array becomes:
#       [0, 1, 2, 3, 4, 5, 6]
#
#   pivot returns index 5 (value 5 now at index 5)
#
#   Recurse on left of pivot (4..4): single element -> sorted
#   Recurse on right of pivot (6..6): single element -> sorted
#
# ------------------------------------------------------------------------
# Final array (after all recursion completes):
#   [0, 1, 2, 3, 4, 5, 6]
#
# This is the sorted output returned by quickSort().
#
# ------------------------------------------------------------------------
# VISUAL SUMMARY (compact)
#
# Initial: [3, 5, 0, 6, 2, 1, 4]
# Partition around pivot=3 (index 0):
#   iteration i=1: 5 >= 3  => no swap
#   iteration i=2: 0 < 3   => swap_index=1, swap(1,2) -> [3,0,5,6,2,1,4]
#   iteration i=3: 6 >= 3  => no swap
#   iteration i=4: 2 < 3   => swap_index=2, swap(2,4) -> [3,0,2,6,5,1,4]
#   iteration i=5: 1 < 3   => swap_index=3, swap(3,5) -> [3,0,2,1,5,6,4]
#   iteration i=6: 4 >= 3  => no swap
#   final swap pivot with swap_index(3): swap(0,3) -> [1,0,2,3,5,6,4]
# Left partition [1,0,2] sorted to [0,1,2]
# Right partition [5,6,4] sorted to [4,5,6]
# Final merge (conceptual) -> [0,1,2,3,4,5,6]
#
# ------------------------------------------------------------------------
# POINTER / ASCII VISUAL EXAMPLE (one of the partitioning steps)
#
# After a few steps during the first partition when swap_index=2 and i=4:
#
#  [ 3 | 0 | 2 | 6 | 5 | 1 | 4 ]
#   p    s    .    i
#
#  meaning:
#   p = pivot index (0)
#   s = swap_index (2)
#   i = current index being inspected (4)
#
# (Then because array[4] < pivot, we increment s -> 3 and swap positions 3 and 4)
#
# ------------------------------------------------------------------------
# Note on indices:
# - pivot(), quickSort_helper() operate on full-array indices (not slice copies)
# - swap_index and i are absolute indices in the full array
#
# ------------------------------------------------------------------------
# END OF DRY-RUN COMMENTS
# =========================

