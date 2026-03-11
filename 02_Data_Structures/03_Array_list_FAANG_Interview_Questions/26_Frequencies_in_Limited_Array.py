"""
===============================================================================
📘 note_frequency_limited_array.py — Frequencies in a Limited Array
===============================================================================

Problem
-------
Given an array arr[] of size n where:

    1 ≤ arr[i] ≤ n

We must return an array result[] of size n such that:

    result[i] = frequency of number (i+1)

(1-based number mapping to 0-based index)

Example
-------
arr = [2, 3, 2, 3, 5]
n = 5

Numbers from 1 to 5

1 → 0 times
2 → 2 times
3 → 2 times
4 → 0 times
5 → 1 time

Output:
[0, 2, 2, 0, 1]

===============================================================================
Important Observation
===============================================================================

Since elements are in range 1 to n,
we can directly use an array of size n for counting.

Index mapping:

Number x  → index x-1

===============================================================================
Approach 1 — Using Frequency Array (Best & Optimal)
===============================================================================

Idea
----
1) Create freq array of size n
2) Traverse arr
3) Increment freq[num-1]

Code
----
"""

class SolutionArray:
    def frequencyCount(self, arr):
        n = len(arr)
        freq = [0] * n
        
        for num in arr:
            freq[num - 1] += 1
        
        return freq

"""

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(n)

Why This Is Best
----------------
✔ Uses given constraints efficiently
✔ Fastest approach
✔ Simple logic

===============================================================================
Approach 2 — Using Dictionary (HashMap)
===============================================================================

Idea
----
Count using dictionary, then build result array.

Code
----
"""

class SolutionDict:
    def frequencyCount(self, arr):
        n = len(arr)
        freq = {}
        
        for num in arr:
            freq[num] = freq.get(num, 0) + 1
        
        result = [0] * n
        for i in range(1, n + 1):
            result[i - 1] = freq.get(i, 0)
        
        return result

"""

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(n)

When Useful?
------------
✔ When range is NOT limited to 1..n

===============================================================================
Approach 3 — Using collections.Counter
===============================================================================

Code
----
"""

from collections import Counter

class SolutionCounter:
    def frequencyCount(self, arr):
        n = len(arr)
        count = Counter(arr)
        
        return [count.get(i, 0) for i in range(1, n + 1)]

"""

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(n)

Pros
----
✔ Clean
✔ Pythonic

===============================================================================
Dry Run
===============================================================================

arr = [3,3,3,3]
n = 4

freq = [0,0,0,0]

num = 3 → freq[2] += 1 → [0,0,1,0]
num = 3 → [0,0,2,0]
num = 3 → [0,0,3,0]
num = 3 → [0,0,4,0]

Final result
[0,0,4,0]

===============================================================================
Comparison Table
===============================================================================

Method        | Time | Space | Recommended
--------------|------|-------|------------
Array Count   | O(n) | O(n)  | ⭐ Best
Dictionary    | O(n) | O(n)  | Good
Counter       | O(n) | O(n)  | Cleanest

===============================================================================
Demo Execution (Run to See Output)
===============================================================================
"""
if __name__ == "__main__":

    arr1 = [2, 3, 2, 3, 5]
    arr2 = [3, 3, 3, 3]
    arr3 = [1]

    print("=========== Using Array Method ===========")
    s1 = SolutionArray()
    print("Input:", arr1)
    print("Output:", s1.frequencyCount(arr1))
    print("Input:", arr2)
    print("Output:", s1.frequencyCount(arr2))
    print("Input:", arr3)
    print("Output:", s1.frequencyCount(arr3))

    print("\n=========== Using Dictionary Method ===========")
    s2 = SolutionDict()
    print("Input:", arr1)
    print("Output:", s2.frequencyCount(arr1))

    print("\n=========== Using Counter Method ===========")
    s3 = SolutionCounter()
    print("Input:", arr1)
    print("Output:", s3.frequencyCount(arr1))
"""
===============================================================================
Interview Tip
===============================================================================

If interviewer mentions:

"Values are between 1 and n"

Immediately think:

→ Direct index mapping (value - 1)

This pattern appears frequently in DSA problems.

===============================================================================
"""