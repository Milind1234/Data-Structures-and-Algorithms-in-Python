# ------------------------------------------------------------
# 📘 note.py — Recursion: Product of Array (Your Code Style)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to calculate the product (multiplication) of all elements
   in an array (list) using recursion.
 - Follow the same 3-step recursive pattern:
      1️⃣ Recursive Case
      2️⃣ Base Case
      3️⃣ Unintentional (edge) Cases
 - Keep your original function — simple and elegant.
 - Add visual explanation, examples, time/space complexity,
   and small practice questions.
"""

# ============================================================
# 🔎 0. Quick Overview
# ============================================================
"""
Problem:
  Given an array (list) of numbers, find the product of all its elements using recursion.

Example:
  arr = [1, 2, 3, 4]
  product = 1 × 2 × 3 × 4 = 24

Goal:
  Implement a recursive function that returns this product
  without using loops or built-in product functions.
"""

# ============================================================
# 🔁 1. Three-step recursive approach (applied)
# ============================================================
"""
Step 1️⃣ — Recursive Case:
   productOfArray(arr) = arr[0] × productOfArray(arr[1:])
   → Multiply first element by the product of remaining elements.

Step 2️⃣ — Base Case:
   When the list is empty (len(arr) == 0), return 1.
   → 1 is the **multiplicative identity** — it doesn’t affect the product.

Step 3️⃣ — Unintentional/Edge Cases:
   - Input should be a list (or iterable) containing numeric values.
   - If array contains non-numerical elements, multiplication will fail.
   - Empty list returns 1 by design.
"""

# ============================================================
# ✅ 2. Your Code (unchanged)
# ============================================================

def productOfArray(arr):
    if len(arr) == 0:
        return 1 
    return arr[0] * productOfArray(arr[1:])


# ============================================================
# 🧪 3. Examples & Tests
# ============================================================
if __name__ == "__main__":
    print("✅ Product of Array using Recursion:\n")

    examples = [
        [1, 2, 3, 4],         # 24
        [5],                  # 5
        [2, 3, 5],            # 30
        [],                   # 1 (empty list)
        [10, -2, 3],          # -60
    ]

    for arr in examples:
        print(f"productOfArray({arr}) = {productOfArray(arr)}")

    # Uncomment to see what happens for invalid input
    # print(productOfArray(['a', 2, 3]))  # TypeError expected


# ============================================================
# 🧭 4. How recursion works (example: [1, 2, 3])
# ============================================================
"""
Call stack trace for productOfArray([1, 2, 3]):

productOfArray([1, 2, 3])
 → 1 × productOfArray([2, 3])
      → 2 × productOfArray([3])
           → 3 × productOfArray([])
                → 1  (base case reached)

Return flow (bottom-up):
 productOfArray([])  → 1
 productOfArray([3]) → 3 × 1 = 3
 productOfArray([2,3]) → 2 × 3 = 6
 productOfArray([1,2,3]) → 1 × 6 = 6
✅ Final result: 6
"""

# ============================================================
# 🎨 5. Visualization (ASCII)
# ============================================================
"""
       [1, 2, 3]
          ↓
     1 × productOfArray([2, 3])
              ↓
         2 × productOfArray([3])
                      ↓
                 3 × productOfArray([])
                            ↓
                         return 1 (base case)

Return path:
1 × (2 × (3 × 1)) = 6
"""

# ============================================================
# 📈 6. Complexity Analysis
# ============================================================
"""
Let n = length of the array.

⏱ Time Complexity: O(n)
 - One recursive call per element.

🧮 Space Complexity: O(n)
 - Each recursive call is stored on the call stack until base case is reached.

Best case (empty list): returns immediately (O(1)).
Worst case: array length n → n recursive calls.
"""

# ============================================================
# ⚠️ 7. Common Mistakes & Fixes
# ============================================================
"""
❌ Forgetting the base case → infinite recursion.
✅ Always include `if len(arr) == 0: return 1`.

❌ Returning 0 for empty array.
✅ Wrong because 0 would zero out the entire product.

❌ Mutating list inside recursion.
✅ Avoid modifying the list directly (like arr.pop(0)), because that changes the original list.

💡 Tip: Using arr[1:] creates a new list each call — fine for small arrays,
   but not memory-efficient for huge arrays. Iterative methods or index tracking are faster.
"""

# ============================================================
# 🧩 8. Practice Exercises
# ============================================================
"""
1️⃣ Modify this function to calculate the **sum** of array elements instead of product.
     Hint: Replace `*` with `+` and base case 1 → 0.

2️⃣ Write an iterative version of this function using a for loop.

3️⃣ Extend it to handle nested lists:
     Example: [1, [2, 3], 4] → product = 24
     (Use recursion to flatten.)

4️⃣ Count recursive calls using a counter variable or print statements.

5️⃣ For a list of 100 elements, predict recursion depth — verify with Python’s recursion limit.
"""

# ============================================================
# ❓ 9. Mini Quiz (answers below)
# ============================================================
"""
Q1: What happens when the input list is empty?
Q2: Why do we return 1 instead of 0 for empty list?
Q3: What is the time complexity?
Q4: What will productOfArray([10]) return?

✅ Answers:
A1: It returns 1 (base case).
A2: Because 1 is the multiplicative identity — multiplying by 1 keeps the product unchanged.
A3: O(n) time and O(n) space.
A4: 10.
"""

# ============================================================
# ✅ End of note.py — Product of Array (Recursion)
# ============================================================
"""
Summary:
 - Base Case: Empty list → return 1
 - Recursive Case: arr[0] * productOfArray(arr[1:])
 - Works beautifully for small lists.
 - Time & space complexity: O(n)
 - Great stepping stone for understanding divide-and-conquer recursion.

Next:
→ You can extend this logic to find the **sum of elements**, **maximum element**, or **array flattening** recursively.
"""
