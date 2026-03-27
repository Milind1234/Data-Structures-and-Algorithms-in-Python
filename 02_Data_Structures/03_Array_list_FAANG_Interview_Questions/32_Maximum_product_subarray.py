"""
===============================================================================
📘 note_max_product_subarray.py — Maximum Product Subarray
===============================================================================

Problem
-------
Given an array with positive, negative and zero values,
find the maximum product of a contiguous subarray.

===============================================================================
Key Challenge
===============================================================================

Unlike sum:
- Negative × Negative = Positive
- Zero resets product

So we must track BOTH:
✔ Maximum product
✔ Minimum product

===============================================================================
Approach 1 — Brute Force (O(n²))
===============================================================================

"""

def maxProduct_bruteforce(arr):
    """
    ==============================================================================
    🔹 Purpose
    ------------------------------------------------------------------------------
    Compute maximum product of all possible subarrays using brute force.

    🔹 Core Idea
    ------------------------------------------------------------------------------
    Try every possible subarray and calculate its product.

    🔹 Steps
    ------------------------------------------------------------------------------
    1. Fix a starting index i
    2. Initialize product = 1
    3. Extend subarray till j
    4. Update maxProd at every step

    🔹 Visualization
    ------------------------------------------------------------------------------
    arr = [-2, 6, -3]

    Subarrays:
    [-2]
    [-2, 6]
    [-2, 6, -3]
    [6]
    [6, -3]
    [-3]

    🔹 Complexity
    ------------------------------------------------------------------------------
    ⏱️ Time Complexity: O(n²)
    ⏱️ Space Complexity: O(1)
    ==============================================================================
    """

    n = len(arr)
    maxProd = arr[0]

    for i in range(n):
        mul = 1
        for j in range(i, n):
            mul *= arr[j]
            maxProd = max(maxProd, mul)

    return maxProd


"""
Dry Run (Brute Force — FULL ITERATION)
---------------------
arr = [-2, 6, -3]

Start:
maxProd = -2

---------------------------------
i = 0
mul = 1

j = 0 → mul = -2
maxProd = max(-2, -2) = -2

j = 1 → mul = -2 * 6 = -12
maxProd = max(-2, -12) = -2

j = 2 → mul = -12 * -3 = 36
maxProd = max(-2, 36) = 36

---------------------------------
i = 1
mul = 1

j = 1 → mul = 6
maxProd = max(36, 6) = 36

j = 2 → mul = 6 * -3 = -18
maxProd = max(36, -18) = 36

---------------------------------
i = 2
mul = 1

j = 2 → mul = -3
maxProd = max(36, -3) = 36

Final Answer = 36


===============================================================================
Approach 2 — Kadane Variant (Optimal O(n))
===============================================================================
"""

def maxProduct_kadane(arr):
    """
    ==============================================================================
    🔹 Purpose
    ------------------------------------------------------------------------------
    Efficiently compute maximum product subarray using Kadane-like logic.

    🔹 Core Insight
    ------------------------------------------------------------------------------
    Negative numbers flip signs:
    - Max can become Min
    - Min can become Max

    So we track BOTH:
    ✔ currMax → maximum product till current index
    ✔ currMin → minimum product till current index

    🔹 Steps
    ------------------------------------------------------------------------------
    1. Initialize currMax, currMin, maxProd
    2. For each element:
        - Calculate 3 choices:
            a) current number
            b) current number * currMax
            c) current number * currMin
        - Update currMax and currMin
    3. Update global maxProd

    🔹 Why it Works
    ------------------------------------------------------------------------------
    Because a negative × negative becomes positive,
    we must not lose track of minimum product.

    🔹 Complexity
    ------------------------------------------------------------------------------
    ⏱️ Time Complexity: O(n)
    ⏱️ Space Complexity: O(1)
    ==============================================================================

    """
    currMax = arr[0]
    currMin = arr[0]
    maxProd = arr[0]

    for i in range(1, len(arr)):
        num = arr[i]

        temp = max(num, num * currMax, num * currMin)
        currMin = min(num, num * currMax, num * currMin)
        currMax = temp

        maxProd = max(maxProd, currMax)

    return maxProd


