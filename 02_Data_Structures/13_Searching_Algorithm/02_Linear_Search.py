"""
===============================================================================
📘 Linear Search — Concept, Algorithm, Pseudocode, Visualization, Dry Run
===============================================================================

Purpose
-------
Linear Search (also called Sequential Search) is the simplest searching algorithm.
It checks elements one-by-one from left to right until the target is found.

This method works for:
    ✔ Unsorted arrays
    ✔ Sorted arrays
    ✔ Small datasets
    ✔ Situations where data cannot be indexed

Linear Search is very intuitive and forms the foundation of all search algorithms.

===============================================================================
1) WHAT IS LINEAR SEARCH?
===============================================================================

• We begin from the FIRST element in the list.
• Compare it with the target.
• If equal → return index.
• If not → move to the next element.
• Continue until:
        - we find the element, OR
        - we reach the end (element not found)

Linear search does NOT skip any element → every element is checked sequentially.

Hence the name "SEQUENTIAL SEARCH".

Example:
    Searching for 7 in:
        [5, 9, 3, 1, 2, 8, 4, 7, 6]

    Check each element in order:
         5 → no
         9 → no
         3 → no
         1 → no
         2 → no
         8 → no
         4 → no
         7 → YES → found at index 7

===============================================================================
2) PSEUDOCODE OF LINEAR SEARCH
===============================================================================

FUNCTION LinearSearch(array, value):

    FOR i FROM 0 TO length(array)-1:
        IF array[i] == value:
            RETURN i
    END FOR

    RETURN -1      # if value not found


===============================================================================
3) ALGORITHM (STEP-BY-STEP)
===============================================================================

1. Start from index 0.
2. Compare array[i] with target_value.
3. If equal → return index i.
4. If not equal → move to next index.
5. Continue until end of array.
6. If loop finishes without finding target → return -1.

This is the direct implementation of the pseudocode.

===============================================================================
4) PYTHON IMPLEMENTATION (YOUR CODE)
===============================================================================
"""

def linearSearch(arr, target_value):
    # Loop through all elements of the list
    for i in range(len(arr)):

        # Check whether current element matches the target
        if arr[i] == target_value:

            # Found — return index with a message
            return f"Element found at index {i}"

    # If the loop completes, element does NOT exist
    return "Element not Present"


arr = [1,2,4,5,3,6,8,7,9]
print(linearSearch(arr, 8))
print(linearSearch(arr, 10))

"""
===============================================================================
5) DRY RUN (STEP-BY-STEP EXECUTION)
===============================================================================

Example array:
    arr = [1,2,4,5,3,6,8,7,9]
    target = 8

We will follow the loop one index at a time:

i=0 → arr[0] = 1 → 1 == 8 ? NO  
        [1, 2, 4, 5, 3, 6, 8, 7, 9]
         ↑
         i

i=1 → arr[1] = 2 → 2 == 8 ? NO  
        [1, 2, 4, 5, 3, 6, 8, 7, 9]
             ↑
             i

i=2 → arr[2] = 4 → 4 == 8 ? NO  

i=3 → arr[3] = 5 → 5 == 8 ? NO  

i=4 → arr[4] = 3 → 3 == 8 ? NO  

i=5 → arr[5] = 6 → 6 == 8 ? NO  

i=6 → arr[6] = 8 → 8 == 8 ? YES  
        Return: "Element found at index 6"

OUTPUT:
    Element found at index 6


----------------------------------------
Dry Run 2 (Target NOT Present)
----------------------------------------

target = 10

i=0 → 1 == 10 ? NO  
i=1 → 2 == 10 ? NO  
i=2 → 4 == 10 ? NO  
i=3 → 5 == 10 ? NO  
i=4 → 3 == 10 ? NO  
i=5 → 6 == 10 ? NO  
i=6 → 8 == 10 ? NO  
i=7 → 7 == 10 ? NO  
i=8 → 9 == 10 ? NO  

Loop ends → no match found.

Return:
    "Element not Present"


===============================================================================
6) ASCII VISUALIZATION OF SEARCHING PROCESS
===============================================================================

Target = 8

Index:     0   1   2   3   4   5   6   7   8
Array:    [1 | 2 | 4 | 5 | 3 | 6 | 8 | 7 | 9]

Scan each item:

Step 1:
    Checking index 0
    [1 | 2 | 4 | 5 | 3 | 6 | 8 | 7 | 9]
     ↑
     i=0

Step 2:
    Checking index 1
    [1 | 2 | 4 | 5 | 3 | 6 | 8 | 7 | 9]
         ↑
         i=1

Step 3:
    ...
Step 6:
    [1 | 2 | 4 | 5 | 3 | 6 | 8 | 7 | 9]
                         ↑
                         i=6  → FOUND!


===============================================================================
7) TIME & SPACE COMPLEXITY
===============================================================================

TIME COMPLEXITY:
    Worst Case  → O(n)      (target at the end or not present)
    Best Case   → O(1)      (target at first index)
    Average     → O(n)

SPACE COMPLEXITY:
    O(1)
    → No extra memory used.
    → Only simple variables (i, arr, target).


===============================================================================
8) WHEN TO USE LINEAR SEARCH?
===============================================================================

Use Linear Search when:
    ✔ Data is UNSORTED
    ✔ List is small
    ✔ Minimal memory usage required
    ✔ Searching happens rarely
    ✔ No indexing structure exists (like hash table or BST)

Do not use Linear Search when:
    ✘ List is large AND sorted (use Binary Search)
    ✘ You need repeated fast lookups (use Hash Table or BST)


===============================================================================
9) SUMMARY
===============================================================================

• Linear Search scans elements one-by-one.
• Works on both sorted and unsorted lists.
• Time complexity is O(n).
• Very simple and reliable for small datasets.
• Foundation of all searching algorithms.

Next:
    → Binary Search (logarithmic time, uses divide-and-conquer)
===============================================================================
"""
