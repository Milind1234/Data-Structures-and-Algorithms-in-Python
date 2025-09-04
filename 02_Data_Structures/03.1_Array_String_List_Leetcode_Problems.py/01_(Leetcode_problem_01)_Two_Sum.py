"""
1. Two Sum
Difficulty: Easy

🔍 Problem:
Given an array of integers `nums` and an integer `target`, return the indices of the two numbers
such that they add up to `target`.

📌 Example:
Input: nums = [2, 7, 11, 15], target = 9
Output: [0, 1]
Explanation: Because nums[0] + nums[1] == 9

🧾 Constraints:
- 2 <= nums.length <= 10⁴
- -10⁹ <= nums[i] <= 10⁹
- -10⁹ <= target <= 10⁹
- Only one valid answer exists.

🚀 Follow-up:
Can you come up with an algorithm with better than O(n²) time complexity?

------------------------------------------------------------

💡 Optimal Steps to Code the Solution:

1. Loop through the list using enumerate() to get both index and value.
2. For each number, calculate the **complement**: 
       complement = target - num
   👉 This tells us: "What number would I need to add to `num` to reach the `target`?"
3. Use a dictionary to store numbers we've already seen along with their indices.
4. If the **complement** already exists in the dictionary, it means we’ve previously seen the exact number
   that, when added to the current number, gives the target.
5. Return the indices of the current number and its complement.
6. Time Complexity: O(n)

------------------------------------------------------------

🧠 Detailed Explanation of:
    complement = target - num

Let's say:
    target = 9
    num = 2

Now we ask: "What do I need to add to 2 to make 9?"
    complement = 9 - 2 = 7

So we now look: "Have we seen 7 before in the list?" 
If yes — return the index of 7 and 2. If not — keep going.

It's like solving this:
    num + complement = target
Rearranged as:
    complement = target - num

------------------------------------------------------------

🔁 Understanding enumerate(nums):

In Python, `enumerate()` allows us to loop through a list while keeping track of both the **index** and the **value** at the same time.

Instead of writing:

    index = 0
    for num in nums:
        ...
        index += 1

We use:

    for index, num in enumerate(nums):
        ...

📌 Example:

    nums = [2, 7, 11, 15]
    for index, num in enumerate(nums):
        print(index, num)

    Output:
        0 2
        1 7
        2 11
        3 15

So we know:
    - `index` gives us the position in the list
    - `num` gives us the value at that position

------------------------------------------------------------
"""

# ✅ Two Sum Solution using HashMap

nums = [2, 7, 11, 15]

class Solution(object):
    def twoSum(self, nums, target):
        num_map = {}  # Stores number as key and index as value

        # Loop through the list with both index and number using enumerate
        for index, num in enumerate(nums):
            complement = target - num  # Key logic: what number added to current num gives target?
            
            # If we’ve already seen the complement, return its index and current index
            if complement in num_map:
                return [num_map[complement], index]

            # Otherwise, store the current number with its index
            num_map[num] = index

# Create instance of class
s1 = Solution()

# Run function with test case
print(s1.twoSum(nums, 9))  # Output: [0, 1]
