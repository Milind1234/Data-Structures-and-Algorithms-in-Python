# note.py
# ------------------------------------------------------
# 📘 Linked List - Notes File
# ✅ Topic: Intersection of Two Singly Linked Lists (by reference)
# ------------------------------------------------------

# ❓ PROBLEM:
# Given two singly linked lists, determine if they intersect.
# Intersection is defined based on the node reference (memory address),
# not the node value.
#
# If the kth node of list A is the exact same object as the jth node of list B,
# then the lists intersect. Return that intersecting node.
#
# Example:
# A: 3 -> 1 -> 5
#               \
#                7 -> 11 -> 14
#               /
# B:     9 -> 2
#
# Intersection node = 7


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
        return new_node

    def __len__(self):
        """Return length of list."""
        count = 0
        cur = self.head
        while cur:
            count += 1
            cur = cur.next
        return count

    def __str__(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.value))
            cur = cur.next
        return " -> ".join(vals) if vals else "Empty"


# ---------------------------------------------------------------
# 1️⃣ intersection(llA, llB) → returns intersecting node if exists
# ---------------------------------------------------------------
def intersection(llA: LinkedList, llB: LinkedList):
    """
    Purpose:
    Find the intersection node (by reference) of two linked lists.

    ⏱️ Time Complexity: O(A + B) → traverse both lists once
    💾 Space Complexity: O(1)   → no extra space required

    Example:
    A: 3 -> 1 -> 5 -> 7 -> 11 -> 14
    B:     9 -> 2 -> 7 -> 11 -> 14
    Intersection = node with value 7
    """

    if not llA.head or not llB.head:
        return False

    # Step 1: If tails are different → no intersection
    if llA.tail is not llB.tail:
        return False

    # Step 2: Compute lengths
    lenA = len(llA)
    lenB = len(llB)

    # Step 3: Identify longer & shorter
    shorter = llA if lenA < lenB else llB
    longer = llB if lenA < lenB else llA

    # Step 4: Advance longer pointer by difference
    diff = abs(lenA - lenB)
    longerNode = longer.head
    shorterNode = shorter.head

    for _ in range(diff):
        longerNode = longerNode.next

    # Step 5: Traverse both simultaneously until they meet
    while shorterNode is not longerNode:
        shorterNode = shorterNode.next
        longerNode = longerNode.next

    return longerNode


# ---------------------------------------------------------------
# Helper: addSameNode → attach SAME node to both lists (intersection)
# ---------------------------------------------------------------
def addSameNode(llA: LinkedList, llB: LinkedList, value):
    """
    Create a new Node(value) and attach it to both list tails,
    making them intersect at this node.
    """
    tempNode = Node(value)

    if llA.tail:
        llA.tail.next = tempNode
        llA.tail = tempNode
    else:
        llA.head = llA.tail = tempNode

    if llB.tail:
        llB.tail.next = tempNode
        llB.tail = tempNode
    else:
        llB.head = llB.tail = tempNode


# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
# A: 3 -> 1 -> 5 -> 7 -> 11 -> 14
# B:     9 -> 2 -> 7 -> 11 -> 14
#
# len(A) = 6, len(B) = 5
# diff = 1 → advance A by 1
#
# Iteration Trace Table 👇
#
# Step | longer(A) | shorter(B) | Same? | Action
# -----|-----------|------------|-------|----------------
# 1    | 1         | 9          |  No   | move both
# 2    | 5         | 2          |  No   | move both
# 3    | 7         | 7          | Yes   | ✅ Intersection
#
# Result → Node with value 7


# ---------------------------------------------------------------
# 📘 Visual Example
# ---------------------------------------------------------------
# Before:
# A: [3] -> [1] -> [5] -> [7] -> [11] -> [14]
# B:     [9] -> [2] -/
#
# After aligning & traversing:
# Intersection found at node [7] → lists overlap from here till the end.


# ---------------------------------------------------------------
# 📝 Detailed Example Walkthrough
# ---------------------------------------------------------------
"""
Example Walkthrough:

Input:
  List A = 3 → 1 → 5 → 7 → 11 → 14
  List B = 9 → 2 → 7 → 11 → 14

Step 1: Compare tails
  Tail(A) = 14, Tail(B) = 14 → same reference → ✅ possible intersection

Step 2: Lengths
  len(A) = 6
  len(B) = 5
  diff = 1

Step 3: Advance longer list (A) by 1 node
  Now pointers:
    longer(A) = 1
    shorter(B) = 9

Step 4: Traverse simultaneously
  Iteration 1: A=1, B=9 → not same → move both
  Iteration 2: A=5, B=2 → not same → move both
  Iteration 3: A=7, B=7 → ✅ same node → intersection found

Step 5: Return
  Intersection node = 7

Final Answer:
  Both lists intersect starting from node with value 7.
"""


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Create two lists
    llA = LinkedList()
    for v in [3, 1, 5]:
        llA.append(v)

    llB = LinkedList()
    for v in [9, 2]:
        llB.append(v)

    # Add same nodes to both (creates intersection)
    addSameNode(llA, llB, 7)
    addSameNode(llA, llB, 11)
    addSameNode(llA, llB, 14)

    print("List A:", llA)   # 3 -> 1 -> 5 -> 7 -> 11 -> 14
    print("List B:", llB)   # 9 -> 2 -> 7 -> 11 -> 14

    result = intersection(llA, llB)
    if result:
        print("✅ Intersection at node:", result, "with value:", result.value)
    else:
        print("❌ No intersection found.")
