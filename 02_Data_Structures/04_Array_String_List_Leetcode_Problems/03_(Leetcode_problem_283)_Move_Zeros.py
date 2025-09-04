"""
notes.py
---------
Topic: Move Zeroes (LeetCode 283)

Problem:
--------
Given an integer array `nums`, move all 0's to the end of it while maintaining
the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Function Signature:
-------------------
def moveZeroes(nums: List[int]) -> None

Approach:
---------
- Use the two pointers technique:
    - `i` → slow pointer (points to the index where the next non-zero should go).
    - `j` → fast pointer (scans through the array).
- If nums[j] is non-zero:
    - Swap nums[i] and nums[j].
    - Increment i (to prepare for the next non-zero).
- By the end, all non-zeros are shifted to the front, and all zeros end up at the back.
- The order of non-zero elements remains unchanged.

Code:
-----
"""

class Solution(object):
    def moveZeroes(self, nums):
        i = 0  # pointer for next non-zero position
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

"""
Dry Run:
--------
nums = [0,1,0,3,12]

Start: i=0
j=0: nums[0]=0 → skip
j=1: nums[1]=1 != 0 → swap nums[0], nums[1] → [1,0,0,3,12], i=1
j=2: nums[2]=0 → skip
j=3: nums[3]=3 != 0 → swap nums[1], nums[3] → [1,3,0,0,12], i=2
j=4: nums[4]=12 != 0 → swap nums[2], nums[4] → [1,3,12,0,0], i=3

Final Array:
[1, 3, 12, 0, 0]

Return → None (in-place modification)

Time Complexity:
----------------
- O(n), where n = length of nums
  (each element is checked once).

Space Complexity:
-----------------
- O(1), since only pointers (i, j) are used.

Interview Notes:
----------------
- Important to remember: j always moves forward, i only moves when a non-zero is found.
- This ensures stability (relative order of non-zeros is preserved).
- A classic two-pointer in-place array manipulation problem.
"""
