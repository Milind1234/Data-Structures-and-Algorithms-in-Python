# ------------------------------------------------------------
# 📘 note.py — Recursion: stringifyNumbers (Convert Numbers to Strings)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to use recursion to transform nested dictionary values.
 - Understand how to traverse objects recursively without mutating the original.
 - Practice handling multiple data types (dict, int, list, bool) safely.

Problem Definition:
 Write a recursive function `stringifyNumbers(obj)` that takes an object
 and converts all its numeric (int) values into strings.

Example:
 Input  →
  {
    "num": 1,
    "test": [],
    "data": {
      "val": 4,
      "info": {
        "isRight": True,
        "random": 66
      }
    }
  }

 Output →
  {
    "num": "1",
    "test": [],
    "data": {
      "val": "4",
      "info": {
        "isRight": True,
        "random": "66"
      }
    }
  }
"""

# ============================================================
# 🔁 1. Step-by-step recursion logic
# ============================================================
"""
We follow the standard 3-step recursion framework:

Step 1️⃣ — Recursive Case:
  - Traverse all keys of the dictionary.
  - If the value is another dict → recurse deeper.
  - If the value is an integer → convert to string.
  - Otherwise → keep as is.

Step 2️⃣ — Base Case:
  - When there are no nested dictionaries left (no more recursion possible).

Step 3️⃣ — Unintentional Cases:
  - Ignore lists, booleans, and strings (do not recurse inside lists).
  - Ensure we always create a new dictionary, not modify the original.
"""

# ============================================================
# ✅ 2. Fixed + Clean Version of Your Code
# ============================================================

def stringifyNumbers(obj):
    newObj = {}
    for key in obj:
        value = obj[key]
        # If the value is a dictionary → recurse deeper
        if isinstance(value, dict):
            newObj[key] = stringifyNumbers(value)
        # If it's an integer → convert to string
        elif isinstance(value, int):
            newObj[key] = str(value)
        # Otherwise → keep as-is
        else:
            newObj[key] = value
    return newObj


# ============================================================
# 🧪 3. Example Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Recursive Example: stringifyNumbers()\n")

    obj = {
      "num": 1,
      "test": [],
      "data": {
        "val": 4,
        "info": {
          "isRight": True,
          "random": 66
        }
      }
    }

    result = stringifyNumbers(obj)
    print("Original Object:")
    print(obj)
    print("\nStringified Numbers Object:")
    print(result)


# ============================================================
# 🧭 4. How recursion works (Example)
# ============================================================
"""
Input:
{
  "num": 1,
  "test": [],
  "data": {
    "val": 4,
    "info": {
      "isRight": True,
      "random": 66
    }
  }
}

Recursive Flow:
1️⃣ stringifyNumbers(obj)
   → num = 1 → "1"
   → test = [] → []
   → data = {...} → recurse

2️⃣ stringifyNumbers(obj["data"])
   → val = 4 → "4"
   → info = {...} → recurse

3️⃣ stringifyNumbers(obj["data"]["info"])
   → isRight = True → keep
   → random = 66 → "66"

Return flow:
   info → {'isRight': True, 'random': '66'}
   data → {'val': '4', 'info': {...}}
✅ Final Output:
   {'num': '1', 'test': [], 'data': {...}}
"""

# ============================================================
# 🎨 5. Visualization (Call Stack)
# ============================================================
"""
stringifyNumbers(obj)
  ↓
stringifyNumbers(obj['data'])
  ↓
stringifyNumbers(obj['data']['info'])
  ↓
returns {'isRight': True, 'random': '66'}
  ↓
returns {'val': '4', 'info': {...}}
  ↓
returns {'num': '1', 'test': [], 'data': {...}}
"""

# ============================================================
# ⚙️ 6. Optional Safe Version (Input Validation)
# ============================================================
def safe_stringifyNumbers(obj):
    """Version with validation for safety."""
    assert isinstance(obj, dict), "Input must be a dictionary."
    newObj = {}
    for key, value in obj.items():
        if isinstance(value, dict):
            newObj[key] = safe_stringifyNumbers(value)
        elif isinstance(value, int):
            newObj[key] = str(value)
        else:
            newObj[key] = value
    return newObj


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let n = total number of keys (including nested ones).

⏱ Time Complexity: O(n)
 - Each key/value pair is processed once.

🧮 Space Complexity: O(d)
 - d = maximum depth of nested objects (recursion stack depth).
 - Plus O(n) for the new dictionary returned.
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Using 'newObj = obj':
   - Causes mutation of the original dictionary.
   ✅ Fix: Always initialize newObj = {}.

❌ Recursing into lists:
   - Lists don’t follow key-value structure, skip them.

❌ Forgetting base case:
   - Not a typical base case here, but ensure recursion ends when value is not a dict.
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Modify stringifyNumbers() to also convert floats → strings.

2️⃣ Extend it to stringify even numbers only (using %2 check).

3️⃣ Write `stringifyBooleans()` that converts all booleans → strings.

4️⃣ Write `deepStringify()` that stringifies *every* non-dict type.

5️⃣ Add handling for lists containing numbers:
    Example:
    {'a': [1, 2, {'b': 3}]} → {'a': ['1', '2', {'b': '3'}]}
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What happens if input has nested dictionaries?
Q2: What if a value is a list of numbers?
Q3: Why shouldn’t we use newObj = obj?
Q4: What is the time complexity?

✅ Answers:
A1: Function handles it recursively.
A2: Lists are ignored (they remain unchanged).
A3: Because it modifies the original dictionary.
A4: O(n)
"""

# ============================================================
# ✅ End of note.py — stringifyNumbers (Recursion)
# ============================================================
"""
Summary:
 - Base Case: no nested dicts left → return current object.
 - Recursive Case: process nested dicts recursively.
 - Converts only integers → strings, ignores all other types.
 - Time: O(n), Space: O(d)
 - A great example of recursion on nested data structures (e.g. JSON).

Next:
 → Try **stringifyAll()** that converts *all* non-dict values to strings recursively.
"""
