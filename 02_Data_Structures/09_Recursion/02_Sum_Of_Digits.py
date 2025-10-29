# ------------------------------------------------------------
# 📘 note.py — Recursion: Sum of Digits (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to build a recursive solution to find
   the sum of digits of any positive integer.
 - Use our 3-step recursive approach:
      1️⃣ Recursive Case
      2️⃣ Base Case
      3️⃣ Unintentional Case (Input validation)
 - Understand the working, visualization, complexity, and edge cases.

Note:
 - This version uses YOUR original function and code style.
 - Only comments, formatting, and explanations are added for clarity.
"""

# ============================================================
# 🔎 0. Problem Definition
# ============================================================
"""
🧩 Problem:
Find the sum of digits of a given positive integer using recursion.

📘 Example:
n = 112
Sum of digits = 1 + 1 + 2 = 4

Approach:
We can peel off each digit (using modulus % 10)
and reduce the number each time (using floor division // 10)
until it becomes zero.
"""

# ============================================================
# 🔁 1. Three Step Recursive Approach
# ============================================================
"""
Step 1️⃣: Recursive Case
    - Divide number by 10 to remove its last digit.
    - Use remainder (n % 10) to get last digit.
    - Add it to recursive call: sumOfDigits(n // 10)

Step 2️⃣: Base Case
    - When n becomes 0 → return 0
      (no digits left to add)

Step 3️⃣: Unintentional Case (Validation)
    - Number must be positive AND integer.
    - Use 'assert' to enforce this.
"""

# ============================================================
# ✅ 2. Your Code (Kept exactly same logic)
# ============================================================

def sumOfDigits(n):
    # Step 3️⃣: Input validation
    assert n >= 0 and int(n) == n, "Number should be a positive integer only"

    # Step 2️⃣: Base case
    if n == 0:
        return 0

    # Step 1️⃣: Recursive case
    # Take last digit (n % 10) + recursive call for remaining digits
    return int(n % 10) + sumOfDigits(int(n // 10))


# ============================================================
# 🧪 3. Examples & Testing
# ============================================================
if __name__ == "__main__":
    print("✅ Running Recursive Function Tests:\n")

    examples = [4, 12, 112, 1234, 10000, 0, 5.0]
    for num in examples:
        print(f"sumOfDigits({num}) = {sumOfDigits(num)}")

    # ❌ Uncomment these to see validation errors
    # print(sumOfDigits(-112))   # AssertionError
    # print(sumOfDigits(3.14))   # AssertionError


# ============================================================
# 🧭 4. Visualization — How recursion works internally
# ============================================================
"""
Example: n = 112

👉 Step-by-step breakdown:

sumOfDigits(112)
 = (112 % 10) + sumOfDigits(112 // 10)
 = 2 + sumOfDigits(11)

sumOfDigits(11)
 = (11 % 10) + sumOfDigits(11 // 10)
 = 1 + sumOfDigits(1)

sumOfDigits(1)
 = (1 % 10) + sumOfDigits(1 // 10)
 = 1 + sumOfDigits(0)

sumOfDigits(0)
 = 0   # base case reached

Now return values back up the stack:

sumOfDigits(0) → 0  
sumOfDigits(1) → 1 + 0 = 1  
sumOfDigits(11) → 1 + 1 = 2  
sumOfDigits(112) → 2 + 2 = 4 ✅
"""

# ============================================================
# 🎨 5. ASCII Visualization of Recursion Tree
# ============================================================
"""
               sumOfDigits(112)
                      |
          ----------------------------
          |                          |
   (n % 10)=2               sumOfDigits(11)
                                     |
                          --------------------
                          |                  |
                   (n % 10)=1       sumOfDigits(1)
                                           |
                                   ---------------
                                   |             |
                             (n % 10)=1   sumOfDigits(0)
                                               |
                                               0 (Base Case)
"""

# ============================================================
# 📈 6. Time and Space Complexity
# ============================================================
"""
Let d = number of digits in n.

- ⏱ Time Complexity: O(d)
  Each recursive call removes one digit.

- 🧮 Space Complexity: O(d)
  Each call is stored in the call stack until base case.

Example:
n = 12345  → 5 recursive calls
"""

# ============================================================
# ⚠️ 7. Common Mistakes & Fixes
# ============================================================
"""
❌ 1. Using 'or' instead of 'and' in assert
   - 'or' allows negative integers (since int(-5)==-5 is True)
   ✅ Use 'and' → both conditions must be True.

❌ 2. Missing base case
   - Without it → infinite recursion → RecursionError.

❌ 3. Not converting float inputs
   - 5.0 works (integer-valued float)
   - 3.14 fails (non-integer)

✅ 4. For large numbers:
   - Python recursion limit (~1000 calls) may stop recursion.
   - For very long numbers, use an iterative approach.
"""

# ============================================================
# 🧩 8. Practice Exercises (For You)
# ============================================================
"""
1️⃣ Modify this function to handle negative numbers
    ➤ Hint: use abs(n) before recursion.

2️⃣ Write a recursive function to count digits of n.
    ➤ Example: countDigits(112) = 3

3️⃣ Write a function to reverse digits using recursion.
    ➤ Example: reverse(1234) = 4321

4️⃣ Find product of digits of n recursively.
    ➤ Example: product(112) = 1 * 1 * 2 = 2

5️⃣ Try tracing the recursive calls for n = 305 manually
    ➤ Observe when zeros appear in recursion.
"""

# ============================================================
# ❓ 9. Mini Quiz (Test Your Understanding)
# ============================================================
"""
Q1: What is the base case in this recursion?
Q2: Why do we use int(n // 10) in the function?
Q3: What will happen if we remove the base case?
Q4: How many recursive calls for n = 99999?
Q5: What is the output for sumOfDigits(0)?

✅ Answers:
A1: When n == 0 → return 0
A2: To remove last digit and reduce the number each step
A3: Infinite recursion → RecursionError
A4: 6 calls (one per digit + base case)
A5: 0
"""

# ============================================================
# ✅ End of note.py — Recursion: Sum of Digits
# ============================================================
"""
🎯 Summary:
 - We applied the 3-step recursion rule.
 - Used modulus and division to peel digits.
 - Ensured base case & input validation.
 - Understood recursion flow and complexity.

Next Step:
→ Practice writing similar recursive problems (e.g., factorial, Fibonacci, sum of array elements).
"""
