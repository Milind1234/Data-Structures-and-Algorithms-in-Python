# note.py
# ------------------------------------------------------
# 📘 Linked List - Notes File
# ✅ Topic: Partition a Linked List Around Value x
# ------------------------------------------------------

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
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def __str__(self):
        vals = []
        cur = self.head
        while cur:
            vals.append(str(cur.value))
            cur = cur.next
        return " -> ".join(vals) if vals else "Empty"

    # ---------------------------------------------------------------
    # 1️⃣ partition(x) → Rearrange list so nodes < x come before >= x
    # ---------------------------------------------------------------
    def partition(self, x):
        """
        Rearranges nodes into two lists:
        - before: nodes with value < x
        - after:  nodes with value >= x
        Then merges them.

        Steps:
        1. Traverse original list with `current`.
        2. For each node, detach it (`current.next = None`) to avoid stale links.
        3. Add node to before list (< x) or after list (>= x).
        4. Finally, merge before and after.
        """
        if self.head is None:
            return self

        before_head = before_tail = None
        after_head = after_tail = None
        current = self.head

        while current:
            next_node = current.next
            current.next = None  # detach to avoid stale links

            if current.value < x:
                if before_head is None:
                    before_head = before_tail = current
                else:
                    before_tail.next = current
                    before_tail = current
            else:
                if after_head is None:
                    after_head = after_tail = current
                else:
                    after_tail.next = current
                    after_tail = current

            current = next_node

        # Merge before + after
        if before_head is None:
            self.head = after_head
            self.tail = after_tail
        else:
            before_tail.next = after_head
            self.head = before_head
            self.tail = after_tail if after_tail else before_tail

        return self


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    ll = LinkedList()
    for v in [3, 5, 8, 5, 10, 2, 1]:
        ll.append(v)

    print("Before partition(5):", ll)
    ll.partition(5)
    print("After partition(5):", ll)
    # Expected: 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10



# ---------------------------------------------------------------
# 📊 Complexity Analysis
# ---------------------------------------------------------------
# Time Complexity:
# - O(n) → one pass over all nodes
#
# Space Complexity:
# - O(1) → uses only a few extra pointers (no extra data structures)
#
# ---------------------------------------------------------------
# 📘 Visual Example
# ---------------------------------------------------------------
# Input:   3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1   (x = 5)
#
# Step 1: Partition into two lists:
#   before: 3 -> 2 -> 1
#   after:  5 -> 8 -> 5 -> 10
#
# Step 2: Merge them:
#   before + after = 3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10
#
# Final Output:
#   3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10
#
# ✅ Nodes less than 5 appear first, order preserved.
# ✅ Nodes greater or equal to 5 appear later, order preserved.

# ---------------------------------------------------------------
# 📖 Iteration-wise Dry Run (partition(5))
# ---------------------------------------------------------------
"""
Input:
    3 -> 5 -> 8 -> 5 -> 10 -> 2 -> 1
    x = 5

🌀 Initial State:
    before_head = None
    before_tail = None
    after_head  = None
    after_tail  = None
    current = 3

🔹 Iteration 1: current = 3
    next_node = 5
    current.next = None  # Detach 3
    3 < 5 → goes to BEFORE list
    before_head = 3, before_tail = 3
    current = 5
    Lists → before: 3 | after: –

🔹 Iteration 2: current = 5
    next_node = 8
    current.next = None
    5 >= 5 → goes to AFTER list
    after_head = 5, after_tail = 5
    current = 8
    Lists → before: 3 | after: 5

🔹 Iteration 3: current = 8
    next_node = 5
    current.next = None
    8 >= 5 → goes to AFTER list
    after_tail.next = 8, after_tail = 8
    current = 5
    Lists → before: 3 | after: 5 -> 8

🔹 Iteration 4: current = 5
    next_node = 10
    current.next = None
    5 >= 5 → goes to AFTER list
    after_tail.next = 5, after_tail = 5
    current = 10
    Lists → before: 3 | after: 5 -> 8 -> 5

🔹 Iteration 5: current = 10
    next_node = 2
    current.next = None
    10 >= 5 → goes to AFTER list
    after_tail.next = 10, after_tail = 10
    current = 2
    Lists → before: 3 | after: 5 -> 8 -> 5 -> 10

🔹 Iteration 6: current = 2
    next_node = 1
    current.next = None
    2 < 5 → goes to BEFORE list
    before_tail.next = 2, before_tail = 2
    current = 1
    Lists → before: 3 -> 2 | after: 5 -> 8 -> 5 -> 10

🔹 Iteration 7: current = 1
    next_node = None
    current.next = None
    1 < 5 → goes to BEFORE list
    before_tail.next = 1, before_tail = 1
    current = None (loop ends)
    Lists → before: 3 -> 2 -> 1 | after: 5 -> 8 -> 5 -> 10

🏁 Merge Step:
    before_tail.next = after_head
    head = before_head (3)
    tail = after_tail (10)

Final Output:
    3 -> 2 -> 1 -> 5 -> 8 -> 5 -> 10
"""
