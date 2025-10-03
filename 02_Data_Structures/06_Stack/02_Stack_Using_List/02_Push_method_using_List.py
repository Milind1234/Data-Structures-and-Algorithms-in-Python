# note.py
# ------------------------------------------------------
# 📘 Stack - Notes File
# ✅ Topic: Implementation of Stack using Python List (Push Operation)
# ------------------------------------------------------

# ❓ QUESTION:
# How to implement a Stack with push() operation in Python
# using built-in list as internal storage?

# ---------------------------------------------------------------
# 🔷 Stack Structure
# ---------------------------------------------------------------
class Stack:
    def __init__(self):
        # Internal list to store stack elements
        self.items = []

    # -----------------------------------------------------------
    # 1️⃣ push(element) → Insert element at the top of stack
    # -----------------------------------------------------------
    def push(self, element):
        """
        Purpose:
        Add a new element to the top of the stack.

        Implementation Idea:
        - Use list.append(element) because:
            * appending at end = O(1)
            * no shifting of elements
        - Treat the end of the list as the "top of stack".

        ⏱️ Time Complexity: O(1) (amortized)
        💾 Space Complexity: O(1) (per push)
        """
        self.items.append(element)

    # (Optional) make printing easier
    def __str__(self):
        return str(self.items)


# ---------------------------------------------------------------
# ✅ Usage Example & Dry Run
# ---------------------------------------------------------------
if __name__ == "__main__":
    my_stack = Stack()

    # Push elements
    my_stack.push(1)   # stack: [1]
    my_stack.push(2)   # stack: [1, 2]
    my_stack.push(3)   # stack: [1, 2, 3]
    print("After pushing 1, 2, 3:", my_stack.items)

    my_stack.push(4)   # stack: [1, 2, 3, 4]
    my_stack.push(5)   # stack: [1, 2, 3, 4, 5]
    print("After pushing 4, 5:", my_stack.items)

"""
📘 STACK OPERATION → PUSH (Using Python List)

🔹 Definition:
Push = Insert element at the top of the stack.
- In Python list-based implementation → end of list = top of stack.
- Use append() → efficient O(1).

🔹 Visualization:
Initially:
    [   ]

push(1):  [1]
push(2):  [1, 2]
push(3):  [1, 2, 3]
push(4):  [1, 2, 3, 4]
push(5):  [1, 2, 3, 4, 5]

🔹 Time Complexity:
- push() → O(1) average (amortized)
- Efficient because no shifting happens.

🔹 Space Complexity:
- O(1) extra for each push.
- O(n) total for n elements.

✅ SUMMARY:
- push() inserts at the top of stack.
- End of Python list is used as "top".
- Implementation uses list.append().
- Stack grows as: [] → [1] → [1,2] → [1,2,3] → ...
"""
