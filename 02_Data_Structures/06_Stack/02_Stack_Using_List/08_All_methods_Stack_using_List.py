# stack_notes_list.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Implementation of Stack using Python List
# ✅ Covers ALL Operations: push, pop, peek, is_empty, size, clear, __str__
# ------------------------------------------------------

# ❓ QUESTION:
# How to implement a complete stack in Python using built-in list?

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

        ⏱️ Time Complexity: O(1) (amortized append at end)
        💾 Space Complexity: O(1)
        """
        return self.items.append(element)

    # -----------------------------------------------------------
    # 4️⃣ pop() → Remove and return the top element
    # -----------------------------------------------------------
    def pop(self):
        """
        Purpose:
        Remove the last inserted element (top of stack).
        If empty → return message instead of error.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if self.is_empty():
            return "Stack is Empty"
        return self.items.pop()

    # -----------------------------------------------------------
    # 5️⃣ peek() → Return the top element without removing it
    # -----------------------------------------------------------
    def peek(self):
        """
        Purpose:
        Return the element at the top of the stack without removing it.
        If empty → return message instead of error.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if self.is_empty():
            return "Stack is Empty"
        return self.items[-1]

    # -----------------------------------------------------------
    # 6️⃣ size() → Return number of elements in stack
    # -----------------------------------------------------------
    def size(self):
        """
        Purpose:
        Return number of elements currently in stack.

        ⏱️ Time Complexity: O(1) (Python stores list length)
        💾 Space Complexity: O(1)
        """
        return len(self.items)

    # -----------------------------------------------------------
    # 7️⃣ clear() → Remove all elements from stack
    # -----------------------------------------------------------
    def clear(self):
        """
        Purpose:
        Remove all elements, making stack empty.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        self.items = []


# ---------------------------------------------------------------
# ✅ Usage Example & Dry Run
# ---------------------------------------------------------------
if __name__ == "__main__":
    my_stack = Stack()

    print("Is stack empty?", my_stack.is_empty())  # True

    # Push elements
    my_stack.push(10)   # [10]
    my_stack.push(20)   # [10, 20]
    my_stack.push(30)   # [10, 20, 30]

    print("\nVisualized stack:")
    print(my_stack)  # prints vertical format

    # Peek
    print("\nPeek top element:", my_stack.peek())  # 30

    # Size
    print("Stack size:", my_stack.size())  # 3

    # Pop
    print("\nPopped element:", my_stack.pop())  # removes 30
    print("Stack after pop:\n", my_stack)

    # Clear
    my_stack.clear()
    print("\nAfter clear():")
    print(my_stack)       # "Stack is Empty"
    print("Stack size:", my_stack.size())  # 0


# ---------------------------------------------------------------
# 📊 Visualization of All Operations
# ---------------------------------------------------------------
# Initial: []
# is_empty() → True
#
# push(10): [10]
# push(20): [10, 20]
# push(30): [10, 20, 30]
#
# __str__ prints:
#   30  ← top
#   20
#   10
#
# peek() → 30 (stack unchanged)
# size() → 3
#
# pop() → removes 30
# Stack after pop:
#   20  ← top
#   10
#
# clear() → []
# "Stack is Empty"
# size() → 0
# ---------------------------------------------------------------


"""
📘 STACK (Python List Implementation) → ALL OPERATIONS

🔹 push(element):
- Insert at top (end of list).
- ⏱️ O(1), 💾 O(1)

🔹 pop():
- Remove & return top element.
- ⏱️ O(1), 💾 O(1)

🔹 peek():
- Return top element without removing.
- ⏱️ O(1), 💾 O(1)

🔹 is_empty():
- Check if stack empty.
- ⏱️ O(1), 💾 O(1)

🔹 size():
- Return number of elements.
- ⏱️ O(1), 💾 O(1)

🔹 clear():
- Remove all elements.
- ⏱️ O(1), 💾 O(1)

🔹 __str__():
- Pretty vertical stack view.
- ⏱️ O(n), 💾 O(n)

---------------------------------------------------------
✅ SUMMARY:
- Python list makes stack implementation simple.
- All core ops → O(1).
- __str__ useful for visualization/debugging.
- This file = full stack reference using list.
"""
