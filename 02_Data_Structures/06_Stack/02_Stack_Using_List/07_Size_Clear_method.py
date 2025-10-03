# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Implementation of Stack using Python List
# ✅ Operations: push(), size(), clear(), is_empty(), __str__()
# ------------------------------------------------------

# ❓ QUESTION:
# How to implement size() and clear() operations in a stack?
# Use Python's built-in list to store elements.

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
        return len(self.items) == 0

    # -----------------------------------------------------------
    # 2️⃣ __str__() → Custom string representation
    # -----------------------------------------------------------
    def __str__(self):
        if self.is_empty():
            return "Stack is Empty"
        values = [str(x) for x in reversed(self.items)]
        return '\n'.join(values)

    # -----------------------------------------------------------
    # 3️⃣ push(element) → Insert element at the top of stack
    # -----------------------------------------------------------
    def push(self, element):
        return self.items.append(element)

    # -----------------------------------------------------------
    # 4️⃣ size() → Return number of elements in stack
    # -----------------------------------------------------------
    def size(self):
        """
        Purpose:
        Return number of elements currently in stack.

        ⏱️ Time Complexity: O(1) → Python stores length metadata
        💾 Space Complexity: O(1)
        """
        return len(self.items)

    # -----------------------------------------------------------
    # 5️⃣ clear() → Remove all elements from stack
    # -----------------------------------------------------------
    def clear(self):
        """
        Purpose:
        Remove all elements, making stack empty.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1) (dereferences all items at once)
        """
        self.items = []


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

    # Stack size
    print("\nStack Size:", my_stack.size())  # 3

    # Clear stack
    my_stack.clear()
    print("\nAfter clear():")
    print(my_stack)           # "Stack is Empty"
    print("Stack Size:", my_stack.size())  # 0


# ---------------------------------------------------------------
# 📊 Visualization
# ---------------------------------------------------------------
# Initial:
#   []
#   size() → 0
#
# push(1): [1]
# push(2): [1, 2]
# push(3): [1, 2, 3]
#   size() → 3
#
# __str__ prints:
#   3  ← top
#   2
#   1
#
# clear():
#   []
#   "Stack is Empty"
#   size() → 0
# ---------------------------------------------------------------


"""
📘 STACK OPERATIONS → size(), clear(), push(), is_empty(), __str__()

🔹 size():
- Returns number of elements in stack.
- ⏱️ O(1), 💾 O(1).

🔹 clear():
- Removes all elements (empties stack).
- ⏱️ O(1), 💾 O(1).

🔹 push():
- Inserts element at top.
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
size() → 3
clear() → []
size() → 0

---------------------------------------------------------
✅ SUMMARY:
- size() and clear() complete the core stack operations.
- Together with push(), pop(), peek(), and is_empty(),
  we have a fully functional stack.
"""
