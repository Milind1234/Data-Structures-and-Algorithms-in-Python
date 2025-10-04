# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Pop Method in Stack (Linked List Implementation)
# ------------------------------------------------------

"""
📌 OVERVIEW:
The `pop()` operation in a **Linked List–based Stack** removes and returns
the **top element** of the stack.

Stack follows **LIFO (Last In, First Out)**, meaning:
→ The last inserted node is always removed first.

In a linked list implementation:
- `top` always points to the most recently inserted node.
- To remove it, we move `top` one step down (to top.next).

---------------------------------------------------------
🔹 CONCEPT:
When we call `pop()`:
1️⃣ Check if the stack is empty.
2️⃣ If not, store a reference to the top node (to return it later).
3️⃣ Move top pointer to the next node.
4️⃣ Disconnect popped node’s `next` pointer (set to None).
5️⃣ Decrease stack length by 1.
6️⃣ Return the popped node’s value.
"""

# ---------------------------------------------------------------
# 🧩 NODE CLASS
# ---------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------------------------------------------------------------
# 🧱 STACK CLASS (with push & pop methods)
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
        Add a new node on top of the stack.
        ⏱️ O(1), 💾 O(1)
        """
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node
        self.length += 1

    # -----------------------------------------------------------
    # 2️⃣ POP METHOD
    # -----------------------------------------------------------
    def pop(self):
        """
        Purpose:
        Remove and return the top node’s value from the stack.

        Steps:
        1️⃣ Check if stack is empty → return "Empty Stack"
        2️⃣ Save reference to top node (popped_node)
        3️⃣ Move top pointer to next node
        4️⃣ Set popped_node.next = None (break link)
        5️⃣ Decrement length
        6️⃣ Return popped node’s value

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if self.length == 0:
            return "Empty stack"

        popped_node = self.top             # Step 2
        self.top = self.top.next           # Step 3
        popped_node.next = None            # Step 4
        self.length -= 1                   # Step 5

        return popped_node.value           # Step 6

    # -----------------------------------------------------------
    # 3️⃣ __str__() → for visualization
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


# ---------------------------------------------------------------
# ✅ USAGE EXAMPLE & DRY RUN
# ---------------------------------------------------------------
if __name__ == "__main__":
    new_stack = Stack()

    # Push elements
    new_stack.push(10)   # Stack: [10]
    new_stack.push(20)   # Stack: [20 → 10]
    new_stack.push(30)   # Stack: [30 → 20 → 10]

    print("Stack before pop():")
    print(new_stack)
    print("\nValue at Top:", new_stack.top.value)

    print("\nPopped Node:", new_stack.pop())   # → 30
    print("\nAfter popping top node:")
    print(new_stack)


# ---------------------------------------------------------------
# 📊 VISUALIZATION (POP OPERATION)
# ---------------------------------------------------------------
# Initial Stack:
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

# After pop():
#   top moves one step down

#   +----+
#   | 20 | ← top
#   +----+
#     ↓
#   +----+
#   | 10 |
#   +----+
#     ↓
#   None

# The popped node (30) is detached:
# popped_node.next → None
# returned value → 30
# ---------------------------------------------------------------


"""
📘 STACK (Linked List Implementation) — POP METHOD SUMMARY

🔹 What It Does:
Removes and returns the top node from the stack.

🔹 Steps:
1️⃣ Check if stack is empty.
2️⃣ Store top node.
3️⃣ Move top to next.
4️⃣ Break the link of popped node.
5️⃣ Decrease length.
6️⃣ Return popped node’s value.

🔹 Example:
Stack before pop: [30 → 20 → 10]
After pop:        [20 → 10]
Returned value:    30

---------------------------------------------------------
🔹 Time & Space Complexity
Operation           Time Complexity     Space Complexity
---------------------------------------------------------
Check Empty          O(1)                O(1)
Pointer Update       O(1)                O(1)
Length Update        O(1)                O(1)
TOTAL                O(1)                O(1)

---------------------------------------------------------
✅ SUMMARY:
- pop() removes the most recently added element (LIFO).
- Efficient: O(1) time, O(1) space.
- No traversal needed.
"""
