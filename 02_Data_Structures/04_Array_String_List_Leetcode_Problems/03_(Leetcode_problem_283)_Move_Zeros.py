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
Approach 0: Brute Force (Shift Zeros)
---------------------------------------------------
- Scan the array, and whenever you find a zero at index i:
    - Shift all elements after i one step left.
    - Place a zero at the last index.
    - Continue scanning.
- This maintains order, but requires repeated shifting.

Code:
-----
"""

class SolutionBruteForce(object):
    def moveZeroes(self, nums):
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] == 0:
                # Shift elements left
                for j in range(i, n - 1):
                    nums[j] = nums[j + 1]
                nums[n - 1] = 0
                n -= 1  # Reduce the "active length"
            else:
                i += 1

"""
Dry Run (Brute Force):
----------------------
nums = [0,1,0,3,12]

i=0 → nums[0]=0 → shift left → [1,0,3,12,0]
i=0 again → nums[0]=1 → not zero → i=1
i=1 → nums[1]=0 → shift left → [1,3,12,0,0]
i=1 again → nums[1]=3 → not zero → i=2
i=2 → nums[2]=12 → not zero → i=3 (loop ends because n shrinks)

Final Array:
[1, 3, 12, 0, 0]

Time Complexity:
----------------
- Worst case: O(n²), because for every zero found, we may shift ~n elements.

Space Complexity:
-----------------
- O(1), in-place shifting.

Interview Notes:
----------------
- Brute force works conceptually but is inefficient for large arrays.
- Useful as a first idea before optimizing.

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
Brute Force:
- Pros: Simple to think about.
- Cons: Very slow (O(n²)), not suitable for large arrays.

Approach 1 (Swap-on-the-fly):
- Pros: One pass, straightforward two-pointer method.
- Cons: More writes (every swap does two writes).

Approach 2 (Compact then Fill):
- Pros: Fewer writes → useful when memory writes are expensive
  (e.g., flash memory, large datasets).
- Cons: Requires two passes (but still O(n)).

Time Complexity:
----------------
- Brute Force: O(n²)
- Approach 1: O(n)
- Approach 2: O(n)

Space Complexity:
-----------------
All are O(1).

Interview Notes:
----------------
- Start with brute force to show understanding.
- Optimize to Approach 1 or 2 for efficiency.
- Mention trade-offs (swaps vs fewer writes).
"""
