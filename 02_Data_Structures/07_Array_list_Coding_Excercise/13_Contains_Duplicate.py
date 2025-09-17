# ===================================================
# 🔁 CONTAINS DUPLICATE - LeetCode Easy
# ===================================================

# ✅ Problem Statement:
# Given an integer array nums, return True if any value 
# appears at least twice in the array, and return False 
# if every element is distinct.

# ---------------------------------------------------
# 📥 Example:
# Input : nums = [1, 2, 3, 1]
# Output: True

# ---------------------------------------------------
# 💡 Hint: Use Sets or Sorting
# ---------------------------------------------------

# ===================================================
# 1️⃣ Approach: Using Sorting
# ===================================================
# ✔️ Steps:
# - First, sort the array.
# - Then loop through it and compare each element with its next neighbor.
# - If any two consecutive elements are equal, return True.

# ⏱️ Time Complexity: O(n log n)
# 💾 Space Complexity: O(1) if sorting is done in-place

def contains_duplicate_sorted(nums):
    nums.sort()
    for i in range(len(nums) - 1):
        if nums[i] == nums[i + 1]:
            return True
    return False

# ✅ Example Test
nums = [1, 2, 3, 1]
print("Duplicate Exists (Sorted Check)?", contains_duplicate_sorted(nums))  # Output: True


# ===================================================
# 2️⃣ Optimal Approach: Using Set
# ===================================================
# ✔️ Steps:
# - Initialize an empty set.
# - Iterate through the array.
# - If the element is already in the set, return True.
# - Otherwise, add it to the set.

# ⏱️ Time Complexity: O(n)
# 💾 Space Complexity: O(n)

def contains_duplicate_set(nums):
    seen = set()
    for num in nums:
        if num in seen:
            return True
        seen.add(num)
    return False

# ✅ Example Test
nums = [1, 2, 1 , 3, 4]
print("Duplicate Exists (Set Check)?", contains_duplicate_set(nums))  # Output: False
