# 🚀 Find the Largest Element in an Array
# ---------------------------------------
# ✅ Problem:
# Given an array of integers, return the largest element.
#
# Example:
# Input:  [3, 3, 0, 99, -40]
# Output: 99
#
# ---------------------------------------
# ✅ Approach:
# 1. Assume the first element is the largest → largest = nums[0].
# 2. Traverse the array from index 1 onwards.
# 3. For each element:
#    - If nums[i] > largest → update largest.
# 4. Return largest after the loop ends.
#
# Time Complexity: O(n)  ⏳  (every element checked once)
# Space Complexity: O(1) 📦  (only one variable used)


def largestElement(nums):
    # Step 1: Assume first element is largest
    largest = nums[0]

    # Step 2: Traverse the array
    for i in range(1, len(nums)):
        # Step 3: Compare and update if bigger found
        if nums[i] > largest:
            largest = nums[i]

    # Step 4: Return result
    return largest


# ---------------------------------------
# 📝 Iteration Walkthrough Example
# Input: nums = [3, 3, 0, 99, -40]
#
# Initial:
# largest = 3
#
# Iteration 1: i=1 → nums[1] = 3
# - 3 is NOT > largest(3) → do nothing
# - largest = 3
#
# Iteration 2: i=2 → nums[2] = 0
# - 0 is NOT > largest(3) → do nothing
# - largest = 3
#
# Iteration 3: i=3 → nums[3] = 99
# - 99 > 3 ✅ → update
# - largest = 99
#
# Iteration 4: i=4 → nums[4] = -40
# - -40 is NOT > largest(99) → do nothing
# - largest = 99
#
# End of loop → largest = 99
#
# ✅ Output:
# 99


# ---------------------------------------
# 🔹 Example Run
if __name__ == "__main__":
    nums = [3, 3, 0, 99, -40]
    print(largestElement(nums))   # Output: 99
