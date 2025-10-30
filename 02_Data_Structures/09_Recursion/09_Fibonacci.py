# ------------------------------------------------------------
# 📘 note.py — Recursion: Fibonacci Sequence (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to generate Fibonacci numbers using recursion.
 - Understand the recursive structure, base cases, and overlapping subproblems.
 - Visualize how recursive calls branch (tree-shaped recursion).
 - Analyze performance and introduce the concept of optimization (memoization).

Mathematical Definition:
  Fibonacci sequence is defined as:
     F(0) = 0
     F(1) = 1
     F(n) = F(n-1) + F(n-2)   for n ≥ 2

Examples:
  F(0) = 0
  F(1) = 1
  F(2) = 1
  F(3) = 2
  F(4) = 3
  F(5) = 5
  F(6) = 8
"""

# ============================================================
# 🔁 1. Step-by-step recursive logic
# ============================================================
"""
Step 1️⃣ — Recursive Case:
   fib(n) = fib(n - 1) + fib(n - 2)
   → To find F(n), add the two previous Fibonacci numbers.

Step 2️⃣ — Base Case:
   When n == 0 or n == 1 → return n
   → Stops recursion for the first two Fibonacci numbers.

Step 3️⃣ — Unintentional Cases:
   - n must be a non-negative integer.
   - For negative or non-integer values, recursion misbehaves or loops infinitely.
   - Add input validation using assert if needed.
"""

# ============================================================
# ✅ 2. Your Code (original and clean)
# ============================================================

def fib(num):
    if num == 0 or num == 1:
        return num
    return fib(num - 1) + fib(num - 2)


# ============================================================
# 🧪 3. Examples & Demonstration
# ============================================================
if __name__ == "__main__":
    print("✅ Fibonacci Numbers using Recursion:\n")
    for n in range(8):
        print(f"fib({n}) = {fib(n)}")

    # Expected Output:
    # fib(0) = 0
    # fib(1) = 1
    # fib(2) = 1
    # fib(3) = 2
    # fib(4) = 3
    # fib(5) = 5
    # fib(6) = 8
    # fib(7) = 13


# ============================================================
# 🧭 4. Recursion Flow Example (n = 4)
# ============================================================
"""
fib(4)
 → fib(3) + fib(2)
     → (fib(2) + fib(1)) + (fib(1) + fib(0))
         → ((fib(1) + fib(0)) + 1) + (1 + 0)
         → ((1 + 0) + 1) + (1 + 0)
         = (2) + (1)
         = 3
✅ fib(4) = 3
"""

# ============================================================
# 🎨 5. Visualization (Recursion Tree for fib(4))
# ============================================================
"""
                 fib(4)
               /       \
           fib(3)       fib(2)
          /     \        /   \
      fib(2)   fib(1)  fib(1) fib(0)
      /   \
  fib(1) fib(0)

Computation order:
fib(1) and fib(0) are called many times repeatedly.
This repetition causes exponential growth in recursive calls.
"""

# ============================================================
# ⚙️ 6. Add Input Validation (optional enhancement)
# ============================================================
def safe_fib(num):
    """
    Fibonacci function with input validation.
    """
    assert int(num) == num and num >= 0, "Input must be a non-negative integer."
    if num == 0 or num == 1:
        return num
    return safe_fib(num - 1) + safe_fib(num - 2)

# Example:
# print(safe_fib(5))  # 5
# print(safe_fib(-1)) # AssertionError


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let’s analyze time and space complexity:

⏱ Time Complexity: O(2^n)
 - Each fib(n) recursively calls fib(n-1) and fib(n-2).
 - Many subproblems (like fib(2), fib(3)) are recalculated repeatedly.

🧮 Space Complexity: O(n)
 - The recursion depth is equal to n (max chain length).

💡 Optimization Idea:
 - Use **memoization** (store previously computed values).
 - Reduces time complexity to O(n).
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Forgetting base cases:
   → Infinite recursion (RecursionError).

❌ Negative inputs:
   → Causes infinite recursion (no decreasing towards base case).

✅ Always define:
   if num == 0 or num == 1: return num

💡 Tip:
   For large Fibonacci numbers, recursion is inefficient.
   Use iteration or dynamic programming.
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Modify this function to print the first N Fibonacci numbers in a sequence.
   (Hint: Use a loop or list comprehension calling fib(i).)

2️⃣ Write an iterative version of fib().

3️⃣ Add a print() statement inside fib() to trace each recursive call.

4️⃣ Implement memoization:
   Create a dictionary cache so fib(n) is computed only once.

5️⃣ Compare recursive and iterative runtimes for n = 30.
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What is fib(0)?
Q2: What is fib(1)?
Q3: What is the time complexity of this recursive version?
Q4: Why is recursion inefficient for Fibonacci?
Q5: How can we improve efficiency?

✅ Answers:
A1: 0
A2: 1
A3: O(2^n)
A4: Because the same values are recomputed multiple times.
A5: Use memoization or iteration (dynamic programming).
"""

# ============================================================
# ✅ End of note.py — Fibonacci Sequence (Recursion)
# ============================================================
"""
Summary:
 - Base Case: n == 0 → 0, n == 1 → 1
 - Recursive Case: fib(n) = fib(n−1) + fib(n−2)
 - Time: O(2^n), Space: O(n)
 - Demonstrates how recursion branches exponentially.
 - Leads naturally into dynamic programming and memoization.

Next:
 → Learn how to optimize this with **Memoization** to achieve O(n) time.
"""
