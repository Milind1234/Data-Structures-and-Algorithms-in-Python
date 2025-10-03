# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: Search by Value | Search by Node (Index)
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
    # 2️⃣ __str__() → String Representation
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
    # 3️⃣ search_by_val(target) → search by value
    # ---------------------------------------------------------------
    # _______________________________________________________________________________________________________________________
    # 📘 Visual Example — search_by_val(target)
    #
    # Purpose:
    # Find the index (0-based) of the first node with value == target.
    #
    # Behavior:
    # - Traverse forward from head, compare each node value.
    # - Stop and return index on match.
    # - If full circle completed without match, return "Targeted Value Not Found".
    # _______________________________________________________________________________________________________________________

    # Case: Search when list is empty
    # ------------------------------
    # Before:
    # None
    #
    # search_by_val(10) -> "List is empty" or "Targeted Value Not Found"
    #
    # _______________________________________________________________________________________________________________________

    # Case: Search value present
    # --------------------------
    # CDLL = [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]
    # search_by_val(30):
    # Step 1: Compare 10 (idx 0) → no
    # Step 2: Compare 20 (idx 1) → no
    # Step 3: Compare 30 (idx 2) → yes → return 2
    #
    # _______________________________________________________________________________________________________________________

    # Case: Search value absent
    # -------------------------
    # CDLL = [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]
    # search_by_val(99):
    # Compare 10, 20, 30, 40 → full circle → return "Targeted Value Not Found"
    #
    # Complexity:
    # - Time: O(n)
    # - Space: O(1)
    # _______________________________________________________________________________________________________________________

    
    def search_by_val(self, target):
        """
        Purpose:
        Find the index (0-based) of the first node containing `target`.

        Steps:
        1. Check if list is empty → return "List is empty".
        2. Start from head and set index = 0.
        3. Traverse the list node by node:
             - If current_node.value == target → return index.
             - Else move to current_node.next and increase index.
        4. Stop when you return back to head (full circle completed).
        5. If not found, return "Targeted Value Not Found".

        🔍 Visualization:

        CDLL = [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40]

        search_by_val(20):
        Step 1: Compare 10 (index 0) ❌
        Step 2: Compare 20 (index 1) ✅ → return 1

        search_by_val(99):
        Step 1: Compare 10 (index 0)
        Step 2: Compare 20 (index 1)
        Step 3: Compare 30 (index 2)
        Step 4: Compare 40 (index 3)
        Full circle → return "Targeted Value Not Found"

        ⏱️ Time: O(n) → checks each node once
        ⏱️ Space: O(1) → constant space
        """
        if self.length == 0:
            return "List is empty"
        current_node = self.head
        index = 0
        while current_node:
            if current_node.value == target:
                return index
            current_node = current_node.next
            index += 1
            if current_node == self.head:
                break
        return "Targeted Value Not Found"

    # ---------------------------------------------------------------
    # 4️⃣ search_by_node(node_no) → search by index
    # ---------------------------------------------------------------
    
    # _______________________________________________________________________________________________________________________
    # 📘 Visual Example — search_by_node(node_no)
    #
    # Purpose:
    # Return the value at index node_no (0-based).
    #
    # Behavior:
    # - If list empty → "List is empty"
    # - If index invalid (<0 or >= length) → "Index out of range"
    # - Otherwise traverse (optimized: from head or tail depending on index)
    # _______________________________________________________________________________________________________________________

    # Case: Index out of range
    # ------------------------
    # CDLL = [10] ◀——▶ [20] ◀——▶ [30]
    # get index 5 -> "Index out of range"
    #
    # _______________________________________________________________________________________________________________________

    # Case: Get head (index 0)
    # ------------------------
    # CDLL = [10] ◀——▶ [20] ◀——▶ [30]
    # search_by_node(0) -> returns 10
    #
    # _______________________________________________________________________________________________________________________

    # Case: Get tail (index length-1)
    # -------------------------------
    # CDLL = [10] ◀——▶ [20] ◀——▶ [30]
    # search_by_node(2) -> returns 30
    #
    # _______________________________________________________________________________________________________________________

    # Case: Get middle (use optimized direction)
    # ------------------------------------------
    # CDLL = [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40] ◀——▶ [50]
    # search_by_node(3):
    # - index 3 >= length//2 (5//2=2) → start from tail
    # - tail (50) → prev → 40 → return 40
    #
    # Complexity:
    # - Time: O(k) up to O(n) worst-case (optimized average O(n/2))
    # - Space: O(1)
    # _______________________________________________________________________________________________________________________


    def search_by_node(self, node_no):
        """
        Purpose:
        Return the value stored at the given node index (0-based).

        Steps:
        1. Check if list is empty → return "List is empty".
        2. If node_no < 0 or node_no >= length → return "Index out of range".
        3. Start from head, set count = 0.
        4. Traverse forward until count == node_no.
        5. Return the value of that node.

        🔍 Visualization:

        CDLL = [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40]

        search_by_node(2):
        Step 1: Start at head = 10 (count=0)
        Step 2: Move to 20 (count=1)
        Step 3: Move to 30 (count=2) → return 30

        search_by_node(6):
        Step 1: Index out of range → return "Index out of range"

        ⏱️ Time: O(k) → proportional to index searched (worst O(n))
        ⏱️ Space: O(1)
        """
        if self.length == 0:
            return "List is empty"
        if node_no < 0 or node_no >= self.length:
            return "Index out of range"

        current_node = self.head
        count = 0
        while count < node_no:
            current_node = current_node.next
            count += 1
        return current_node.value


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    CDLL = CircularDoublyLinkedList()
    CDLL.append(10)
    CDLL.append(20)
    CDLL.append(30)
    CDLL.append(40)

    print("CDLL:", CDLL)
    # Output: 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40

    # --- search_by_val ---
    print("Search 20:", CDLL.search_by_val(20))
    # Output: 1

    print("Search 99:", CDLL.search_by_val(99))
    # Output: Targeted Value Not Found

    # --- search_by_node ---
    print("Node at index 2:", CDLL.search_by_node(2))
    # Output: 30

    print("Node at index 6:", CDLL.search_by_node(6))
    # Output: Index out of range
