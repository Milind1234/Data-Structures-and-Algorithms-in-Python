"""
===============================================================================
📘 note_kadanes_algorithm.py — Maximum Subarray Sum (Kadane's Algorithm)
===============================================================================

Problem
-------
Given an integer array arr[], find the maximum sum of a subarray.

Important:
- Subarray must be continuous.
- Must contain at least one element.

===============================================================================
Example 1
===============================================================================

Input:
arr = [2, 3, -8, 7, -1, 2, 3]

Best subarray:
[7, -1, 2, 3]

Sum = 11

===============================================================================
Example 2 (All Negative Case)
===============================================================================

Input:
arr = [-2, -4]

Best subarray:
[-2]

Output = -2

Important:
Even if all numbers are negative,
we must return the largest (least negative) number.

===============================================================================
Approach 1 — Brute Force (O(n²))
===============================================================================

Idea
----
Check every possible subarray.
Keep track of maximum sum.

Code
----
"""

class SolutionBrute:
    def maxSubArraySum(self, arr):
        n = len(arr)
        max_sum = float("-inf")
        
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += arr[j]
                max_sum = max(max_sum, current_sum)
        
        return max_sum

"""

Time Complexity
---------------
Outer loop → n
Inner loop → n

Total → O(n²)

Space Complexity → O(1)

===============================================================================
Approach 2 — Kadane's Algorithm (O(n))
===============================================================================

Core Idea
---------
At each position, decide:

Should we:
1) Extend the current subarray?
OR
2) Start a new subarray from this element?

Key Formula
-----------

current_sum = max(arr[i], current_sum + arr[i])
max_sum = max(max_sum, current_sum)

Code (Standard Version)
------------------------
"""

class SolutionKadane:
    def maxSubArraySum(self, arr):
        max_sum = float("-inf")
        current_sum = 0
        
        for num in arr:
            current_sum += num
            current_sum = max(current_sum, num)
            max_sum = max(max_sum, current_sum)
        
        return max_sum

"""

Time Complexity → O(n)
Space Complexity → O(1)

===============================================================================
Dry Run (Kadane)
===============================================================================

arr = [2, 3, -8, 7, -1, 2, 3]

Step-by-step:

Start
max_sum = -inf
current_sum = 0

2 → current = 2 → max = 2
3 → current = 5 → max = 5
-8 → current = -3 → max = 5
7 → current = 7 → max = 7
-1 → current = 6 → max = 7
2 → current = 8 → max = 8
3 → current = 11 → max = 11

Final Answer = 11

===============================================================================
Approach 3 — Kadane with Subarray Tracking
===============================================================================

We can also return the actual subarray.

Code (Your Version)
--------------------
"""

class SolutionKadaneWithSubarray:
    def maxSubArraySum(self, arr):
        max_sum = arr[0]
        current_sum = arr[0]
        start = end = temp_start = 0

        for i in range(1, len(arr)):
            if arr[i] > current_sum + arr[i]:
                current_sum = arr[i]
                temp_start = i
            else:
                current_sum += arr[i]

            if current_sum > max_sum:
                max_sum = current_sum
                start = temp_start
                end = i

        return max_sum, arr[start:end+1]

"""

===============================================================================
Dry Run (Kadane with Subarray Tracking)
===============================================================================

Example:
arr = [2, 3, -8, 7, -1, 2, 3]

Initialize:
max_sum = 2
current_sum = 2
start = 0, end = 0, temp_start = 0

i = 1 (value = 3)
current_sum + 3 = 5 > 3 → extend subarray
current_sum = 5
max_sum updated to 5
start = 0, end = 1

i = 2 (value = -8)
current_sum + (-8) = -3 > -8 → extend
current_sum = -3
max_sum remains 5

i = 3 (value = 7)
7 > (-3 + 7 = 4) → start new subarray
current_sum = 7
temp_start = 3
max_sum updated to 7
start = 3, end = 3

i = 4 (value = -1)
current_sum + (-1) = 6 > -1 → extend
current_sum = 6
max_sum remains 7

i = 5 (value = 2)
current_sum + 2 = 8 > 2 → extend
current_sum = 8
max_sum updated to 8
start = 3, end = 5

i = 6 (value = 3)
current_sum + 3 = 11 > 3 → extend
current_sum = 11
max_sum updated to 11
start = 3, end = 6

Final Result:
max_sum = 11
subarray = arr[3:7] = [7, -1, 2, 3]

===============================================================================
Visualization
===============================================================================

Think of it like:

If current sum becomes negative,
it will only hurt future sums.

So we reset.

Negative prefix → discard it.

===============================================================================
Edge Cases
===============================================================================

1) Single element
   arr = [5] → 5

2) All negative
   arr = [-3,-2,-1] → -1

3) All positive
   arr = [1,2,3] → 6

===============================================================================
Comparison
===============================================================================

Method        | Time   | Space | Recommended
--------------|--------|-------|------------
Brute Force   | O(n²)  | O(1)  | ❌
Kadane        | O(n)   | O(1)  | ⭐ Best

===============================================================================
Demo Execution
===============================================================================
"""
if __name__ == "__main__":

    arr = [2, 3, -8, 7, -1, 2, 3]

    print("=========== Brute Force ===========")
    s1 = SolutionBrute()
    print("Max Sum:", s1.maxSubArraySum(arr))

    print("\n=========== Kadane (Sum Only) ===========")
    s2 = SolutionKadane()
    print("Max Sum:", s2.maxSubArraySum(arr))

    print("\n=========== Kadane (With Subarray) ===========")
    s3 = SolutionKadaneWithSubarray()
    print("Max Sum and Subarray:", s3.maxSubArraySum(arr))
"""
===============================================================================

How To Run
----------

    python note_kadanes_algorithm.py

===============================================================================
Interview Cheat Sheet
===============================================================================

Formula:

current_sum = max(arr[i], current_sum + arr[i])
max_sum = max(max_sum, current_sum)

Time  → O(n)
Space → O(1)

If interviewer says:
"Maximum Subarray"

Immediately think → KADANE

===============================================================================
"""