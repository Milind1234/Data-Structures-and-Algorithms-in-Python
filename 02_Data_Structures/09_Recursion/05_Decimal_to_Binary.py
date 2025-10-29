# ------------------------------------------------------------
# 📘 note.py — Recursion: Decimal → Binary (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Teach a beginner how to convert a decimal integer to binary using recursion.
 - Follow the 3-step recursive approach: Recursive case, Base case, Unintentional cases.
 - Use the exact function you provided (no logic changes).
 - Provide clear explanations, visualization, examples, complexity analysis,
   common pitfalls, practice exercises and a mini quiz.

Note:
 - The function uses n % 2 for the remainder and int(n/2) for the quotient
   (this is exactly your implementation choice).
 - The assertion requires the parameter to be integer-valued.
"""

# ============================================================
# 🔎 0. Quick Overview
# ============================================================
"""
Problem:
 Convert a given decimal integer n to its binary representation as an integer.
 Example: n = 13 -> binary digits 1101 -> function returns integer 1101

Mathematical idea:
 - Repeatedly divide n by 2.
 - The remainder (n % 2) is the current least significant bit (LSB).
 - Continue with the integer quotient (n // 2 or int(n/2)) until quotient is 0.
 - The binary number is formed by combining remainders from last to first.
"""

# ============================================================
# 🔁 1. Three-step recursion recipe (applied)
# ============================================================
"""
Step 1 — Recursive case:
  DecimalToBinary(n) = (n % 2) + 10 * DecimalToBinary(int(n / 2))

  Explanation:
    - (n % 2) gives the current rightmost binary digit (0 or 1).
    - Multiply result of the recursive call by 10 to shift previously computed bits left.
      (This constructs the binary digits as a decimal integer, e.g., 1101.)

Step 2 — Base case:
  When n == 0 → return 0
  (No more digits to produce; recursion stops.)

Step 3 — Unintentional cases:
  The code asserts the input is integer-valued:
    assert int(n) == n , ' the parameter must be an integer only'
  If the input is non-integer (e.g., 1.5) the function raises AssertionError.
"""

# ============================================================
# ✅ 2. Your function (unchanged)
# ============================================================
def DecimalToBinary(n):
    assert int(n) == n , ' the parameter must be an integer only'
    if n == 0:
        return 0
    return n % 2 + 10 * DecimalToBinary(int(n/2))


# ============================================================
# 🧪 3. Examples & demonstration (run to see outputs)
# ============================================================
if __name__ == "__main__":
    examples = [10, 13, 0, -13, 5, 102, 1.0]  # includes negative and integer-valued float
    print("Decimal -> Binary (as integer):")
    for val in examples:
        try:
            print(f"  DecimalToBinary({val!r}) = {DecimalToBinary(val)}")
        except AssertionError as e:
            print(f"  DecimalToBinary({val!r}) -> AssertionError: {e}")

    # Uncomment to see assertion for non-integer
    # print(DecimalToBinary(2.5))  # will raise AssertionError


# ============================================================
# 🧭 4. How the recursion works — step-by-step (example n = 13)
# ============================================================
"""
Compute DecimalToBinary(13):

1) DecimalToBinary(13)
   => 13 % 2 + 10 * DecimalToBinary(int(13/2))
   => 1 + 10 * DecimalToBinary(6)

2) DecimalToBinary(6)
   => 6 % 2 + 10 * DecimalToBinary(int(6/2))
   => 0 + 10 * DecimalToBinary(3)

3) DecimalToBinary(3)
   => 3 % 2 + 10 * DecimalToBinary(int(3/2))
   => 1 + 10 * DecimalToBinary(1)

4) DecimalToBinary(1)
   => 1 % 2 + 10 * DecimalToBinary(int(1/2))
   => 1 + 10 * DecimalToBinary(0)

5) DecimalToBinary(0) => base case -> 0

Return flow:
 DecimalToBinary(1) -> 1 + 10*0 = 1
 DecimalToBinary(3) -> 1 + 10*1 = 11
 DecimalToBinary(6) -> 0 + 10*11 = 110
 DecimalToBinary(13) -> 1 + 10*110 = 1101  (correct binary for 13)
