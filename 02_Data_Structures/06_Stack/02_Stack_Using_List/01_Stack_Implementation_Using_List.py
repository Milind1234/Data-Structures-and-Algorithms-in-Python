"""
📘 STACK IMPLEMENTATION USING PYTHON LIST

In Python, a stack can be implemented using a **list**.  
But we must be careful which **end of the list** we treat as the "top of the stack".

---------------------------------------------------------
🔹 Which End to Use? (Beginning vs End of List)
---------------------------------------------------------
- If we insert/remove elements at the **beginning** of a list:
  - All other elements must shift right/left.
  - ❌ Time complexity → O(n) for each push/pop.

- If we insert/remove elements at the **end** of a list:
  - No shifting needed (Python internally optimizes this).
  - ✅ Time complexity → O(1) for push/pop.

👉 Therefore, when implementing a stack in Python,  
   we always use the **end of the list as the Top of Stack**.

---------------------------------------------------------
🔹 Visualization (Using End of List as Top)
---------------------------------------------------------
Initial empty list (stack):
    [   ]   ← top not defined yet

push(10):
    [ 10 ]  ← top

push(20):
    [ 10, 20 ]
           ↑ top

push(30):
    [ 10, 20, 30 ]
                 ↑ top

pop():
    [ 10, 20 ]  ← top now at 20

---------------------------------------------------------
🔹 Implementation (Custom Stack Class)
---------------------------------------------------------
We create a class `Stack`:
- Constructor `__init__()` → initializes an empty list `items`.
- We treat the **end of the list** as the **top of stack**.

"""

# Stack implementation using Python list
class Stack:
    def __init__(self):
        """Initialize an empty stack using Python list."""
        self.items = []   # empty list, top = end of list

# ---------------------------------------------------------
# Usage Example
# ---------------------------------------------------------
my_stack = Stack()

# Initially empty
print("Stack Items:", my_stack.items)      # []
print("Stack Size:", len(my_stack.items))  # 0

"""
---------------------------------------------------------
🔹 Why len() is O(1) in Python?
---------------------------------------------------------
- Python internally maintains the size of list/set/dict/tuple in metadata.
- Calling len() does NOT count elements, it simply returns stored size.
- ✅ Time complexity of len() → O(1).

---------------------------------------------------------
🔹 Complexity of Stack Creation
---------------------------------------------------------
- Time Complexity → O(1) (creating an empty list).
- Space Complexity → O(1) (no data stored yet).

---------------------------------------------------------
✅ SUMMARY
---------------------------------------------------------
- Use Python list’s **end** as top of stack.
- push → list.append(x) → O(1)
- pop → list.pop() → O(1)
- peek → list[-1] → O(1)
- isEmpty → len(list) == 0 → O(1)
- size → len(list) → O(1)
"""
