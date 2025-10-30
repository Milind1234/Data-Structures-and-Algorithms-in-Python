# ------------------------------------------------------------
# 📘 note.py — Recursion: someRecursive (Array + Callback)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to use recursion with callbacks (functions as arguments).
 - Understand how to check if *any* element in a list satisfies a condition.
 - Strengthen recursion fundamentals with array traversal and boolean return logic.

Problem Definition:
 Write a recursive function `someRecursive` which accepts:
   - an array (list)
   - a callback function `cb`

Return:
   - True → if *any* element in the array returns True when passed to `cb`
   - False → otherwise

Example:
  someRecursive([1,2,3,4], isOdd) → True
  someRecursive([4,6,8,9], isOdd) → True
  someRecursive([4,6,8], isOdd) → False
"""

# ============================================================
# 🔁 1. Step-by-step recursion logic
# ============================================================
"""
We will follow the standard 3-step recursion plan:

Step 1️⃣ — Recursive Case:
  - Keep checking one element (arr[0]) at a time.
  - If the callback returns False for this element,
    call someRecursive() again for the rest of the array.

Step 2️⃣ — Base Case:
  - If the array becomes empty → return False
    (means no element satisfied the condition).

Step 3️⃣ — Unintentional Cases:
  - arr must be a list, and cb must be a callable function.
  - You can add asserts to ensure this if needed.
"""

# ============================================================
# ✅ 2. Your code (kept exactly same)
# ============================================================

def isOdd(num):
    """Callback function to test if a number is odd."""
    if num % 2 == 0:
        return False
    else:
        return True


def someRecursive(arr, cb):
    """Returns True if any element in arr passes the callback test."""
    if len(arr) == 0:
        return False
    if not cb(arr[0]):
        return someRecursive(arr[1:], cb)
    return True


# ============================================================
# 🧪 3. Example Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Recursive Callback Example: someRecursive()\n")

    print(f"someRecursive([1, 2, 3, 4], isOdd) → {someRecursive([1, 2, 3, 4], isOdd)}")   # True (1 is odd)
    print(f"someRecursive([4, 6, 8, 9], isOdd) → {someRecursive([4, 6, 8, 9], isOdd)}")   # True (9 is odd)
    print(f"someRecursive([4, 6, 8], isOdd) → {someRecursive([4, 6, 8], isOdd)}")         # False (no odd numbers)
    print(f"someRecursive([], isOdd) → {someRecursive([], isOdd)}")                       # False (empty array)


# ============================================================
# 🧭 4. How recursion works (Example: [4,6,8,9], isOdd)
# ============================================================
"""
Call Flow:
 someRecursive([4,6,8,9], isOdd)
   → isOdd(4) = False → recurse on [6,8,9]
       → isOdd(6) = False → recurse on [8,9]
           → isOdd(8) = False → recurse on [9]
               → isOdd(9) = True → ✅ return True

Backtracking:
 True bubbles up through all previous calls:
  → someRecursive([8,9]) → True
  → someRecursive([6,8,9]) → True
  → someRecursive([4,6,8,9]) → True
✅ Final Output: True
"""

# ============================================================
# 🎨 5. Visualization (Call Stack)
# ============================================================
"""
                  someRecursive([4,6,8,9])
                         ↓
                  someRecursive([6,8,9])
                         ↓
                  someRecursive([8,9])
                         ↓
                  someRecursive([9])
                         ↓
                  isOdd(9) → True
Return flow (bubbles up):
 True → True → True → ✅ True
"""

# ============================================================
# ⚙️ 6. Optional Safe Version (Input Validation)
# ============================================================
def safe_someRecursive(arr, cb):
    """Version with basic type validation."""
    assert isinstance(arr, list), "Input must be a list."
    assert callable(cb), "Callback must be a function."

    if len(arr) == 0:
        return False
    if not cb(arr[0]):
        return safe_someRecursive(arr[1:], cb)
    return True


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let n = length of array.

⏱ Time Complexity: O(n)
 - Each recursive call processes one element.
 - Worst case: traverses entire array.

🧮 Space Complexity: O(n)
 - One recursive call stored in stack for each element.
 - Each call holds a smaller slice of the array (new list).
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Forgetting base case:
   → Infinite recursion → RecursionError.

❌ Not returning result of recursive call:
   → Must return the recursive call result (someRecursive(arr[1:], cb)).

❌ Forgetting to negate callback (not cb(arr[0])):
   → Causes reversed logic.

💡 Tip:
   Instead of slicing (arr[1:]), you can use an index parameter to avoid extra memory usage.
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Write a recursive function `allRecursive()` that returns True only if
    *all* elements in array return True when passed to the callback.

2️⃣ Write a recursive function `productOfArray()` (you already did earlier).
    Compare its structure to this one — both use similar recursion logic.

3️⃣ Modify `someRecursive()` to stop early when a True value is found.
    (Already works like this naturally — test it with print statements!)

4️⃣ Implement an iterative version of someRecursive() using a loop.

5️⃣ Create new callbacks:
      - isEven()
      - isPositive()
      - greaterThanTen()
    and test your function with them.
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What happens if the array is empty?
Q2: What does someRecursive([2,4,6], isOdd) return?
Q3: What is the time complexity?
Q4: What does the callback function do here?

✅ Answers:
A1: Returns False (base case).
A2: False (none are odd).
A3: O(n) time, O(n) space.
A4: The callback checks each value; recursion stops when one returns True.
"""

# ============================================================
# ✅ End of note.py — someRecursive (Recursion + Callback)
# ============================================================
"""
Summary:
 - Base Case: empty array → return False
 - Recursive Case: test arr[0]; if False → recurse on arr[1:]
 - Returns True if any element satisfies callback condition.
 - Time: O(n), Space: O(n)
 - Demonstrates recursion + higher-order functions beautifully.

Next:
 → Try building the reverse version: **allRecursive()**
    (returns True only if *every* element passes the callback).
"""
