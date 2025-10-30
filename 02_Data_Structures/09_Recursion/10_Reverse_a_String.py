# ------------------------------------------------------------
# 📘 note.py — Recursion: Reverse a String (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to reverse a string using recursion.
 - Understand how to process strings character by character (from end to start).
 - Visualize how recursive calls build the reversed string step-by-step.
 - Keep code simple, clean, and beginner-friendly.

Real-world use:
 - String reversal logic is the foundation for many interview problems,
   such as palindrome checks and data structure traversal.
"""

# ============================================================
# 🔎 0. Quick Overview
# ============================================================
"""
Problem:
  Given a string, return its reverse using recursion.

Example:
  Input  → "abc"
  Output → "cba"

We will use the **3-step recursive approach**:
  1️⃣ Recursive Case — process one character, call function for the rest.
  2️⃣ Base Case — stop when string length ≤ 1.
  3️⃣ Unintentional Case — handle non-string inputs if needed.
"""

# ============================================================
# 🔁 1. The recursive idea (step-by-step)
# ============================================================
"""
Step 1️⃣ — Recursive Case:
   reverse(strng) = last_char + reverse(all_but_last)
   → Take the last character and append the reverse of the remaining string.

Step 2️⃣ — Base Case:
   If length of string ≤ 1 → return string as it is.
   → When there’s only 1 or 0 characters, it’s already reversed.

Step 3️⃣ — Unintentional Cases:
   - Input should be of type `str`.
   - Empty strings should return "" (which is fine with this base case).
   - Add an assertion to validate type if desired.
"""

# ============================================================
# ✅ 2. Your Function (kept exactly same)
# ============================================================

def reverse(strng):
    if len(strng) <= 1:
        return strng
    return strng[len(strng) - 1] + reverse(strng[0:len(strng) - 1])


# ============================================================
# 🧪 3. Example Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Reverse String using Recursion:\n")

    examples = [
        "hello",
        "abcd",
        "a",
        "",
        "madam",
        "12345"
    ]

    for s in examples:
        print(f"reverse('{s}') → '{reverse(s)}'")

    # Expected Output:
    # 'hello' → 'olleh'
    # 'abcd' → 'dcba'
    # 'a' → 'a'
    # '' → ''
    # 'madam' → 'madam'
    # '12345' → '54321'


# ============================================================
# 🧭 4. How recursion works (example: "abc")
# ============================================================
"""
reverse("abc")
 → "c" + reverse("ab")
        → "b" + reverse("a")
                → "a"  (base case)

Return flow:
 reverse("a") = "a"
 reverse("ab") = "b" + "a" = "ba"
 reverse("abc") = "c" + "ba" = "cba"
✅ Final Output: "cba"
"""

# ============================================================
# 🎨 5. Visualization (Call Stack)
# ============================================================
"""
            reverse("abc")
                 ↓
       "c" + reverse("ab")
                 ↓
           "b" + reverse("a")
                 ↓
               "a"
Return Path:
reverse("a") → "a"
reverse("ab") → "b" + "a" = "ba"
reverse("abc") → "c" + "ba" = "cba"

Stack Unwinding (Bottom-up):
| "a" |
| "b" + "a" |
| "c" + "ba" |
Result = "cba"
"""

# ============================================================
# ⚙️ 6. Optional Enhancement (Input Validation)
# ============================================================
def safe_reverse(strng):
    assert isinstance(strng, str), "Input must be a string."
    if len(strng) <= 1:
        return strng
    return strng[-1] + safe_reverse(strng[:-1])

# Example:
# print(safe_reverse("Python"))  # no issue
# print(safe_reverse(123))       # raises AssertionError


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let n = length of string.

⏱ Time Complexity: O(n)
 - Each recursive call processes one character.

🧮 Space Complexity: O(n)
 - Each call stores a new string slice and recursion depth increases by 1.
 - Due to slicing (strng[0:len-1]), a new string is created every time,
   so actual memory usage is higher than iterative approach.
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Missing base case → infinite recursion.
✅ Fix: Add `if len(strng) <= 1: return strng`

❌ Forgetting to handle empty string.
✅ Fix: Base case covers it — returns "" safely.

❌ Forgetting return statement in recursive call.
✅ Always return the concatenated result.

💡 Tip:
   String slicing creates a new copy each call — fine for small inputs,
   but for large strings (>1000 chars), use an iterative or two-pointer approach.
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Write a recursive function `isPalindrome(strng)` using reverse().
     Hint: A string is a palindrome if strng == reverse(strng)

2️⃣ Modify reverse() to reverse a list instead of string.

3️⃣ Add print statements inside reverse() to trace each recursive call.

4️⃣ Rewrite reverse() iteratively using a for-loop.

5️⃣ Challenge: Reverse only words, not characters.
   Example: "I love Python" → "Python love I"
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What is the base case in this recursion?
Q2: What happens if input = "" ?
Q3: What is the time complexity?
Q4: Why is recursion less efficient for long strings?

✅ Answers:
A1: len(strng) <= 1 → return strng
A2: Returns "" (base case)
A3: O(n)
A4: Because slicing creates new strings each call (extra memory overhead).
"""

# ============================================================
# ✅ End of note.py — Reverse a String (Recursion)
# ============================================================
"""
Summary:
 - Base Case: len(strng) <= 1 → return strng
 - Recursive Case: last char + reverse(remaining)
 - Time: O(n), Space: O(n)
 - Simple yet powerful recursion — demonstrates call stack behavior clearly.

Next:
 → Try implementing a recursive **palindrome checker** using this reverse() function.
"""
