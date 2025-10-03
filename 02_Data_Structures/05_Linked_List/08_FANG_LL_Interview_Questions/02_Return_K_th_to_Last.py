# note.py
# ------------------------------------------------------
# 📘 Singly Linked List - Notes File
# ✅ Topic: nth-to-last (iterative + recursive) with deep recursion trace
# ------------------------------------------------------

"""
Purpose:
Find the nth-to-last node in a singly linked list.

Two approaches provided:
1. nthToLast(n)            → Two-pointer (iterative) O(n) time, O(1) space
2. nthToLastRecursive(n)   → Recursion-based O(n) time, O(n) call-stack space

Example used in notes & trace:
List: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
n = 3  → 3rd last node = 6
"""

# ---------------------------------------------------------------
# Node class
# ---------------------------------------------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

# ---------------------------------------------------------------
# LinkedList class with nth-to-last methods
# ---------------------------------------------------------------
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        """Return a string representation of the linked list."""
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
            temp_node = temp_node.next
        return result

    def append(self, value):
        """Insert node at the end"""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # ---------------------------------------------------------------
    # Iterative (two-pointer) nth-to-last
    # ---------------------------------------------------------------
    def nthToLast(self, n):
        """
        Two-pointer technique (fast & slow):

        Steps:
        1. Initialize pointer1 = head, pointer2 = head.
        2. Advance pointer2 by n steps.
           - If pointer2 becomes None during this step => list shorter than n -> return None.
        3. Move pointer1 and pointer2 forward together until pointer2 becomes None.
        4. At that moment pointer1 points to the nth-to-last node. Return it.

        Example (n=3, list length 8):
        - After advancing pointer2 by 3 steps, pointer2 points to node 4.
        - Move both pointers forward until pointer2 is None; pointer1 ends at node 6.

        Complexity:
        - Time: O(n)
        - Space: O(1)
        """
        if self.head is None:
            return None

        pointer1 = self.head
        pointer2 = self.head

        # Move pointer2 n steps ahead
        for i in range(n):
            if pointer2 is None:
                return None
            pointer2 = pointer2.next

        # Move both until pointer2 reaches the end
        while pointer2:
            pointer1 = pointer1.next
            pointer2 = pointer2.next

        return pointer1

    # ---------------------------------------------------------------
    # Recursive nth-to-last
    # ---------------------------------------------------------------
    def nthToLastRecursive(self, n):
        """
        Recursive approach:

        Idea:
        - Recurse to the end of the list, then as the recursion unwinds,
          keep a counter of how many nodes we have seen from the end.
        - When the counter equals n, the current node is the nth-to-last node.

        Implementation notes:
        - We use a helper function `recurse(node)` that returns a tuple:
            (count_from_end, found_node)
          where:
            - count_from_end: integer count of nodes seen so far from the tail
            - found_node: the Node that matches nth-from-last once discovered, else None
        - Base case: recurse(None) returns (0, None)
        - On return from recursion:
            count += 1
            if count == n: return (count, node)  # found
            else: return (count, found)  # propagate found (if any) upward

        Complexity:
        - Time: O(n)
        - Space: O(n) due to recursion call stack
        """
        def recurse(node):
            # Base case: reached past the last node
            if node is None:
                return 0, None  # (count, foundNode)

            count, found = recurse(node.next)  # recursive call deeper
            count += 1  # as we unwind, increment count

            # If this is the nth node from the end, set found to current node
            if count == n:
                return count, node

            # otherwise propagate any previously found node (or None)
            return count, found

        _, result_node = recurse(self.head)
        return result_node


# ---------------------------------------------------------------
# Detailed Recursion Execution Trace (example)
# ---------------------------------------------------------------
"""
📖 Execution Trace (Iteration-wise)
Using the example list: 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7 -> 8
n = 3

Step 1: Going down (recursive calls)
We call recurse() until we hit None:

recurse(1) -> recurse(2) -> recurse(3) -> recurse(4) -> recurse(5) -> recurse(6) -> recurse(7) -> recurse(8) -> recurse(None)

At recurse(None):
    returns (0, None) because we are at the end.

Step 2: Coming back (unwinding, counting)

I'll keep a trace table below showing:
Node | Call Received From | Returned (count, found) | After count+=1 | Condition (count==n?) | What’s Returned

None   | Base case        | -        | 0 |  -       | (0, None)
8      | recurse(None)    | (0, None)| 1 | 1==3? ❌ | (1, None)
7      | recurse(8)       | (1, None)| 2 | 2==3? ❌ | (2, None)
6      | recurse(7)       | (2, None)| 3 | 3==3? ✅ | (3, node=6)
5      | recurse(6)       | (3, 6)   | 4 | 4==3? ❌ | (4, 6)
4      | recurse(5)       | (4, 6)   | 5 | 5==3? ❌ | (5, 6)
3      | recurse(4)       | (5, 6)   | 6 | 6==3? ❌ | (6, 6)
2      | recurse(3)       | (6, 6)   | 7 | 7==3? ❌ | (7, 6)
1      | recurse(2)       | (7, 6)   | 8 | 8==3? ❌ | (8, 6)

🔎 Explanation
- At node 8, count = 1 (1st last node).
- At node 7, count = 2 (2nd last node).
- At node 6, count = 3 → matches n → 🎯 FOUND node 6.
- For earlier nodes (5, 4, 3, 2, 1), the found node (6) is carried upward unchanged.
- Final result returned to the top-level call is node 6.
"""

# ---------------------------------------------------------------
# ✅ How to Use & Quick Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    SLL = LinkedList()
    for i in range(1, 9):   # create list 1..8
        SLL.append(i)

    print("List:", SLL)                     # prints 1 -> 2 -> ... -> 8

    n = 3
    it_node = SLL.nthToLast(n)
    rec_node = SLL.nthToLastRecursive(n)

    if it_node:
        print(f"Iterative: {n}rd last node is {it_node.value}")
    else:
        print("Iterative: Not found (list shorter than n)")

    if rec_node:
        print(f"Recursive: {n}rd last node is {rec_node.value}")
    else:
        print("Recursive: Not found (list shorter than n)")

# ---------------------------------------------------------------
# 🔎 Notes / Tips
# ---------------------------------------------------------------
# - Iterative (two-pointer) approach is preferred when recursion depth or stack
#   usage is a concern (very long lists).
# - Recursive approach is elegant and easy to reason about, but uses O(n) stack space.
# - Both methods return the Node object (or None if n is invalid). To get the value,
#   access node.value.
# - Edge cases: n == 0 (meaning "0th from last") is ambiguous — typical definitions expect n >= 1.
#   If you want to support 0-based from-last, adjust the loop that advances pointer2 accordingly.
# ---------------------------------------------------------------
