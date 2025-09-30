# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topics: Append | Prepend | get_node | insert | insert_direct | __str__
# ------------------------------------------------------

# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # backward pointer for doubly linked

    def __str__(self):
        return str(self.value)


# 🔷 Circular Doubly Linked List (CDLL)
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0   # initially empty list has 0 length

    # ---------------------------------------------------------------
    # 1️⃣ Append() → Insert node at the end
    # ---------------------------------------------------------------
    def append(self, value):
        new_node = Node(value)
        # Case 1: Empty CDLL
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Case 2: Non-Empty CDLL
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        self.length += 1

    # ---------------------------------------------------------------
    # 2️⃣ Prepend() → Insert node at the beginning
    # (kept short here; same logic used by insert when index == 0)
    # ---------------------------------------------------------------
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
        self.length += 1

    # ---------------------------------------------------------------
    # 3️⃣ __str__() → String Representation
    # ---------------------------------------------------------------
    def __str__(self):
        if self.head is None:
            return "Empty CDLL"
        result = []
        current_node = self.head
        while True:
            result.append(str(current_node.value))
            current_node = current_node.next
            if current_node == self.head:
                break
        return " ◀——▶ ".join(result)

    # ---------------------------------------------------------------
    # 4️⃣ get_node(index) → Get node by index (helper)
    # Optimized: start from head or tail depending on index position
    # ---------------------------------------------------------------
    def get_node(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev
        return current_node

    # ---------------------------------------------------------------
    # 5️⃣ insert(index, value) → insert node at given index (uses helper)
    # ---------------------------------------------------------------
    def insert(self, index, value):
        """
        Purpose:
        Insert a new node at position `index` (0-based).

        Steps:
        1. Validate index: must be in [0, length]. If invalid → return "Index out of Bound".
        2. If index == 0 → call prepend(value).
        3. If index == length → call append(value).
        4. Else:
           - Locate previous node using get_node(index - 1).
           - new_node.next = prev.next
           - new_node.prev = prev
           - prev.next.prev = new_node
           - prev.next = new_node
           - length += 1
        5. Return None (or nothing) on success (keeps behavior consistent with original).
        
        🔍 Visualization:
        Before (length=4): [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40]
        insert(2, 99):
         - prev = node at index 1 (20)
         - new_node(99) inserted between 20 and 30
        After: [10] ◀──▶ [20] ◀──▶ [99] ◀──▶ [30] ◀──▶ [40]

        ⏱️ Time: O(n) (but optimized traversal via get_node)
        ⏱️ Space: O(1)
        """
        if index < 0 or index > self.length:
            return "Index out of Bound"
        if index == 0:
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return

        new_node = Node(value)
        temp_node = self.get_node(index - 1)   # guaranteed not None here
        # link new_node
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1

    # ---------------------------------------------------------------
    # 6️⃣ insert_direct(index, value) → insert without using helper
    # Handle all cases explicitly (empty, head, tail, middle)
    # ---------------------------------------------------------------
    def insert_direct(self, index, value):
        """
        Purpose:
        Insert a new node at `index` without calling helper methods.

        Steps & Cases:
        1. If index invalid (index < 0 or index > length) → return "Index out of Bound".
        2. If list empty (length == 0):
             - create node, set head = tail = node, node.next = node.prev = node
             - length += 1, return "Inserted Successfully"
        3. If index == 0 (insert at start):
             - new_node.next = head
             - new_node.prev = tail
             - head.prev = new_node
             - tail.next = new_node
             - head = new_node
             - length += 1, return "Inserted Successfully"
        4. If index == length (insert at end):
             - new_node.prev = tail
             - new_node.next = head
             - tail.next = new_node
             - head.prev = new_node
             - tail = new_node
             - length += 1, return "Inserted Successfully"
        5. Else (middle insertion):
             - Walk from head index-1 steps to find temp_node
             - Insert new_node after temp_node (same linking as in insert)
             - length += 1, return "Inserted Successfully"

        🔍 Visualization (middle insert):
        Before: [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40]
        insert_direct(2, 99):
         - walk temp_node -> 20
         - link 99 between 20 and 30
        After: [10] ◀──▶ [20] ◀──▶ [99] ◀──▶ [30] ◀──▶ [40]

        ⏱️ Time: O(n) (worst-case)
        ⏱️ Space: O(1)
        """
        new_node = Node(value)

        # case 1 : Invalid Index
        if index < 0 or index > self.length:
            return "Index out of Bound"

        # case 2 : empty list
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
            self.length += 1
            return "Inserted Successfully"

        # case 3 : Insert at start (head)
        if index == 0:
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node
            self.length += 1
            return "Inserted Successfully"

        # case 4 : Insert at end (tail)
        if index == self.length:
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node
            self.length += 1
            return "Inserted Successfully"

        # case 5 : middle insertion
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        # insert after temp_node
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        return "Inserted Successfully"


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    CDLL = CircularDoublyLinkedList()
    CDLL.append(10)
    CDLL.append(20)
    CDLL.append(30)
    CDLL.append(40)
    CDLL.append(50)
    print("before insert :", CDLL)                   # 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    CDLL.insert(0, 100)
    print("After insert 100 at index 0:", CDLL)     # 100 ◀——▶ 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    CDLL.insert(3, 110)
    print("After insert 110 at index 3:", CDLL)     # ... 20 ◀——▶ 30 ◀——▶ 110 ◀——▶ 40 ...

    print("Try out-of-bound insert:", CDLL.insert(8, 120))  # "Index out of Bound"

    print("After insert 200 at index 10 (invalid):", CDLL.insert(10, 200))  # "Index out of Bound"

    CDLL.insert_direct(7, 500)
    print("After insert 500 at index 7:", CDLL)
    # depending on current length this will insert and print final list
