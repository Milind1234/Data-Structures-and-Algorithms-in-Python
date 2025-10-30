# ------------------------------------------------------------
# 📘 note.py — Recursion: Palindrome Checker (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to check whether a string is a palindrome using recursion.
 - Understand how to compare characters from both ends moving inward.
 - Reinforce recursive pattern recognition (base case + recursive case).
 - Visualize how recursion reduces the problem step by step.

Definition:
 A palindrome is a word, number, phrase, or sequence that reads the same
 backward as forward.

Examples:
 "madam"  ✅
 "racecar" ✅
 "python"  ❌
 "a"       ✅
 ""        ✅ (empty string is considered palindrome)
"""

# ============================================================
# 🔎 0. Quick Overview
# ============================================================
"""
We follow the standard 3-step recursion pattern:

Step 1️⃣ — Recursive Case:
   Compare first and last characters:
   - If they are equal, recurse on the substring between them.
   - If not, return False.

Step 2️⃣ — Base Case:
   When the string is empty (or 1 char), it is a palindrome.
   → Return True

Step 3️⃣ — Unintentional Case:
   Input must be a string.
   You can add an assert to handle invalid input if needed.
"""

# ============================================================
# ✅ 1. Your Function (kept exactly same)
# ============================================================

def isPalindrome(strng):
    if len(strng) == 0:
        return True
    if strng[0] != strng[len(strng) - 1]:
        return False
    return isPalindrome(strng[1:-1])


# ============================================================
# 🧪 2. Example Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Palindrome Check using Recursion:\n")

    examples = [
        "madam",
        "racecar",
        "level",
        "python",
        "a",
        "",
        "refer",
        "hello"
    ]

    for s in examples:
        result = isPalindrome(s)
        print(f"isPalindrome('{s}') → {result}")

    # Expected Output:
    # 'madam' → True
    # 'racecar' → True
    # 'level' → True
    # 'python' → False
    # 'a' → True
    # '' → True
    # 'refer' → True
    # 'hello' → False


# ============================================================
# 🧭 3. Step-by-Step Recursion Flow (Example: "madam")
# ============================================================
"""
Initial call: isPalindrome("madam")
 → Compare 'm' == 'm' ✅ → call isPalindrome("ada")

     isPalindrome("ada")
      → Compare 'a' == 'a' ✅ → call isPalindrome("d")

         isPalindrome("d")
          → len == 1 → return True

Backtracking:
 isPalindrome("d") → True
 isPalindrome("ada") → True
 isPalindrome("madam") → True
✅ Final Output: True
"""

# ============================================================
# 🎨 4. Visualization (Call Stack)
# ============================================================
"""
                 isPalindrome("madam")
                    ↓
                 isPalindrome("ada")
                    ↓
                 isPalindrome("d")
                    ↓
                 return True
Return flow:
 True → True → True → ✅ True
"""

# ============================================================
# ⚙️ 5. Optional Safe Version (with Input Validation)
# ============================================================
def safe_isPalindrome(strng):
    """
    Palindrome check with input validation.
    """
    assert isinstance(strng, str), "Input must be a string."
    if len(strng) == 0 or len(strng) == 1:
        return True
    if strng[0] != strng[-1]:
        return False
    return safe_isPalindrome(strng[1:-1])

# Example:
# print(safe_isPalindrome("noon"))  # True
# print(safe_isPalindrome(12321))   # AssertionError


# ============================================================
# 📈 6. Complexity Analysis
# ============================================================
"""
Let n = length of the string.

⏱ Time Complexity: O(n)
 - Each recursive call processes 2 characters (front and back).

🧮 Space Complexity: O(n)
 - Each recursive call stores a substring and recursion depth increases by 1.
 - String slicing creates new substrings each time → higher memory use.
"""

# ============================================================
# ⚠️ 7. Common Mistakes & Fixes
# ============================================================
"""
❌ Forgetting base case:
   → Causes infinite recursion on empty strings.

❌ Using slicing incorrectly:
   → Be careful with strng[1:-1] — it correctly removes first and last chars.

❌ Not returning boolean values consistently:
   → Always return True or False, not mixed types.

✅ Tip:
   You can also normalize input before checking (e.g., lowercase, remove spaces):
      s = ''.join(ch.lower() for ch in strng if ch.isalnum())
      Then call isPalindrome(s)
"""

# ============================================================
# 🧩 8. Practice Exercises
# ============================================================
"""
1️⃣ Modify isPalindrome() to ignore case and spaces.
   Example: "A man a plan a canal Panama" → True

2️⃣ Write an iterative (loop-based) palindrome checker for comparison.

3️⃣ Add print() statements in isPalindrome() to trace the recursive calls.

4️⃣ Try it on numbers converted to strings: isPalindrome(str(12321)).

5️⃣ Implement a recursive function that counts palindromic substrings.
"""

# ============================================================
# ❓ 9. Mini Quiz (answers below)
# ============================================================
"""
Q1: What is the base case in this function?
Q2: What does isPalindrome("") return?
Q3: What happens if the first and last characters differ?
Q4: What is the time complexity?
Q5: Why is recursion less efficient here?

✅ Answers:
A1: When len(strng) == 0 → True
A2: True (empty string is palindrome)
A3: Immediately returns False
A4: O(n)
A5: Because each recursive call slices the string, creating a new copy
"""
# ============================================================
# ✅ End of note.py — Palindrome Check (Recursion)
# ============================================================
"""
Summary:
 - Base Case: empty string → True
 - Recursive Case: compare first and last characters → recurse on middle
 - Time: O(n), Space: O(n)
 - Clear, elegant example of reducing a problem step-by-step.

Next:
 → Try a similar recursion challenge:
    “Check if a string is palindrome using **two pointers** (no slicing)”.
"""
