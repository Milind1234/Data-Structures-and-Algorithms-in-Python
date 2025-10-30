# ------------------------------------------------------------
# 📘 note.py — Recursion: Flatten a Nested List
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to use recursion to flatten (unpack) a deeply nested list.
 - Understand how recursion traverses nested structures.
 - Strengthen understanding of recursive traversal and list extension.

Definition:
 Flattening means converting a nested list (lists inside lists)
 into a single list containing all elements in order.

Example:
 Input  → [1, [2, [3, 4], 5]]
 Output → [1, 2, 3, 4, 5]
"""

# ============================================================
# 🔁 1. Step-by-step recursion logic
# ============================================================
"""
We will follow the standard 3-step recursion pattern:

Step 1️⃣ — Recursive Case:
  - Traverse the array.
  - If an element is a list → recursively flatten that sublist
    and extend the result into our main list.

Step 2️⃣ — Base Case:
  - When there are no more nested lists (i.e., the element is not a list),
    simply append the element to the result.

Step 3️⃣ — Unintentional Cases:
  - Ensure the input is a list.
  - You can add asserts for input validation if needed.
"""

# ============================================================
# ✅ 2. Your Code (kept exactly same)
# ============================================================

def flatten(arr):
    resultArr = []
    for custItem in arr:
        if type(custItem) is list:
            resultArr.extend(flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr


# ============================================================
# 🧪 3. Example Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Recursive Example: Flatten a Nested List\n")

    print(f"flatten([1, 2, 3])                               =>     {flatten([1, 2, 3])}")                        # [1, 2, 3]
    print(f"flatten([1, [2, 3]])                             =>     {flatten([1, [2, 3]])}")                      # [1, 2, 3]
    print(f"flatten([1, [2, [3, 4], [5, 6]], 7])             =>     {flatten([1, [2, [3, 4], [5, 6]], 7])}")      # [1, 2, 3, 4, 5, 6, 7]
    print(f"flatten([[1, 2], [[3, 4], [5, [6, 7]]]])         =>     {flatten([[1, 2], [[3, 4], [5, [6, 7]]]])}")  # [1, 2, 3, 4, 5, 6, 7]
    print(f"flatten([])                                      =>     {flatten([])}")                               # []
    print(f"flatten([[[[42]]]])                              =>     {flatten([[[[42]]]])}")                       # [42]


# ============================================================
# 🧭 4. How recursion works (Example: [1, [2, [3, 4]], 5])
# ============================================================
"""
Flatten([1, [2, [3, 4]], 5])
→ Loop over elements:
   - 1 → append → [1]
   - [2, [3, 4]] → recursive call:
         Flatten([2, [3, 4]])
         → 2 → append → [2]
         → [3, 4] → recursive call:
              Flatten([3, 4]) → [3, 4]
         → extend → [2, 3, 4]
     → extend to parent → [1, 2, 3, 4]
   - 5 → append → [1, 2, 3, 4, 5]
✅ Final Output: [1, 2, 3, 4, 5]
"""

# ============================================================
# 🎨 5. Visualization (Call Stack)
# ============================================================
"""
flatten([1, [2, [3, 4]], 5])
|
├── flatten([2, [3, 4]])
│     └── flatten([3, 4])
│           └── returns [3, 4]
│     └── returns [2, 3, 4]
|
└── returns [1, 2, 3, 4, 5]
"""

# ============================================================
# ⚙️ 6. Optional Safe Version (Input Validation)
# ============================================================
def safe_flatten(arr):
    """Version with type checking for safety."""
    assert isinstance(arr, list), "Input must be a list."

    resultArr = []
    for custItem in arr:
        if isinstance(custItem, list):
            resultArr.extend(safe_flatten(custItem))
        else:
            resultArr.append(custItem)
    return resultArr


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let n = total number of elements (including nested ones).

⏱ Time Complexity: O(n)
 - Each element is visited exactly once.

🧮 Space Complexity: O(n)
 - The recursion stack grows based on the nesting depth.
 - Result array also stores n elements.
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Using append() instead of extend() for nested lists:
   → Causes sublists to appear instead of being merged.

✅ Fix: Use extend() to merge flattened results.

❌ Forgetting to handle empty lists:
   → Always handle base case by returning [] when input is empty.

💡 Tip:
   - To check deep recursion, try lists like [1, [2, [3, [4, [5]]]]].
   - Python has a recursion depth limit (~1000 by default).
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Modify flatten() to handle tuples as well as lists.

2️⃣ Write a version that counts total elements while flattening.

3️⃣ Write an iterative version using a stack.

4️⃣ Create a recursive function to flatten dictionaries (nested keys).

5️⃣ Challenge: flatten() a list and remove duplicates while doing it.
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What happens when input = [] ?
Q2: What happens when an element is not a list?
Q3: What is the time complexity?
Q4: Why is extend() better than append() here?

✅ Answers:
A1: Returns [] (empty list).
A2: Gets added directly to the result array.
A3: O(n)
A4: Because extend() merges lists; append() would insert a sublist.
"""

# ============================================================
# ✅ End of note.py — Flatten (Recursion)
# ============================================================
"""
Summary:
 - Base Case: no nested lists → return element.
 - Recursive Case: flatten each sublist and extend result.
 - Time: O(n), Space: O(n)
 - A powerful recursion pattern — used in tree traversals and JSON parsing.

Next:
 → Try writing a function to **flatten a nested dictionary** using recursion.
"""
