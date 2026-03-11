"""
===============================================================================
📘 note_first_non_repeating.py — First Non-Repeating Element
===============================================================================

Problem
-------
Find the FIRST non-repeating element in an array.
If none exists, return 0.

Important:
- Array contains positive and negative integers
- 0 is NOT present in array
- If no unique element → return 0

===============================================================================
Example 1
===============================================================================

Input:
arr = [-1, 2, -1, 3, 2]

Frequencies
-1 → 2 times
 2 → 2 times
 3 → 1 time

First element occurring once → 3

Output → 3

===============================================================================
Example 2
===============================================================================

Input:
arr = [1,1,1]

All elements repeat

Output → 0

===============================================================================
Approach 1 — HashMap (Frequency Dictionary)
===============================================================================

Idea
----
1) Count frequency of each element
2) Traverse array again in original order
3) Return first element with frequency 1

Code (Corrected Version)
------------------------
"""

class SolutionDict:
    def firstNonRepeating(self, arr): 
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        for num in arr:   # IMPORTANT: iterate original array
            if freq[num] == 1:
                return num
        
        return 0

"""

Why We Must Iterate arr Again?
--------------------------------
If we iterate over dictionary keys directly,
we may not preserve original order in some languages.

Always check in original order to ensure FIRST non-repeating.

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(n)

===============================================================================
Dry Run (Approach 1)
===============================================================================

arr = [-1, 2, -1, 3, 2]

Step 1: Build frequency map

{
 -1:2,
  2:2,
  3:1
}

Step 2: Traverse array

-1 → freq=2 (skip)
 2 → freq=2 (skip)
-1 → freq=2 (skip)
 3 → freq=1 (return 3)

===============================================================================
Approach 2 — Queue + HashMap (Streaming Style)
===============================================================================

Idea
----
Used when elements come one by one (streaming problem).

1) Maintain frequency dictionary
2) Maintain queue of candidates
3) Remove from queue while front is repeating

Code
----
"""

from collections import deque

class SolutionQueue:
    def firstNonRepeating(self, arr):
        freq = {}
        q = deque()
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
            q.append(num)
            
            while q and freq[q[0]] > 1:
                q.popleft()
        
        return q[0] if q else 0

"""

When Is This Useful?
--------------------
✔ When input is a stream
✔ When we need real-time first non-repeating element

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(n)

===============================================================================
Comparison
===============================================================================

Method            | Time | Space | Use Case
------------------|------|-------|----------
Dictionary Only   | O(n) | O(n)  | ⭐ Best for static array
Queue + Dict      | O(n) | O(n)  | Streaming problems

===============================================================================
Edge Cases
===============================================================================

1) Single element
   arr = [5]
   → 5

2) All repeating
   arr = [2,2,3,3]
   → 0

3) Negative numbers allowed
   arr = [-1,-2,-1]
   → -2

===============================================================================
Demo Execution
===============================================================================
"""
if __name__ == "__main__":

    arr1 = [-1, 2, -1, 3, 2]
    arr2 = [1, 1, 1]
    arr3 = [4, 5, 4, 6, 5]

    print("=========== Using Dictionary Method ===========")
    s1 = SolutionDict()
    print("Input:", arr1)
    print("Output:", s1.firstNonRepeating(arr1))
    print("Input:", arr2)
    print("Output:", s1.firstNonRepeating(arr2))
    print("Input:", arr3)
    print("Output:", s1.firstNonRepeating(arr3))

    print("\n=========== Using Queue Method ===========")
    s2 = SolutionQueue()
    print("Input:", arr1)
    print("Output:", s2.firstNonRepeating(arr1))
    print("Input:", arr2)
    print("Output:", s2.firstNonRepeating(arr2))
    print("Input:", arr3)
    print("Output:", s2.firstNonRepeating(arr3))
    
"""
===============================================================================

How To Run
----------

    python note_first_non_repeating.py

===============================================================================
Interview Cheat Sheet
===============================================================================

Step 1 → Count frequencies
Step 2 → Traverse original array
Step 3 → Return first element with freq == 1

Time → O(n)
Space → O(n)

This is a classic hashing problem.

===============================================================================
"""