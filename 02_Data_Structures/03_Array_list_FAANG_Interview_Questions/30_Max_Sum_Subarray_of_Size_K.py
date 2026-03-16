"""
===============================================================================
📘 note_max_sum_subarray_k.py — Maximum Sum Subarray of Size K
===============================================================================

Problem
-------
Given an array arr[] and integer k,
find the maximum sum of any contiguous subarray of size k.

Constraint Insight
------------------
1 ≤ k ≤ n
0 ≤ arr[i]

Expected:
Time  → O(n)
Space → O(1)

===============================================================================
Approach 1 — Sliding Window (Optimal O(n))
===============================================================================

Idea
----
Maintain a window of size k.
Add next element and remove previous element.

Code
----
"""

class SolutionSliding:
    def maxSubarraySum(self, arr, k):
        ans = 0
        window_sum = 0
        
        for i in range(len(arr)):
            window_sum += arr[i]
            
            if i >= k:
                window_sum -= arr[i-k]
            
            if i >= k-1:
                ans = max(ans, window_sum)
        
        return ans

"""
Dry Run
-------
arr = [100,200,300,400]
k = 2

Window 1: [100,200] → 300
Window 2: [200,300] → 500
Window 3: [300,400] → 700

Max = 700

Time → O(n)
Space → O(1)

===============================================================================
Approach 2 — Prefix Sum (O(n))
===============================================================================

Idea
----
Use prefix array to compute range sums quickly.

Code
----
"""

class SolutionPrefix:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        prefix = [0] * (n + 1)
        
        for i in range(n):
            prefix[i+1] = prefix[i] + arr[i]
        
        max_sum = float('-inf')
        
        for i in range(n - k + 1):
            current_sum = prefix[i+k] - prefix[i]
            max_sum = max(max_sum, current_sum)
        
        return max_sum

"""
Dry Run (FULL Prefix Iteration Breakdown)
-------
arr = [1,4,2,10,23,3,1,0,20]
k = 4

Step 1: Build Prefix Array Step-by-Step

Initialize:
prefix[0] = 0

Iteration i=0
prefix[1] = prefix[0] + 1 = 0 + 1 = 1

Iteration i=1
prefix[2] = prefix[1] + 4 = 1 + 4 = 5

Iteration i=2
prefix[3] = prefix[2] + 2 = 5 + 2 = 7

Iteration i=3
prefix[4] = prefix[3] + 10 = 7 + 10 = 17

Iteration i=4
prefix[5] = prefix[4] + 23 = 17 + 23 = 40

Iteration i=5
prefix[6] = prefix[5] + 3 = 40 + 3 = 43

Iteration i=6
prefix[7] = prefix[6] + 1 = 43 + 1 = 44

Iteration i=7
prefix[8] = prefix[7] + 0 = 44 + 0 = 44

Iteration i=8
prefix[9] = prefix[8] + 20 = 44 + 20 = 64

Final Prefix Array:
[0,1,5,7,17,40,43,44,44,64]

Step 2: Compute Every Window Using Formula

Formula:
current_sum = prefix[i+k] - prefix[i]

Window i=0 (0 to 3)
current_sum = prefix[4] - prefix[0]
= 17 - 0 = 17
max_sum = 17

Window i=1 (1 to 4)
current_sum = prefix[5] - prefix[1]
= 40 - 1 = 39
max_sum = 39

Window i=2 (2 to 5)
current_sum = prefix[6] - prefix[2]
= 43 - 5 = 38
max_sum remains 39

Window i=3 (3 to 6)
current_sum = prefix[7] - prefix[3]
= 44 - 7 = 37
max_sum remains 39

Window i=4 (4 to 7)
current_sum = prefix[8] - prefix[4]
= 44 - 17 = 27
max_sum remains 39

Window i=5 (5 to 8)
current_sum = prefix[9] - prefix[5]
= 64 - 40 = 24
max_sum remains 39

Final Answer = 39

Time → O(n)
Space → O(n)

===============================================================================
Approach 3 — Precompute First Window then Slide (Clean Sliding)
===============================================================================

Code
----
"""

class SolutionCleanSliding:
    def maxSubarraySum(self, arr, k):
        window_sum = 0
        
        for i in range(k):
            window_sum += arr[i]
        
        max_sum = window_sum
        
        for i in range(k, len(arr)):
            window_sum += arr[i] - arr[i-k]
            max_sum = max(max_sum, window_sum)
        
        return max_sum

"""
Dry Run
-------
arr = [100,200,300,400]
k = 2

Initial window → 300
Slide:
+300 -100 → 500
+400 -200 → 700

Max = 700

Time → O(n)
Space → O(1)

===============================================================================
Approach 4 — Brute Force (O(n*k))
===============================================================================

Code
----
"""

