# plate_stack_note.py
# ------------------------------------------------------
# 📘 PlateStack — Simple Set of Stacks (Note-style)
# ✅ Beginner-friendly: each method clearly explained with visuals and examples
# ------------------------------------------------------

"""
OVERVIEW

This note explains a simple **Set of Stacks** implementation — sometimes
called the *Plate Stack* problem — inspired by a real-world scenario:

Imagine stacking dinner plates. When a stack becomes too tall (reaches
its `capacity`), you start a new stack. Similarly, this class manages
multiple sub-stacks automatically, so each stays below a defined limit.

Key concepts:
  • Each sub-stack behaves like a regular stack (LIFO).
  • `push(item)` adds an item to the last stack; if it’s full, creates a new one.
  • `pop()` removes from the last stack.
  • `pop_at(i)` removes from a specific sub-stack.

This version does **not** do rollover (unlike `StackOfPlates`); each stack
works independently.
"""

# ---------------------------------------------------------------
# CLASS: PlateStack
# ---------------------------------------------------------------
class PlateStack:
    """A simple set of stacks with a fixed capacity per sub-stack."""

    # -----------------------------------------------------------
    # 1️⃣ __init__() — create the structure
    # -----------------------------------------------------------
    def __init__(self, capacity):
        """
        Initialize the PlateStack with a given per-stack capacity.

        Example (capacity = 2):
            stacks = []  # no sub-stacks initially

        When you push elements, new lists are created when needed.
        """
        self.capacity = capacity
        self.stacks = []  # list of sub-stacks (each sub-stack = list)

    # -----------------------------------------------------------
    # 2️⃣ __str__() — print helper
    # -----------------------------------------------------------
    def __str__(self):
        """Return visual representation of all sub-stacks."""
        return str(self.stacks)

    # -----------------------------------------------------------
    # 3️⃣ push(item) — add item to top of last sub-stack
    # -----------------------------------------------------------
    def push(self, item):
        """
        Push an item to the most recent sub-stack.

        Steps:
          1. If at least one sub-stack exists and it's not full, append there.
          2. Else, create a new sub-stack and push the item.

        Visual Example (capacity=2):
            push(1) -> [[1]]
            push(2) -> [[1,2]]  (stack full)
            push(3) -> [[1,2],[3]]  (new stack created)

        Complexity:
          ⏱️ Time: O(1)
          💾 Space: O(n)
        """
        if len(self.stacks) > 0 and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append([item])

    # -----------------------------------------------------------
    # 4️⃣ pop() — remove top from last sub-stack
    # -----------------------------------------------------------
    def pop(self):
        """
        Pop the top element from the last non-empty sub-stack.

        Steps:
          1. While the last stack is empty, remove it.
          2. If no stacks remain, return None.
          3. Otherwise, pop the top from the last stack.

        Visual Example:
            stacks = [[1,2],[3,4]]
            pop() -> removes 4 -> [[1,2],[3]]
            pop() -> removes 3 -> [[1,2]]

        Complexity:
          ⏱️ Time: O(1) average
          💾 Space: O(n)
        """
        while len(self.stacks) and len(self.stacks[-1]) == 0:
            self.stacks.pop()
        if len(self.stacks) == 0:
            return None
        return self.stacks[-1].pop()

    # -----------------------------------------------------------
    # 5️⃣ pop_at(index) — remove from specific sub-stack
    # -----------------------------------------------------------
    def pop_at(self, stackNumber):
        """
        Pop the top element from a specific sub-stack (by index).

        Steps:
          1. Validate the index.
          2. If stack has items, pop and return it.
          3. Otherwise, return None.

        Example:
            stacks = [[1,2],[3,4]]
            pop_at(1) -> removes 4 -> [[1,2],[3]]
            pop_at(0) -> removes 2 -> [[1],[3]]

        Complexity:
          ⏱️ Time: O(1)
          💾 Space: O(n)
        """
        if stackNumber < 0 or stackNumber >= len(self.stacks):
            return None
        if len(self.stacks[stackNumber]) > 0:
            return self.stacks[stackNumber].pop()
        return None


# ---------------------------------------------------------------
# DEMONSTRATION — beginner-friendly trace
# ---------------------------------------------------------------
if __name__ == '__main__':
    print("=== PlateStack Demo (capacity=2) ===")
    customStack = PlateStack(2)

    customStack.push(1)
    customStack.push(2)
    customStack.push(3)
    customStack.push(4)

    print("Stacks after pushes:", customStack)
    print("pop_at(1):", customStack.pop_at(1))
    print("Stacks after pop_at(1):", customStack)
    print("pop():", customStack.pop())
    print("Final Stacks:", customStack)

# ---------------------------------------------------------------
# COMPLEXITY SUMMARY
# ---------------------------------------------------------------
"""
Operation | Time | Space | Notes
---------------------------------
push      | O(1) | O(1)  | May create new sub-stack
pop       | O(1) | O(1)  | Removes from last non-empty stack
pop_at    | O(1) | O(1)  | Removes from a specific stack

Each operation touches at most one stack — constant time work.
"""