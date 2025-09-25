# 📌 QUESTION:
# Implement "remove by index" in a Doubly Linked List (DLL) in two ways:
# 1️⃣ remove_element → with helper (uses get_value, pop_first, pop_last)
# 2️⃣ remove_element_direct → without helpers (handles everything manually)

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes (Remove by Index)
# ------------------------------------------------------

# ✅ Node class: creates a node with value, prev, next
class Node:
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None


# ✅ DLL Implementation
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # --------------------------------------------------
    # __str__ Method → for pretty printing
    # --------------------------------------------------
    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.value))
            temp = temp.next
        return " <-> ".join(result) if result else "Empty DLL"

    # --------------------------------------------------
    # Append → O(1)
    # --------------------------------------------------
    def append(self, value):
        new_node = Node(value)
        if self.head is None:             # empty DLL
            self.head = self.tail = new_node
        else:                             # non-empty DLL
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # --------------------------------------------------
    # Get Node by Index → O(n)
    # (used in helper version)
    # --------------------------------------------------
    def get_value(self, index):
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:      # closer to head
            current = self.head
            for _ in range(index):
                current = current.next
        else:                             # closer to tail
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        return current

    # --------------------------------------------------
    # pop_first & pop_last (support functions)
    # --------------------------------------------------
    def pop_first(self):
        if not self.head: return None
        popped = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = self.head.next
            self.head.prev = None
            popped.next = None
        self.length -= 1
        return popped.value

    def pop_last(self):
        if not self.head: return None
        popped = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = self.tail.prev
            self.tail.next = None
            popped.prev = None
        self.length -= 1
        return popped.value

    # --------------------------------------------------
    # 1️⃣ Remove by Index (with helper functions)
    # --------------------------------------------------
    """
    Steps:
    1. If index == 0 → use pop_first()
    2. If index == length-1 → use pop_last()
    3. Else:
         - find node using get_value(index)
         - unlink it from neighbors
    ⏱️ Time: O(n)
    ⏱️ Space: O(1)
    """
    def remove_element(self, index):
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()
        popped = self.get_value(index)
        popped.prev.next = popped.next
        popped.next.prev = popped.prev
        popped.prev = None
        popped.next = None
        self.length -= 1
        return popped.value

    # --------------------------------------------------
    # 2️⃣ Remove by Index (without helper functions)
    # --------------------------------------------------
    """
    Steps:
    1. Validate index
    2. If index == 0 → manually unlink head
    3. If index == length-1 → manually unlink tail
    4. Else:
         - traverse manually (from head/tail depending on index)
         - unlink the found node
    ⏱️ Time: O(n)
    ⏱️ Space: O(1)
    """
    def remove_element_direct(self, index):
        if index < 0 or index >= self.length:
            return None

        # Case 1: remove head
        if index == 0:
            popped = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                self.head = self.head.next
                self.head.prev = None
                popped.next = None
            self.length -= 1
            return popped.value

        # Case 2: remove tail
        if index == self.length - 1:
            popped = self.tail
            self.tail = self.tail.prev
            self.tail.next = None
            popped.prev = None
            self.length -= 1
            return popped.value

        # Case 3: middle node
        if index < self.length // 2:      # closer to head
            current = self.head
            for _ in range(index):
                current = current.next
        else:                             # closer to tail
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev

        current.prev.next = current.next
        current.next.prev = current.prev
        current.prev = None
        current.next = None
        self.length -= 1
        return current.value


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(10)
DLL.append(20)
DLL.append(30)
DLL.append(40)

print("Initial DLL:", DLL)                     # 10 <-> 20 <-> 30 <-> 40
print("Removed (helper):", DLL.remove_element(0))       # removes 10
print("Removed (direct):", DLL.remove_element_direct(1))# removes 30
print("DLL after removals:", DLL)              # 20 <-> 40
print("Length:", DLL.length)                   # 2


# ------------------------------------------------------
# 📊 Visualizations
# ------------------------------------------------------
# Initial:
# None <- [10] <-> [20] <-> [30] <-> [40] -> None
# index:   0        1        2        3

# Case 1: remove index=0 (head)
# None <- [20] <-> [30] <-> [40] -> None

# Case 2: remove index=3 (tail)
# None <- [10] <-> [20] <-> [30] -> None

# Case 3: remove index=2 (middle, node=30)
# None <- [10] <-> [20] <-> [40] -> None
