"""
notes.py
---------
Topic: Remove Duplicates from Sorted Array (LeetCode 26)

Problem:
--------
Given a sorted integer array `nums`, remove the duplicates in-place such that 
each unique element appears only once. 
The relative order of elements should be kept the same.

You must do it with O(1) extra memory.

Function Signature:
-------------------
def removeDuplicates(nums: List[int]) -> int

Approach:
---------
- The array is sorted, so duplicates are always next to each other.
- Use two pointers technique:
    - `i` → slow pointer (tracks last unique element's index).
    - `j` → fast pointer (scans through the array).
- When nums[j] != nums[i], we found a new unique element:
    - Increment i
    - Place nums[j] at nums[i] (overwriting duplicate).
- Return i+1 (number of unique elements).

Code:
-----"""

class Solution(object):
    def removeDuplicates(self, nums):
        if not nums:
            return 0

        i = 0
        for j in range(1, len(nums)):
            if nums[j] != nums[i]:
                i += 1
                nums[i] = nums[j]
        return i + 1
"""
Dry Run:
--------
nums = [0,0,1,1,2,2,3]

Start: i=0
j=1: nums[1]=0 == nums[0]=0 → duplicate → skip
j=2: nums[2]=1 != nums[0]=0 → i=1, nums[1]=1 → [0,1,1,1,2,2,3]
j=3: nums[3]=1 == nums[1]=1 → skip
j=4: nums[4]=2 != nums[1]=1 → i=2, nums[2]=2 → [0,1,2,1,2,2,3]
j=5: nums[5]=2 == nums[2]=2 → skip
j=6: nums[6]=3 != nums[2]=2 → i=3, nums[3]=3 → [0,1,2,3,2,2,3]

Final Array (first i+1 = 4 elements are unique):
[0, 1, 2, 3, _, _, _]

Return → 4

Time Complexity:
----------------
- O(n), where n = length of nums
  (we scan each element once).

Space Complexity:
-----------------
- O(1), since in-place modification is done without extra space.

Interview Notes:
----------------
- Always check if input array is empty.
- This is a standard two-pointer pattern.
- Works only because array is sorted.
- Useful to demonstrate knowledge of in-place array manipulation.
"""
