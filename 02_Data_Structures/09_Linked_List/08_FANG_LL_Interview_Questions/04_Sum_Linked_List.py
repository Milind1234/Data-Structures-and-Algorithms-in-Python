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
