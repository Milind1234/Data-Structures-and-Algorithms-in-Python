"""
🔢 Problem: Maximum Consecutive 0s or 1s in a Binary Array

🎯 Goal:
Given a binary array arr[] consisting only of 0’s and 1’s,
return the maximum number of consecutive identical bits
(either 0s or 1s).

──────────────────────────────────────────────
📥 Examples

Example 1:
Input  : [0, 1, 0, 1, 1, 1, 1]
Output : 4
Explanation: Maximum consecutive 1’s from index 3–6.

Example 2:
Input  : [0, 0, 1, 0, 1, 0]
Output : 2
Explanation: Maximum consecutive 0’s from index 0–1.

Example 3:
Input  : [0, 0, 0, 0]
Output : 4

──────────────────────────────────────────────
🔍 Approach 1: Brute Force (Check every streak)

🧠 Idea:
For each index, count how long the streak continues.

🪜 Steps:
1. Initialize max_count = 0.
2. For each index i:
   - Start count = 1.
   - Move forward while elements are same.
3. Update max_count.
4. Return max_count.

⏱ Time Complexity : O(n²)
🧠 Space Complexity: O(1)
"""

def maxConsecBits_brute(arr):
    n = len(arr)
    max_count = 0

    for i in range(n):
        count = 1
        for j in range(i + 1, n):
            if arr[j] == arr[i]:
                count += 1
            else:
                break
        max_count = max(max_count, count)

    return max_count


# ✅ Test Brute Force
arr = [0, 1, 0, 1, 1, 1, 1]
print("Brute Force Result:", maxConsecBits_brute(arr))  # 4


"""
──────────────────────────────────────────────
⚡ Approach 2: Optimized (Single Pass / Streak Counting)

🧠 Core Insight:
Since array is sequential, just compare with previous element.

If same → extend streak  
If different → reset streak  

🪜 Steps:
1. Handle empty array.
2. Initialize:
      current_count = 1
      max_count = 1
3. Traverse from index 1:
      - if arr[i] == arr[i-1] → increment
      - else → reset to 1
4. Update max every step.
5. Return max_count.

✅ Why this works:
The longest consecutive block is tracked in one pass.

⏱ Time Complexity : O(n)
🧠 Space Complexity: O(1)
"""

class Solution:
    def maxConsecBits(self, arr):
        # Edge case
        if not arr:
            return 0

        max_count = 1
        current_count = 1

        for i in range(1, len(arr)):
            if arr[i] == arr[i - 1]:
                current_count += 1
            else:
                current_count = 1

            max_count = max(max_count, current_count)

        return max_count


# ✅ Test Optimized
arr = [0, 1, 0, 1, 1, 1, 1]
print("Optimized Result:", Solution().maxConsecBits(arr))  # 4


"""
──────────────────────────────────────────────
🧪 Dry Run (Important)

Input:
arr = [0, 1, 0, 1, 1, 1, 1]

Start:
current = 1, max = 1

i=1 → different → current=1
i=2 → different → current=1
i=3 → different → current=1
i=4 → same → current=2, max=2
i=5 → same → current=3, max=3
i=6 → same → current=4, max=4

Final Answer = 4

──────────────────────────────────────────────
⚠️ Edge Cases

✔ Empty array → return 0  
✔ Single element → return 1  
✔ All same → return n  
✔ Alternating bits → return 1  

──────────────────────────────────────────────
🧾 Summary

• Brute Force → simple but slow → O(n²)  
• Optimal → single pass → O(n)  
• Space in both → O(1)  
• Pattern name → Longest consecutive streak

🚀 Interview Tip:
Whenever you see "consecutive", think:
→ running counter
→ compare with previous
→ update max
"""