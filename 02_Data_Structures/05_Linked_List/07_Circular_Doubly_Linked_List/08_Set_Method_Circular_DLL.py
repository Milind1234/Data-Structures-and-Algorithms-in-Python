# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: Set Value (update node by index)
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
    # 3️⃣ get_node(index) → Get node by index
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
    # 4️⃣ set_value(index, value) → update using helper (get_node)
    # ---------------------------------------------------------------
    def set_value(self, index, value):
        """
        Purpose:
        Update the value of a node at a given index (0-based).
        Uses the helper method get_node() to locate the node.

        Steps:
        1. Call get_node(index) → returns node if valid index, else None.
        2. If node exists:
             - Replace node.value with new value.
             - Return True (successful update).
        3. Else:
             - Return False (invalid index).

        🔍 Visualization:

        Before:
        [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40]

        set_value(2, 100):
        → get_node(2) = node with value 30
        → update 30 → 100

        After:
        [10] ◀──▶ [20] ◀──▶ [100] ◀──▶ [40]

        ⏱️ Time Complexity:
        - get_node(): O(n/2) → O(n)
        - update: O(1)
        → Overall: O(n)

        ⏱️ Space Complexity:
        - O(1)
        """
        node = self.get_node(index)
        if node:
            node.value = value
            return True
        return False

    # -----------------------------------------------------------------------
    # 5️⃣ set_value_direct(index, value) → update without helper
    # -----------------------------------------------------------------------
    def set_value_direct(self, index, value):
        """
        Purpose:
        Update the value of a node at a given index (0-based),
        without calling get_node (direct traversal).

        Steps:
        1. If index invalid (<0 or >= length) → return False.
        2. If index is in the **first half**:
             - Start at head, move forward index times.
        3. Else (index in second half):
             - Start at tail, move backward until index is reached.
        4. Update node.value = new value.
        5. Return True.

        🔍 Visualization:

        Before:
        [10] ◀──▶ [20] ◀──▶ [100] ◀──▶ [40]

        set_value_direct(3, 200):
        → Start from tail = 40 (index=3)
        → Directly update value 40 → 200

        After:
        [10] ◀──▶ [20] ◀──▶ [100] ◀──▶ [200]

        ⏱️ Time Complexity:
        - Traversal: O(n/2) → O(n)
        - Update: O(1)
        → Overall: O(n)

        ⏱️ Space Complexity:
        - O(1)
        """
        if index < 0 or index >= self.length:
            return False

        if index < self.length // 2:
            temp_node = self.head
            for _ in range(index):
                temp_node = temp_node.next
        else:
            temp_node = self.tail
            for _ in range(self.length - 1, index, -1):
                temp_node = temp_node.prev
        temp_node.value = value
        return True


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
if __name__ == "__main__":
    CDLL = CircularDoublyLinkedList()
    CDLL.append(10)
    CDLL.append(20)
    CDLL.append(30)
    CDLL.append(40)

    print("Before:", CDLL)  
    # Output: 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40

    # Using helper-based set_value
    success = CDLL.set_value(2, 100)  
    print("set_value returned:", success)  
    # Output: True
    print("After set_value:", CDLL)  
    # Output: 10 ◀——▶ 20 ◀——▶ 100 ◀——▶ 40

    # Using direct set_value (no helper)
    success2 = CDLL.set_value_direct(3, 200)  
    print("set_value_direct returned:", success2)  
    # Output: True
    print("After set_value_direct:", CDLL)  
    # Output: 10 ◀——▶ 20 ◀——▶ 100 ◀——▶ 200

# _______________________________________________________________________________________________________________________
# 📘 Visual Example — set_value(index, value) & set_value_direct(index, value)
#
# Purpose:
# Update the `value` stored in the node at a given index.
# Two implementations:
# - set_value uses helper get_node(index) (reuses optimized traversal)
# - set_value_direct performs traversal inside the function (no helper call)
#
# Behavior cases covered:
# - invalid index
# - set at head (index 0)
# - set at tail (index = length-1)
# - set in middle
# _______________________________________________________________________________________________________________________

# Case: Invalid Index
# -------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head              ↑tail
#
# set_value(5, 100)  or set_value_direct(5, 100)
# - index 5 >= length (3) → return False / "Index out of range" (depending on API)
#
# _______________________________________________________________________________________________________________________

# Case: Set Head (index 0)
# ------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head              ↑tail
#
# set_value(0, 100):
# - get_node(0) returns head ([10])
# - head.value = 100
#
# After:
# [100] ◀——▶ [20] ◀——▶ [30]
#  ↑head              ↑tail
#
# Using set_value_direct(0, 100) does the same but traverses inside the function.
#
# _______________________________________________________________________________________________________________________

# Case: Set Tail (index = length - 1)
# -----------------------------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30]
#  ↑head              ↑tail
#
# set_value(2, 999):
# - get_node(2) optimized to return tail ([30])
# - tail.value = 999
#
# After:
# [10] ◀——▶ [20] ◀——▶ [999]
#  ↑head              ↑tail
#
# _______________________________________________________________________________________________________________________

# Case: Set Middle
# ----------------
# Before:
# [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]
#  ↑head                         ↑tail
#
# set_value(2, 333):
# - get_node(2) returns node [30]
# - update value 30 → 333
#
# After:
# [10] ◀——▶ [20] ◀——▶ [333] ◀——▶ [40]
#  ↑head                         ↑tail
#
# set_value_direct(2, 333) behaves the same but uses direct traversal.
#
# _______________________________________________________________________________________________________________________
# Pointer changes: NONE — only node.value is changed; next/prev pointers unchanged.
#
# Complexity:
# - Time: O(n) (helper-based uses get_node so O(n) worst-case)
# - Space: O(1)
# _______________________________________________________________________________________________________________________