"""
Detailed Dry Run (Kadane Variant — FULL ITERATION)
----------------
arr = [-2, 6, -3, -10]

Initialize:
currMax = -2
currMin = -2
maxProd = -2

---------------------------------
i = 1 → num = 6

Options:
6
6 * (-2) = -12
6 * (-2) = -12

currMax = 6
currMin = -12
maxProd = 6

---------------------------------
i = 2 → num = -3

Options:
-3
-3 * 6 = -18
-3 * (-12) = 36

currMax = 36
currMin = -18
maxProd = 36

---------------------------------
i = 3 → num = -10

Options:
-10
-10 * 36 = -360
-10 * (-18) = 180

currMax = 180
currMin = -360
maxProd = 180

Final Answer = 180

===============================================================================
Approach 3 — Prefix + Suffix Scan (Two Pass)
===============================================================================
"""

def maxProduct_prefix_suffix(arr):
    """
    ==============================================================================
    🔹 Purpose
    ------------------------------------------------------------------------------
    Compute maximum product using prefix and suffix traversal.

    🔹 Core Idea
    ------------------------------------------------------------------------------
    - Traverse from left → right
    - Traverse from right → left
    - Handle zeros by resetting product

    🔹 Why This Works
    ------------------------------------------------------------------------------
    If there are odd negatives:
    - Left scan may miss optimal subarray
    - Right scan captures it

    So we take max from both directions.

    🔹 Steps
    ------------------------------------------------------------------------------
    1. Initialize left and right products
    2. Traverse array
    3. Multiply from both ends
    4. Reset when encountering zero
    5. Track maximum product

    🔹 Complexity
    ------------------------------------------------------------------------------
    ⏱️ Time Complexity: O(n)
    ⏱️ Space Complexity: O(1)
    ==============================================================================
    """

    maxProd = float('-inf')
    left = 1
    right = 1
    n = len(arr)

    for i in range(n):
        if left == 0:
            left = 1
        if right == 0:
            right = 1

        left *= arr[i]
        right *= arr[n - i - 1]

        maxProd = max(maxProd, left, right)

    return maxProd


"""
Dry Run (Prefix-Suffix — FULL ITERATION)
-----------------------
arr = [-2, 6, -3, -10, 0, 2]

Initialize:
left = 1
right = 1
maxProd = -inf

---------------------------------
i = 0
left = 1 * -2 = -2
right = 1 * 2 = 2
maxProd = 2

---------------------------------
i = 1
left = -2 * 6 = -12
right = 2 * 0 = 0
maxProd = 2

---------------------------------
i = 2
left = -12 * -3 = 36
right reset to 1 (because 0)
right = 1 * -10 = -10
maxProd = 36

---------------------------------
i = 3
left = 36 * -10 = -360
right = -10 * -3 = 30
maxProd = 36

---------------------------------
i = 4
left reset to 1 (because 0 encountered next)
left = 1 * 0 = 0
right = 30 * 6 = 180
maxProd = 180

---------------------------------
i = 5
left reset to 1
left = 1 * 2 = 2
right = 180 * -2 = -360
maxProd = 180

Final Answer = 180


===============================================================================
Comparison
===============================================================================

Method           | Time   | Space | Recommended
-----------------|--------|-------|------------
Brute Force      | O(n²)  | O(1)  | ❌
Kadane Variant   | O(n)   | O(1)  | ⭐ Best
Prefix-Suffix    | O(n)   | O(1)  | ⭐ Good

===============================================================================
Demo Execution
===============================================================================
"""
if __name__ == "__main__":

    arr = [-2, 6, -3, -10, 0, 2]

    print("Brute Force:", maxProduct_bruteforce(arr))
    print("Kadane Variant:", maxProduct_kadane(arr))
    print("Prefix-Suffix:", maxProduct_prefix_suffix(arr))
"""
===============================================================================
Interview Cheat Sheet
===============================================================================

Track TWO values:
- currMax
- currMin

Formula:

currMax = max(num, num*currMax, num*currMin)
currMin = min(num, num*currMax, num*currMin)

This handles negative flipping.

===============================================================================
"""
