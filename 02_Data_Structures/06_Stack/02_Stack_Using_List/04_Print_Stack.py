# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Implementation of Stack using Python List
# ✅ Operations: push(), is_empty(), __str__()
# ------------------------------------------------------

# ❓ QUESTION:
# How to implement push and is_empty, and also display the stack
# in a more natural vertical format using __str__?

# ---------------------------------------------------------------
# 🔷 Stack Structure
# ---------------------------------------------------------------
class Stack:
    def __init__(self):
        # Internal list to store stack elements
        self.items = []

    # -----------------------------------------------------------
    # 1️⃣ is_empty() → Check if stack has no elements
    # -----------------------------------------------------------
    def is_empty(self):
        """
        Purpose:
        Check if the stack is empty.

        Returns:
        True if stack has no elements, False otherwise.

        ⏱️ Time Complexity: O(1)
        """
        return len(self.items) == 0

    # -----------------------------------------------------------
    # 2️⃣ __str__() → Custom string representation
    # -----------------------------------------------------------
    def __str__(self):
        """
        Purpose:
        Print stack in a vertical format with the top element shown first.

        Steps:
        - If empty → return "Stack is Empty"
        - Else:
            * Reverse the internal list (so top appears first).
            * Convert all items to string.
            * Join them line by line for vertical display.

        Example:
        stack: [1,2,3]
        Output:
            3   ← top
            2
            1
        """
        if self.is_empty():
            return "Stack is Empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    # -----------------------------------------------------------
    # 3️⃣ push(element) → Insert element at the top of stack
    # -----------------------------------------------------------
    def push(self, element):
        """
        Purpose:
        Add a new element to the top of the stack.

        ⏱️ Time Complexity: O(1)
        """
        self.items.append(element)


# ---------------------------------------------------------------
# ✅ Usage Example & Dry Run
# ---------------------------------------------------------------
if __name__ == "__main__":
    my_stack = Stack()

    # Initially empty
    print("Is stack empty?", my_stack.is_empty())  # True

    # Push elements
    my_stack.push(1)   # stack: [1]
    my_stack.push(2)   # stack: [1, 2]
    my_stack.push(3)   # stack: [1, 2, 3]

    print("Internal list:", my_stack.items)   # [1, 2, 3]

    # Using __str__ → prints in vertical stack format
    print("Visualized stack:\n",my_stack)


# ---------------------------------------------------------------
# 📊 Visualization
# ---------------------------------------------------------------
# Internal list: [1, 2, 3]
#
# __str__ Output:
#   3   ← top
#   2
#   1
#
# If empty:
#   "Stack is Empty"
# ---------------------------------------------------------------


"""
📘 STACK OPERATIONS → push(), is_empty(), __str__()

🔹 push():
- Insert element at top (end of list).
- Uses list.append() → O(1).

🔹 is_empty():
- Returns True if no elements, else False.
- Uses len() → O(1).

🔹 __str__():
- Provides a nice vertical view of the stack.
- Top element is shown first.
- If empty → "Stack is Empty".

---------------------------------------------------------
🔹 Dry Run:
Initial: []
is_empty() → True

push(1): [1]
push(2): [1, 2]
push(3): [1, 2, 3]

Internal list: [1, 2, 3]
Printed stack:
3   ← top
2
1

---------------------------------------------------------
✅ SUMMARY:
- __str__ improves readability.
- Shows stack as it actually looks (top-down).
- Great for debugging & visualization.
"""
