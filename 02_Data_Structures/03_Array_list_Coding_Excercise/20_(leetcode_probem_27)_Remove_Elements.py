"""
==========================================================
Problem: Remove Element (LeetCode 27)
==========================================================

🔹 Problem Statement:
- Given an integer array `nums` and an integer `val`, remove all occurrences of `val` in-place.
- The order of remaining elements may change.
- Return the number of elements `k` that are not equal to `val`.
- The first `k` elements of `nums` must contain only elements not equal to `val`.

==========================================================
Example:
----------------------------------------------------------
Input:  nums = [3, 2, 2, 3], val = 3
Output: k = 2, nums = [2, 2, _, _]

Input:  nums = [0, 1, 2, 2, 3, 0, 4, 2], val = 2
Output: k = 5, nums = [0, 1, 3, 0, 4, _, _, _]

==========================================================
Code:
----------------------------------------------------------
"""
class Solution(object):
    def removeElement(self, nums, val):
        k = 0
        for i in range(len(nums)):
            if nums[i] != val:   # Keep only values not equal to val
                nums[k] = nums[i]
                k += 1
        return k

nums = [3, 2, 2, 3]
s1 = Solution()
k = s1.removeElement(nums, 3)
print(k)      # 2
print(nums)   # [2, 2, 2, 3] (only first 2 elements matter)
"""
==========================================================
Step-by-Step Working:
----------------------------------------------------------
nums = [3, 2, 2, 3], val = 3
k = 0

i=0 → nums[0]=3 == val → skip  
i=1 → nums[1]=2 != val → nums[0]=2 → k=1  
i=2 → nums[2]=2 != val → nums[1]=2 → k=2  
i=3 → nums[3]=3 == val → skip  

Result:
k = 2
nums (first k elements): [2, 2, ...]

==========================================================
Complexity:
----------------------------------------------------------
Time Complexity:  O(n) → Single pass through list
Space Complexity: O(1) → No extra space used

==========================================================
Key Points:
----------------------------------------------------------
- In-place modification, no additional array
- Order of elements can change (but here order is preserved)
- Only first `k` elements matter, rest can be ignored

==========================================================
Summary Table:
----------------------------------------------------------
Task                | Complexity
--------------------|----------------
Remove elements     | O(n)
In-place memory use | O(1)
Return count k      | O(1)
==========================================================
"""
