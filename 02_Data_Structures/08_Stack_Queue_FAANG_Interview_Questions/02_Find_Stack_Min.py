# min_stack_note.py
# ------------------------------------------------------
# 📘 Min Stack — Stack with O(1) min() (Note-style)
# ✅ Beginner-friendly: each method in its own section with visuals and examples
# ------------------------------------------------------

"""
OVERVIEW

This note explains a linked-list stack implementation that also tracks
the current minimum element in O(1) time.

Key idea:
  • Maintain two linked lists simultaneously:
      - `top`   : the regular stack of pushed values
      - `minNode`: a parallel stack where each node stores the minimum
                   value among all elements at or below that level

On push(x): push x onto `top`, and push min(x, current_min) onto `minNode`.
On pop(): pop from both `top` and `minNode` so the current_min always
reflects the stack's state.

Why this is useful:
  • min() returns the minimum element in constant time without scanning the stack.

"""

# ---------------------------------------------------------------
# Node class — simple linked-list node
# ---------------------------------------------------------------
class Node:
    """Linked-list node used by both stacks (value + next)."""
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

    def __str__(self):
        # Represent node chain as a comma-separated list of values
        s = str(self.value)
        if self.next:
            s += "," + str(self.next)
        return s


# ---------------------------------------------------------------
# Stack class with min-tracking
# ---------------------------------------------------------------
class Stack:
    """A stack that supports push, pop, and min in O(1) time."""

    def __init__(self):
        """Create an empty stack and an empty min tracker."""
        self.top = None      # top of the value stack
        self.minNode = None  # top of the min-value stack

    # -----------------------------------------------------------
    # 1️⃣ min() — read current minimum
    # -----------------------------------------------------------
    def min(self):
        """
        Return the current minimum value in the stack.

        Visual idea:
          minNode stores a parallel value for every push. The top of minNode
          is the current minimum for the whole stack.

        Example:
          push(5) -> minNode top = 5
          push(3) -> minNode top = 3
          push(4) -> minNode top = 3 (since 3 < 4)

        Returns:
          The minimum value or None if the stack is empty.
        """
        if not self.minNode:
            return None
        return self.minNode.value

    # -----------------------------------------------------------
    # 2️⃣ push(item) — push value and update minNode
    # -----------------------------------------------------------
    def push(self, item):
        """
        Push `item` onto the stack and update minNode.

        Steps:
          1. If minNode exists and its value < item, push the old min value
             again onto minNode (duplicate the previous min).
          2. Otherwise push item onto minNode (it becomes the new min).
          3. Push item onto the regular top stack.

        Why duplicate the min when item is larger?
          - We need minNode to remain aligned with the value stack: for every
            value pushed, there is a corresponding min value at the same depth.

        Visual trace:
          Start: top=None, min=None
          push(5): top -> 5 ; min -> 5
          push(3): top -> 3 -> 5 ; min -> 3 -> 5
          push(7): top -> 7 -> 3 -> 5 ; min -> 3 -> 3 -> 5

        Returns:
          A short confirmation string.
        """
        if self.minNode is not None and (self.minNode.value < item):
            # previous minimum is smaller, carry it forward
            self.minNode = Node(value=self.minNode.value, next=self.minNode)
        else:
            # new item is the new minimum (or minNode is empty)
            self.minNode = Node(value=item, next=self.minNode)

        # push to the actual stack
        self.top = Node(value=item, next=self.top)
        return f"Pushed: {self.top.value}"

    # -----------------------------------------------------------
    # 3️⃣ pop() — remove top value and update minNode
    # -----------------------------------------------------------
    def pop(self):
        """
        Pop the top element and return it.

        Steps:
          1. If the stack is empty (self.top is None), return None.
          2. Move minNode forward (pop its top) so current min updates.
          3. Remove top from the value stack and return its value.

        Visual example:
          top -> 4 -> 1 -> 3 ; min -> 1 -> 1 -> 3
          pop() => removes 4 ; new top -> 1 -> 3 ; new min -> 1 -> 3

        Returns:
          The popped value as a string message, or None when empty.
        """
        if not self.top:
            return None
        # pop min tracker
        self.minNode = self.minNode.next
        # pop value stack
        item = self.top.value
        self.top = self.top.next
        return f"Popped: {item}"

    # -----------------------------------------------------------
    # Debug: representation
    # -----------------------------------------------------------
    def __repr__(self):
        vals = []
        cur = self.top
        while cur:
            vals.append(str(cur.value))
            cur = cur.next
        return " -> ".join(vals) if vals else "[Empty Stack]"


# ---------------------------------------------------------------
# DEMONSTRATION — beginner-friendly trace
# ---------------------------------------------------------------
if __name__ == '__main__':
    s = Stack()
    print(s.push(5))   # Pushed: 5
    print("Min:", s.min())  # 5
    print(s)
    
    print(s.push(3))   # Pushed: 3
    print("Min:", s.min())  # 3
    print(s)
    
    print(s.push(1))   # Pushed: 1
    print("Min:", s.min())  # 1
    print(s)

    print(s.push(4))   # Pushed: 4
    print("Min:", s.min())  # still 1
    print(s)
    
    print(s.pop())     # Popped: 4
    print("Min:", s.min())  # 1
    print(s)

    print(s.pop())     # Popped: 1
    print("Min:", s.min())  # 3
    print(s)
    
# ---------------------------------------------------------------
# COMPLEXITY SUMMARY
# ---------------------------------------------------------------
"""
Operation | Time | Space
-------------------------
push      | O(1) | O(1)
pop       | O(1) | O(1)
min       | O(1) | O(1)

All operations are constant-time and use O(1) additional space per element.
"""