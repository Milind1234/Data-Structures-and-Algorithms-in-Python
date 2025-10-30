# ------------------------------------------------------------
# 📘 note.py — Recursion: nestedEvenSum (Sum of Even Numbers in Nested Objects)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to use recursion to traverse nested dictionaries.
 - Understand how to combine type checking, recursion, and condition-based summation.
 - Strengthen recursion logic applied to hierarchical data structures.

Problem Definition:
 Write a recursive function `nestedEvenSum(obj)` that returns the sum
 of all even numbers inside an object (which may contain nested objects).

Example:
 obj1 = {
   "outer": 2,
   "obj": {
     "inner": 2,
     "otherObj": {
       "superInner": 2,
       "notANumber": True,
       "alsoNotANumber": "yup"
     }
   }
 }
 nestedEvenSum(obj1) → 6
"""

# ============================================================
# 🔁 1. Step-by-step recursion logic
# ============================================================
"""
We will follow the standard 3-step recursion framework:

Step 1️⃣ — Recursive Case:
  - Loop through each key in the dictionary.
  - If the value is another dictionary → recursively call nestedEvenSum().
  - If the value is an even integer → add it to the sum.

Step 2️⃣ — Base Case:
  - When no nested objects are left, the recursion ends
    (no more dict values → return accumulated sum).

Step 3️⃣ — Unintentional Cases:
  - Ignore non-integer and non-dict values (like strings, booleans, lists, etc.).
  - Validate that input is a dictionary before recursion.
"""

# ============================================================
# ✅ 2. Your Code (kept exactly same)
# ============================================================

def nestedEvenSum(obj, sum=0):
    for key in obj:
        if type(obj[key]) is dict:
            sum += nestedEvenSum(obj[key])
        elif type(obj[key]) is int and obj[key] % 2 == 0:
            sum += obj[key]
    return sum


# ============================================================
# 🧪 3. Example Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Recursive Example: nestedEvenSum()\n")

    obj1 = {
      "outer": 2,
      "obj": {
        "inner": 2,
        "otherObj": {
          "superInner": 2,
          "notANumber": True,
          "alsoNotANumber": "yup"
        }
      }
    }

    obj2 = {
      "a": 2,
      "b": {"b": 2, "bb": {"b": 3, "bb": {"b": 2}}},
      "c": {"c": {"c": 2}, "cc": 'ball', "ccc": 5},
      "d": 1,
      "e": {"e": {"e": 2}, "ee": 'car'}
    }

    print(f"obj1 result → {nestedEvenSum(obj1)}")  # 6
    print(f"obj2 result → {nestedEvenSum(obj2)}")  # 10
    print(f"Empty dict → {nestedEvenSum({})}")     # 0


# ============================================================
# 🧭 4. How recursion works (Example: obj1)
# ============================================================
"""
obj1 = {
  "outer": 2,
  "obj": {
    "inner": 2,
    "otherObj": {
      "superInner": 2,
      "notANumber": True,
      "alsoNotANumber": "yup"
    }
  }
}

Flow:
 nestedEvenSum(obj1)
   → finds "outer" (2) → add 2
   → finds "obj" → recursive call

 nestedEvenSum(obj["obj"])
   → finds "inner" (2) → add 2
   → finds "otherObj" → recursive call

 nestedEvenSum(obj["obj"]["otherObj"])
   → finds "superInner" (2) → add 2
   → ignores True and "yup"

Total = 2 + 2 + 2 = ✅ 6
"""

# ============================================================
# 🎨 5. Visualization (Call Stack)
# ============================================================
"""
nestedEvenSum(obj1)
  ↓
nestedEvenSum(obj['obj'])
  ↓
nestedEvenSum(obj['obj']['otherObj'])
  ↓
Returns 2 → bubbles up
  2 + 2 + 2 = 6
"""

# ============================================================
# ⚙️ 6. Optional Safe Version (Input Validation)
# ============================================================
def safe_nestedEvenSum(obj, sum=0):
    """Version with input validation."""
    assert isinstance(obj, dict), "Input must be a dictionary."

    for key in obj:
        value = obj[key]
        if isinstance(value, dict):
            sum += safe_nestedEvenSum(value)
        elif isinstance(value, int) and value % 2 == 0:
            sum += value
    return sum


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let n = total number of keys (including nested ones).

⏱ Time Complexity: O(n)
 - Each key/value is visited exactly once.

🧮 Space Complexity: O(d)
 - d = depth of nested objects (recursion stack grows with depth).
 - Worst case: deeply nested dictionary.
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Forgetting base case:
   - Causes infinite recursion if you don’t handle non-dict values properly.

❌ Adding all numbers (not only even ones):
   - Must check 'value % 2 == 0' condition.

❌ Forgetting to return the accumulated sum:
   - Must return sum at the end of each recursive call.

✅ Tip:
   - Use isinstance(value, dict) instead of type(value) is dict → more Pythonic.
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Write a recursive function `nestedOddSum()` that sums all odd numbers.

2️⃣ Write `nestedCountNumbers()` that counts how many numeric values (int/float) exist.

3️⃣ Modify nestedEvenSum() to handle lists inside objects:
     e.g. {"a": [2, 4, 5]} → should also count 2 and 4.

4️⃣ Write a recursive version that returns both:
     - The total even sum
     - The count of even numbers (as a tuple).

5️⃣ Challenge:
     Write `nestedSumByCondition(obj, condition_fn)` where condition_fn
     is a callback that decides whether to include a number.
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What happens if input object is empty?
Q2: What if an even number is deeply nested?
Q3: What is the base case here?
Q4: Why do we check 'type(value) is dict'?

✅ Answers:
A1: Returns 0 (no even numbers).
A2: Recursion finds it — depth doesn’t matter.
A3: When there are no nested dictionaries left.
A4: To recursively handle nested dictionaries correctly.
"""

# ============================================================
# ✅ End of note.py — nestedEvenSum (Recursion)
# ============================================================
"""
Summary:
 - Base Case: no nested dict → return sum.
 - Recursive Case: traverse deeper if value is dict.
 - Time: O(n), Space: O(d)
 - Practical example of recursion in real data (JSON, configs).

Next:
 → Try **nestedOddSum()** or **sumNestedLists()** to extend this logic.
"""
