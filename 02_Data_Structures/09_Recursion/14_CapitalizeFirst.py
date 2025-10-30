# ------------------------------------------------------------
# 📘 note.py — Recursion: Capitalize First Letter of Words
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to use recursion to modify each string element in an array.
 - Specifically: capitalize the first letter of every word in a list.
 - Understand how to combine recursion with string slicing and concatenation.

Problem Definition:
 Given a list of lowercase words, return a new list with the
 first letter of each word capitalized.

Example:
 Input  → ['apple', 'banana', 'cherry']
 Output → ['Apple', 'Banana', 'Cherry']
"""

# ============================================================
# 🔁 1. Step-by-step recursion logic
# ============================================================
"""
We follow the standard 3-step recursion process:

Step 1️⃣ — Recursive Case:
  - Capitalize the first word in the array (arr[0]).
  - Recurse on the remaining array (arr[1:]).
  - Combine both using list concatenation.

Step 2️⃣ — Base Case:
  - If the array is empty → return an empty list.

Step 3️⃣ — Unintentional Cases:
  - Ensure arr is a list of strings.
  - Each string should have at least one character (non-empty words).
"""

# ============================================================
# ✅ 2. Your code (kept exactly same)
# ============================================================

def capitalizeFirst(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + capitalizeFirst(arr[1:])


# ============================================================
# 🧪 3. Example Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Recursive Example: capitalizeFirst()\n")

    words1 = ['apple', 'banana', 'cherry']
    words2 = ['dog', 'cat', 'elephant']
    words3 = ['python', 'recursion', 'rocks']
    words4 = []
    words5 = ['a', 'b', 'c']

    print(f"{words1}             →         {capitalizeFirst(words1)}")
    print(f"{words2}                →         {capitalizeFirst(words2)}")
    print(f"{words3}          →         {capitalizeFirst(words3)}")
    print(f"{words4}                                        →         {capitalizeFirst(words4)}")
    print(f"{words5}                           →         {capitalizeFirst(words5)}")
 

# ============================================================
# 🧭 4. How recursion works (Example: ['apple','banana','cherry'])
# ============================================================
"""
Call 1:
 capitalizeFirst(['apple','banana','cherry'])
 → result = ['Apple']
 → recursive call with ['banana','cherry']

Call 2:
 capitalizeFirst(['banana','cherry'])
 → result = ['Banana']
 → recursive call with ['cherry']

Call 3:
 capitalizeFirst(['cherry'])
 → result = ['Cherry']
 → recursive call with []

Call 4:
 capitalizeFirst([]) → returns []

Backtracking:
 ['Cherry'] returned → ['Banana'] + ['Cherry'] = ['Banana', 'Cherry']
 ['Apple'] + ['Banana', 'Cherry'] = ['Apple', 'Banana', 'Cherry']
✅ Final Output: ['Apple', 'Banana', 'Cherry']
"""

# ============================================================
# 🎨 5. Visualization (Call Stack)
# ============================================================
"""
capitalizeFirst(['apple','banana','cherry'])
        ↓
capitalizeFirst(['banana','cherry'])
        ↓
capitalizeFirst(['cherry'])
        ↓
capitalizeFirst([]) → []

Backtracking:
 [] → ['Cherry'] → ['Banana', 'Cherry'] → ['Apple', 'Banana', 'Cherry']
"""

# ============================================================
# ⚙️ 6. Optional Safe Version (Input Validation)
# ============================================================
def safe_capitalizeFirst(arr):
    """Version with type checking."""
    assert isinstance(arr, list), "Input must be a list."
    for word in arr:
        assert isinstance(word, str), "All elements must be strings."

    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0][0].upper() + arr[0][1:])
    return result + safe_capitalizeFirst(arr[1:])


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let n = number of strings in array
Let k = average length of each string

⏱ Time Complexity: O(n * k)
 - Each recursive call processes one word (O(k)) and recurses on n-1 elements.

🧮 Space Complexity: O(n)
 - Recursion stack depth proportional to the array length.
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Forgetting base case:
   → Causes infinite recursion (stack overflow).

❌ Using append() without combining with recursive result:
   → Only first word gets processed.

✅ Fix: Combine with recursive call → result + capitalizeFirst(arr[1:])

❌ Not handling empty array:
   → Should return [] (base case).
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Modify capitalizeFirst() to capitalize the *entire* word instead of just the first letter.

2️⃣ Write a recursive function `capitalizeWords()`:
     Input: ['hello', 'world'] → Output: ['HELLO', 'WORLD']

3️⃣ Write a recursive function `reverseWords()`:
     Input: ['apple', 'banana'] → Output: ['elppa', 'ananab']

4️⃣ Combine with user input: accept a list of words and return the capitalized list recursively.

5️⃣ Write an iterative version using a loop and compare performance.
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What is the base case for capitalizeFirst()?
Q2: What happens if the input list is empty?
Q3: What does capitalizeFirst(['a','b']) return?
Q4: What is the time complexity?

✅ Answers:
A1: When len(arr) == 0 → return []
A2: Returns []
A3: ['A', 'B']
A4: O(n * k)
"""

# ============================================================
# ✅ End of note.py — capitalizeFirst (Recursion)
# ============================================================
"""
Summary:
 - Base Case: empty list → []
 - Recursive Case: capitalize first element + recurse on rest.
 - Uses string slicing and recursion to process all words.
 - Time: O(n * k), Space: O(n)
 - Simple and elegant recursive problem to practice string and list handling.

Next:
 → Try **capitalizeWords()** to make every character uppercase recursively.
"""
