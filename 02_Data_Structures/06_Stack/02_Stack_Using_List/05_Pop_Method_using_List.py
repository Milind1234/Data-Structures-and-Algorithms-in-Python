# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Implementation of Stack using Python List
# ✅ Operations: push(), pop(), is_empty(), __str__()
# ------------------------------------------------------

# ❓ QUESTION:
# How to implement push and pop operations in a stack?
# Use Python's built-in list as internal storage.

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
        """Return True if stack is empty, else False (O(1))."""
        return len(self.items) == 0

    # -----------------------------------------------------------
    # 2️⃣ __str__() → Custom string representation
    # -----------------------------------------------------------
    def __str__(self):
        """
        Print stack in vertical format with the top element first.
        If empty → return "Stack is Empty".
        """
        if self.is_empty():
            return "Stack is Empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    # -----------------------------------------------------------
    # 3️⃣ push(element) → Insert element at the top of stack
    # -----------------------------------------------------------
    def push(self, element):
        """Add element at the top of stack (end of list). O(1)."""
        return self.items.append(element)

    # -----------------------------------------------------------
    # 4️⃣ pop() → Remove and return the top element
    # -----------------------------------------------------------
    def pop(self):
        """
        Remove the last inserted element (top of stack).
        If empty → return message instead of error.
        ⏱️ O(1)
        """
        if self.is_empty():
            return "Stack is Empty"
        return self.items.pop()


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

    # Pop last element
    print("\nLast popped item:", my_stack.pop())  # → 3

    # Show stack after pop
    print("Visualized stack after pop:")
    print(my_stack)


# ---------------------------------------------------------------
# 📊 Visualization
# ---------------------------------------------------------------
# Initial:
#   []
#   is_empty() → True
#
# push(1): [1]
# push(2): [1, 2]
# push(3): [1, 2, 3]
#
# __str__ prints:
#   3  ← top
#   2
#   1
#
# pop() → removes 3
#
# Stack after pop:
#   2  ← top
#   1
# ---------------------------------------------------------------


"""
📘 STACK OPERATIONS → push(), pop(), is_empty(), __str__()

🔹 push():
- Insert element at top (end of list).
- Uses list.append() → O(1).

🔹 pop():
- Removes and returns top element (end of list).
- Uses list.pop() → O(1).
- If stack empty → handle gracefully.

🔹 is_empty():
- Returns True if no elements.
- O(1) using len().

🔹 __str__():
- Pretty vertical display.
- Top element printed first.
- If empty → "Stack is Empty".

---------------------------------------------------------
🔹 Dry Run:
Initial: []
push(1) → [1]
push(2) → [1, 2]
push(3) → [1, 2, 3]
__str__ → 
    3
    2
    1
pop() → 3
Stack after pop:
    2
    1

---------------------------------------------------------
✅ SUMMARY:
- Stack with push/pop is now functional.
- Both operations are O(1).
- __str__ helps visualize stack top-down.
"""
