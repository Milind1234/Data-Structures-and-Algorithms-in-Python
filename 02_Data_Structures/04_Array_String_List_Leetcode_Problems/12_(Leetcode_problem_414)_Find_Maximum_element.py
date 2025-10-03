# ============================================================
# Problem: Third Maximum Number
# Given an integer array nums, return the third distinct maximum number.
# If the third maximum does not exist, return the maximum number.
# ============================================================


# ------------------------------------------------------------
# Approach 1: Sorting (Simple)
# Time Complexity: O(n log n) (because of sorting)
# Space Complexity: O(n) (because of set and sorted list)
# ------------------------------------------------------------
class SolutionApproach1(object):
    def thirdMax(self, nums):
        # Remove duplicates and sort in descending order
        unique_nums = sorted(set(nums), reverse=True)

        # If we have at least 3 distinct numbers, return the third max
        if len(unique_nums) >= 3:
            return unique_nums[2]
        else:
            # Otherwise, return the largest number
            return unique_nums[0]


# ------------------------------------------------------------
# Approach 2: One-pass without sorting (Optimal)
# Time Complexity: O(n)
# Space Complexity: O(1)
# ------------------------------------------------------------
class SolutionApproach2(object):
    def thirdMax(self, nums):
        # Initialize max values to negative infinity
        max1, max2, max3 = float('-inf'), float('-inf'), float('-inf')

        for num in nums:
            # Skip duplicates
            if num == max1 or num == max2 or num == max3:
                continue

            # Update top three numbers
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num

        # If third maximum doesn't exist, return the maximum
        if max3 == float('-inf'):
            return max1
        return max3


# ------------------------------------------------------------
# Test Both Approaches
# ------------------------------------------------------------
if __name__ == "__main__":
    nums = [2, 2, 3, 1]
    print("Approach 1 Output:", SolutionApproach1().thirdMax(nums))
    print("Approach 2 Output:", SolutionApproach2().thirdMax(nums))
