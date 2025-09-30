# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Complete implementation: append | prepend | traverse |
#    reverse_traverse | __str__ | get | set_value | insert |
#    Pop_first | Pop_last | remove | delete_all
# ------------------------------------------------------

# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None    # Pointer to next node
        self.prev = None    # Pointer to previous node

    def __str__(self):
        return str(self.value)


# 🔷 Circular Doubly Linked List (CDLL) Structure
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None    # First node
        self.tail = None    # Last node
        self.length = 0     # Total number of nodes

    # ---------------------------------------------------------------
    # 1️⃣ append(value) → Insert node at the end
    # ---------------------------------------------------------------
    def append(self, value):
        """
        Purpose:
        Insert a new node at the end (tail) of the CDLL.

        Steps:
        1. Create new_node.
        2. If list empty:
             - head = tail = new_node
             - new_node.next = new_node.prev = new_node
        3. Else:
             - tail.next = new_node
             - new_node.prev = tail
             - new_node.next = head
             - head.prev = new_node
             - tail = new_node
        4. length += 1

        Time: O(1), Space: O(1)
        """
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            self.tail.next = new_node
            new_node.prev = self.tail
            new_node.next = self.head
            self.head.prev = new_node
            self.tail = new_node
        self.length += 1

    # ---------------------------------------------------------------
    # 2️⃣ prepend(value) → Insert node at the beginning (head)
    # ---------------------------------------------------------------
    def prepend(self, value):
        """
        Purpose:
        Insert a new node at the beginning (head) of the CDLL.

        Steps:
        1. Create new_node.
        2. If list empty:
             - head = tail = new_node; new_node points to itself
        3. Else:
             - new_node.next = head
             - new_node.prev = tail
             - head.prev = new_node
             - tail.next = new_node
             - head = new_node
        4. length += 1

        Time: O(1), Space: O(1)
        """
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
    # 3️⃣ traverse() → Print all node values (forward)
    # ---------------------------------------------------------------
    def traverse(self):
        """
        Purpose:
        Visit each node starting from head and print its value.

        Behavior:
        - If empty: prints nothing.
        - Otherwise prints values until we loop back to head.

        Time: O(n), Space: O(1)
        """
        current_node = self.head
        if current_node is None:
            return
        while True:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break

    # ---------------------------------------------------------------
    # 4️⃣ reverse_traverse() → Print all node values in reverse
    # ---------------------------------------------------------------
    def reverse_traverse(self):
        """
        Purpose:
        Visit each node starting from tail and print its value in reverse order.

        Time: O(n), Space: O(1)
        """
        current_node = self.tail
        if current_node is None:
            return
        while True:
            print(current_node.value)
            current_node = current_node.prev
            if current_node == self.tail:
                break

    # ---------------------------------------------------------------
    # 5️⃣ __str__() → String Representation
    # ---------------------------------------------------------------
    def __str__(self):
        """
        Return a readable string representation of the CDLL values from head.
        Example: "10 ◀——▶ 20 ◀——▶ 30"
        """
        if self.head is None:
            return "Empty CDLL"
        current_node = self.head
        parts = []
        while True:
            parts.append(str(current_node.value))
            current_node = current_node.next
            if current_node == self.head:
                break
        return " ◀——▶ ".join(parts)

    # ---------------------------------------------------------------
    # 6️⃣ get(index) → Get node object by index (helper)
    # ---------------------------------------------------------------
    def get(self, index):
        """
        Purpose:
        Return the Node object at 0-based `index`, or None if invalid.

        Optimization:
        - If index < length//2: walk from head forward.
        - Else: walk from tail backward.

        Time: O(n) worst-case, O(n/2) average; Space: O(1)
        """
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            current = self.head
            for _ in range(index):
                current = current.next
        else:
            current = self.tail
            for _ in range(self.length - 1, index, -1):
                current = current.prev
        return current

    # ---------------------------------------------------------------
    # 7️⃣ set_value(index, value) → update node's value using get()
    # ---------------------------------------------------------------
    def set_value(self, index, value):
        """
        Purpose:
        Update value at `index`. Returns True if updated else False.
        """
        node = self.get(index)
        if node:
            node.value = value
            return True
        return False

    # ---------------------------------------------------------------
    # 8️⃣ insert(index, value) → Insert node at given index (uses get())
    # ---------------------------------------------------------------
    def insert(self, index, value):
        """
        Purpose:
        Insert a new node at position `index` (0-based).

        Behavior:
        - index < 0 or index > length => "Index out of Bound"
        - index == 0 => prepend
        - index == length => append
        - otherwise insert in middle by locating previous node with get(index-1)

        Time: O(n) worst-case (get() optimized), Space: O(1)
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
        prev_node = self.get(index - 1)   # not None here
        new_node.next = prev_node.next
        new_node.prev = prev_node
        prev_node.next.prev = new_node
        prev_node.next = new_node
        self.length += 1

    # ---------------------------------------------------------------
    # 9️⃣ Pop_first() → Remove first node
    # ---------------------------------------------------------------
    def Pop_first(self):
        """
        Purpose:
        Remove and return the head node. If empty return None.
        """
        if self.length == 0:
            return None
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped.prev = None
            popped.next = None
            self.head.prev = self.tail
            self.tail.next = self.head
        self.length -= 1
        return popped

    # ---------------------------------------------------------------
    # 🔟 Pop_last() → Remove last node
    # ---------------------------------------------------------------
    def Pop_last(self):
        """
        Purpose:
        Remove and return the tail node. If empty return None.
        """
        if self.length == 0:
            return None
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.tail = self.tail.prev
            popped.prev = None
            popped.next = None
            self.tail.next = self.head
            self.head.prev = self.tail
        self.length -= 1
        return popped

    # ---------------------------------------------------------------
    # 1️⃣1️⃣ remove(index) → Remove node by index using get()
    # ---------------------------------------------------------------
    def remove(self, index):
        """
        Purpose:
        Remove and return node at `index` using the helper get().

        Steps:
        1. If invalid index -> return "Index out of Bound".
        2. If index == 0 -> Pop_first()
        3. If index == length-1 -> Pop_last()
        4. Else:
             - node = get(index)
             - unlink node: node.prev.next = node.next; node.next.prev = node.prev
             - isolate node and length -= 1
             - return node
        """
        if index < 0 or index >= self.length:
            return "Index out of Bound"
        if index == 0:
            return self.Pop_first()
        if index == self.length - 1:
            return self.Pop_last()

        node = self.get(index)
        node.prev.next = node.next
        node.next.prev = node.prev
        node.next = None
        node.prev = None
        self.length -= 1
        return node

    # ---------------------------------------------------------------
    # 1️⃣2️⃣ delete_all() → Remove all nodes
    # ---------------------------------------------------------------
    def delete_all(self):
        """
        Purpose:
        Clear the entire list by removing references to head and tail.
        Python's garbage collector will free nodes if no external refs exist.

        Steps:
        1. head = None
        2. tail = None
        3. length = 0
        4. return None

        Time: O(1), Space: O(1)
        """
        self.head = None
        self.tail = None
        self.length = 0
        return None


# ---------------------------------------------------------------
# ✅ Visual Examples (short) — paste into notes where helpful
# ---------------------------------------------------------------
# Append on Empty List:
# Before: None
# After append(10): [10]  (head & tail point to same node)
#
# Pop_first on Multi-Node:
# Before: [10] ◀——▶ [20] ◀——▶ [30]
# Pop_first() -> popped [10]
# After: [20] ◀——▶ [30]   (head updated, circular links preserved)
#
# Insert in Middle:
# Before: [10] ◀——▶ [20] ◀——▶ [30]
# insert(1, 99) -> [10] ◀——▶ [99] ◀——▶ [20] ◀——▶ [30]
#
# Remove tail:
# Before: [10] ◀——▶ [20] ◀——▶ [30]
# remove(2) -> popped [30]
# After: [10] ◀——▶ [20]

# ---------------------------------------------------------------
# ✅ How to Use & Quick Tests
# ---------------------------------------------------------------
if __name__ == "__main__":
    dll = CircularDoublyLinkedList()
    for v in [10, 20, 30, 40, 50]:
        dll.append(v)

    print("Start:", dll)                     # 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40 ◀——▶ 50

    # traverse (forward)
    print("\nTraverse forward:")
    dll.traverse()

    # reverse traverse
    print("\nTraverse reverse:")
    dll.reverse_traverse()

    # get and set
    node = dll.get(2)
    print("\nNode at index 2:", node)        # Node object str -> 30
    print("set_value(2, 300):", dll.set_value(2, 300))
    print("After set:", dll)

    # insert
    dll.insert(0, 5)
    print("\nAfter insert at 0:", dll)      # 5 at head
    dll.insert(len([1,2]) + 1, 999)  # harmless no-op style placeholder (keeps method available)
    dll.insert(3, 25)
    print("After insert at 3:", dll)

    # pops
    popped_first = dll.Pop_first()
    print("\nPopped first:", popped_first)
    print("After Pop_first:", dll)

    popped_last = dll.Pop_last()
    print("\nPopped last:", popped_last)
    print("After Pop_last:", dll)

    # remove using helper
    popped = dll.remove(1)
    print("\nRemoved index 1 (helper):", popped)
    print("After remove:", dll)

    # delete_all
    dll.delete_all()
    print("\nAfter delete_all:", dll)       # Empty CDLL

# ---------------------------------------------------------------
# 📊 Complexity Summary
# ---------------------------------------------------------------
# append/prepend/Pop_first/Pop_last/delete_all:
# - Time: O(1), Space: O(1)
#
# traverse / reverse_traverse / get / insert / remove / set_value:
# - Time: O(n) worst-case; get/insert/remove optimized average O(n/2) when using get()
# - Space: O(1)
# ---------------------------------------------------------------
