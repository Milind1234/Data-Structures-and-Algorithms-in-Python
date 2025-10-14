# multi_stack_note.py
# ------------------------------------------------------
# 📘 MultiStack — Three Stacks in One Array (Beginner-friendly Notes)
# ✅ Each function explained in its own section with visuals, step-by-step reasoning
# ------------------------------------------------------

"""
OVERVIEW

This file teaches a simple MultiStack implementation that stores
**three fixed-size stacks** inside a single Python list (array).
It is written for a beginner: each method has its own section, a
plain-language explanation, a small visual diagram, and an example
showing what changes in the internal state.

High-level design:
  • One backing list: `custList` of length = 3 * stacksize
  • sizes: list of three integers that track how many elements are in each stack
  • stack regions are contiguous blocks inside custList:
      Stack 0 -> indices 0..stacksize-1
      Stack 1 -> indices stacksize..2*stacksize-1
      Stack 2 -> indices 2*stacksize..3*stacksize-1

Goal: By the time you finish reading this file, you should be able to
explain push/pop/peek for a multi-stack and trace the internal array.
"""

# -----------------------------------------------------------------------------
# CLASS: MultiStack
# -----------------------------------------------------------------------------
class MultiStack:
    """Three fixed-size stacks stored inside one list.

    Methods are documented in separate sections below so beginners can
    read one short unit at a time.
    """

    # ----------------------------
    # Constructor: Setup storage
    # ----------------------------
    def __init__(self, stacksize):
        """
        Initialize internal storage for 3 stacks.

        Example (stacksize=3):
        custList = [None, None, None, None, None, None, None, None, None]
        indices   0  1  2 | 3  4  5 | 6  7  8
        regions  S0       | S1       | S2
        sizes = [0, 0, 0]
        """
        self.numberofstacks = 3
        self.custList = [None] * (stacksize * self.numberofstacks)
        self.sizes = [0] * self.numberofstacks
        self.stacksize = stacksize

   # -----------------------------------------------------------
    # 1️⃣ isFull() — simple helper checks
    # -----------------------------------------------------------
    def isFull(self, stacknum):
        """Return True if stack `stacknum` has reached capacity."""
        return self.sizes[stacknum] == self.stacksize

    # ----------------------------
    # isEmpty() — simple helper checks
    # ----------------------------
    def isEmpty(self, stacknum):
        """Return True if stack `stacknum` is empty."""
        return self.sizes[stacknum] == 0

   # -----------------------------------------------------------
    # 2️⃣ indexOfTop() — find where the top element lives
    # -----------------------------------------------------------
    def indexOfTop(self, stacknum):
        """
        3️⃣ MAP STACK NUMBER → LIST INDEX : indexOfTop(stacknum)

        Purpose
        -------
        Calculate the exact index in `custList` where the current top item
        of `stacknum` is stored.

        Explanation (step-by-step)
        --------------------------
        1. Each stack gets a block of length `stacksize` in the large array.
           The starting index (offset) for stack `stacknum` is:

               offset = stacknum * stacksize

           Example (stacksize=3):
               offset(0) = 0
               offset(1) = 3
               offset(2) = 6

        2. If a stack currently has `n` items (sizes[stacknum] == n), the
           top item is the (n-1)-th index inside that block. So overall:

               top_index = offset + n - 1

        Important
        ---------
        Callers must ensure the stack is not empty before calling this.
        If sizes[stacknum] == 0, this formula returns offset - 1 which is
        not a valid "top" location.

        Visual example (stacksize=3):
            sizes = [2, 0, 1]
            indexOfTop(0) -> offset 0 + 2 - 1 = 1  (custList[1])
            indexOfTop(2) -> offset 6 + 1 - 1 = 6  (custList[6])

        Returns
        -------
        int : index in custList of the current top element
        """
        offset = stacknum * self.stacksize
        return offset + self.sizes[stacknum] - 1

    # -----------------------------------------------------------
    # 3️⃣ PUSH METHOD → Insert new value at top
    # -----------------------------------------------------------
    def push(self, item, stacknum):
        """
        4️⃣ PUSH METHOD → Insert new item at top of chosen stack

        Purpose
        -------
        Place `item` on the top of stack `stacknum`.

        Steps (what this function does)
        --------------------------------
        1. Check if the chosen stack is full using `isFull`. If it is, return
           a friendly error message.
        2. Otherwise, **increase** sizes[stacknum] by 1. This reserves the
           next slot inside that stack's block.
        3. Compute the index of the (new) top using `indexOfTop` and write
           `item` into `custList` at that index.

        Why increase size *before* writing?
        ------------------------------------
        We increment `sizes` first so `indexOfTop` computes the index of the
        new top. If we incremented after, we'd need to compute a different
        index (more confusing) and risk off-by-one bugs.

        Visual step-by-step (stacksize=3)
        ---------------------------------
        Initial:
            custList = [__ | __ | __] | [__ | __ | __] | [__ | __ | __]
            sizes = [0, 0, 0]

        push(10, 0):
            sizes -> [1,0,0]
            indexOfTop(0) -> 0 + 1 - 1 = 0
            custList[0] = 10
            -> custList = [10, __, __] | [__ | __ | __] | [__ | __ | __]

        push(20, 0):
            sizes -> [2,0,0]
            indexOfTop(0) -> 0 + 2 - 1 = 1
            custList[1] = 20
            -> custList = [10, 20, __] | ...

        Return value
        ------------
        A success message (string) or an error message if stack was full.

        Complexity
        ----------
        Time: O(1)  Space: O(1)
        """
        if self.isFull(stacknum):
            return "The Stack is Full"
        self.sizes[stacknum] += 1
        self.custList[self.indexOfTop(stacknum)] = item
        return f"Pushed {item} to stack {stacknum}"

    # -----------------------------------------------------------
    # 4️⃣ POP METHOD → Remove and return top element
    # -----------------------------------------------------------
    def pop(self, stacknum):
        """
        5️⃣ POP METHOD → Remove and return top item from chosen stack

        Purpose
        -------
        Remove the top element from `stacknum` and return its value.

        Steps
        -----
        1. Check `isEmpty`: if empty, return a friendly message.
        2. Compute top_index via `indexOfTop` and read the value.
        3. Set the slot in `custList` back to None (clear it).
        4. Decrease `sizes[stacknum]` by 1 (since we removed an element).
        5. Return the popped value.

        Visual example (stacksize=3):
            Before pop (sizes=[2,0,1]):
                custList = [10, 20, __] | [__ | __ | __] | [99, __, __]
            pop(0):
                top_index = 1, value = 20
                custList[1] = None
                sizes -> [1,0,1]
                After: custList = [10, __, __] | ...

        Note
        ----
        Clearing the slot (setting to None) is optional for correctness but
        helpful for debugging and for distinguishing an actual stored None/0
        from an empty slot.

        Complexity
        ----------
        Time: O(1)  Space: O(1)
        """
        if self.isEmpty(stacknum):
            return "The Stack is Empty"
        top_index = self.indexOfTop(stacknum)
        value = self.custList[top_index]
        self.custList[top_index] = None
        self.sizes[stacknum] -= 1
        return value

    # -----------------------------------------------------------
    # 5️⃣ PEEK METHOD → Look at top without removing
    # -----------------------------------------------------------
    def peek(self, stacknum):
        """
        6️⃣ PEEK METHOD → Read top item without removing it

        Purpose
        -------
        Return the top element of the chosen stack but do not remove it.

        Steps
        -----
        1. Check `isEmpty`. If empty, return a friendly message.
        2. Otherwise compute `indexOfTop` and return `custList` at that index.

        Visual example:
            sizes = [1,2,0]
            custList = [10, None, None] | [5, 6, None] | [__, __, __]
            peek(1) -> index 3+2-1 = 4 -> custList[4] = 6

        Complexity
        ----------
        Time: O(1)  Space: O(1)
        """
        if self.isEmpty(stacknum):
            return "The Stack is Empty"
        return self.custList[self.indexOfTop(stacknum)]

    # ----------------------------
    # Debug: representation and helpers
    # ----------------------------
    def __repr__(self):
        blocks = []
        for i in range(self.numberofstacks):
            start = i * self.stacksize
            end = start + self.stacksize
            blocks.append(str(self.custList[start:end]))
        return " | ".join(blocks) + f"  sizes={self.sizes}"


