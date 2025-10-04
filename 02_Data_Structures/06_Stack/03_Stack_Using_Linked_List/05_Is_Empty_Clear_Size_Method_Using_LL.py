# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: is_empty(), size(), and clear() Methods
# ✅ Implementation: Linked List–based Stack
# ------------------------------------------------------

"""
📌 OVERVIEW:
In addition to the main stack operations (push, pop, peek),
there are several **utility methods** that help manage the stack.

In this section, we’ll implement:
1️⃣ `is_empty()` → Check if stack is empty  
2️⃣ `size()`     → Get number of elements  
3️⃣ `clear()`    → Remove all elements

All these methods are **O(1)** operations,
since they rely only on maintaining simple metadata (`top` and `length`).
"""

# ---------------------------------------------------------------
# 🧩 NODE CLASS
# ---------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------------------------------------------------------------
# 🧱 STACK CLASS (with utility methods)
# ---------------------------------------------------------------
class Stack:
    def __init__(self):
        """
        Create an empty stack.
        - top → None
        - length → 0

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        self.top = None
        self.length = 0

    # -----------------------------------------------------------
    # 1️⃣ PUSH METHOD (for setup)
    # -----------------------------------------------------------
    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    # -----------------------------------------------------------
    # 2️⃣ IS_EMPTY METHOD
    # -----------------------------------------------------------
    def is_empty(self):
        """
        Purpose:
        Check if stack is empty.

        Returns:
        - True  → if stack has 0 elements
        - False → otherwise

        Logic:
        If top pointer is None or length = 0 → stack is empty.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        return self.length == 0

    # -----------------------------------------------------------
    # 3️⃣ SIZE METHOD
    # -----------------------------------------------------------
    def size(self):
        """
        Purpose:
        Return number of elements in the stack.

        Returns:
        - self.length

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        return self.length

    # -----------------------------------------------------------
    # 4️⃣ CLEAR METHOD
    # -----------------------------------------------------------
    def clear(self):
        """
        Purpose:
        Remove all elements from the stack.

        Steps:
        1️⃣ Set top → None
        2️⃣ Reset length → 0

        Note:
        Python garbage collector automatically removes unreferenced nodes.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        self.top = None
        self.length = 0

    # -----------------------------------------------------------
    # 5️⃣ __str__() for visualization
    # -----------------------------------------------------------
    def __str__(self):
        if self.length == 0:
            return "Stack is Empty"
        values = []
        current = self.top
        while current:
            values.append(str(current.value))
            current = current.next
        return "\n".join(values)


# ---------------------------------------------------------------
# ✅ USAGE EXAMPLE & DRY RUN
# ---------------------------------------------------------------
if __name__ == "__main__":
    my_stack = Stack()

    print("Initially:")
    print("Is stack empty?", my_stack.is_empty())  # True
    print("Size:", my_stack.size())                # 0
    print(my_stack)

    # Push some elements
    my_stack.push(10)
    my_stack.push(20)
    my_stack.push(30)

    print("\nAfter pushing elements:")
    print(my_stack)
    print("Is stack empty?", my_stack.is_empty())  # False
    print("Size:", my_stack.size())                # 3

    # Clear the stack
    print("\nClearing the stack...")
    my_stack.clear()

    print("After clear:")
    print("Is stack empty?", my_stack.is_empty())  # True
    print("Size:", my_stack.size())                # 0
    print(my_stack)


# ---------------------------------------------------------------
# 📊 VISUALIZATION
# ---------------------------------------------------------------

# Initial Stack:
# top → None
# length = 0
# Output: "Stack is Empty"

# After pushing (10, 20, 30):
#   +----+
#   | 30 | ← top
#   +----+
#     ↓
#   +----+
#   | 20 |
#   +----+
#     ↓
#   +----+
#   | 10 |
#   +----+
#     ↓
#   None
#
# is_empty() → False
# size() → 3

# After clear():
# top → None
# length = 0
# Stack becomes empty again.
# ---------------------------------------------------------------


"""
📘 STACK (Linked List Implementation) — UTILITY METHODS SUMMARY

🔹 1️⃣ is_empty()
- Checks if stack has no elements.
- Returns True if top = None or length = 0.
- O(1) time, O(1) space.

🔹 2️⃣ size()
- Returns number of elements currently in stack.
- Simply returns `self.length`.
- O(1) time, O(1) space.

🔹 3️⃣ clear()
- Deletes all elements from stack.
- Sets top = None, length = 0.
- Stack reset in O(1) time.

---------------------------------------------------------
🔹 EXAMPLE:
Initial: []
push(10), push(20), push(30)
→ size() = 3
→ is_empty() = False
clear()
→ size() = 0
→ is_empty() = True

---------------------------------------------------------
🔹 COMPLEXITY SUMMARY:
Operation     Time Complexity     Space Complexity
-------------------------------------------------
is_empty()     O(1)                O(1)
size()         O(1)                O(1)
clear()        O(1)                O(1)

---------------------------------------------------------
✅ SUMMARY:
- All utility operations execute in constant time.
- These methods help manage and monitor stack state.
- No traversal or extra memory needed.
"""
