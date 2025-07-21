"""
Problem: Middle Function
-----------------------------------
Write a function called `middle` that takes a list and returns a new list 
that contains all but the first and last elements.

Example:
---------
Input: [1, 2, 3, 4]
Output: [2, 3]
"""

# -----------------------------
# ✅ Steps to Solve the Problem
# -----------------------------
# 1. Understand what is asked: 
#    You are given a list and you need to remove the first and last elements.
#
# 2. Use Python slicing to achieve this:
#    Slicing allows you to get a subset of a list.
#    Syntax: list[start_index : end_index]
#    Example: lst[1:-1] will skip the first (0th) and last (-1) elements.
#
# 3. Return the sliced list as the result.

# -----------------------------
# ✅ Time and Space Complexity
# -----------------------------
# Time Complexity: O(k), where k = len(lst) - 2 (elements in the middle).
# Space Complexity: O(k), since a new list of size k is created.

# -----------------------------
# ✅ Optimal Code Implementation
# -----------------------------
def middle(lst):
    # Return a new list containing all elements from the original list,
    # excluding the first and last elements
    return lst[1:-1]

# -----------------------------
# ✅ Test Case
# -----------------------------
myList = [1, 2, 3, 4]
print(middle(myList))  # Output: [2, 3]

# -----------------------------
# ✅ Explanation
# -----------------------------
# Input list:     [1, 2, 3, 4]
# Slicing:         1:-1   → from 2nd element (index 1) to second last (index -2)
# Resulting list: [2, 3]
"""
This approach is optimal, readable, and uses Python's built-in slicing capabilities.
Avoid using loops or external lists when a simple slice can solve the problem.
"""
