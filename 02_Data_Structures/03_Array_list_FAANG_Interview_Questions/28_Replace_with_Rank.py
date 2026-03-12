"""
===============================================================================
📘 note_replace_with_rank.py — Replace Elements by Its Rank in the Array
===============================================================================

Problem
-------
Given an array arr of N integers, replace each element with its rank
when the array is sorted in ascending order.

Definition of Rank
------------------
- Rank starts from 1.
- If two elements are equal → they share the same rank.
- Rank increases only when we encounter a new distinct element.

Important:
Rank is based on sorted unique order, NOT original position.

===============================================================================
Example 1
===============================================================================

Input:
arr = [20, 15, 26, 2, 98, 6]

Sorted array:
[2, 6, 15, 20, 26, 98]

Assign ranks:
2  → 1
6  → 2
15 → 3
20 → 4
26 → 5
98 → 6

Final Output:
[4, 3, 5, 1, 6, 2]

===============================================================================
Example 2 (Duplicates Case)
===============================================================================

Input:
arr = [2, 2, 1, 6]

Sorted array:
[1, 2, 2, 6]

Ranks:
1 → 1
2 → 2
2 → 2   (same rank as first 2)
6 → 3

Output:
[2, 2, 1, 3]

===============================================================================
Core Idea
===============================================================================

Step 1 → Sort the array
Step 2 → Assign rank to unique elements only
Step 3 → Map original elements to their rank

We use a dictionary (hashmap) to store:

    value → rank

===============================================================================
Implementation (Your Solution)
===============================================================================
"""
class Solution:
    def replaceWithRank(self, N, arr):
        sorted_arr = sorted(arr)
        rank_map = {}
        rank = 1
        
        for num in sorted_arr:
            if num not in rank_map:
                rank_map[num] = rank
                rank += 1
        
        result = []
        for num in arr:
            result.append(rank_map[num])
            
        return result
"""
===============================================================================
Dry Run
===============================================================================

arr = [20, 15, 26, 2, 98, 6]

Step 1: Sort
sorted_arr = [2, 6, 15, 20, 26, 98]

Step 2: Build rank_map

2  → 1
6  → 2
15 → 3
20 → 4
26 → 5
98 → 6

rank_map = {
    2:1,
    6:2,
    15:3,
    20:4,
    26:5,
    98:6
}

Step 3: Build result

20 → 4
15 → 3
26 → 5
2  → 1
98 → 6
6  → 2

Result = [4,3,5,1,6,2]

===============================================================================
Time & Space Complexity
===============================================================================

Sorting          → O(N log N)
Building map     → O(N)
Building result  → O(N)

Overall Time Complexity → O(N log N)

Space Complexity → O(N)
(for sorted array + hashmap + result)

Meets expected constraints.

===============================================================================
Alternative Cleaner Version (Using Sorted Unique Values)
===============================================================================
"""
class SolutionBetter:
    def replaceWithRank(self, N, arr):
        sorted_unique = sorted(set(arr))
        
        rank_map = {value: idx + 1 for idx, value in enumerate(sorted_unique)}
        
        return [rank_map[num] for num in arr]
"""
This removes duplicate checks manually.

===============================================================================
Edge Cases
===============================================================================

1) Single element
   arr = [10]
   → [1]

2) All elements same
   arr = [5,5,5]
   → [1,1,1]

3) Already sorted array
   arr = [1,2,3,4]
   → [1,2,3,4]

===============================================================================
Comparison with Similar Problems
===============================================================================

Problem Type                 | Difference
-----------------------------|------------------------------
Coordinate Compression       | Same concept
Relative Ranking             | Slight variation
Frequency Rank               | Different logic

This problem is a form of Coordinate Compression.

===============================================================================
Demo Execution (Run the Code)
===============================================================================
"""
if __name__ == "__main__":

    arr1 = [20, 15, 26, 2, 98, 6]
    arr2 = [2, 2, 1, 6]

    s = Solution()

    print("Input:", arr1)
    print("Output:", s.replaceWithRank(len(arr1), arr1))

    print("\nInput:", arr2)
    print("Output:", s.replaceWithRank(len(arr2), arr2))
"""
===============================================================================

How To Run
----------

    python note_replace_with_rank.py

===============================================================================
Interview Cheat Sheet
===============================================================================

1) Sort array
2) Assign rank to unique elements
3) Map original array

Time  → O(N log N)
Space → O(N)

If you hear "replace by rank" or "compress values",
think: SORT + HASHMAP

===============================================================================
"""