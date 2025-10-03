# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Time and Space Complexity of Stack (Using Python List)
# ------------------------------------------------------

"""
📌 Problem: Time and Space Complexity of Stack (Python List)

This file summarizes the **time complexity** and **space complexity**
for the most common operations on a stack implemented using a Python list.

✅ Stack uses the **end of the list as the Top**.
✅ Python’s list.append() and list.pop() are O(1) on average.
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
Stack → Linear data structure that follows **LIFO (Last In, First Out)**.
- Insert (push) and remove (pop) only at one end (top of stack).
- Python’s list is used for internal storage.

Operations:
- O(1) if they involve append/pop from the end.
- O(n) only for visualization (__str__) or traversal.
"""

# ---------------------------------------------------------------
# 📝 Time & Space Complexities
# ---------------------------------------------------------------
"""
Operation           Time Complexity        Space Complexity
-----------------------------------------------------------
Create              O(1)                   O(1)
Push                O(1)                   O(1)
Pop                 O(1)                   O(1)
Peek                O(1)                   O(1)
isEmpty             O(1)                   O(1)
Size                O(1)                   O(1)
Clear               O(1)                   O(1)
__str__ (print)     O(n)                   O(n)
"""

# ---------------------------------------------------------------
# ✅ Explanation of Each Operation
# ---------------------------------------------------------------
"""
1. Create
   - Initialize empty list.
   - Time = O(1), Space = O(1).

2. Push
   - Append element at end (list.append()).
   - Time = O(1), Space = O(1).

3. Pop
   - Remove last element (list.pop()).
   - Time = O(1), Space = O(1).

4. Peek
   - Return last element without removing.
   - Time = O(1), Space = O(1).

5. isEmpty
   - Check if length == 0.
   - Time = O(1), Space = O(1).

6. Size
   - Return len(list).
   - Time = O(1), Space = O(1).

7. Clear
   - Reset list to [].
   - Time = O(1), Space = O(1).

8. __str__
   - Reverse list and join for display.
   - Time = O(n), Space = O(n).
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example for Operations
# ---------------------------------------------------------------
"""
Stack (using list): []

1. Push(10):
   [10] (top = 10)
   Time = O(1)

2. Push(20):
   [10, 20] (top = 20)
   Time = O(1)

3. Push(30):
   [10, 20, 30] (top = 30)
   Time = O(1)

4. Peek():
   Returns 30 (stack unchanged)
   Time = O(1)

5. Pop():
   Removes 30
   Result: [10, 20]
   Time = O(1)

6. Size():
   Returns 2
   Time = O(1)

7. Clear():
   []
   Time = O(1)
"""

# ---------------------------------------------------------------
# 📊 Summary Table (as Python dict)
# ---------------------------------------------------------------
stack_complexities = {
    "Create":    {"time": "O(1)", "space": "O(1)"},
    "Push":      {"time": "O(1)", "space": "O(1)"},
    "Pop":       {"time": "O(1)", "space": "O(1)"},
    "Peek":      {"time": "O(1)", "space": "O(1)"},
    "isEmpty":   {"time": "O(1)", "space": "O(1)"},
    "Size":      {"time": "O(1)", "space": "O(1)"},
    "Clear":     {"time": "O(1)", "space": "O(1)"},
    "__str__":   {"time": "O(n)", "space": "O(n)"}
}

if __name__ == "__main__":
    from pprint import pprint
    print("Time and Space Complexity of Stack (Python List) Operations:\n")
    pprint(stack_complexities)
