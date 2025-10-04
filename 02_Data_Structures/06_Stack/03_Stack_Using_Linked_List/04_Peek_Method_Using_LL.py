# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Peek Method in Stack (Linked List Implementation)
# ------------------------------------------------------

"""
📌 OVERVIEW:
In a **Linked List–based Stack**, the `peek()` method allows us to **see**
the top element of the stack *without removing it*.

Unlike `pop()`, which removes the top node,
`peek()` simply returns the top node (or its value).

---------------------------------------------------------
🔹 PURPOSE:
- Useful when we only need to check which element is currently at the top.
- Does not modify the stack.
"""

# ---------------------------------------------------------------
# 🧩 NODE CLASS
# ---------------------------------------------------------------
class Node:
    def __init__(self, value):
        """
        Each node stores:
        - value → data
        - next → pointer to next node
        """
        self.value = value
        self.next = None


# ---------------------------------------------------------------
# 🧱 STACK CLASS (with push & peek methods)
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
    # 1️⃣ PUSH METHOD
    # -----------------------------------------------------------
    def push(self, value):
        """
        Insert a new node at the top of the stack.
        ⏱️ O(1) | 💾 O(1)
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    # -----------------------------------------------------------
    # 2️⃣ __str__() → Print Stack (Top → Bottom)
    # -----------------------------------------------------------
    def __str__(self):
        if self.length == 0:
            return "Stack is Empty"
        values = []
        current_node = self.top
        while current_node:
            values.append(str(current_node.value))
            current_node = current_node.next
        return "\n".join(values)

    # -----------------------------------------------------------
    # 3️⃣ PEEK METHOD
    # -----------------------------------------------------------
    def peek(self):
        """
        Purpose:
        Return the top element of the stack *without removing it*.

        Steps:
        1️⃣ Check if stack is empty → return "Stack is Empty".
        2️⃣ If not empty, return self.top.value.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if self.top is None:
            return "Stack is Empty"
        return self.top.value


# ---------------------------------------------------------------
# ✅ USAGE EXAMPLE & DRY RUN
# ---------------------------------------------------------------
if __name__ == "__main__":
    new_stack = Stack()

    # Push elements
    new_stack.push(10)   # Stack: [10]
    new_stack.push(20)   # Stack: [20 → 10]
    new_stack.push(30)   # Stack: [30 → 20 → 10]

    print("Current Stack:")
    print(new_stack)

    # Peek top element
    print("\nValue at Top (using peek):", new_stack.peek())  # → 30


# ---------------------------------------------------------------
# 📊 VISUALIZATION (PEEK OPERATION)
# ---------------------------------------------------------------
# Stack (Top → Bottom):
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
# peek() → returns top value = 30
# Stack remains unchanged.
# ---------------------------------------------------------------


"""
📘 STACK (Linked List Implementation) — PEEK METHOD SUMMARY

🔹 What It Does:
Returns the top element of the stack *without removing it*.

🔹 Steps:
1️⃣ Check if stack is empty.
2️⃣ Return top.value.

🔹 Behavior:
- Does not modify stack.
- Safe to call multiple times.

---------------------------------------------------------
🔹 Example:
Stack: [30 → 20 → 10]
peek() → 30
Stack after peek() → [30 → 20 → 10] (unchanged)

---------------------------------------------------------
🔹 Time & Space Complexity
Operation        Time Complexity     Space Complexity
----------------------------------------------------
Check Empty       O(1)                O(1)
Access Top        O(1)                O(1)
TOTAL             O(1)                O(1)

---------------------------------------------------------
✅ SUMMARY:
- peek() is an efficient O(1) operation.
- Used to inspect the top without removing it.
- Does not alter the stack structure.
"""
