"""
===============================================================================
📘 note_prefix_sum_1D.py — 1D Prefix Sum (Concept + In-place + Applications)
===============================================================================

Problem
-------
Given an array arr[], compute its Prefix Sum array.

Definition
----------
Prefix Sum at index i:

    prefix[i] = arr[0] + arr[1] + ... + arr[i]

In simple words:
Each position stores the cumulative sum from start to that index.

===============================================================================
Example 1
===============================================================================

Input:
arr = [10, 20, 10, 5, 15]

Step-by-step calculation

Index 0
prefix[0] = 10

Index 1
prefix[1] = 10 + 20 = 30

Index 2
prefix[2] = 30 + 10 = 40

Index 3
prefix[3] = 40 + 5 = 45

Index 4
prefix[4] = 45 + 15 = 60

Output:
[10, 30, 40, 45, 60]

===============================================================================
Core Idea (Important)
===============================================================================

Instead of calculating sum from 0 to i every time (which is slow),
we maintain a running total.

We keep a variable:

    total = 0

For each element:

    total += arr[i]
    prefix[i] = total

This avoids repeated summation.

===============================================================================
Approach 1 — Using Separate Prefix Array
===============================================================================

Idea
----
Create a new array to store prefix sums.

Code (Your Version)
--------------------
"""

class Solution:
    def prefSum(self, arr):
        n = len(arr)
        prefix_arr = [0] * n
        
        total = 0
        
        for i in range(n):
            total += arr[i]
            prefix_arr[i] = total 
            
        return prefix_arr

"""

Dry Run
-------

arr = [10, 20, 10, 5, 15]

Iteration 1
 total = 10
 prefix = [10,0,0,0,0]

Iteration 2
 total = 30
 prefix = [10,30,0,0,0]

Iteration 3
 total = 40
 prefix = [10,30,40,0,0]

Iteration 4
 total = 45
 prefix = [10,30,40,45,0]

Iteration 5
 total = 60
 prefix = [10,30,40,45,60]

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(n)

Pros
----
✔ Original array remains unchanged
✔ Clear and readable

Cons
----
❌ Uses extra space

===============================================================================
Approach 2 — In-Place Prefix Sum
===============================================================================

Idea
----
Instead of using a new array, modify the original array.

Code (Your Version)
--------------------
"""

class Solution:
    def prefSum(self, arr):
        n = len(arr)
        
        total = 0
        
        for i in range(n):
            total += arr[i]
            arr[i] = total 
            
        return arr

"""

Dry Run
-------

arr = [30, 10, 10, 5, 50]

Iteration 1
 total = 30
 arr = [30,10,10,5,50]

Iteration 2
 total = 40
 arr = [30,40,10,5,50]

Iteration 3
 total = 50
 arr = [30,40,50,5,50]

Iteration 4
 total = 55
 arr = [30,40,50,55,50]

Iteration 5
 total = 105
 arr = [30,40,50,55,105]

Time Complexity
---------------
O(n)

Space Complexity
----------------
O(1)

Pros
----
✔ No extra space
✔ Efficient

Cons
----
❌ Original array is modified

===============================================================================
Visual Understanding
===============================================================================

Original Array

10  20  10  5  15

Prefix Sum Builds Like

10
10+20
10+20+10
10+20+10+5
10+20+10+5+15

Think of prefix sum as building a running staircase of sums.

===============================================================================
Why Prefix Sum is Powerful (Important for Interviews)
===============================================================================

Prefix sum allows fast range sum queries.

Without prefix sum:
To find sum from L to R
We need O(n) time.

With prefix sum:
We can answer in O(1) time.

Formula
-------

If L == 0:
    sum = prefix[R]

Else:
    sum = prefix[R] - prefix[L-1]

Example
-------
arr = [10,20,10,5,15]
prefix = [10,30,40,45,60]

Find sum from index 1 to 3

sum = prefix[3] - prefix[0]
    = 45 - 10
    = 35

(20 + 10 + 5 = 35)

===============================================================================
Common Interview Extensions
===============================================================================

1) Range sum queries
2) Subarray sum equals K
3) Equilibrium index
4) Maximum subarray problems
5) 2D prefix sum (matrix problems)

===============================================================================
Edge Cases
===============================================================================

1) Single element
   arr = [5]
   prefix = [5]

2) All same elements
   arr = [1,1,1,1]
   prefix = [1,2,3,4]

3) Large constraints
   Works efficiently for n up to 10^5

===============================================================================
Comparison
===============================================================================

Method          | Time Complexity | Space Complexity
----------------|----------------|-----------------
New Array       | O(n)           | O(n)
In-place        | O(n)           | O(1)

===============================================================================
Interview Cheat Sheet
===============================================================================

Step 1
Initialize total = 0

Step 2
Loop through array

Step 3
Add current element to total

Step 4
Store total at index i

Time = O(n)
Space = O(1) or O(n)

Prefix sum is one of the most IMPORTANT foundations in DSA.

===============================================================================
Demo Execution (Run the Function)
===============================================================================
"""
if __name__ == "__main__":

    print("=========== Using Separate Prefix Array ===========")
    arr1 = [10, 20, 10, 5, 15]
    print("Original Array:", arr1)

    s1 = Solution()
    result1 = s1.prefSum(arr1.copy())  # using copy to preserve original

    print("Prefix Sum:", result1)


    print("\n=========== Using In-Place Prefix Sum ===========")
    arr2 = [30, 10, 10, 5, 50]
    print("Original Array:", arr2)

    s2 = Solution()
    result2 = s2.prefSum(arr2)

    print("Modified Array (Prefix Sum):", result2)


