"""
📌 Problem: Contains Duplicate (LeetCode 217)

Given an integer array nums, return True if any value appears 
at least twice in the array, and return False if every element is distinct.

Example 1:
Input : nums = [1, 2, 3, 1]
Output: True

Example 2:
Input : nums = [1, 2, 3, 4]
Output: False
"""

# ---------------------------------------------------------------
# 1️⃣ Brute Force Approach (Sorting)
# ---------------------------------------------------------------
"""
Idea:
- First, sort the array.
- Compare each element with its next neighbor.
- If any two consecutive elements are equal → duplicate found.

Algorithm:
1. Sort nums
2. Loop i = 0 to len(nums)-2
3. If nums[i] == nums[i+1], return True
4. Else, continue loop
5. Return False

⏱️ Time Complexity: O(n log n) → sorting dominates
💾 Space Complexity: O(1) if in-place sort is used
"""

def contains_duplicate_sorted(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False


# ---------------------------------------------------------------
# 2️⃣ Optimal Approach (Using Hash Set)
# ---------------------------------------------------------------
"""
Idea:
- Use a set to keep track of seen numbers.
- While iterating:
  • If number already in set → duplicate found
  • Else, add it to the set
- Return False if no duplicates found

Algorithm:
1. Initialize empty set `seen`
2. For each number in nums:
   - If num in seen → return True
   - Else add num to seen
3. After loop → return False

⏱️ Time Complexity: O(n) → single pass
💾 Space Complexity: O(n) → extra set storage
"""

def contains_duplicate_set(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False


# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
"""
nums = [1, 2, 3, 1]

Sorted Approach:
- Sort → [1, 1, 2, 3]
- Compare neighbors: 1 == 1 → return True

Set Approach:
- seen = {}
- num=1 → add {1}
- num=2 → add {1,2}
- num=3 → add {1,2,3}
- num=1 → already in set → return True
"""


# ---------------------------------------------------------------
# 🧪 Example Tests
# ---------------------------------------------------------------
if __name__ == "__main__":
    nums1 = [1, 2, 3, 1]
    print("Duplicate Exists (Sorted Check)?", contains_duplicate_sorted(nums1))  # True

    nums2 = [1, 2, 3, 4]
    print("Duplicate Exists (Set Check)?", contains_duplicate_set(nums2))        # False
