# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Implementation of Stack using Python List
# ✅ Operations: push(), peek(), is_empty(), __str__()
# ------------------------------------------------------

# ❓ QUESTION:
# How to implement peek operation in a stack?
# Peek = return the top element without removing it.

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
        Return True if stack is empty, else False.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        return len(self.items) == 0

    # -----------------------------------------------------------
    # 2️⃣ __str__() → Custom string representation
    # -----------------------------------------------------------
    def __str__(self):
        """
        Purpose:
        Print stack in vertical format with the top element first.
        If empty → return "Stack is Empty".

        ⏱️ Time Complexity: O(n) → reversing + joining
        💾 Space Complexity: O(n) → temporary strings
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

        ⏱️ Time Complexity: O(1) (append at end)
        💾 Space Complexity: O(1) extra
        """
        return self.items.append(element)

    # -----------------------------------------------------------
    # 4️⃣ peek() → Return the top element without removing it
    # -----------------------------------------------------------
    def peek(self):
        """
        Purpose:
        Return the element at the top of the stack without removing it.
        If empty → return "Stack is Empty".

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if self.is_empty():
            return "Stack is empty"
        return self.items[-1]


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

    # Show vertical stack
    print("\nVisualized stack:")
    print(my_stack)  # prints top first

    # Peek at last element
    print("\nLast appended element is:", my_stack.peek())  # 3


# ---------------------------------------------------------------
# 📊 Visualization
# ---------------------------------------------------------------
# Internal list: [1, 2, 3]
#
# __str__ Output:
#   3  ← top
#   2
#   1
#
# peek() → 3 (stack unchanged)
# ---------------------------------------------------------------


"""
📘 STACK OPERATIONS → push(), peek(), is_empty(), __str__()

🔹 push():
- Insert element at top (end of list).
- ⏱️ O(1), 💾 O(1).

🔹 peek():
- Returns top element without removing it.
- If stack empty → raises IndexError (Python default).
- ⏱️ O(1), 💾 O(1).

🔹 is_empty():
- Checks if stack has elements.
- ⏱️ O(1), 💾 O(1).

🔹 __str__():
- Displays stack vertically (top element first).
- ⏱️ O(n), 💾 O(n).

---------------------------------------------------------
🔹 Dry Run:
Initial: []
push(1): [1]
push(2): [1, 2]
push(3): [1, 2, 3]

Stack printed:
    3
    2
    1

peek() → 3
(stack unchanged)
---------------------------------------------------------

✅ SUMMARY:
- peek() is useful when you only want to check the top.
- push(), peek(), is_empty() all run in O(1).
- __str__ helps visualize stack state clearly.
"""
