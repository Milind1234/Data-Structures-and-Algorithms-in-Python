"""
===============================================================================
📘 Searching Algorithms — Time Complexity Notes (Binary Search + Linear Search)
===============================================================================
These notes explain:

    ✓ Time complexity of Linear Search  
    ✓ Time complexity of Binary Search  
    ✓ Why Binary Search is much faster  
    ✓ Step-by-step examples showing search depth expansion  
    ✓ Why doubling the array size increases steps by +1 (log₂N behavior)

Everything is written in Python-comment style for learning / revision.

===============================================================================
1) LINEAR SEARCH — TIME COMPLEXITY
===============================================================================

🔍 How it works:
----------------
Linear Search checks elements one by one:

    Start → arr[0] → arr[1] → arr[2] → ... → arr[n-1]

It stops when:
    • the element is found, OR
    • the array ends

Worst Case:
    → Element not present
    → Must scan the entire array
    → Steps = n

Best Case:
    → Element found at first index
    → Steps = 1

Average Case:
    → Element found somewhere in the middle
    → Steps ≈ n/2  → still O(n)

Time Complexity:
    • Worst:   O(n)
    • Average: O(n)
    • Best:    O(1)

Space Complexity:
    • O(1)  (no extra memory required)

Visualization:
--------------
Example array:  
    [5,9,3,4,8,2,1,7]

Search for 7:

    Step 1: 5 != 7  
    Step 2: 9 != 7  
    Step 3: 3 != 7  
    Step 4: 4 != 7  
    Step 5: 8 != 7  
    Step 6: 2 != 7  
    Step 7: 1 != 7  
    Step 8: 7 == target → FOUND  

→ Took 8 steps → O(n)

If searching for 5 (first element) → O(1)

-------------------------------------------------------------------------------


===============================================================================
2) BINARY SEARCH — TIME COMPLEXITY
===============================================================================

Binary Search works ONLY on *sorted* arrays.

Idea:
-----
Instead of eliminating ONE element each step (like linear search),
binary search eliminates HALF of the array each step.

At every step:
    middle = (left + right) // 2

    If target < middle value  → search left half  
    If target > middle value  → search right half  
    If equal                  → found  

Because we cut the search space in half each time,
the number of steps needed is log₂(N).

-------------------------------------------------------------------------------
2.1 BEST CASE — O(1)
-------------------------------------------------------------------------------
If the *first* middle element is the target:
    
    Example array: [1,2,3,4,5,6,7]  
    Search for 4:

        middle = 4 → found in 1 step

Hence, best case = O(1)

-------------------------------------------------------------------------------
2.2 WORST CASE — WHY O(logN)?
-------------------------------------------------------------------------------

Let's use an array of 16 sorted elements.

Case 1: N = 16 elements
------------------------

Step 1 → middle = 15  
Step 2 → middle = 9  
Step 3 → middle = 13  
Step 4 → middle = 11  
Step 5 → only 1 element left → not found  

Steps taken: **4**

Because:
    log₂(16) = 4

-----------------------------------------

Case 2: Double the size → N = 32 elements
-----------------------------------------

Search for: 72

Step 1 → middle = 39  
Step 2 → middle = 55  
Step 3 → middle = 68  
Step 4 → middle = 70  
Step 5 → middle = 72 → FOUND  

Steps required: **5**

Because:
    log₂(32) = 5

-----------------------------------------

Notice:
    16 → 4 steps  
    32 → 5 steps  
    array doubled → steps increased by +1

That’s logarithmic growth.

-------------------------------------------------------------------------------
2.3 WHY O(logN) IS AMAZING
-------------------------------------------------------------------------------

Comparison table for number of steps in worst-case search:

    N = number of items
    Steps = binary search depth

    N         Steps
    -------------------
    8         3
    16        4
    32        5
    64        6
    128       7
    1,000     10
    1,000,000 20

Binary Search can find an element inside a list of **one MILLION items**  
in only **20 steps**!

This is MUCH closer to O(1) than to O(n).

-------------------------------------------------------------------------------
Binary Search Complexity Summary
-------------------------------------------------------------------------------
Time:
    • Worst Case:   O(logN)
    • Average Case: O(logN)
    • Best Case:    O(1)

Space:
    • Iterative version: O(1)
    • Recursive version: O(logN) (due to recursion stack)

-------------------------------------------------------------------------------


===============================================================================
3) FULL COMPARISON — LINEAR SEARCH vs BINARY SEARCH
===============================================================================

+------------------+-----------------+----------------------+------------------+
| Algorithm        | Time Complexity | Requires Sorted Data | Space Complexity |
+------------------+-----------------+----------------------+------------------+
| Linear Search    | O(n)            | No                   | O(1)             |
| Binary Search    | O(logN)         | YES                  | O(1)             |
+------------------+-----------------+----------------------+------------------+

Which one should you choose?

Case 1: Array is UNSORTED  
    → Use Linear Search (O(n))

Case 2: Array is SORTED  
    → Use Binary Search (O(logN))  
    → MUCH faster for large datasets

Case 3: You search repeatedly  
    → Sort once, then use binary search many times  
      (Total performance improves greatly)

-------------------------------------------------------------------------------


===============================================================================
4) OPTIONAL — SHORT PYTHON CODE REFERENCE
===============================================================================

# Linear Search
def linearSearch(arr, target):
    for i in range(len(arr)):
        if arr[i] == target:
            return i
    return -1

# Binary Search (iterative)
def binarySearch(arr, target):
    start, end = 0, len(arr)-1
    while start <= end:
        mid = (start + end) // 2
        if arr[mid] == target:
            return mid
        elif target < arr[mid]:
            end = mid - 1
        else:
            start = mid + 1
    return -1

-------------------------------------------------------------------------------


===============================================================================
5) SUMMARY (INTERVIEW-READY KEY POINTS)
===============================================================================

• Linear Search → O(n)  
  → Works for ANY array  
  → Use when array unsorted and sorting is expensive

• Binary Search → O(logN)  
  → Works only for SORTED arrays  
  → Extremely fast for large datasets  
  → Best practical searching algorithm for sorted data

• Doubling the input size only adds +1 extra step in binary search  
  → logarithmic growth is slow  
  → reason why binary search ≈ O(1) in feel

===============================================================================
END OF NOTES — Time Complexity of Searching Algorithms
===============================================================================
"""
