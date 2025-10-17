# stack_of_plates_note.py
# ------------------------------------------------------
# 📘 StackOfPlates — Set of Stacks with Rollover pop_at() (Note-style)
# ✅ Beginner-friendly: each method in its own section with visuals and examples
# ------------------------------------------------------

"""
OVERVIEW

This note explains a "Stack of Plates" implementation where multiple
sub-stacks are used, each with a fixed capacity. When one sub-stack
fills, a new sub-stack is created. The special operation `pop_at(i)`
removes the top from sub-stack `i` and then "rolls over" the bottom
items from the following stacks so earlier stacks stay compact.

Key ideas:
  • Use a list of deques (one deque per sub-stack) so we can remove
    bottoms efficiently with popleft().
  • push/pop operate on the last sub-stack (behave like a normal stack).
  • pop_at(i) removes from sub-stack i then repeatedly takes the bottom
    of stack i+1 and appends it to stack i, then bottom of i+2 -> i+1, etc.

Why rollover?
  • Keeps the distribution of plates compact (no holes in earlier stacks).
  • Matches an interview variant of the problem where stacks should stay balanced.

Trade-offs:
  • pop_at with rollover costs O(k) where k is number of stacks after index
    because we may move one bottom per following stack. But each popleft is O(1).

"""

# ---------------------------------------------------------------
# IMPORTS
# ---------------------------------------------------------------
from collections import deque
from typing import Optional


# ---------------------------------------------------------------
# CLASS: StackOfPlates
# ---------------------------------------------------------------
class StackOfPlates:
    """Set of stacks with fixed-capacity sub-stacks and rollover pop_at.

    Public methods:
      - push(item)
      - pop()
      - pop_at(index)

    Internals:
      - self.stacks: list of deque objects, each deque is a sub-stack
      - self.capacity: max items in each sub-stack
    """

    # ----------------------------
    # Constructor
    # ----------------------------
    def __init__(self, capacity: int):
        """
        Create an empty StackOfPlates.

        Args:
            capacity (int): maximum number of items per sub-stack. Must be > 0.

        Visual on init (capacity=3):
            stacks = []  # no sub-stacks yet
        """
        if capacity <= 0:
            raise ValueError("capacity must be > 0")
        self.capacity = capacity
        self.stacks: list[deque] = []

    # ----------------------------
    # Nicely print internal state
    # ----------------------------
    def __str__(self):
        """
        Show the stacks as a list-of-lists for readability.

        Example:
            [[1, 2], [3, 4]]
        """
        return "[" + ", ".join(str(list(d)) for d in self.stacks) + "]"

    # ----------------------------
    # push(item)
    # ----------------------------
    def push(self, item) -> str:
        """
        Push an item onto the last sub-stack. Create a new sub-stack if needed.

        Steps:
          1. If there is at least one sub-stack and its size < capacity, append there.
          2. Otherwise create a new deque and append the item.

        Complexity: O(1)

        Visual example (capacity=2):
            start: []
            push(1) -> [[1]]
            push(2) -> [[1,2]]
            push(3) -> [[1,2], [3]]  # new sub-stack

        Returns: confirmation string.
        """
        if self.stacks and len(self.stacks[-1]) < self.capacity:
            self.stacks[-1].append(item)
        else:
            self.stacks.append(deque([item]))
        return f"Enqueued {item}"

    # ----------------------------
    # pop()
    # ----------------------------
    def pop(self) -> Optional[str]:
        """
        Pop an element from the last non-empty sub-stack.

        Steps:
          1. Remove any trailing empty sub-stacks (they can appear after pop_at).
          2. If no sub-stacks remain, return None.
          3. Otherwise pop from the last deque and if it becomes empty remove it.

        Complexity: O(1) amortized

        Visual example:
            stacks = [[1,2],[3,4]]
            pop() -> pops 4 -> [[1,2],[3]]
        """
        # Clean up trailing empty stacks
        while self.stacks and len(self.stacks[-1]) == 0:
            self.stacks.pop()

        if not self.stacks:
            return None

        value = self.stacks[-1].pop()

        # If last stack became empty after pop, remove it
        if self.stacks and len(self.stacks[-1]) == 0:
            self.stacks.pop()

        return f"Popped {value}"

    # ----------------------------
    # Helper: _remove_bottom(i)
    # ----------------------------
    def _remove_bottom(self, i: int) -> Optional[object]:
        """
        Remove and return the bottom (left-most) element of sub-stack i.

        If the sub-stack becomes empty after removal, remove that sub-stack from self.stacks.

        Returns the removed value, or None if i is invalid or stack i is empty.

        Complexity: O(1) because deque.popleft() is O(1).
        """
        if i < 0 or i >= len(self.stacks):
            return None
        if not self.stacks[i]:
            return None
        bottom = self.stacks[i].popleft()
        if len(self.stacks[i]) == 0:
            # remove the empty deque
            self.stacks.pop(i)
        return bottom

    # ----------------------------
    # pop_at(index) with rollover
    # ----------------------------
    def pop_at(self, index: int) -> Optional[str]:
        """
        Pop the top item from sub-stack at `index`, then roll over bottoms from
        subsequent stacks to keep earlier stacks compact.

        Steps:
          1. Validate index and check target stack is not empty.
          2. Pop the top item from stacks[index].
          3. If that sub-stack becomes empty, remove it.
          4. For each following sub-stack (index+1, index+2, ...):
               - remove its bottom element and append it to the previous stack.
               - if a following sub-stack becomes empty, it is removed automatically by _remove_bottom.

        Example (capacity=2):
            start: [[1,2],[3,4],[5]]
            pop_at(0) -> pop 2 from stack0
                then remove bottom of stack1 (3) and append to stack0 -> [[1,3],[4],[5]]
                then remove bottom of stack2 (5) and append to stack1 -> [[1,3],[4,5]]

        Complexity: O(k) where k is number of stacks after index (each popleft is O(1)).

        Returns message string or None if index invalid or empty.
        """
        if index < 0 or index >= len(self.stacks):
            return None
        if not self.stacks[index]:
            return None

        popped = self.stacks[index].pop()

        # If chosen stack became empty after pop, remove it
        if len(self.stacks[index]) == 0:
            self.stacks.pop(index)

        # Now roll bottoms leftwards to fill gaps
        cur = index
        while cur < len(self.stacks) - 1:
            # remove bottom from the next stack (cur+1)
            bottom = self._remove_bottom(cur + 1)
            if bottom is None:
                break
            # append bottom to current stack; create the stack if it was removed
            if cur >= len(self.stacks):
                self.stacks.append(deque([bottom]))
            else:
                self.stacks[cur].append(bottom)
            cur += 1

        return f"Popped : {popped} from stacknum :{index}"


