"""
===================================================
🔁 MAXIMUM SUBARRAY (LeetCode 53)
===================================================

✅ Problem Statement:
Given an integer array nums, find the contiguous subarray 
(containing at least one number) which has the largest sum 
and return its sum.

---------------------------------------------------
📥 Example:
Input : nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

---------------------------------------------------
🛠️ Approaches:

1. BRUTE FORCE (Check all subarrays) – O(n^2)
--------------------------------
Idea:
- Try all possible subarrays nums[i:j].
- For each subarray, calculate the sum.
- Keep track of the maximum sum.

Code:
"""
class Solution(object):
    def maxSubArray(self, nums):
        n = len(nums)
        max_sum = float('-inf')
        for i in range(n):
            current_sum = 0
            for j in range(i, n):
                current_sum += nums[j]  # extend sum
                max_sum = max(max_sum, current_sum)
        return max_sum

"""
Iteration Walkthrough:
nums = [-2,1,-3,4]

i=0 → j=0 sum=-2 max=-2; j=1 sum=-1 max=-1; j=2 sum=-4; j=3 sum=0 max=0
i=1 → j=1 sum=1 max=1; j=2 sum=-2; j=3 sum=2 max=2
i=2 → j=2 sum=-3; j=3 sum=1
i=3 → j=3 sum=4 max=4
Final → max_sum=4

Complexity: O(n^2), Space O(1)
---------------------------------------------------

2. KADANE’S ALGORITHM (Elegant Form) – O(n)
--------------------------------
Idea:
- Maintain `current_sum` = max sum ending at this element.
- If extending the previous sum is better → add.
- Otherwise, restart with current element.
- Track global max.

Code:
"""
class Solution(object):
    def maxSubArray(self, nums):
        current_sum = max_sum = nums[0]
        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)
        return max_sum

"""
Iteration Walkthrough:
nums = [-2,1,-3,4]

Start: current_sum=-2, max_sum=-2
num=1 → current_sum=max(1,-2+1)=1, max_sum=1
num=-3 → current_sum=max(-3,1-3)=-2, max_sum=1
num=4 → current_sum=max(4,-2+4)=4, max_sum=4
Final = 4

Complexity: O(n), Space O(1)
---------------------------------------------------

3. KADANE’S (with reset-to-0 form) – O(n)
--------------------------------
Idea:
- Keep running sum.
- If sum > max_num → update max.
- If sum < 0 → reset sum to 0 (bad prefix).
- Equivalent to Kadane’s but written differently.

Code:
"""
class Solution(object):
    def maxSubArray(self, nums):
        sum = 0
        max_num = float('-inf')
        for num in nums:
            sum += num
            if sum > max_num:
                max_num = sum
            if sum < 0:
                sum = 0
        return max_num

"""
Iteration Walkthrough:
nums = [-2,1,-3,4]

sum=0, max_num=-inf
num=-2 → sum=-2, max_num=-2 → reset sum=0
num=1 → sum=1, max_num=1
num=-3 → sum=-2, max_num=1 → reset sum=0
num=4 → sum=4, max_num=4
Final = 4

Complexity: O(n), Space O(1)
---------------------------------------------------

📊 Comparison:

Approach        Time        Space    Notes
---------------------------------------------------
Brute Force     O(n^2)      O(1)     Simple but slow
Kadane (form 1) O(n)        O(1)     Elegant & standard
Kadane (form 2) O(n)        O(1)     Same logic, reset style

===================================================
"""
