"""
===============================================================================
📘 note_array_subset.py — Array Subset (Sorting + Hashing + Counter)
===============================================================================

Problem
-------
Given two arrays a[] and b[], determine whether b[] is a subset of a[].

Definition (Important):
- b[] is a subset of a[] if every element of b appears in a
- Frequency matters (duplicates matter)

Example:
    a = [11, 7, 1, 13, 21, 3, 7, 3]
    b = [11, 3, 7, 1, 7]

Here, b is a subset because:
    - 11 appears once in a
    - 3 appears twice in a
    - 7 appears twice in a
    - 1 appears once in a

If b required 7 three times → it would NOT be a subset.

Constraints:
    1 <= len(a), len(b) <= 10^5
    1 <= values <= 10^6

===============================================================================
Approach 1: Sorting + Two Pointers
===============================================================================

Idea
----
1. Sort both arrays.
2. Use two pointers (i for a, j for b).
3. Traverse both arrays:
    - If a[i] == b[j] → match found → move both pointers.
    - Otherwise move pointer i only.
4. If we matched all elements of b (j == len(b)), return True.

Code (Your Version)
--------------------
"""

class Solution:
    def isSubset(self, a, b):
        a.sort()
        b.sort()
        
        i = 0
        j = 0
        
        while i < len(a) and j < len(b):
            if a[i] == b[j]:
                i += 1
                j += 1
            else:
                i += 1
        
        if j == len(b):
            return True
        return False

"""
How It Works (Step-by-step Example)
-----------------------------------

Example:
    a = [1, 2, 3, 4, 4, 5, 6]
    b = [1, 2, 4]

After sorting:
    a = [1,2,3,4,4,5,6]
    b = [1,2,4]

Comparison flow:

    i  j
    ↓  ↓
    1  1  → match → i++, j++
    2  2  → match → i++, j++
    3  4  → not match → i++
    4  4  → match → i++, j++

Now j reached end → subset = True

Time Complexity:
    Sorting a: O(n log n)
    Sorting b: O(m log m)
    Traversal: O(n + m)
    Overall: O(n log n + m log m)

Space Complexity:
    O(1) (if sorting in-place)

Pros:
    ✔ Simple logic
    ✔ No extra data structures

Cons:
    ❌ Sorting changes original arrays
    ❌ Slower than hashing for large inputs

===============================================================================
Approach 2: Frequency Dictionary (Hash Map)
===============================================================================

Idea
----
1. Count frequency of elements in array a using dictionary.
2. Traverse b:
      - If element not present or frequency is 0 → return False
      - Otherwise decrease frequency

Code (Your Version)
--------------------
"""

class Solution:
    def isSubset(self, a, b):
        freq = {}
        
        for num in a:
            freq[num] = freq.get(num, 0) + 1
            
        for num in b:
            if num not in freq or freq[num] == 0:
                return False
            freq[num] -= 1
        
        return True

"""

Why This Works
--------------

Example:
    a = [10, 5, 2, 23, 19]
    b = [19, 5, 3]

Frequency table of a:
    {
      10:1,
      5:1,
      2:1,
      23:1,
      19:1
    }

Checking b:
    19 → exists → decrease count
    5  → exists → decrease count
    3  → NOT exists → return False

Time Complexity:
    Build dictionary: O(n)
    Check b: O(m)
    Overall: O(n + m)

Space Complexity:
    O(n)

Pros:
    ✔ Fast (linear time)
    ✔ Does not modify arrays
    ✔ Handles duplicates correctly

Cons:
    ❌ Extra memory used

===============================================================================
Approach 3: Using collections.Counter (Clean Version)
===============================================================================

Python provides built-in Counter class.
It automatically builds frequency map.

Code (Your Version)
--------------------
"""

from collections import Counter

class Solution:
    def isSubset(self, a, b):
        freq = Counter(a)

        for num in b:
            if freq[num] == 0:
                return False
            freq[num] -= 1

        return True

"""

Why Counter is Better
---------------------
- Cleaner syntax
- Built-in optimized implementation
- Same time complexity: O(n + m)

===============================================================================
Edge Cases to Remember
===============================================================================

1) b larger than a
   a = [1,2]
   b = [1,2,3]
   → False

2) Duplicates matter
   a = [1,1,2]
   b = [1,1,1]
   → False

3) Empty b
   b = []
   → Always True (empty set is subset)

4) Empty a but non-empty b
   → False

===============================================================================
Which Approach Should You Use?
===============================================================================

Interview Recommendation:
    ✔ Use HashMap / Counter approach (O(n + m))

Competitive Programming:
    ✔ Counter version (clean + fast)

Avoid:
    ❌ Sorting approach if input size is very large

===============================================================================
Complexity Comparison Table
===============================================================================

Method                | Time Complexity     | Space Complexity
----------------------|--------------------|-----------------
Sorting + 2 pointers  | O(n log n + m log m)| O(1)
Dictionary            | O(n + m)            | O(n)
Counter               | O(n + m)            | O(n)

===============================================================================
Final Recommendation
===============================================================================

Best balance of clarity + performance:

    from collections import Counter
    freq = Counter(a)
    for num in b:
        if freq[num] == 0:
            return False
        freq[num] -= 1
    return True

This is clean, efficient, and interview-ready.

===============================================================================
"""


# ===============================================================================
# Demo Execution (Printing Results for Each Approach)
# ===============================================================================

if __name__ == "__main__":

    a1 = [11, 7, 1, 13, 21, 3, 7, 3]
    b1 = [11, 3, 7, 1, 7]

    a2 = [10, 5, 2, 23, 19]
    b2 = [19, 5, 3]

    print("================= Approach 1: Sorting + Two Pointers =================")
    sol1 = Solution()
    print("Example 1:", sol1.isSubset(a1.copy(), b1.copy()))
    print("Example 2:", sol1.isSubset(a2.copy(), b2.copy()))

    print("================= Approach 2: Dictionary (HashMap) =================")
    class Solution2:
        def isSubset(self, a, b):
            freq = {}
            for num in a:
                freq[num] = freq.get(num, 0) + 1
            for num in b:
                if num not in freq or freq[num] == 0:
                    return False
                freq[num] -= 1
            return True

    sol2 = Solution2()
    print("Example 1:", sol2.isSubset(a1, b1))
    print("Example 2:", sol2.isSubset(a2, b2))

    print("================= Approach 3: Counter =================")
    from collections import Counter

    class Solution3:
        def isSubset(self, a, b):
            freq = Counter(a)
            for num in b:
                if freq[num] == 0:
                    return False
                freq[num] -= 1
            return True

    sol3 = Solution3()
    print("Example 1:", sol3.isSubset(a1, b1))
    print("Example 2:", sol3.isSubset(a2, b2))

# ===============================================================================

