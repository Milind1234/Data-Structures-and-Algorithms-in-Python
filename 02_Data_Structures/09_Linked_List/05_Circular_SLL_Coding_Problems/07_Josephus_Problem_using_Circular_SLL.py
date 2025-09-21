"""
note_josephus_circle.py - Josephus Problem using Circular Singly Linked List (CSLL)

📌 Question:
Implement the Josephus Problem using a Circular Singly Linked List. 
Given n people standing in a circle and a step size k, eliminate every k-th person 
until only one person remains. Return the position of the last person.

---

📖 Explanation:
The Josephus problem is a classic elimination puzzle:
1. People are arranged in a circle.
2. Starting from head, count step (k) people.
3. Eliminate the k-th person.
4. Continue counting from the next person after the eliminated one.
5. Repeat until only one person remains.

We can simulate this using a Circular Singly Linked List (CSLL):
- Each node represents a person.
- The circle is maintained by keeping tail.next = head.
- By moving step-1 nodes forward, the node after that will be eliminated.

---

Step-by-step logic for `josephus_circle`:
------------------------------------------
1) **Initialize:**
   - Find number of nodes using `count_nodes()`.
   - Find the tail (node just before head).
   - Start with `temp = tail`.

2) **Loop until one remains (n > 1):**
   - Move `(step-1)` times: `temp = temp.next` in a loop.
   - Now `temp.next` is the node to remove (the k-th person).
   - Delete it (either manually unlink or via helper).
   - If the removed node was `head`, update `head = head.next`.
   - Decrease node count `n -= 1`.

3) **End condition:**
   - When `n == 1`, only one node is left.
   - That node is the last person standing.
   - Return its value.

---

🧮 Complexity:
- Time: O(n * step) in worst case (each elimination requires up to `step` moves).
- Space: O(1) extra (no additional data structures).

---
"""

# ============================================================
# Node
# ============================================================
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def __str__(self):
        return str(self.data)


# ============================================================
# Circular Singly Linked List (CSLL)
# ============================================================
class CircularLinkedList:
    def __init__(self):
        self.head = None

    def append(self, data):
        if not self.head:
            self.head = Node(data)
            self.head.next = self.head
        else:
            new_node = Node(data)
            temp = self.head
            while temp.next != self.head:
                temp = temp.next
            temp.next = new_node
            new_node.next = self.head

    def count_nodes(self):
        """Return number of nodes in CSLL."""
        if not self.head:
            return 0
        count = 1
        temp = self.head
        while temp.next != self.head:
            count += 1
            temp = temp.next
        return count

    # ---------------------------------------------------------
    # Helper delete_node (used in version 2)
    # ---------------------------------------------------------
    def delete_node(self, key):
        """Delete a node by value (if exists)."""
        if not self.head:
            return

        # Case 1: head matches
        if self.head.data == key:
            cur = self.head
            while cur.next != self.head:
                cur = cur.next
            if self.head == self.head.next:  # single node
                self.head = None
            else:
                cur.next = self.head.next
                self.head = cur.next
            return

        # Case 2: non-head node
        cur = self.head
        prev = None
        while cur.next != self.head:
            prev = cur
            cur = cur.next
            if cur.data == key:
                prev.next = cur.next
                return

    # ---------------------------------------------------------
    # Version 1: Direct pointer manipulation
    # ---------------------------------------------------------
    def josephus_circle_direct(self, step):
        """
        Solve Josephus problem using direct unlinking.
        """
        if not self.head:
            return "List is empty"
        if step <= 0:
            raise ValueError("step must be a positive integer")

        n = self.count_nodes()
        temp = self.head
        while temp.next != self.head:
            temp = temp.next  # find tail

        while n > 1:
            for _ in range((step - 1) % n):
                temp = temp.next

            to_remove = temp.next
            temp.next = to_remove.next

            if to_remove == self.head:
                self.head = to_remove.next

            n -= 1

        self.head = temp.next
        return f"Last person left standing: {temp.data}"

    # ---------------------------------------------------------
    # Version 2: Using delete_node() helper
    # ---------------------------------------------------------
    def josephus_circle_with_helper(self, step):
        """
        Solve Josephus problem but use delete_node() for removals.
        """
        if not self.head:
            return "List is empty"
        if step <= 0:
            raise ValueError("step must be a positive integer")

        n = self.count_nodes()
        temp = self.head
        while temp.next != self.head:
            temp = temp.next  # find tail

        while n > 1:
            for _ in range((step - 1) % n):
                temp = temp.next

            to_remove = temp.next
            self.delete_node(to_remove.data)
            temp = temp.next
            n -= 1

        return f"Last person left standing: {self.head.data}"


# ============================================================
# ▶️ Dry-run Examples
# ============================================================
"""
Example 1:
Input: n=5, step=2
List: 1 -> 2 -> 3 -> 4 -> 5 -> (back to head)

- Start at tail=5
- Move 1 step -> eliminate 1
- Remaining: [2,3,4,5]
- Next temp points to 2

- Move 1 step -> eliminate 3
- Remaining: [2,4,5]
- Next temp points to 4

- Move 1 step -> eliminate 5
- Remaining: [2,4]
- Next temp points to 2

- Move 1 step -> eliminate 2
- Remaining: [4]
Answer: 4

Output: "Last person left standing: 4"

---

Example 2:
Input: n=7, step=3
Elimination order: 3,6,2,7,5,1
Last standing: 4
"""
