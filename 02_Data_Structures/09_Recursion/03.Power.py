# ------------------------------------------------------------
# 📘 note.py — Recursion: Power Function (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Teach a beginner how to compute x^n (power) using recursion.
 - Follow the 3-step recursion recipe: Recursive case, Base case,
   and Unintentional cases (input validation).
 - Use your original function and code style (kept exactly).
 - Provide step-by-step explanation, visualization, examples,
   complexity analysis, pitfalls, exercises and a quick quiz.

How to read:
 - Read top → down. Code is runnable as-is.
 - All explanations reference your function `power(base, exp)`.
"""

# ============================================================
# 🔎 0. Quick Overview
# ============================================================
"""
Problem:
 Compute the power of a number: given base x and exponent n, compute x^n.

Mathematical meaning:
 x^n = x * x * x * ... (n times) for n > 0
 x^0 = 1
 x^(-n) = 1 / (x^n)

Goal:
 - Implement x^n using recursion.
 - Handle positive, zero and negative integer exponents.
 - Validate exponent to be an integer (your implementation requires integer-valued exponents).
"""

# ============================================================
# 🔁 1. The three-step recursion recipe (applied)
# ============================================================
"""
Step 1 — Recursive case:
  x^n = x * x^(n-1)  (for n > 0)
  For negative n: x^n = (1 / x) * x^(n + 1)  (because adding 1 moves toward 0)

Step 2 — Base case:
  x^0 = 1  → when exponent reaches 0 return 1

Step 3 — Unintentional cases (validation):
  - Exponent should be an integer (e.g., 3, -2, 0). Your code asserts this.
  - If exponent is non-integer (e.g., 2.5) the function asserts.
  - Negative exponents handled by separate branch (elif exp < 0).
"""

# ============================================================
# ✅ 2. Your original code (kept exactly — only comments added)
# ============================================================
def power(base, exp):
    """
    Compute base ** exp using recursion.

    Preconditions (enforced by assertion):
      - exp must be integer-valued (e.g., 3, -1, 0). The assertion checks that.
    Behavior:
      - Positive exp: return base * power(base, exp - 1)
      - Zero exp: return 1
      - Negative exp: return 1/base * power(base, exp + 1)
    """
    # Validate exponent is an integer (integer-valued float allowed like 3.0)
    assert int(exp) == exp, 'The exponent must be integer number only'

    # Base case: exponent 0
    if exp == 0:
        return 1

    # Negative exponent: move exp toward 0 by adding 1 and divide by base
    elif exp < 0:
        return 1 / base * power(base, exp + 1)

    # Positive exponent: multiply base and decrease exp by 1
    return base * power(base, exp - 1)


# ============================================================
# 🧪 3. Examples & small demonstrations
# ============================================================
if __name__ == "__main__":
    tests = [
        (4, 2),     # 4^2 = 16
        (4, 4),     # 4^4 = 256
        (2, 0),     # 2^0 = 1
        (2, -1),    # 2^-1 = 0.5
        (5, -3),    # 5^-3 = 1/125 = 0.008
        (-2, 3),    # (-2)^3 = -8
        (2.5, 2),   # base can be float: 2.5^2 = 6.25
        (3, 1.0),   # exp as integer-valued float → allowed (3^1 = 3)
    ]

    print("Examples (using your power function):")
    for b, e in tests:
        try:
            result = power(b, e)
            print(f"  power({b!r}, {e!r}) = {result}")
        except AssertionError as err:
            print(f"  power({b!r}, {e!r}) -> AssertionError: {err}")

    # Validation examples (uncomment to see assertions)
    # power(2, 2.5)    # should raise AssertionError because exponent not integer-valued
    # power(0, -1)     # will attempt division by zero; will raise ZeroDivisionError


# ============================================================
# 🧭 4. How the recursion works (step-by-step)
# ============================================================
"""
Example 1: power(4, 2)
  power(4,2) -> 4 * power(4,1)
  power(4,1) -> 4 * power(4,0)
  power(4,0) -> 1  (base case)
  return flow:
    power(4,1) -> 4 * 1 = 4
    power(4,2) -> 4 * 4 = 16