# ---------------------------------------------------------------
# DEMONSTRATION — beginner-friendly trace
# ---------------------------------------------------------------
if __name__ == '__main__':
    print("=== StackOfPlates Demo (capacity=2) ===")

    s = StackOfPlates(2)
    print(s.push(1))  # Enqueued 1
    print(s.push(2))  # Enqueued 2
    print(s.push(3))  # Enqueued 3 -> new sub-stack
    print(s.push(4))  # Enqueued 4
    print("Stacks:", s)       # [[1,2], [3,4]]

    print("\n-- pop_at(0) (rollover)")
    print(s.pop_at(0))        # pop from first sub-stack and rollover
    print("After pop_at(0):", s)

    print("\n-- pop() from last")
    print(s.pop())            # pop from last
    print("Final Stacks:", s)

    print("\n-- Edge cases")
    print("pop_at invalid:", s.pop_at(10))   # None
    print("pop until empty:")
    print(s.pop())
    print(s.pop())
    print(s.pop())  # None when empty

# ---------------------------------------------------------------
# COMPLEXITY SUMMARY (concise)
# ---------------------------------------------------------------
"""
Operation | Time  | Notes
-------------------------
push      | O(1)  | append to last deque or create new
pop       | O(1)  | pop from last deque + cleanup
pop_at    | O(k)  | k = number of stacks after index (popleft per stack)

Using deque keeps bottom removals O(1). Overall pop_at may be O(k) because
it may perform one popleft per following stack.
"""
