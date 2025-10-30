# ------------------------------------------------------------
# 📘 note.py — Recursion: Factorial of a Number (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Understand how to calculate factorial of a number using recursion.
 - Keep the code simple (your version).
 - Learn base case, recursive case, input validation, and visualize the call stack.

Mathematical definition:
 n! = n × (n−1) × (n−2) × ... × 1
 Example: 5! = 5 × 4 × 3 × 2 × 1 = 120
"""

# ============================================================
# ✅ 1. Your function (slightly commented)
# ============================================================

def factorial(num):
    # Base case — stop when num == 1
    if num == 1:
        return 1
    # Recursive case — multiply current number by factorial of (num-1)
    return num * factorial(num - 1)


# ============================================================
# 🧪 2. Example runs
# ============================================================
if __name__ == "__main__":
    print(factorial(1))   # 1
    print(factorial(3))   # 6 = 3*2*1
    print(factorial(5))   # 120 = 5*4*3*2*1
    print(factorial(6))   # 720


# ============================================================
# 🧭 3. How it works (trace for factorial(4))
# ============================================================
"""
factorial(4)
 → 4 * factorial(3)
       → 3 * factorial(2)
             → 2 * factorial(1)
                   → 1  (base case)

Return flow:
 factorial(2) = 2 * 1 = 2
 factorial(3) = 3 * 2 = 6
 factorial(4) = 4 * 6 = 24
✅ final result = 24
"""

# ============================================================
# 🎨 4. Visualization (call stack)
# ============================================================
"""
           factorial(4)
               ↓
           factorial(3)
               ↓
           factorial(2)
               ↓
           factorial(1)
               ↑
   returns up: 1 → 2 → 6 → 24
"""

# ============================================================
# ⚠️ 5. Important improvements
# ============================================================
"""
✅ Add input validation to handle unintentional cases:
   - Factorial is only defined for non-negative integers.

✅ Add second base case for num == 0, since 0! = 1 by definition.
"""

# ------------------------------------------------------------
# ✨ Improved Safe Version
# ------------------------------------------------------------
def safe_factorial(num):
    assert int(num) == num and num >= 0, "Number must be a non-negative integer"
    if num in (0, 1):
        return 1
    return num * safe_factorial(num - 1)

# Example:
# print(safe_factorial(0))  # 1
# print(safe_factorial(5))  # 120


# ============================================================
# 📈 6. Time & Space Complexity
# ============================================================
"""
Time Complexity: O(n)
 - Each recursive call computes factorial(num-1) once.

Space Complexity: O(n)
 - Each call is stored in the recursion stack until base case is reached.
"""

# ============================================================
# 🧩 7. Practice Exercises
# ============================================================
"""
1️⃣ Add print statements inside factorial() to trace the recursive calls.
2️⃣ Implement an iterative version using a while loop.
3️⃣ Try calling factorial(0) — fix it using the safe version above.
4️⃣ Modify it to handle negative numbers gracefully (raise an error).
5️⃣ Compute factorial of large numbers (e.g. 100) and observe recursion limit.
"""

# ============================================================
# ✅ End of note.py — Factorial (Recursion)
# ============================================================
"""
Summary:
 - Base Case: num == 1 (or 0)
 - Recursive Case: num * factorial(num-1)
 - Handles integers only.
 - Simple, powerful, and commonly asked interview question.

Next idea:
 → Try writing “sum of first n natural numbers” recursively.
"""
