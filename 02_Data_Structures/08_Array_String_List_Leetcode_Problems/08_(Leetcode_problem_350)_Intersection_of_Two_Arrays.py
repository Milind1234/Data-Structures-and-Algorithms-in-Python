"""
===================================================
🔁 INTERSECTION OF TWO ARRAYS II (LeetCode 350)
===================================================

✅ Problem Statement:
Given two integer arrays nums1 and nums2, return an 
array of their intersection. Each element in the result 
must appear as many times as it shows in both arrays 
and the result can be in any order.

---------------------------------------------------
📥 Example:
Input : nums1 = [1,2,2,1], nums2 = [2,2]
Output: [2,2]

---------------------------------------------------
🛠️ Approaches:

1. BRUTE FORCE (O(n * m))
--------------------------------
Idea:
- For each element in nums1:
    - Scan nums2 for a match.
    - If match found → add to result & mark nums2 element as used.
    - Break inner loop.

Code:
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        seen = []
        for i in range(len(nums1)):
            for j in range(len(nums2)):
                if nums1[i] == nums2[j]:
                    seen.append(nums1[i])
                    nums2[j] = None   # mark as used
                    break             # stop for this nums1[i]
        return seen

"""
Iteration Walkthrough:
nums1 = [1,2,2,1], nums2 = [2,2]

i=0 → nums1[0]=1 → check nums2 → no match
i=1 → nums1[1]=2 → nums2[0]=2 → match → result=[2], mark nums2[0]=None
i=2 → nums1[2]=2 → nums2[0]=None, nums2[1]=2 → match → result=[2,2], mark nums2[1]=None
i=3 → nums1[3]=1 → nums2=[None,None] → no match
Final result = [2,2]

Complexity: O(n*m), Space O(1)
---------------------------------------------------

2. HASHMAP / FREQUENCY COUNTER (O(n+m))
--------------------------------
Idea:
- Build frequency map from nums1.
- Loop over nums2:
    - If num exists in map and count > 0 → add to result & decrement count.

Code:
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        freq = {}
        for num in nums1:
            if num in freq:
                freq[num] += 1
            else:
                freq[num] = 1
        
        result = []
        for num in nums2:
            if num in freq and freq[num] > 0:
                result.append(num)
                freq[num] -= 1
        return result

"""
Iteration Walkthrough:
nums1 = [1,2,2,1], nums2 = [2,2]

Step 1 → Build freq from nums1:
- 1 → freq={1:1}
- 2 → freq={1:1,2:1}
- 2 → freq={1:1,2:2}
- 1 → freq={1:2,2:2}

Step 2 → Process nums2:
- num=2 → freq[2]=2 > 0 → result=[2], freq={1:2,2:1}
- num=2 → freq[2]=1 > 0 → result=[2,2], freq={1:2,2:0}

Final result = [2,2]

Complexity: O(n+m), Space O(min(n,m))
---------------------------------------------------

3. TWO POINTERS (Sorting + Merge Style)
--------------------------------
Idea:
- Sort both arrays.
- Use two pointers (i, j).
- If nums1[i]==nums2[j] → add to result, move both.
- Else move the smaller one.

Code:
"""
class Solution(object):
    def intersect(self, nums1, nums2):
        nums1.sort()
        nums2.sort()
        
        i, j = 0, 0
        result = []
        
        while i < len(nums1) and j < len(nums2):
            if nums1[i] == nums2[j]:
                result.append(nums1[i])
                i += 1
                j += 1
            elif nums1[i] < nums2[j]:
                i += 1
            else:
                j += 1
        return result

"""
Iteration Walkthrough:
nums1 = [1,2,2,1] → sorted → [1,1,2,2]
nums2 = [2,2]     → sorted → [2,2]

i=0,j=0 → 1<2 → i=1
i=1,j=0 → 1<2 → i=2
i=2,j=0 → 2==2 → result=[2], i=3,j=1
i=3,j=1 → 2==2 → result=[2,2], i=4,j=2 → stop

Final result = [2,2]

Complexity: O(n log n + m log m), Space O(1)
---------------------------------------------------

📊 Comparison:

Approach      Time Complexity       Space     When to Use
-----------------------------------------------------------
Brute Force   O(n*m)                O(1)      For small inputs
Hashmap       O(n+m)                O(min)    Best for unsorted arrays
Two Pointers  O(n log n + m log m)  O(1)      Best if arrays are sorted

===================================================
"""
