# ------------------------------------------------------------
# 📘 note.py — Recursion: Sum of Natural Numbers (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to find the sum of all numbers from 1 to n using recursion.
 - Continue the same 3-step recursion framework:
      1️⃣ Recursive Case
      2️⃣ Base Case
      3️⃣ Unintentional / Input Validation Cases
 - Keep your original function exactly as is.
 - Understand how the recursion unfolds, how the call stack works,
   and how to compute time and space complexity.
"""

# ============================================================
# 🔎 0. Quick Overview
# ============================================================
"""
Problem:
  Find the sum of all numbers from 1 up to n.
  Example: n = 5 → 5 + 4 + 3 + 2 + 1 = 15

Mathematical formula (for comparison):
  n(n + 1) / 2
  But here, we’ll do it using recursion to learn the concept.
"""

# ============================================================
# 🔁 1. Three-step recursive approach (applied)
# ============================================================
"""
Step 1️⃣ — Recursive Case:
  recursiveRange(n) = n + recursiveRange(n - 1)
  Explanation:
    - Keep adding current number (n) to the sum of numbers before it (n-1 down to 1).

Step 2️⃣ — Base Case:
  When n <= 0 → return 0
  (When we go below 1, recursion stops.)

Step 3️⃣ — Unintentional Case (optional):
  - The function assumes n is an integer.
  - For non-integer inputs, recursion may behave unpredictably.
  - You can add an assert to ensure integer input if you like.
"""

# ============================================================
# ✅ 2. Your Function (kept exactly same)
# ============================================================

def recursiveRange(num):
    if num <= 0:
        return 0
    return num + recursiveRange(num - 1)


# ============================================================
# 🧪 3. Examples & Tests
# ============================================================
if __name__ == "__main__":
    print("✅ Sum of natural numbers using recursion:\n")

    examples = [5, 6, 10, 0, -3]
    for n in examples:
        print(f"recursiveRange({n}) = {recursiveRange(n)}")

    # Uncomment to test validation (if you later add assert)
    # print(recursiveRange(4.5))  # Non-integer (will recurse oddly)


# ============================================================
# 🧭 4. How recursion works (example: n = 4)
# ============================================================
"""
recursiveRange(4)
 → 4 + recursiveRange(3)
       → 3 + recursiveRange(2)
             → 2 + recursiveRange(1)
                   → 1 + recursiveRange(0)
                        → 0 (base case)
Return flow:
 recursiveRange(0) → 0
 recursiveRange(1) → 1 + 0 = 1
 recursiveRange(2) → 2 + 1 = 3
 recursiveRange(3) → 3 + 3 = 6
 recursiveRange(4) → 4 + 6 = 10
✅ Final result: 10
"""

# ============================================================
# 🎨 5. Visualization (ASCII diagram)
# ============================================================
"""
             recursiveRange(4)
                     ↓
             4 + recursiveRange(3)
                         ↓
                 3 + recursiveRange(2)
                             ↓
                     2 + recursiveRange(1)
                                 ↓
                         1 + recursiveRange(0)
                                     ↓
                                 return 0 (base case)

Return path:
1 + 0 = 1
2 + 1 = 3
3 + 3 = 6
4 + 6 = 10
"""

# ============================================================
# 📈 6. Complexity Analysis
# ============================================================
"""
Let n = input number.

⏱ Time Complexity: O(n)
 - Each recursive call reduces n by 1.
 - One addition per call.

🧮 Space Complexity: O(n)
 - Each call is stored in the call stack until n reaches 0.

✅ Both time and space grow linearly with n.
"""

# ============================================================
# ⚠️ 7. Common Mistakes & Fixes
# ============================================================
"""
❌ Forgetting base case:
   → Causes infinite recursion → RecursionError.

❌ Using '==' instead of '<=' in base case:
   → Works for positive n but not for negative inputs (since recursion never stops).

❌ Floating point input:
   → If n = 4.5, it never reaches base case cleanly.
   ✅ Add assertion if needed:
       assert int(num) == num, "Input must be an integer"
"""

# ============================================================
# 🧩 8. Practice Exercises
# ============================================================
"""
1️⃣ Modify the function to compute the sum from 1 to n,
     but skip even numbers (sum only odd numbers).

2️⃣ Write a similar function for factorial using recursion.
     (Hint: change '+' to '*', base case returns 1.)

3️⃣ Add a print statement to trace each call — observe the order of calls.

4️⃣ Try rewriting this using a loop instead of recursion.

5️⃣ Add error handling for float or negative inputs — return a message instead of recursing infinitely.
"""

# ============================================================
# ❓ 9. Mini Quiz (answers below)
# ============================================================
"""
Q1: What is the base case here?
Q2: What is recursiveRange(0)?
Q3: What happens if num is negative?
Q4: What is the time complexity?

✅ Answers:
A1: When num <= 0 → return 0
A2: 0
A3: It immediately returns 0 (base case triggers)
A4: O(n)
"""

# ============================================================
# ✅ End of note.py — Sum of Natural Numbers (Recursion)
# ============================================================
"""
Summary:
 - Simple recursion: n + recursiveRange(n - 1)
 - Base case: n <= 0 → return 0
 - Time: O(n), Space: O(n)
 - Great example to practice recursive flow and stack behavior.

Next:
 → Try writing “sum of digits of a number” or “power of a number” using the same pattern.
"""
