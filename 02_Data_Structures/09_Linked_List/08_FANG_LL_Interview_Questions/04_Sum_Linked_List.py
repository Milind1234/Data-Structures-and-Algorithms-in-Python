# note.py
# ------------------------------------------------------
# 📘 Linked List - Notes File
# ✅ Topic: Sum Lists (Add two numbers represented by linked lists)
# ------------------------------------------------------

# ❓ PROBLEM:
# You are given two numbers represented as linked lists,
# where each node contains a single digit.
# The digits are stored in reverse order (1’s digit at head).
# Write a function to add the two numbers and return the sum as a new linked list.
#
# Example:
# Input:  (7 -> 1 -> 6)  +  (5 -> 9 -> 2)
#         (represents 617 + 295)
# Output: (2 -> 1 -> 9)
#         (represents 912)


# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


# 🔷 Linked List Structure
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def append(self, value):
        """Insert node at the end."""
        new_node = Node(value)
        if not self.head:
            self.head = self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node

    def __str__(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.value))
            cur = cur.next
        return " -> ".join(vals) if vals else "Empty"


# ---------------------------------------------------------------
# 1️⃣ sum_lists(l1, l2) → returns a new linked list with sum
# ---------------------------------------------------------------
def sum_lists(l1: LinkedList, l2: LinkedList) -> LinkedList:
    """
    Purpose:
    Adds two numbers represented by linked lists (digits in reverse order).
    Returns a new linked list storing the result.

    ⏱️ Time Complexity: O(max(n, m)) → traverse both lists once
    💾 Space Complexity: O(max(n, m)) → result list stores the sum

    Example:
    Input:  (7 -> 1 -> 6)  +  (5 -> 9 -> 2)
    Output: (2 -> 1 -> 9)  # because 617 + 295 = 912
    """
    p1, p2 = l1.head, l2.head
    carry = 0
    result = LinkedList()

    # Loop until both lists are exhausted and carry is zero
    while p1 or p2 or carry:
        val1 = p1.value if p1 else 0
        val2 = p2.value if p2 else 0

        total = val1 + val2 + carry
        carry = total // 10
        digit = total % 10

        result.append(digit)

        if p1: p1 = p1.next
        if p2: p2 = p2.next

    return result


# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
# Example:
# l1 = 7 -> 1 -> 6   (represents 617)
# l2 = 5 -> 9 -> 2   (represents 295)
#
# Expected sum = 912 → Result list = 2 -> 1 -> 9
#
# Iteration Trace Table 👇
#
# Step | p1 | p2 | val1 | val2 | carry_in | total | digit | carry_out | Result List
# -----|----|----|------|------|----------|-------|-------|-----------|----------------
# 1    | 7  | 5  | 7    | 5    | 0        | 12    | 2     | 1         | 2
# 2    | 1  | 9  | 1    | 9    | 1        | 11    | 1     | 1         | 2 -> 1
# 3    | 6  | 2  | 6    | 2    | 1        | 9     | 9     | 0         | 2 -> 1 -> 9
#
# ✅ Loop ends: p1=None, p2=None, carry=0
# Final Answer → 2 -> 1 -> 9 (represents 912)


# ---------------------------------------------------------------
# 📘 Visual Example
# ---------------------------------------------------------------
# Before:
# L1: [7] -> [1] -> [6]   (617)
# L2: [5] -> [9] -> [2]   (295)
#
# Adding digit by digit (reverse order):
#   7 + 5 = 12 → digit=2, carry=1
#   1 + 9 + 1 = 11 → digit=1, carry=1
#   6 + 2 + 1 = 9 → digit=9, carry=0
#
# After:
# Result: [2] -> [1] -> [9]   (912)


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Number 617 → 7 -> 1 -> 6
    l1 = LinkedList()
    for v in [7, 1, 6]:
        l1.append(v)

    # Number 295 → 5 -> 9 -> 2
    l2 = LinkedList()
    for v in [5, 9, 2]:
        l2.append(v)

    print("L1:", l1)   # 7 -> 1 -> 6
    print("L2:", l2)   # 5 -> 9 -> 2

    result = sum_lists(l1, l2)
    print("Sum:", result)  # 2 -> 1 -> 9  (912)


    """ Example Walkthrough:
    --------------------
    Input:
      l1 = 7 → 1 → 6   # represents number 617 (reverse order)
      l2 = 5 → 9 → 2   # represents number 295 (reverse order)

    Expected Output:
      2 → 1 → 9        # represents number 912

    ---- Step-by-Step Execution ----

    Step 1: Initialization
      p1 = 7, p2 = 5, carry = 0
      result = []

    Step 2: First Iteration
      val1 = 7, val2 = 5
      total = 7 + 5 + 0 = 12
      carry = 12 // 10 = 1
      digit = 12 % 10 = 2
      Append → result = [2]
      Move p1 → 1, p2 → 9

    Step 3: Second Iteration
      val1 = 1, val2 = 9
      total = 1 + 9 + 1(carry) = 11
      carry = 11 // 10 = 1
      digit = 11 % 10 = 1
      Append → result = [2 → 1]
      Move p1 → 6, p2 → 2

    Step 4: Third Iteration
      val1 = 6, val2 = 2
      total = 6 + 2 + 1(carry) = 9
      carry = 0
      digit = 9
      Append → result = [2 → 1 → 9]
      Move p1 → None, p2 → None

    Step 5: Fourth Iteration
      Both lists exhausted, carry = 0 → loop ends.

    Step 6: Return
      result = 2 → 1 → 9 (represents 912)


    ---- Visualization Table ----
    Iter | p1.val | p2.val | carry(in) | total | digit | carry(out) | Result
    -----|--------|--------|-----------|-------|-------|------------|-------------
      1  |   7    |   5    |    0      |  12   |   2   |     1      | [2]
      2  |   1    |   9    |    1      |  11   |   1   |     1      | [2 → 1]
      3  |   6    |   2    |    1      |   9   |   9   |     0      | [2 → 1 → 9]
      4  |  None  |  None  |    0      |   -   |   -   |     -      | Done
    """
    