"""

# ============================================================
# 🎨 5. ASCII Recursion Tree (n = 10)
# ============================================================
"""
DecimalToBinary(10)
 ├─ 10 % 2 = 0
 └─ 10 * DecimalToBinary(5)
      ├─ 5 % 2 = 1
      └─ 10 * DecimalToBinary(2)
           ├─ 2 % 2 = 0
           └─ 10 * DecimalToBinary(1)
                ├─ 1 % 2 = 1
                └─ 10 * DecimalToBinary(0)
                     └─ 0 (base)

Return (bottom-up):
 ... -> 1 -> 10*1 + 0 -> 101 -> 10*101 + 0 -> 1010
DecimalToBinary(10) = 1010
"""

# ============================================================
# 📈 6. Complexity Analysis (short & clear)
# ============================================================
"""
Let d = number of binary digits in n (d ≈ floor(log2 |n|) + 1)

- Time complexity: O(d)
  Each recursion divides n by 2, so number of calls equals number of binary digits.

- Space complexity: O(d)
  Recursion depth equals number of recursive calls until n reaches 0.

Notes:
 - Complexity depends on number of bits (log2 n), not the decimal magnitude directly.
 - Using multiplication by 10 builds the binary digits as a decimal integer (1101),
   which is convenient for printing but is not the numeric binary value (i.e., it's an integer holding the bit string).
"""

# ============================================================
# ⚠️ 7. Important pitfalls & notes (explicit)
# ============================================================
"""
1) Assertion:
   - Your function asserts `int(n) == n`, so floats like 1.0 pass, floats like 1.5 fail.
   - Non-integers will raise AssertionError with your original message.

2) Negative inputs:
   - Your implementation works for negative integers too because:
       a) Python's % operator returns non-negative remainder for negative operands: (-13) % 2 == 1
       b) int(n/2) truncates toward zero (int(-13/2) == -6), and repeated truncation reaches 0.
     So DecimalToBinary(-13) returns the same bit pattern as DecimalToBinary(13) (no sign shown).
   - If you want signed binary (two's complement) you'd need a different approach — not implemented here.

3) Use of int(n/2) (vs n // 2):
   - You used `int(n/2)` — this truncates toward zero for negative numbers.
   - Using `n // 2` uses floor division (different behavior for negatives). You intentionally used `int(n/2)`.

4) Representation:
   - The function returns an integer like 1101, which is the textual bit sequence as a decimal integer.
   - If you need the true integer value (i.e., 13) as binary *number* in base 2, typically you would return a string
     '1101' or return the numeric value 13 (already the input). The returned integer 1101 is convenient for visual display.

5) Very large n:
   - For extremely large n this recursive method can hit recursion limits. Iterative conversion is safer in production.
"""

# ============================================================
# 🧩 8. Practice Exercises (with hints)
# ============================================================
"""
1) Trace by hand:
   - Trace DecimalToBinary(13) using the steps above — show each recursive call and remainder.

2) Negative check:
   - Evaluate DecimalToBinary(-13) and explain why it returns the same bit pattern as 13 with your implementation.

3) String version:
   - Reimplement (as a separate function) to return a string of bits e.g., "1101" instead of integer 1101.
     (Keep this separate from the provided function.)

4) Iterative version:
   - Write an iterative loop (while n > 0) that builds the binary digits and returns a string.

5) Fractional numbers:
   - Decide and explain how you would handle non-integers (e.g., 13.5) — whether to reject them or extend to fractional binary.
"""

# ============================================================
# ❓ 9. Mini Quiz (answers below)
# ============================================================
"""
Q1: What is the base case in this function?
Q2: Why does DecimalToBinary(-13) produce the same digits as DecimalToBinary(13) here?
Q3: What is the time complexity in terms of number of bits?
Q4: What happens if the input is 2.5?

Answers:
A1: n == 0 → return 0
A2: Because (-13) % 2 == 1 and int(-13/2) truncates toward zero; remainders and truncations lead to same bit sequence.
A3: O(d) where d = number of binary digits (≈ log2 |n|)
A4: AssertionError: ' the parameter must be an integer only'
"""

# ============================================================
# ✅ End of note.py — Decimal to Binary (Recursion)
# ============================================================
"""
Summary:
 - You used modulus and integer division to extract binary digits.
 - The recursion builds the binary digits as a decimal integer by shifting with *10* at each step.
 - Input is asserted to be integer-valued; negative integers also work with this implementation.
 - For production use or very large inputs, consider iterative approach or return string-based binary.

"""
