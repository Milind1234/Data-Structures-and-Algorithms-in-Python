# note.py
# ------------------------------------------------------
# 📘 Linked List - Notes File
# ✅ Topic: Remove Duplicates from a Linked List
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
        """Insert node at the end."""
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # ---------------------------------------------------------------
    # 1️⃣ remove_duplicates_sorted() → works only on sorted lists
    # ---------------------------------------------------------------
    def remove_duplicates_sorted(self):
        """
        Removes duplicates from a **sorted linked list**.
        Works only if duplicates are consecutive (adjacent).

        Steps:
        1. Start from head, keep `prev` and `current`.
        2. Compare values:
             - If equal → skip current (unlink node).
             - Else → advance both pointers.
        3. Continue until end of list.

        Example:
        Input:  1 -> 2 -> 2 -> 3 -> 4 -> 4 -> 5
        Output: 1 -> 2 -> 3 -> 4 -> 5

        ⏱️ Time: O(n) — single traversal
        💾 Space: O(1) — no extra memory

        📌 When to Use?
        - Use when the linked list is **sorted**.
        - This is the most efficient option for sorted data.
        - Fails on unsorted lists because duplicates may not be adjacent.
        """
        if self.head is None:
            return None

        prev = self.head
        current = prev.next

        while current:
            if prev.value == current.value:
                prev.next = current.next  # unlink duplicate
                current = prev.next
            else:
                prev = current
                current = current.next

        return self.head

    # ---------------------------------------------------------------
    # 2️⃣ remove_duplicates_unsorted() → uses set (buffer)
    # ---------------------------------------------------------------
    def remove_duplicates_unsorted(self):
        """
        Removes duplicates from an **unsorted linked list**.
        Uses a set to track seen values.

        Steps:
        1. Initialize an empty set `seen`.
        2. Traverse list:
             - If value in seen → unlink node.
             - Else → add value to set, move on.
        3. Update prev.next accordingly.

        Example:
        Input:  1 -> 3 -> 2 -> 3 -> 4 -> 1
        Output: 1 -> 3 -> 2 -> 4

        ⏱️ Time: O(n) — one traversal
        💾 Space: O(n) — set stores seen values

        📌 When to Use?
        - Best option for **unsorted lists** when extra memory is available.
        - Fastest way to remove duplicates (O(n)).
        - Not suitable if memory is strictly limited.
        """
        if self.head is None:
            return None

        seen = set()
        current = self.head
        prev = None

        while current:
            if current.value in seen:
                prev.next = current.next  # unlink duplicate
            else:
                seen.add(current.value)
                prev = current
            current = current.next

        return self.head

    # ---------------------------------------------------------------
    # 3️⃣ remove_duplicates_no_buffer() → no extra space
    # ---------------------------------------------------------------
    def remove_duplicates_no_buffer(self):
        """
        Removes duplicates from an unsorted linked list
        WITHOUT using extra space. Uses nested loops.

        Steps:
        1. Use `current` to traverse each node.
        2. For each node, use `runner` to scan future nodes.
        3. If runner.value == current.value → unlink runner.
        4. Else → move runner forward.
        5. Repeat for every current node.

        Example:
        Input:  1 -> 3 -> 2 -> 3 -> 4 -> 1
        Output: 1 -> 3 -> 2 -> 4

        ⏱️ Time: O(n²) — nested traversal
        💾 Space: O(1) — no extra buffer

        📌 When to Use?
        - Use when list is **unsorted** and **extra memory is NOT allowed**.
        - Example: in-memory constraints, interview "no extra space" problems.
        - Tradeoff: much slower (O(n²)) for large lists.
        """
        if self.head is None:
            return self

        current = self.head
        while current is not None:
            runner_prev = current
            runner = current.next
            while runner is not None:
                if runner.value == current.value:
                    runner_prev.next = runner.next  # unlink duplicate
                    runner = runner_prev.next
                else:
                    runner_prev = runner
                    runner = runner.next
            current = current.next

        return self


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    # Example 1: Sorted list duplicate removal
    ll1 = LinkedList()
    for val in [1, 2, 2, 3, 4, 4, 5]:
        ll1.append(val)
    print("Original (sorted):", ll1)
    ll1.remove_duplicates_sorted()
    print("After remove_duplicates_sorted:", ll1)
    print()

    # Example 2: Unsorted list duplicate removal with set
    ll2 = LinkedList()
    for val in [1, 3, 2, 3, 4, 1]:
        ll2.append(val)
    print("Original (unsorted):", ll2)
    ll2.remove_duplicates_unsorted()
    print("After remove_duplicates_unsorted:", ll2)
    print()

    # Example 3: Unsorted list duplicate removal without buffer
    ll3 = LinkedList()
    for val in [1, 3, 2, 3, 4, 1]:
        ll3.append(val)
    print("Original (unsorted):", ll3)
    ll3.remove_duplicates_no_buffer()
    print("After remove_duplicates_no_buffer:", ll3)