# -----------------------------------------------------------------------------
# DEMONSTRATION & TESTS (step-by-step traces for beginners)
# -----------------------------------------------------------------------------
if __name__ == '__main__':
    print("=== MultiStack Beginner Trace ===")
    ms = MultiStack(3)
    print("Initial:", ms)

    print("\n-- push(10,0)")
    print(ms.push(10, 0))
    print(ms)

    print("\n-- push(20,0)")
    print(ms.push(20, 0))
    print(ms)

    print("\n-- push(30,0)")
    print(ms.push(30, 0))
    print(ms)

    print("\n-- push(40,0) (overflow attempt)")
    print(ms.push(40, 0))
    print(ms)

    print("\n-- peek(0)")
    print("Top of S0:", ms.peek(0))

    print("\n-- pop(0)")
    print("Popped:", ms.pop(0))
    print(ms)

    print("\n-- push(100,2) and push(200,2)")
    print(ms.push(100, 2))
    print(ms.push(200, 2))
    print(ms)

    print("\n-- Final sizes and internal array")
    print("sizes:", ms.sizes)
    print("custList:", ms.custList)

# -----------------------------------------------------------------------------
# COMPLEXITY SUMMARY (concise)
# -----------------------------------------------------------------------------
"""
Operation  | Time  | Space
-------------------------
push       | O(1)  | O(1)
pop        | O(1)  | O(1)
peek       | O(1)  | O(1)
isEmpty    | O(1)  | O(1)
isFull     | O(1)  | O(1)

Space to store stacks: O(3 * stacksize) = O(n) (n = total capacity)
"""
