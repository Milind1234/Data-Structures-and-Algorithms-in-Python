# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Stack Implementation using Linked List (Constructor)
# ------------------------------------------------------

"""
📌 OVERVIEW:
A Stack can be implemented using either:
1️⃣ Python List (array-based)
2️⃣ Linked List (node-based)

In this section, we focus on implementing a **Stack using a Singly Linked List**.

---------------------------------------------------------
🔹 CONCEPT RECAP
---------------------------------------------------------
- A **singly linked list** contains nodes where:
    each node → [ value | next ]
- There is a **head** pointer to the first node.
- The **last node’s next** pointer points to None.

Now, to make this behave like a Stack:
- We perform both **push** and **pop** operations **at the head**.
- The head (or “top”) acts as the **top of the stack**.

---------------------------------------------------------
🔹 WHY OPERATE AT THE HEAD?
---------------------------------------------------------
Let’s compare time complexity between performing operations at:
👉 the **end** of a linked list vs  
👉 the **beginning** of a linked list.

Case 1️⃣ — At the End:
- To remove the last node → we must traverse entire list.
- ⏱️ Pop (remove from end) → O(n)
- ⏱️ Push (add at end) → O(1)
→ ❌ Inefficient overall (since pop = O(n))

Case 2️⃣ — At the Beginning:
- Head node can be accessed directly.
- ⏱️ Push (insert at head) → O(1)
- ⏱️ Pop (remove from head) → O(1)
→ ✅ More efficient and ideal for Stack.

Therefore, in a **Stack using Linked List**,  
we always push and pop from the **head (top)** node.

---------------------------------------------------------
🔹 VISUALIZATION
---------------------------------------------------------
Linked List (Normal):
    Head → [10] → [20] → [30] → [40] → None

Stack (Linked List-based):
    Top → [10]
           ↓
          [20]
           ↓
          [30]
           ↓
          [40]
           ↓
          None

Here:
- Top always points to the **most recently added node**.
- When we pop, we remove the node at top.
- When we push, the new node becomes the new top.

---------------------------------------------------------
🔹 STACK NODE STRUCTURE
---------------------------------------------------------
"""

class Node:
    def __init__(self, value):
        """
        A single node of the stack.
        Each node stores:
        - value → actual data
        - next → pointer to next node
        """
        self.value = value
        self.next = None


# ---------------------------------------------------------------
# 🪣 STACK CONSTRUCTORS
# ---------------------------------------------------------------
class Stack:
    def __init__(self):
        """
        ✅ Empty Stack Constructor

        Purpose:
        - Create an empty stack.
        - Set top to None.
        - Set length to 0.

        Example:
            Stack():
                top → None
                length = 0

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        self.top = None
        self.length = 0


# ---------------------------------------------------------------
# 🧱 ALTERNATE CONSTRUCTOR (with one element)
# ---------------------------------------------------------------
class StackWithValue:
    def __init__(self, value):
        """
        ✅ Stack Constructor with Initial Value

        Purpose:
        - Initialize a stack with one element.
        - top → first node
        - length = 1

        Example:
            StackWithValue(10)
            top → [10] → None

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        new_node = Node(value)
        self.top = new_node
        self.length = 1


# ---------------------------------------------------------------
# ✅ USAGE EXAMPLE & DRY RUN
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Empty Stack
    print("Creating Empty Stack:")
    stack = Stack()
    print(f"Top: {stack.top}, Length: {stack.length}")

    # Stack with Initial Value
    print("\nCreating Stack with one element:")
    stack_with_value = StackWithValue(10)
    print(f"Top Value: {stack_with_value.top.value}, Length: {stack_with_value.length}")


# ---------------------------------------------------------------
# 📊 VISUALIZATION (Empty vs Initialized)
# ---------------------------------------------------------------

# Empty Stack:
#   top → None
#   length = 0

# Stack with 1 element:
#   top → [10] → None
#   length = 1

# Concept Diagram:
#        +-------+
# top →  |  10   |
#        +-------+
#           ↓
#         (None)
# ---------------------------------------------------------------


"""
📘 STACK (Linked List Implementation) — SUMMARY

🔹 OPERATIONS AT HEAD (TOP):
- Push → Insert new node at head.
- Pop  → Remove node from head.
✅ Both operations: O(1)

🔹 ADVANTAGES:
- Dynamic size (no fixed array size).
- No wasted memory.

🔹 LIMITATIONS:
- Slightly higher memory usage (due to node pointers).

---------------------------------------------------------
✅ COMPLEXITY
---------------------------------------------------------
Operation         Time Complexity     Space Complexity
---------------------------------------------------------
Create (Empty)    O(1)                O(1)
Create (1 Node)   O(1)                O(1)
Push              O(1)                O(1)
Pop               O(1)                O(1)
Peek              O(1)                O(1)
isEmpty           O(1)                O(1)
Clear             O(1)                O(1)
Traverse (print)  O(n)                O(1)

---------------------------------------------------------
🔹 NEXT STEPS:
After this constructor, implement:
- push()
- pop()
- peek()
- is_empty()
- size()
- clear()
to complete the linked list-based Stack.
"""