class SolutionBrute:
    def maxSubarraySum(self, arr, k):
        n = len(arr)
        max_sum = float('-inf')
        
        for i in range(n - k + 1):
            current_sum = 0
            for j in range(i, i + k):
                current_sum += arr[j]
            max_sum = max(max_sum, current_sum)
        
        return max_sum

"""
Dry Run
-------
arr = [100,200,300,400]
k = 2

Subarrays:
[100,200] → 300
[200,300] → 500
[300,400] → 700

Max = 700

Time → O(n*k)
Space → O(1)

===============================================================================
DETAILED COMPLETE DRY RUNS (STEP‑BY‑STEP)
===============================================================================

We will use the main example:

arr = [1,4,2,10,23,3,1,0,20]
k = 4

-----------------------------------------------------------------
Approach 1 — Sliding Window (Step-by-step table)
-----------------------------------------------------------------

Iteration | i | Added | Removed | Window Sum | Max
-----------------------------------------------------
Start     | - |   -   |   -     |    0       | 0

i=0 → add 1
Window size < k → no max check
Window = [1]

i=1 → add 4
Window = [1,4]

i=2 → add 2
Window = [1,4,2]

i=3 → add 10
Window = [1,4,2,10]
Window sum = 17
Max = 17

i=4 → add 23, remove 1
Window = [4,2,10,23]
Window sum = 39
Max = 39

i=5 → add 3, remove 4
Window = [2,10,23,3]
Window sum = 38
Max remains 39

i=6 → add 1, remove 2
Window = [10,23,3,1]
Window sum = 37

i=7 → add 0, remove 10
Window = [23,3,1,0]
Window sum = 27

i=8 → add 20, remove 23
Window = [3,1,0,20]
Window sum = 24

Final Answer = 39

-----------------------------------------------------------------
Approach 2 — Prefix Sum (Step-by-step)
-----------------------------------------------------------------

Build Prefix Array

Index | Value | Prefix
-----------------------
0     |   -   | 0
1     |   1   | 1
2     |   4   | 5
3     |   2   | 7
4     |  10   | 17
5     |  23   | 40
6     |   3   | 43
7     |   1   | 44
8     |   0   | 44
9     |  20   | 64

Now compute each window sum using:

sum(i to i+k-1) = prefix[i+k] - prefix[i]

Window 0-3 → prefix[4] - prefix[0] = 17
Window 1-4 → prefix[5] - prefix[1] = 40 - 1 = 39
Window 2-5 → 43 - 5 = 38
Window 3-6 → 44 - 7 = 37
Window 4-7 → 44 - 17 = 27
Window 5-8 → 64 - 40 = 24

Maximum = 39

-----------------------------------------------------------------
Approach 3 — Clean Sliding (Detailed)
-----------------------------------------------------------------

Step 1: Compute first window manually

1 + 4 + 2 + 10 = 17
max_sum = 17

Step 2: Slide window one element at a time

Move to window [4,2,10,23]
New sum = 17 + 23 - 1 = 39
max_sum = 39

Move to [2,10,23,3]
New sum = 39 + 3 - 4 = 38

Move to [10,23,3,1]
New sum = 38 + 1 - 2 = 37

Move to [23,3,1,0]
New sum = 37 + 0 - 10 = 27

Move to [3,1,0,20]
New sum = 27 + 20 - 23 = 24

Final max_sum = 39

-----------------------------------------------------------------
Approach 4 — Brute Force (Complete enumeration)
-----------------------------------------------------------------

All possible subarrays of size 4:

[1,4,2,10]  → 17
[4,2,10,23] → 39
[2,10,23,3] → 38
[10,23,3,1] → 37
[23,3,1,0]  → 27
[3,1,0,20]  → 24

Maximum = 39

===============================================================================
Comparison

===============================================================================

Method            | Time     | Space | Recommended
------------------|----------|-------|------------
Sliding Window    | O(n)     | O(1)  | ⭐ Best
Prefix Sum        | O(n)     | O(n)  | Good
Clean Sliding     | O(n)     | O(1)  | ⭐ Best
Brute Force       | O(n*k)   | O(1)  | ❌

===============================================================================
Demo Execution (Run All Approaches)
===============================================================================
"""
if __name__ == "__main__":

    arr = [1,4,2,10,23,3,1,0,20]
    k = 4

    print("Array:", arr)
    print("k:", k)

    print("\nSliding Window:")
    print(SolutionSliding().maxSubarraySum(arr, k))

    print("\nPrefix Sum:")
    print(SolutionPrefix().maxSubarraySum(arr, k))

    print("\nClean Sliding:")
    print(SolutionCleanSliding().maxSubarraySum(arr, k))

    print("\nBrute Force:")
    print(SolutionBrute().maxSubarraySum(arr, k))

"""
===============================================================================
Interview Cheat Sheet
===============================================================================

If fixed size window → THINK SLIDING WINDOW

window_sum += arr[i]
window_sum -= arr[i-k]

Time → O(n)
Space → O(1)

===============================================================================
"""