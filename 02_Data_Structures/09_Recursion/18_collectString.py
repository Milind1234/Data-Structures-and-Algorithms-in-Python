# ------------------------------------------------------------
# 📘 note.py — Recursion: collectStrings (Nested Object Traversal)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to use recursion to traverse deeply nested dictionaries.
 - Collect all string values from an object regardless of nesting depth.
 - Strengthen understanding of recursion on tree-like JSON data.

Problem Definition:
 Write a recursive function `collectStrings(obj)` that accepts a dictionary
 and returns a list of all values that are strings.

Example:
 Input  →
  {
    "stuff": 'foo',
    "data": {
      "val": {
        "thing": {
          "info": 'bar',
          "moreInfo": {
            "evenMoreInfo": {
              "weMadeIt": 'baz'
            }
          }
        }
      }
    }
  }

 Output →
  ['foo', 'bar', 'baz']
"""

# ============================================================
# 🔁 1. Step-by-step recursion logic
# ============================================================
"""
We follow the standard 3-step recursion framework:

Step 1️⃣ — Recursive Case:
  - Loop through each key in the dictionary.
  - If the value is a dictionary → recurse deeper.
  - If the value is a string → collect it.
  - Otherwise → ignore it.

Step 2️⃣ — Base Case:
  - Stop when there are no more nested dictionaries (no deeper recursion possible).

Step 3️⃣ — Unintentional Cases:
  - Input must be a dictionary.
  - Skip non-dictionary types such as lists, integers, booleans, etc.
"""

# ============================================================
# ✅ 2. Final Recursive Code
# ============================================================

def collectStrings(obj):
    assert isinstance(obj, dict), "Input must be a dictionary"
    result = []
    for key in obj:
        value = obj[key]
        # If value is string → collect it
        if isinstance(value, str):
            result.append(value)
        # If value is dictionary → recurse into it
        elif isinstance(value, dict):
            result += collectStrings(value)
    return result


# ============================================================
# 🧪 3. Example Runs
# ============================================================
if __name__ == "__main__":
    obj = {
        "stuff": 'foo',
        "data": {
            "val": {
                "thing": {
                    "info": 'bar',
                    "moreInfo": {
                        "evenMoreInfo": {
                            "weMadeIt": 'baz'
                        }
                    }
                }
            }
        }
    }

    print("✅ Recursive Example: collectStrings()\n")
    print("Input Object:")
    print(obj)
    print("\nCollected Strings:")
    print(collectStrings(obj))
    # Expected Output → ['foo', 'bar', 'baz']


# ============================================================
# 🧭 4. How recursion works (Example)
# ============================================================
"""
Input:
{
  "stuff": 'foo',
  "data": {
    "val": {
      "thing": {
        "info": 'bar',
        "moreInfo": {
          "evenMoreInfo": {
            "weMadeIt": 'baz'
          }
        }
      }
    }
  }
}

Recursive Flow:
1️⃣ collectStrings(obj)
    → stuff = 'foo' → add ['foo']
    → data = {...} → recurse

2️⃣ collectStrings(obj['data'])
    → val = {...} → recurse

3️⃣ collectStrings(obj['data']['val'])
    → thing = {...} → recurse

4️⃣ collectStrings(obj['data']['val']['thing'])
    → info = 'bar' → add ['bar']
    → moreInfo = {...} → recurse

5️⃣ collectStrings(obj['data']['val']['thing']['moreInfo'])
    → evenMoreInfo = {...} → recurse

6️⃣ collectStrings(obj['data']['val']['thing']['moreInfo']['evenMoreInfo'])
    → weMadeIt = 'baz' → add ['baz']

Return Flow:
 → combine ['foo'] + ['bar'] + ['baz'] → ✅ ['foo', 'bar', 'baz']
"""

# ============================================================
# 🎨 5. Visualization (Call Stack)
# ============================================================
"""
collectStrings(obj)
  ↓
collectStrings(obj['data'])
  ↓
collectStrings(obj['data']['val'])
  ↓
collectStrings(obj['data']['val']['thing'])
  ↓
collectStrings(obj['data']['val']['thing']['moreInfo'])
  ↓
collectStrings(obj['data']['val']['thing']['moreInfo']['evenMoreInfo'])
  ↓
returns ['baz']
  ↓
returns ['bar', 'baz']
  ↓
returns ['foo', 'bar', 'baz']
"""

# ============================================================
# ⚙️ 6. Optional Safe Version (with Validation)
# ============================================================
def safe_collectStrings(obj):
    """Safer version with input type validation."""
    assert isinstance(obj, dict), "Input must be a dictionary."
    result = []
    for key, value in obj.items():
        if isinstance(value, str):
            result.append(value)
        elif isinstance(value, dict):
            result += safe_collectStrings(value)
    return result


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let n = total number of keys across all nested dictionaries.

⏱ Time Complexity: O(n)
 - Each key/value pair is visited once.

🧮 Space Complexity: O(d)
 - d = depth of recursion (maximum nesting level).
 - Plus O(k) for storing the result list of strings.
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Returning inside the for loop
   → causes premature return after first key.
✅ Always return after the loop finishes.

❌ Forgetting to merge recursive results
   → only last branch is collected.
✅ Use '+=' or 'extend()' to merge lists.

❌ Mutating input
   → recursion should not modify original dictionary.
✅ Always collect into a new list.
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Modify function to collect only values starting with a specific letter.
2️⃣ Write `collectNumbers()` that returns all numeric values instead of strings.
3️⃣ Combine this logic with `nestedEvenSum()` to collect both even and string values.
4️⃣ Modify to return both keys and string values as tuples.
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What happens if a key’s value is a list?
Q2: Why is the assert statement useful?
Q3: What is the time complexity?
Q4: What is the base case here?

✅ Answers:
A1: Lists are ignored (only dicts and strings are processed).
A2: Ensures input is valid (dictionary only).
A3: O(n)
A4: When no nested dictionaries remain.
"""

# ============================================================
# ✅ End of note.py — collectStrings (Recursion)
# ============================================================
"""
Summary:
 - Traverses nested dictionaries recursively.
 - Collects and returns all string values.
 - Base Case → no nested dicts left.
 - Recursive Case → call function on sub-dictionaries.
 - Time: O(n), Space: O(d)
"""
