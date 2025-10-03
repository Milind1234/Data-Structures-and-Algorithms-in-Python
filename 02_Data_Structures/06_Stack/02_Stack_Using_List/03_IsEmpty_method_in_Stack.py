# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Implementation of Stack using Python List
# ✅ Operations: push(), is_empty()
# ------------------------------------------------------

# ❓ QUESTION:
# How to check if a stack is empty and implement push?
# Implement these operations using Python's built-in list.

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

        Steps:
        - Use len(self.items).
        - If length == 0 → True (stack is empty).
        - Else → False.

        ⏱️ Time Complexity: O(1) 
        💾 Space Complexity: O(1)
        """
        return len(self.items) == 0

    # -----------------------------------------------------------
    # 2️⃣ push(element) → Insert element at the top of stack
    # -----------------------------------------------------------
    def push(self, element):
        self.items.append(element)

    # (Optional) pretty print
    def __str__(self):
        return str(self.items)


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
    my_stack.push(4)   # stack: [1, 2, 3, 4]

    print("After pushing elements:", my_stack.items)
    print("Is stack empty?", my_stack.is_empty())  # False


# ---------------------------------------------------------------
# 📊 Visualization
# ---------------------------------------------------------------

# Initial:
#   []
#   is_empty() → True

# After push(1):
#   [1]
#   is_empty() → False

# push(2) → [1, 2]
# push(3) → [1, 2, 3]
# push(4) → [1, 2, 3, 4]

# Top of stack = rightmost element
# ---------------------------------------------------------------


"""
📘 STACK OPERATIONS → is_empty() + push()

🔹 is_empty():
- Checks if stack has no elements.
- Returns True if empty, else False.

🔹 push():
- Inserts element at the top (end of list).
- Uses list.append() → O(1).

---------------------------------------------------------
🔹 Dry Run:
Initial: []
is_empty() → True

push(1): [1]
push(2): [1, 2]
push(3): [1, 2, 3]
push(4): [1, 2, 3, 4]
is_empty() → False

---------------------------------------------------------
🔹 Complexity:
- is_empty() → O(1)
- push() → O(1)

✅ SUMMARY:
- is_empty() quickly checks stack state.
- push() appends at top efficiently.
- Together → help manage stack operations.
"""
