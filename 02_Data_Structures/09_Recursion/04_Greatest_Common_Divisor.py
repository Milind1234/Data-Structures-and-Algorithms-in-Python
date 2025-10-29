# ------------------------------------------------------------
# 📘 note.py — Recursion: Greatest Common Divisor (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Learn to calculate the Greatest Common Divisor (GCD) of two numbers using recursion.
 - Follow the same 3-step recursive approach:
     1️⃣ Recursive Case
     2️⃣ Base Case
     3️⃣ Unintentional (input validation) Cases
 - Use your own code (kept exactly same in structure and logic).
 - Includes mathematical explanation, visualization, complexity analysis, and practice exercises.

Note:
 - Based on the **Euclidean Algorithm**, which is an efficient method for finding the GCD.
 - Function used: gcd(a, b)
"""

# ============================================================
# 🔎 0. Concept & Mathematical Background
# ============================================================
"""
📘 Definition:
The GCD (Greatest Common Divisor) of two numbers is the largest positive integer
that divides both numbers exactly (without remainder).

Examples:
 - GCD(8, 12) = 4
   because 8 = 2 × 2 × 2  and  12 = 2 × 2 × 3  → common factors are (2 × 2) = 4
 - GCD(48, 18) = 6
   because 48 ÷ 18 → remainder 12
            18 ÷ 12 → remainder 6
            12 ÷ 6  → remainder 0  → stop → GCD = 6

🧮 Euclidean Algorithm Logic:
If we want GCD(a, b):
    GCD(a, b) = GCD(b, a % b)
Keep doing this until b == 0 → then GCD = a.
"""

# ============================================================
# 🔁 1. Three Step Recursive Approach
# ============================================================
"""
Step 1️⃣: Recursive Case
   - GCD(a, b) = GCD(b, a % b)

Step 2️⃣: Base Case
   - If b == 0 → return a
     (because when remainder becomes zero, the current a is the GCD)

Step 3️⃣: Unintentional (Input Validation)
   - Both numbers must be integers.
   - GCD is always defined for positive integers, so convert negatives to positives.
"""

# ============================================================
# ✅ 2. Your Code (Kept same logic)
# ============================================================

def gcd(a, b):
    # Step 3️⃣: Input Validation
    # Ensure both numbers are integers and positive
    assert int(a) == a and int(b) == b, "The numbers must be integers only"

    # Convert negatives to positives (GCD(-a, b) == GCD(a, b))
    if a < 0:
        a = -a
    if b < 0:
        b = -b

    # Step 2️⃣: Base Case — if second number is zero
    if b == 0:
        return a

    # Step 1️⃣: Recursive Case — Euclidean algorithm
    return gcd(b, a % b)


# ============================================================
# 🧪 3. Examples & Test Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Running GCD (Recursive) Tests:\n")

    examples = [
        (48, 18),     # Expected 6
        (8, 12),      # Expected 4
        (270, 192),   # Expected 6
        (-48, 18),    # Negative converted → Expected 6
        (18, -48),    # Expected 6
        (0, 25),      # GCD(0, 25) = 25
        (25, 0),      # GCD(25, 0) = 25
    ]

    for a, b in examples:
        print(f"GCD({a}, {b}) = {gcd(a, b)}")

    # Uncomment to test invalid cases
    # print(gcd(3.5, 7))   # AssertionError
    # print(gcd(8, 0.5))   # AssertionError


# ============================================================
# 🧭 4. How Recursion Works — Step-by-Step
# ============================================================
"""
Example: GCD(48, 18)

Step 1:
  a = 48, b = 18
  → gcd(18, 48 % 18) = gcd(18, 12)

Step 2:
  a = 18, b = 12
  → gcd(12, 18 % 12) = gcd(12, 6)

Step 3:
  a = 12, b = 6
  → gcd(6, 12 % 6) = gcd(6, 0)

Step 4:
  b == 0 → return a = 6 ✅

Return flow:
  gcd(6, 0) → 6
  gcd(12, 6) → 6
  gcd(18, 12) → 6
  gcd(48, 18) → 6
"""

# ============================================================
# 🎨 5. Visualization (ASCII Recursion Diagram)
# ============================================================
"""
                gcd(48, 18)
                     |
             ----------------
             |              |
         gcd(18, 12)     a % b = 12
              |
         -------------
         |           |
     gcd(12, 6)   a % b = 6
          |
      -----------
      |         |
  gcd(6, 0)   a % b = 0  ← Base Case → return 6

Return Path:
  gcd(6,0)=6 → gcd(12,6)=6 → gcd(18,12)=6 → gcd(48,18)=6
"""

# ============================================================
# 📈 6. Complexity Analysis
# ============================================================
"""
Let a > b ≥ 0

- Time Complexity: O(log(min(a, b)))
  The Euclidean algorithm runs in logarithmic time relative to the smaller number.

- Space Complexity: O(log(min(a, b)))
  (due to recursion stack depth)

This is one of the most efficient recursive algorithms in mathematics.
"""

# ============================================================
# ⚠️ 7. Common Mistakes & Fixes
# ============================================================
"""
❌ Mistake 1: Forgetting base case (b == 0)
   → Leads to infinite recursion.

❌ Mistake 2: Using float or non-integer input.
   → Causes incorrect behavior in modulo operation.

❌ Mistake 3: Not handling negatives.
   → Always convert negative inputs to positive before recursion.

✅ Tip: GCD(0, n) = n and GCD(n, 0) = n
✅ Tip: GCD of any number with itself is that number → GCD(n, n) = n
"""

# ============================================================
# 🧩 8. Practice Exercises
# ============================================================
"""
1️⃣ Try tracing gcd(270, 192) manually — verify each step.
     (Expected result: 6)

2️⃣ Modify the function to count how many recursive calls are made
     ➤ Hint: use a counter parameter.

3️⃣ Add print statements inside gcd() to visualize each call.

4️⃣ Write an iterative version (using while loop) and compare recursion depth.

5️⃣ Extend function to handle lists: find GCD of more than two numbers
     ➤ Example: gcd_list([48, 18, 30]) = 6
"""

# ============================================================
# ❓ 9. Mini Quiz (Answers below)
# ============================================================
"""
Q1: What is the base case in the recursive GCD function?
Q2: What does gcd(a, b) compute when b == 0?
Q3: Why do we convert negative numbers to positive?
Q4: What happens if input is a float like gcd(5.5, 2)?
Q5: What is the time complexity of the Euclidean algorithm?

✅ Answers:
A1: Base case → if b == 0 → return a
A2: It returns 'a' because remainder reached 0
A3: GCD(-a, b) = GCD(a, b); negative values don't affect magnitude
A4: AssertionError (input must be integer)
A5: O(log(min(a, b)))
"""

# ============================================================
# ✅ End of note.py — GCD using Recursion
# ============================================================
"""
🎯 Summary:
 - Used Euclidean Algorithm recursively: gcd(a, b) = gcd(b, a % b)
 - Base case: when b == 0 → return a
 - Handled invalid inputs and negatives
 - Complexity: O(log(min(a, b))) — very efficient!
"""
