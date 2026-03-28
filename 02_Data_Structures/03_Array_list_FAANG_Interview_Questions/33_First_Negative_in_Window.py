"""
===============================================================================
📘 note_first_negative_window.py — First Negative in Every Window (Size K)
===============================================================================

Problem
-------
Given an array arr[] and integer k,
for every window of size k, return the FIRST negative number.
If no negative exists → return 0.

===============================================================================
Approach 1 — Index List + Pointer (Your First Code)
===============================================================================
"""
class SolutionListPointer:
    def firstNegInt(self, arr, k):
        """
        🔹 Purpose
        Maintain a list of indices of negative numbers and a pointer (j)
        to track the first valid negative inside current window.

        🔹 Steps
        1. Traverse array
        2. Store index if element is negative
        3. Move pointer j if index goes out of window
        4. If window formed, pick arr[negative[j]] else 0

        ⏱️ Time: O(n)
        ⏱️ Space: O(k)
        """
        j = 0
        n = len(arr)
        negative = []
        ans = []

        for i in range(n):
            if arr[i] < 0:
                negative.append(i)

            # remove outdated index logically using pointer
            if j != len(negative) and negative[j] <= i - k:
                j += 1

            if i >= k - 1:
                if j == len(negative):
                    ans.append(0)
                else:
                    ans.append(arr[negative[j]])
        return ans

"""
FULL DRY RUN (Approach 1 — EVERY ITERATION)
-------------------------------------------
arr = [-8, 2, 3, -6, 10]
k = 2

Initialize:
negative = []
j = 0
ans = []

-------------------------------------------------
i = 0
arr[0] = -8 → negative → store index
negative = [0]

Visualization:
window = [-8]
negative indices = [0]
j -> 0
ans = []

Check outdated: 0 <= -2? NO
Window not formed

-------------------------------------------------
i = 1
arr[1] = 2 → not negative

Visualization:
window = [-8, 2]
negative indices = [0]
j -> 0

Check outdated: 0 <= -1? NO

Window formed:
first negative = -8
ans = [-8]

-------------------------------------------------
i = 2
arr[2] = 3 → not negative

Visualization:
window = [2, 3]
negative indices = [0]
j -> 0

Check outdated: 0 <= 0? YES → j=1

Window formed:
no valid negative
ans = [-8, 0]

-------------------------------------------------
i = 3
arr[3] = -6 → store index
negative = [0, 3]

Visualization:
window = [3, -6]
negative indices = [0, 3]
j -> 1

Check outdated: negative[1] valid

Window formed:
first negative = -6
ans = [-8, 0, -6]

-------------------------------------------------
i = 4
arr[4] = 10 → not negative

Visualization:
window = [-6, 10]
negative indices = [0, 3]
j -> 1

Check outdated: 3 <= 2? NO

Window formed:
first negative = -6
ans = [-8, 0, -6, -6]

Final Answer = [-8, 0, -6, -6]


===============================================================================
Approach 2 — Deque (Optimal Sliding Window)
===============================================================================
"""
from collections import deque

class SolutionDeque:
    def firstNegInt(self, arr, k):
        """
        🔹 Purpose
        Use deque to maintain indices of negative elements in window.

        🔹 Core Idea
        Front of deque always holds first negative of current window.

        🔹 Steps
        1. Traverse array
        2. Push index if negative
        3. Remove indices out of window (front)
        4. If window formed:
            - if deque not empty → arr[q[0]]
            - else → 0

        ⏱️ Time: O(n)
        ⏱️ Space: O(k)
        """
        n = len(arr)
        q = deque()
        ans = []

        for i in range(n):
            if arr[i] < 0:
                q.append(i)

            if q and q[0] <= i - k:
                q.popleft()

            if i >= k - 1:
                if q:
                    ans.append(arr[q[0]])
                else:
                    ans.append(0)
        return ans

"""
FULL DRY RUN (Approach 2 — EVERY ITERATION)
-------------------------------------------
arr = [12, -1, -7, 8, -15, 30, 16, 28]
k = 3

Initialize:
q = deque()
ans = []

-------------------------------------------------
i = 0
12 → not negative
q = []
window = [12]
ans = []

-------------------------------------------------
i = 1
-1 → push index 1
q = [1]
window = [12, -1]
ans = []

-------------------------------------------------
i = 2
-7 → push index 2
q = [1,2]
window = [12, -1, -7]

Window formed:
first negative = -1
ans = [-1]

-------------------------------------------------
i = 3
8 → not negative
Remove outdated? 1 <= 0? NO
q = [1,2]
window = [-1, -7, 8]

ans = [-1, -1]

-------------------------------------------------
i = 4
-15 → push index 4
q = [1,2,4]

Remove outdated: 1 <= 1 → pop → q=[2,4]
window = [-7, 8, -15]

ans = [-1, -1, -7]

-------------------------------------------------
i = 5
30 → not negative
Remove outdated: 2 <= 2 → pop → q=[4]
window = [8, -15, 30]

ans = [-1, -1, -7, -15]

-------------------------------------------------
i = 6
16 → not negative
Remove outdated? 4 <= 3? NO
q = [4]
window = [-15, 30, 16]

ans = [-1, -1, -7, -15, -15]

-------------------------------------------------
i = 7
28 → not negative
Remove outdated: 4 <= 4 → pop → q=[]
window = [30, 16, 28]

no negative → 0
ans = [-1, -1, -7, -15, -15, 0]

Final Answer = [-1, -1, -7, -15, -15, 0]

===============================================================================
Comparison
===============================================================================

Method            | Time | Space | Recommended
------------------|------|-------|------------
List + Pointer    | O(n) | O(k)  | Good
Deque             | O(n) | O(k)  | ⭐ Best

===============================================================================
Demo Execution
===============================================================================
"""
if __name__ == "__main__":

    arr = [-8, 2, 3, -6, 10]
    k = 2

    print("List Pointer:", SolutionListPointer().firstNegInt(arr, k))
    print("Deque:", SolutionDeque().firstNegInt(arr, k))
"""
===============================================================================
Interview Cheat Sheet
===============================================================================

Fixed window + first occurrence → use DEQUE

- push negative indices
- remove out-of-window
- front = answer

===============================================================================
"""
