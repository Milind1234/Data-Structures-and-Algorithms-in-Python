# note.py
# ------------------------------------------------------
# 📘 STACK (Linked List Implementation)
# ✅ All Core Methods: push(), pop(), peek(), is_empty(), size(), clear(), __str__()
# ------------------------------------------------------

"""
📌 INTRODUCTION

In this implementation, a **stack** is built using a **Linked List**.

Each node has:
    - value  → data to store
    - next   → pointer to the next node

The stack maintains:
    - top    → pointer to the most recently added node
    - length → number of elements in stack

---------------------------------------------------------
🔹 Why use Linked List for Stack?
---------------------------------------------------------
✅ No fixed size (dynamic memory allocation)
✅ O(1) time for insertion (push) and deletion (pop)
✅ Easy to implement top-based operations

Visualization:

Top → [ 30 ] → [ 20 ] → [ 10 ] → None
         ↑
      Last inserted element
"""

# ---------------------------------------------------------------
# 🧩 NODE CLASS
# ---------------------------------------------------------------
class Node:
    """Node represents a single element of the stack."""
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------------------------------------------------------------
# 🧱 STACK CLASS
# ---------------------------------------------------------------
class Stack:
    """
    A Stack data structure implemented using Linked List.

    Attributes:
        top     → reference to the top node
        length  → number of elements in stack
    """
    def __init__(self):
        """
        Initialize an empty stack.

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
        🧠 PURPOSE:
        Insert (push) a new node at the top of the stack.

        STEPS:
        1️⃣ Create a new node with given value.
        2️⃣ Point new_node.next to current top.
        3️⃣ Move top pointer to new_node.
        4️⃣ Increment stack length.

        VISUALIZATION:
            Before push(30):
                Top → [20] → [10] → None
            After push(30):
                Top → [30] → [20] → [10] → None

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
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
        🧠 PURPOSE:
        Remove and return the top element from the stack.

        STEPS:
        1️⃣ Check if stack is empty → return message.
        2️⃣ Store current top node in popped_node.
        3️⃣ Move top pointer to next node.
        4️⃣ Detach popped node.
        5️⃣ Decrease length by 1.
        6️⃣ Return popped node value.

        VISUALIZATION:
            Before pop():
                Top → [30] → [20] → [10]
            After pop():
                Top → [20] → [10]
                Returned → 30

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if self.length == 0:
            return "Stack is Empty"

        popped_node = self.top
        self.top = self.top.next
        popped_node.next = None
        self.length -= 1
        return popped_node.value

    # -----------------------------------------------------------
    # 3️⃣ PEEK METHOD
    # -----------------------------------------------------------
    def peek(self):
        """
        🧠 PURPOSE:
        Return the top element without removing it.

        STEPS:
        1️⃣ If stack is empty → return message.
        2️⃣ Else return top.value.

        VISUALIZATION:
            Stack → [30] → [20] → [10]
            peek() → returns 30 (stack unchanged)

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        if self.top is None:
            return "Stack is Empty"
        return self.top.value

    # -----------------------------------------------------------
    # 4️⃣ IS_EMPTY METHOD
    # -----------------------------------------------------------
    def is_empty(self):
        """
        🧠 PURPOSE:
        Check whether the stack is empty or not.

        RETURNS:
        ✅ True  → if stack has no elements.
        🚫 False → otherwise.

        VISUALIZATION:
            []
            is_empty() → True
            After push(5)
            is_empty() → False

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        return self.length == 0

    # -----------------------------------------------------------
    # 5️⃣ SIZE METHOD
    # -----------------------------------------------------------
    def size(self):
        """
        🧠 PURPOSE:
        Return the total number of elements in the stack.

        EXAMPLE:
            push(10), push(20), push(30)
            size() → 3

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        return self.length

    # -----------------------------------------------------------
    # 6️⃣ CLEAR METHOD
    # -----------------------------------------------------------
    def clear(self):
        """
        🧠 PURPOSE:
        Remove all elements from the stack.

        STEPS:
        1️⃣ Set top = None.
        2️⃣ Reset length = 0.

        VISUALIZATION:
            Before clear():
                Top → [30] → [20] → [10]
            After clear():
                Top → None (Empty Stack)

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        self.top = None
        self.length = 0

    # -----------------------------------------------------------
    # 7️⃣ __STR__ METHOD (VISUALIZATION)
    # -----------------------------------------------------------
    def __str__(self):
        """
        🧠 PURPOSE:
        Print the stack elements from top to bottom (vertically).

        EXAMPLE OUTPUT:
            30
            20
            10

        ⏱️ Time Complexity: O(n)
        💾 Space Complexity: O(n)
        """
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
    print("✅ STACK (Linked List Implementation) — Demo\n")

    stack = Stack()

    print("Is Empty?", stack.is_empty())  # True

    # Push elements
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("\nAfter Push Operations:")
    print(stack)  # Top: 30 → 20 → 10

    # Peek top
    print("\nTop Element (peek):", stack.peek())  # 30

    # Size of stack
    print("Size of Stack:", stack.size())  # 3

    # Pop element
    print("\nPopped Element:", stack.pop())  # 30
    print("After Pop:")
    print(stack)  # Top → 20 → 10

    # Clear stack
    stack.clear()
    print("\nAfter Clear:")
    print("Is Empty?", stack.is_empty())  # True
    print(stack)  # Stack is Empty


# ---------------------------------------------------------------
# 📊 SUMMARY OF TIME & SPACE COMPLEXITIES
# ---------------------------------------------------------------
"""
Operation        | Time Complexity | Space Complexity
-----------------------------------------------------
push()           | O(1)            | O(1)
pop()            | O(1)            | O(1)
peek()           | O(1)            | O(1)
is_empty()       | O(1)            | O(1)
size()           | O(1)            | O(1)
clear()          | O(1)            | O(1)
__str__()        | O(n)            | O(n)

✅ Stack operations (push, pop, peek) all run in constant time.
✅ Only visualization (__str__) is linear due to traversal.
"""
