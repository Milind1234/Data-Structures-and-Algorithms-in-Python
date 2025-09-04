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

---------------------------------------------------
Approach 1: Two Pointers with Swapping (Single Pass)
---------------------------------------------------
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
Dry Run (Approach 1):
---------------------
nums = [0,1,0,3,12]

Start: i=0
j=0: nums[0]=0 → skip
j=1: nums[1]=1 != 0 → swap nums[0], nums[1] → [1,0,0,3,12], i=1
j=2: nums[2]=0 → skip
j=3: nums[3]=3 != 0 → swap nums[1], nums[3] → [1,3,0,0,12], i=2
j=4: nums[4]=12 != 0 → swap nums[2], nums[4] → [1,3,12,0,0], i=3

Final Array:
[1, 3, 12, 0, 0]

---------------------------------------------------
Approach 2: Compact then Fill (Two Pass, Fewer Writes)
---------------------------------------------------
- Instead of swapping every time, we "compact" non-zeros forward first.
- Step 1: Copy each non-zero into the front of the array (using pointer i).
- Step 2: After all non-zeros are placed, fill the remaining slots with 0.
- Benefit: Each non-zero is written only once, and zeros are written once.
  → Total writes = n (better when minimizing memory writes is important).

Code:
-----
"""

class SolutionAlternative(object):
    def moveZeroes(self, nums):
        i = 0
        # Pass 1: move all non-zero elements to the front
        for j in range(len(nums)):
            if nums[j] != 0:
                nums[i] = nums[j]
                i += 1
        # Pass 2: fill the rest with zeros
        while i < len(nums):
            nums[i] = 0
            i += 1

"""
Dry Run (Approach 2):
---------------------
nums = [0,1,0,3,12]

Pass 1:
j=0: nums[0]=0 → skip
j=1: nums[1]=1 → nums[0]=1 → [1,1,0,3,12], i=1
j=2: nums[2]=0 → skip
j=3: nums[3]=3 → nums[1]=3 → [1,3,0,3,12], i=2
j=4: nums[4]=12 → nums[2]=12 → [1,3,12,3,12], i=3

Pass 2:
Fill from i=3 to end with 0 → [1,3,12,0,0]

Final Array:
[1, 3, 12, 0, 0]

---------------------------------------------------
Comparison of Approaches:
---------------------------------------------------
Approach 1 (Swap-on-the-fly):
- Pros: One pass, straightforward two-pointer method.
- Cons: More writes (every swap does two writes).

Approach 2 (Compact then Fill):
- Pros: Fewer writes → useful when memory writes are expensive
  (e.g., flash memory, large datasets).
- Cons: Requires two passes (but still O(n)).

Time Complexity:
----------------
Both approaches are O(n).

Space Complexity:
-----------------
Both are O(1).

Interview Notes:
----------------
- Both are valid and optimal solutions.
- Approach 1 is often accepted as the standard answer in interviews.
- Approach 2 shows awareness of write-efficiency trade-offs.
"""
