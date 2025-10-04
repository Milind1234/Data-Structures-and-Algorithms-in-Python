# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Push Method in Stack (Linked List Implementation)
# ------------------------------------------------------

"""
📌 OVERVIEW:
In a **Linked List–based Stack**, every element is represented by a node
containing a value and a pointer (next) to the next node.

When implementing the `push()` operation:
- We always insert (add) the new node **at the beginning** of the linked list.
- This ensures **O(1)** insertion time.

---------------------------------------------------------
🔹 WHY INSERT AT THE BEGINNING?
---------------------------------------------------------
👉 If we insert/remove at the **end**, we must traverse the whole list → O(n)
👉 If we insert/remove at the **head**, we can directly access the node → O(1)

So, inserting and removing elements at the **head (top)** is the most efficient approach.

Therefore, in a linked-list-based stack:
- **Push** = insert node at head
- **Pop**  = remove node from head
- **Top**  = head of the list
"""

# ---------------------------------------------------------------
# 🧩 NODE CLASS
# ---------------------------------------------------------------
class Node:
    def __init__(self, value):
        """
        Represents one element (node) in the stack.
        - value → stored data
        - next  → pointer to the next node
        """
        self.value = value
        self.next = None


# ---------------------------------------------------------------
# 🧱 STACK CLASS (with push method)
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
    # 1️⃣ PUSH METHOD → Insert new node at top
    # -----------------------------------------------------------
    def push(self, value):
        """
        Purpose:
        Insert (push) a new value on top of the stack.

        Steps:
        1️⃣ Create a new node with the given value.
        2️⃣ Point new_node.next to the current top node.
        3️⃣ Update top to the new node.
        4️⃣ Increment length by 1.

        Works for:
        - Empty stack (top = None)
        - Non-empty stack (top points to previous node)

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        new_node = Node(value)
        new_node.next = self.top     # Step 2 → link to previous top
        self.top = new_node          # Step 3 → update new top
        self.length += 1             # Step 4 → increase size

    # -----------------------------------------------------------
    # 2️⃣ __str__() → Visualize stack vertically (top → bottom)
    # -----------------------------------------------------------
    def __str__(self):
        """
        Print the stack from top to bottom in a readable format.

        ⏱️ Time Complexity: O(n)
        💾 Space Complexity: O(n)
        """
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
    new_stack = Stack()

    # Push elements
    new_stack.push(10)   # stack: [10]
    new_stack.push(20)   # stack: [20 → 10]
    new_stack.push(30)   # stack: [30 → 20 → 10]

    # Display top value
    print("Top element:", new_stack.top.value)  # → 30

    # Visualize the stack
    print("\nVisualized Stack:")
    print(new_stack)


# ---------------------------------------------------------------
# 📊 VISUALIZATION (PUSH OPERATION)
# ---------------------------------------------------------------

# Initial: Empty stack
#   top → None

# Push(10):
#   +----+
#   | 10 | ← top
#   +----+
#     ↓
#   None

# Push(20):
#   +----+
#   | 20 | ← top
#   +----+
#     ↓
#   +----+
#   | 10 |
#   +----+
#     ↓
#   None

# Push(30):
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
# ---------------------------------------------------------------


"""
📘 STACK (Linked List Implementation) — PUSH METHOD SUMMARY

🔹 What It Does:
- Inserts a new node at the top of the stack.

🔹 Steps:
1️⃣ Create a new node.
2️⃣ Set new_node.next = current top.
3️⃣ Update top = new_node.
4️⃣ Increment length by 1.

🔹 Works For:
- Empty stack (adds the first element)
- Non-empty stack (adds above previous top)

🔹 Time & Space Complexity:
Operation     Time Complexity     Space Complexity
-------------------------------------------------
Create Node    O(1)                O(1)
Link Top       O(1)                O(1)
Update Pointer O(1)                O(1)
Increment Len  O(1)                O(1)
TOTAL          O(1)                O(1)

---------------------------------------------------------
✅ EXAMPLE:
push(10) → [10]
push(20) → [20 → 10]
push(30) → [30 → 20 → 10]
top → 30

---------------------------------------------------------
✅ SUMMARY:
- push() adds new node at the top of stack.
- Highly efficient: constant time, no traversal.
- Space-efficient: constant memory per node.
"""