Example 2: power(2, -2)
  power(2,-2) -> (1/2) * power(2,-1)
  power(2,-1) -> (1/2) * power(2,0)
  power(2,0)  -> 1
  return flow:
    power(2,-1) -> 0.5 * 1 = 0.5
    power(2,-2) -> 0.5 * 0.5 = 0.25
"""

# ============================================================
# 🎨 5. ASCII Recursion Tree
# ============================================================
"""
Positive exponent example: power(3, 3)

power(3,3)
 ├─ 3 * power(3,2)
      ├─ 3 * power(3,1)
           ├─ 3 * power(3,0)
                └─ 1 (base)
Return:
 power(3,1) = 3 * 1 = 3
 power(3,2) = 3 * 3 = 9
 power(3,3) = 3 * 9 = 27

Negative exponent example: power(2, -3)

power(2,-3)
 ├─ (1/2) * power(2,-2)
      ├─ (1/2) * power(2,-1)
           ├─ (1/2) * power(2,0)
                └─ 1 (base)
Return:
 power(2,-1) = 0.5 * 1 = 0.5
 power(2,-2) = 0.5 * 0.5 = 0.25
 power(2,-3) = 0.5 * 0.25 = 0.125
"""

# ============================================================
# 📈 6. Complexity Analysis
# ============================================================
"""
Let n = absolute value of exponent (|exp|). The recursion performs one multiplication (or division)
per recursive call and moves exponent toward zero by 1 each step.

- Time complexity: O(|exp|)
  Each recursive call reduces |exp| by 1 (exp-1 for positive, exp+1 for negative).

- Space complexity: O(|exp|)
  Recursion depth equals number of recursive calls until exp reaches 0.

Notes:
 - Complexity depends on magnitude of exponent, not on the base.
 - For very large exponent (e.g., exp = 10^6), recursion will be slow and may hit Python recursion limit.
 - For faster exponentiation use exponentiation by squaring (O(log n)) — not implemented here because you requested this exact simple recursive method.
"""

# ============================================================
# ⚠️ 7. Common pitfalls & best practices
# ============================================================
"""
1) Non-integer exponents:
   - The function asserts exp is integer-valued. Calling with exp=2.5 triggers AssertionError.

2) Division by zero for negative exponents:
   - power(0, -1) will attempt 1/0 → ZeroDivisionError. Validate base when using negative exponents.

3) Recursion depth limit:
   - Python has a recursion limit (~1000). Using very large |exp| will hit RecursionError.

4) Efficiency:
   - This simple recursion is O(n). For large exponents use fast exponentiation (exponentiation by squaring) to get O(log n).

5) Float rounding:
   - Multiplying/dividing floats can introduce floating-point inaccuracies; expected for floats.
"""

# ============================================================
# 🧩 8. Practice Exercises (with hints)
# ============================================================
"""
1) Test and reason:
   - Call power(2, 10) and compare with 2 ** 10.
   - Call power(2, -10) and compare with 2 ** -10.

2) Edge cases:
   - What does power(0, 0) return? (Try it — mathematically controversial; in Python 0**0 is 1)
   - What happens for power(0, -1)? (Division by zero)

3) Optimization challenge (advanced):
   - Implement exponentiation by squaring (iterative or recursive) to compute power in O(log n).
     (If you'd like, I can write this separately — but I won't change your original function.)

4) Robustness:
   - Add explicit checks to raise a clearer error when base == 0 and exp < 0.
"""

# ============================================================
# ❓ 9. Mini Quiz (answers below)
# ============================================================
"""
Q1: What is the base case of this recursive power function?
Q2: How does the function handle negative exponents?
Q3: What is the time complexity in terms of exponent magnitude?
Q4: What will power(4, -1) return?

Answers:
A1: exp == 0 → return 1
A2: For exp < 0 it returns (1/base) * power(base, exp + 1) — moves exp toward 0
A3: O(|exp|) time and O(|exp|) space (recursion depth)
A4: power(4, -1) = 0.25
"""

# ============================================================
# ✅ End of note.py — Power Function (Recursion)
# ============================================================
"""
If you want, next I can:
 - Add a unit test file (unittest) that tests many cases using your function.
 - Create a separate file implementing fast exponentiation (O(log n)) for comparison (kept separate).
 - Produce a short slide or printable PDF summarizing this lecture.

Tell me which you want next — I will keep using your function & style.
"""
