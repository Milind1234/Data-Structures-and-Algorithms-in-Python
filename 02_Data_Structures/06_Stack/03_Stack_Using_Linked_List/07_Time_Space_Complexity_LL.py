# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Time and Space Complexity of Stack (Using Linked List)
# ------------------------------------------------------

"""
📌 Problem: Time and Space Complexity of Stack (Linked List Implementation)

This file summarizes the **time complexity** and **space complexity**
for all common operations on a stack implemented using a **Linked List**.

✅ Stack uses the **top (head node)** for all operations.
✅ Insertions and deletions happen at the head for O(1) performance.
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
Stack (Linked List Implementation) → follows **LIFO (Last In, First Out)**.
Each element (Node) contains:
    - value
    - reference to next node

Top pointer → points to the most recently added node (top of stack).

Key Concept:
- Push and Pop at the head for O(1) operations.
- Traversal or visualization (__str__) → O(n).
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
   - Initialize top = None, length = 0.
   - Time = O(1), Space = O(1).

2. Push
   - Create new node, link it to top, move top → new node.
   - Time = O(1), Space = O(1).

3. Pop
   - Move top → top.next, unlink old top.
   - Time = O(1), Space = O(1).

4. Peek
   - Return top.value (no removal).
   - Time = O(1), Space = O(1).

5. isEmpty
   - Check if top == None (or length == 0).
   - Time = O(1), Space = O(1).

6. Size
   - Return stored length attribute.
   - Time = O(1), Space = O(1).

7. Clear
   - Set top = None, length = 0.
   - Python’s GC will remove unreferenced nodes.
   - Time = O(1), Space = O(1).

8. __str__
   - Traverse nodes from top to bottom to print.
   - Time = O(n), Space = O(n).
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example for Operations
# ---------------------------------------------------------------
"""
Linked List Representation (top → next → next):

Step 1: Create Empty Stack
    top = None
    length = 0

Step 2: Push(10)
    top → [10 → None]
    length = 1
    Time = O(1)

Step 3: Push(20)
    top → [20 → 10 → None]
    length = 2
    Time = O(1)

Step 4: Push(30)
    top → [30 → 20 → 10 → None]
    length = 3
    Time = O(1)

Step 5: Peek()
    top.value = 30
    (stack unchanged)
    Time = O(1)

Step 6: Pop()
    Remove 30, top → 20
    New Stack: [20 → 10 → None]
    Time = O(1)

Step 7: Size()
    length = 2
    Time = O(1)

Step 8: Clear()
    top = None
    length = 0
    Time = O(1)
"""

# ---------------------------------------------------------------
# 📊 Summary Table (as Python dict)
# ---------------------------------------------------------------
stack_ll_complexities = {
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
    print("Time and Space Complexity of Stack (Linked List) Operations:\n")
    pprint(stack_ll_complexities)
