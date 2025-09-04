# 🚀 LeetCode 88. Merge Sorted Array
# ---------------------------------
# ✅ Approach (Two-pointer, backwards merge):
# - Use three pointers:
#     p1 = index of last valid element in nums1 (m-1)
#     p2 = index of last element in nums2 (n-1)
#     p  = index of last slot in nums1 (m+n-1)
#
# - While both arrays still have elements:
#     - Compare nums1[p1] and nums2[p2]
#     - Place the larger at nums1[p]
#     - Decrement that pointer and p
#
# - If nums2 still has leftovers, copy them into nums1
# - If nums1 has leftovers, they’re already in the right place
#
# Time Complexity: O(m+n)  ⏳
# Space Complexity: O(1) 📦 (in-place)


def merge(nums1, m, nums2, n):
    p1 = m - 1   # last valid index of nums1
    p2 = n - 1   # last index of nums2
    p  = m + n - 1  # last index of nums1 total size
    
    # 🟢 Step 1: Merge from back
    while p1 >= 0 and p2 >= 0:
        if nums1[p1] > nums2[p2]:
            nums1[p] = nums1[p1]
            p1 -= 1
        else:
            nums1[p] = nums2[p2]
            p2 -= 1
        p -= 1
    
    # 🟢 Step 2: Copy remaining nums2 elements if any
    # (nums1 leftovers are already fine)
    while p2 >= 0:
        nums1[p] = nums2[p2]
        p2 -= 1
        p -= 1
    
    return nums1


# ------------------------------------------------
# 📝 Iteration Walkthrough Example
# Input:
# nums1 = [1,2,3,0,0,0], m=3
# nums2 = [2,5,6], n=3
#
# Initial:
# p1=2 (nums1[2]=3), p2=2 (nums2[2]=6), p=5
#
# Iteration 1:
# Compare 3 vs 6 → 6 bigger
# nums1[5] = 6
# nums1 = [1,2,3,0,0,6]
# p2=1, p=4
#
# Iteration 2:
# Compare 3 vs 5 → 5 bigger
# nums1[4] = 5
# nums1 = [1,2,3,0,5,6]
# p2=0, p=3
#
# Iteration 3:
# Compare 3 vs 2 → 3 bigger
# nums1[3] = 3
# nums1 = [1,2,3,3,5,6]
# p1=1, p=2
#
# Iteration 4:
# Compare 2 vs 2 → equal (take nums2’s 2)
# nums1[2] = 2
# nums1 = [1,2,2,3,5,6]
# p2=-1, p=1
#
# Exit loop: nums2 exhausted
# Final nums1 = [1,2,2,3,5,6]
#
# ✅ Output:
# [1,2,2,3,5,6]


# ------------------------------------------------
# 🔹 Example Run
if __name__ == "__main__":
    nums1 = [1,2,3,0,0,0]
    nums2 = [2,5,6]
    print(merge(nums1, 3, nums2, 3))   # Output: [1,2,2,3,5,6]
