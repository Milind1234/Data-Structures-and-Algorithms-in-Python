"""
===============================================================================
📘 note_equal_sum_equilibrium.py — Equilibrium Index (Equal Left & Right Sum)
===============================================================================

Problem
-------
Given an array arr[], determine if there exists an index such that:

    Sum of elements on LEFT == Sum of elements on RIGHT

Important:
If there are no elements on left or right, that side sum is considered 0.

This is also called:
    ✔ Equilibrium Index
    ✔ Pivot Index (LeetCode term)

===============================================================================
Example 1
===============================================================================

Input:
arr = [1, 2, 3, 3]

Using 1-based indexing:

Index = 3
Left  = [1,2] → sum = 3
Right = [3]   → sum = 3

Since both sums are equal → Answer = true

===============================================================================
Example 2
===============================================================================

Input:
arr = [1,5]

Index 1
Left = 0
Right = 5

Index 2
Left = 1
Right = 0

No index satisfies condition → false

===============================================================================
Approach 1 — Brute Force (Your First Code)
===============================================================================

Idea
----
For every index i:
    Calculate sum(arr[0:i])
    Calculate sum(arr[i+1:])
    Compare both

Code
----
"""

class Solution:
    def equilibrium(self, arr, n): 
        for i in range(n):
            sum1 = sum(arr[:i])
            sum2 = sum(arr[i+1:])
            if sum1 == sum2:
                return "true"
        return "false"

"""

Why This Is Slow
----------------

For every index:
    sum() takes O(n)

And we do it for n indices

Total Time Complexity
---------------------
O(n^2)

Not acceptable for n up to 10^5

Space Complexity
----------------
O(1)

===============================================================================
Approach 2 — Optimized Prefix Technique (Your Second Code)
===============================================================================

Key Insight
-----------
Instead of recalculating sums every time:

We maintain:

    total_sum  → sum of entire array
    left_sum   → sum of elements before current index

At index i:

    right_sum = total_sum - arr[i]

So condition becomes:

    left_sum == right_sum

Algorithm
---------
1) Compute total_sum
2) Initialize left_sum = 0
3) For each index:
       subtract arr[i] from total_sum
       now total_sum becomes right_sum
       compare left_sum and total_sum
       update left_sum

Code
----
"""

class Solution:
    def equilibrium(self, arr): 
        total_sum = sum(arr)
        left_sum = 0
        
        for i in range(len(arr)):
            total_sum -= arr[i]   # right sum
            
            if left_sum == total_sum:
                return True
            
            left_sum += arr[i]
        
        return False

"""

===============================================================================
Dry Run (Important)
===============================================================================

arr = [1,2,3,3]

Step 1
-------

Total sum = 1+2+3+3 = 9
left_sum = 0

Iteration 0
-----------

Subtract arr[0]
right_sum = 9 - 1 = 8

Compare
left_sum (0) != 8

Update left_sum
left_sum = 1

Iteration 1
-----------

right_sum = 8 - 2 = 6

Compare
1 != 6

Update left_sum
left_sum = 3

Iteration 2
-----------

right_sum = 6 - 3 = 3

Compare
left_sum (3) == right_sum (3)

Condition satisfied → return True

===============================================================================
Visual Understanding
===============================================================================

Array

1   2   3   3

At index 2 (0-based)

Left side   → 1 + 2 = 3
Right side  → 3

Balance achieved.

Think of it like a weighing scale ⚖️

Left weight == Right weight

===============================================================================
Time & Space Complexity
===============================================================================

Optimized Approach
------------------
Time Complexity  → O(n)
Space Complexity → O(1)

Meets expected constraints.

===============================================================================
Edge Cases
===============================================================================

1) Single element
   arr = [5]
   Left = 0
   Right = 0
   → True

2) Two elements
   arr = [1,2]
   → False

3) All same elements
   arr = [2,2,2,2]
   → Index 2 works

===============================================================================
LeetCode Variation (Pivot Index)
===============================================================================

Same problem but return index instead of True/False.

Return first index where condition holds.
If none → return -1.

===============================================================================
Demo Execution
===============================================================================
"""
if __name__ == "__main__":

    print("=========== Brute Force Version ===========")

    class SolutionBrute:
        def equilibrium(self, arr, n):
            for i in range(n):
                sum1 = sum(arr[:i])
                sum2 = sum(arr[i+1:])
                if sum1 == sum2:
                    return True
            return False

    arr1 = [1, 2, 3, 3]
    arr2 = [1, 5]

    s1 = SolutionBrute()
    print("Array 1:", arr1)
    print("Equilibrium Exists?", s1.equilibrium(arr1, len(arr1)))
    print("Array 2:", arr2)
    print("Equilibrium Exists?", s1.equilibrium(arr2, len(arr2)))


    print("\n=========== Optimized Version (O(n)) ===========")

    class SolutionOptimized:
        def equilibrium(self, arr):
            total_sum = sum(arr)
            left_sum = 0
            
            for i in range(len(arr)):
                total_sum -= arr[i]
                
                if left_sum == total_sum:
                    return True
                
                left_sum += arr[i]
            
            return False

    s2 = SolutionOptimized()
    print("Array 1:", arr1)
    print("Equilibrium Exists?", s2.equilibrium(arr1))
    print("Array 2:", arr2)
    print("Equilibrium Exists?", s2.equilibrium(arr2))

"""
===============================================================================

Interview Cheat Sheet
===============================================================================

Step 1
Compute total sum

Step 2
Initialize left_sum = 0

Step 3
For each index:
    right_sum = total_sum - arr[i]
    if left_sum == right_sum → return True
    left_sum += arr[i]

Time  → O(n)
Space → O(1)

This is a classic prefix-sum based problem.

===============================================================================
"""
