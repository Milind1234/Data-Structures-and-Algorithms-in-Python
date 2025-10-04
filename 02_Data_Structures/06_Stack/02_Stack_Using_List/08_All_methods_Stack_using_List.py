# note.py
# ------------------------------------------------------
# 📘 STACK (Python list implementation)
# ✅ All Core Methods: push(), pop(), peek(), is_empty(), size(), clear(), __str__()
# ------------------------------------------------------

"""
📌 INTRODUCTION

This file shows a full Stack implementation using Python's built-in list.
We use the **end of the list** as the top of the stack (most efficient choice in Python):
    - push -> list.append(x)
    - pop  -> list.pop()

Why the end?
- Inserting/removing at the beginning of a Python list requires shifting elements → O(n).
- Appending/removing at the end is O(1) amortized (internal dynamic array).
"""

# ---------------------------------------------------------------
# 🧱 STACK CLASS (list-based)
# ---------------------------------------------------------------
class StackList:
    """
    Stack implemented on top of Python's list.

    Internal representation:
        self.items -> Python list, end of list = top of stack
    """
    def __init__(self):
        """
        Initialize an empty stack.

        ⏱️ Time Complexity: O(1)
        💾 Space Complexity: O(1)
        """
        self.items = []

    # -----------------------------------------------------------
    # 1️⃣ PUSH (append to end)
    # -----------------------------------------------------------
    def push(self, element):
        """
        PURPOSE:
        Add element to the top of the stack.

        IMPLEMENTATION IDEA:
        Use list.append(element) — constant time on average.

        VISUAL:
            []                # empty
            push(10) -> [10]
            push(20) -> [10, 20]  (top is 20, rightmost)
            push(30) -> [10, 20, 30] (top is 30)

        EXAMPLE:
            st = StackList()
            st.push(10)
            st.push(20)

        COMPLEXITY:
            Time: O(1) amortized
            Space (aux): O(1)
        """
        self.items.append(element)

    # -----------------------------------------------------------
    # 2️⃣ POP (remove from end)
    # -----------------------------------------------------------
    def pop(self):
        """
        PURPOSE:
        Remove and return the top element of the stack.
        If the stack is empty, return a message (or raise depending on your preference).

        IMPLEMENTATION IDEA:
        Use list.pop() with no index (pops last element).

        VISUAL:
            [10, 20, 30]  (top=30)
            pop() -> returns 30, stack -> [10, 20]

        EXAMPLE:
            st = StackList()
            st.push(10); st.push(20)
            st.pop() -> 20

        COMPLEXITY:
            Time: O(1)
            Space (aux): O(1)
        """
        if len(self.items) == 0:
            return "Stack is Empty"
        return self.items.pop()

    # -----------------------------------------------------------
    # 3️⃣ PEEK (view last element)
    # -----------------------------------------------------------
    def peek(self):
        """
        PURPOSE:
        Return the top element without removing it.

        IMPLEMENTATION IDEA:
        Access last element via self.items[-1] but handle empty stack.

        VISUAL:
            [10, 20, 30] -> peek() => 30 (stack unchanged)

        COMPLEXITY:
            Time: O(1)
            Space: O(1)
        """
        if len(self.items) == 0:
            return "Stack is Empty"
        return self.items[-1]

    # -----------------------------------------------------------
    # 4️⃣ is_empty (check emptiness)
    # -----------------------------------------------------------
    def is_empty(self):
        """
        PURPOSE:
        Return True if stack has no elements else False.

        IMPLEMENTATION IDEA:
        Use len(self.items) == 0 or not self.items.

        COMPLEXITY:
            Time: O(1)
            Space: O(1)
        """
        return len(self.items) == 0

    # -----------------------------------------------------------
    # 5️⃣ size (number of elements)
    # -----------------------------------------------------------
    def size(self):
        """
        PURPOSE:
        Return the number of elements in the stack.

        IMPLEMENTATION IDEA:
        Use len(self.items) — O(1) in Python (length stored internally).

        COMPLEXITY:
            Time: O(1)
            Space: O(1)
        """
        return len(self.items)

    # -----------------------------------------------------------
    # 6️⃣ clear (delete all elements)
    # -----------------------------------------------------------
    def clear(self):
        """
        PURPOSE:
        Remove all elements from the stack.

        IMPLEMENTATION IDEA:
        Assign new empty list or call self.items.clear().

        VISUAL:
            [10,20,30] -> clear() -> []

        COMPLEXITY:
            Time: O(1) (rebind or clear underlying list reference; clear() is O(n) to actually remove elements, but reassigning is O(1) and lets GC handle old list)
            Space: O(1)
        """
        # Prefer rebind to a new list for O(1) behavior in notes:
        self.items = []
        # Alternatively: self.items.clear()  # empties list in-place (O(n) to free refs)

    # -----------------------------------------------------------
    # 7️⃣ __str__ (visualization)
    # -----------------------------------------------------------
    def __str__(self):
        """
        PURPOSE:
        Return a vertical representation of the stack (top first).
        Note: This requires traversing the list and costs O(n).

        VISUAL OUTPUT example:
            30
            20
            10

        COMPLEXITY:
            Time: O(n)
            Space: O(n) (temporary list of strings)
        """
        if self.is_empty():
            return "Stack is Empty"
        # create a vertical top-first view by reversing the list temporarily
        return "\n".join(str(x) for x in reversed(self.items))


# ---------------------------------------------------------------
# ✅ USAGE EXAMPLE & DRY RUN
# ---------------------------------------------------------------
if __name__ == "__main__":
    print("✅ STACK (Python list) — Demo\n")

    st = StackList()
    print("Is Empty?", st.is_empty())   # True
    print("Size:", st.size())           # 0

    # Push elements
    st.push(10)
    st.push(20)
    st.push(30)

    print("\nAfter pushes (visual):")
    print(st)                           # 30 \n 20 \n 10

    # Peek
    print("\npeek:", st.peek())         # 30

    # Size
    print("size:", st.size())           # 3

    # Pop
    print("\npop:", st.pop())           # 30
    print("After pop (visual):")
    print(st)                           # 20 \n 10

    # Clear
    st.clear()
    print("\nAfter clear:")
    print("is_empty?", st.is_empty())   # True
    print(st)                           # Stack is Empty


# ---------------------------------------------------------------
# 📊 SUMMARY OF TIME & SPACE COMPLEXITIES
# ---------------------------------------------------------------
"""
Operation        | Time Complexity | Space Complexity
-----------------------------------------------------
push()           | O(1) amortized  | O(1)
pop()            | O(1)            | O(1)
peek()           | O(1)            | O(1)
is_empty()       | O(1)            | O(1)
size()           | O(1)            | O(1)
clear()          | O(1) (rebind)   | O(1)
__str__()        | O(n)            | O(n)

Notes:
- push/pop/peek are O(1) because we operate on the list's end.
- len(list) is O(1) in Python (length tracked in the object).
- Using rebind in clear() (self.items = []) gives O(1); if you prefer to clear in-place (self.items.clear()), Python will remove refs which is O(n).
"""
