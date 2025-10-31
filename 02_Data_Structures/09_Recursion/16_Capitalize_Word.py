# ------------------------------------------------------------
# 📘 note.py — Recursion: capitalizeWords (Array of Strings)
# ------------------------------------------------------------
"""
Purpose:
 - Learn how to use recursion to modify strings inside a list.
 - Understand how recursion can process one element at a time
   and combine results to form a new list.
 - Build on concepts learned in 'capitalizeFirst', but now
   capitalize the entire word instead of just the first letter.

Problem Definition:
 Write a recursive function called `capitalizeWords`.
 Given an array of words, return a new array containing
 each word fully capitalized.

Example:
 Input  → ['i', 'am', 'learning', 'recursion']
 Output → ['I', 'AM', 'LEARNING', 'RECURSION']
"""

# ============================================================
# 🔁 1. Step-by-step recursion logic
# ============================================================
"""
We follow the standard 3-step recursion approach:

Step 1️⃣ — Recursive Case:
  - Convert the first element to uppercase using `.upper()`.
  - Recurse on the remaining array (arr[1:]).
  - Combine current result + recursive result.

Step 2️⃣ — Base Case:
  - If array is empty → return an empty list.

Step 3️⃣ — Unintentional Cases:
  - Input should be a list of strings.
  - Ignore or raise an error for non-string inputs.
"""

# ============================================================
# ✅ 2. Your Code (kept exactly same)
# ============================================================

def capitalizeWords(arr):
    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + capitalizeWords(arr[1:])


# ============================================================
# 🧪 3. Example Runs
# ============================================================
if __name__ == "__main__":
    print("✅ Recursive Example: capitalizeWords()\n")

    words1 = ['i', 'am', 'learning', 'recursion']
    words2 = ['python', 'rocks']
    words3 = ['data', 'structures', 'and', 'algorithms']
    words4 = []
    words5 = ['hello']

    print(f"{words1}             →     {capitalizeWords(words1)}")
    print(f"{words2}                              →     {capitalizeWords(words2)}")
    print(f"{words3}      →     {capitalizeWords(words3)}")
    print(f"{words4}                                               →     {capitalizeWords(words4)}")
    print(f"{words5}                                        →     {capitalizeWords(words5)}")


# ============================================================
# 🧭 4. How recursion works (Example: ['i','am','learning','recursion'])
# ============================================================
"""
Call 1:
 capitalizeWords(['i','am','learning','recursion'])
 → result = ['I']
 → recursive call with ['am','learning','recursion']

Call 2:
 capitalizeWords(['am','learning','recursion'])
 → result = ['AM']
 → recursive call with ['learning','recursion']

Call 3:
 capitalizeWords(['learning','recursion'])
 → result = ['LEARNING']
 → recursive call with ['recursion']

Call 4:
 capitalizeWords(['recursion'])
 → result = ['RECURSION']
 → recursive call with []

Call 5:
 capitalizeWords([]) → returns []

Backtracking:
 [] → ['RECURSION'] → ['LEARNING', 'RECURSION']
 → ['AM', 'LEARNING', 'RECURSION']
 → ['I', 'AM', 'LEARNING', 'RECURSION']
✅ Final Output: ['I', 'AM', 'LEARNING', 'RECURSION']
"""

# ============================================================
# 🎨 5. Visualization (Call Stack)
# ============================================================
"""
capitalizeWords(['i','am','learning','recursion'])
        ↓
capitalizeWords(['am','learning','recursion'])
        ↓
capitalizeWords(['learning','recursion'])
        ↓
capitalizeWords(['recursion'])
        ↓
capitalizeWords([]) → []

Return flow:
 [] → ['RECURSION'] → ['LEARNING', 'RECURSION']
 → ['AM', 'LEARNING', 'RECURSION']
 → ['I', 'AM', 'LEARNING', 'RECURSION']
"""

# ============================================================
# ⚙️ 6. Optional Safe Version (Input Validation)
# ============================================================
def safe_capitalizeWords(arr):
    """Version with input validation."""
    assert isinstance(arr, list), "Input must be a list."
    for word in arr:
        assert isinstance(word, str), "All elements must be strings."

    result = []
    if len(arr) == 0:
        return result
    result.append(arr[0].upper())
    return result + safe_capitalizeWords(arr[1:])


# ============================================================
# 📈 7. Complexity Analysis
# ============================================================
"""
Let n = number of words
Let k = average length of each word

⏱ Time Complexity: O(n * k)
 - Each recursive call processes one string (O(k)) and recurses on remaining n-1.

🧮 Space Complexity: O(n)
 - Recursion stack depth proportional to array size.
"""

# ============================================================
# ⚠️ 8. Common Mistakes & Fixes
# ============================================================
"""
❌ Forgetting base case:
   → Causes infinite recursion.

❌ Not combining recursive results properly:
   → Must use 'return result + capitalizeWords(arr[1:])'.

❌ Using append() incorrectly:
   → append() returns None, so you must concatenate lists explicitly.

✅ Fix: Use `result + recursive_call` to combine properly.
"""

# ============================================================
# 🧩 9. Practice Exercises
# ============================================================
"""
1️⃣ Write a recursive function `capitalizeFirst()`:
     Input: ['apple','banana'] → Output: ['Apple','Banana']

2️⃣ Write a recursive function `reverseWords()`:
     Input: ['one','two'] → Output: ['eno','owt']

3️⃣ Combine `capitalizeWords()` and `reverseWords()` into one
     function that both capitalizes and reverses words.

4️⃣ Write an iterative version (using a loop) and compare.

5️⃣ Add validation that filters out empty strings automatically.
"""

# ============================================================
# ❓ 10. Mini Quiz (answers below)
# ============================================================
"""
Q1: What is the base case for capitalizeWords()?
Q2: What happens if input list is empty?
Q3: What does capitalizeWords(['a','b']) return?
Q4: What is the time complexity?

✅ Answers:
A1: When len(arr) == 0 → return []
A2: Returns []
A3: ['A', 'B']
A4: O(n * k)
"""

# ============================================================
# ✅ End of note.py — capitalizeWords (Recursion)
# ============================================================
"""
Summary:
 - Base Case: empty list → []
 - Recursive Case: capitalize first element + recurse on rest.
 - Time: O(n * k), Space: O(n)
 - Another elegant example of recursion with strings and arrays.

Next:
 → Try **reverseWords()** or **capitalizeSentences()**
    to practice recursion with string transformations.
"""
