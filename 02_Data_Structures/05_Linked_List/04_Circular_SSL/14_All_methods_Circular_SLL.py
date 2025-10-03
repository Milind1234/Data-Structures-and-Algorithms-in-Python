"""
📌 Circular Singly Linked List - Full Notes + Implementation (note.py)

Each method includes:
- Steps / Idea
- ASCII example
- Time & Space complexity
- Implementation

Circular property: tail.next always points to head (when list is non-empty).
"""

# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)


# ---------------- CIRCULAR SINGLY LINKED LIST CLASS ----------------
class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # =======================================================
    # APPEND (add to tail)
    # =======================================================
    """
    Steps:
    1. Create new node
    2. If list empty:
         - head = tail = new_node
         - new_node.next = new_node (self-loop)
    3. Else:
         - tail.next = new_node
         - new_node.next = head
         - tail = new_node
    4. length += 1

    ASCII:
    Before: 10 --> 20 (tail.next -> head)
    append(30)
    After:  10 --> 20 --> 30  (tail.next -> head)

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            self.tail.next = new_node
            new_node.next = self.head
            self.tail = new_node
        self.length += 1
        return "Appended Successfully"

    # =======================================================
    # PREPEND (add to head)
    # =======================================================
    """
    Steps:
    1. Create new node
    2. If list empty:
         - head = tail = new_node
         - new_node.next = new_node
    3. Else:
         - new_node.next = head
         - head = new_node
         - tail.next = head (maintain circular)
    4. length += 1

    ASCII:
    Before: 10 --> 20 --> 30
    prepend(5)
    After:  5 --> 10 --> 20 --> 30

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
        else:
            new_node.next = self.head
            self.head = new_node
            self.tail.next = self.head
        self.length += 1
        return "Prepended Successfully"

    # =======================================================
    # INSERT (at index)
    # =======================================================
    """
    Steps:
    1. If index < 0 or index > length -> IndexError
    2. If index == 0 -> prepend
    3. If index == length -> append
    4. Else:
         - traverse to index-1
         - new_node.next = prev.next
         - prev.next = new_node
    5. length += 1

    ASCII:
    Before: 10 --> 30 --> 40
    insert(1, 20)
    After:  10 --> 20 --> 30 --> 40

    Time Complexity: O(n) (worst-case traverse)
    Space Complexity: O(1)
    """
    def insert(self, index, value):
        if index < 0 or index > self.length:
            raise IndexError("Index out of range")
        if index == 0:
            return self.prepend(value)
        if index == self.length:
            return self.append(value)
        new_node = Node(value)
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        new_node.next = prev.next
        prev.next = new_node
        self.length += 1
        return "Inserted Successfully"

    # =======================================================
    # POP_FIRST (remove head)
    # =======================================================
    """
    Steps:
    1. If length == 0: return None
    2. popped = head
    3. If length == 1: head = tail = None
    4. Else: head = head.next; tail.next = head
    5. popped.next = None; length -= 1; return popped

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def pop_first(self):
        if self.length == 0:
            return None
        popped = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            self.tail.next = self.head
            popped.next = None
        self.length -= 1
        return popped

    # =======================================================
    # POP_LAST (remove tail)
    # =======================================================
    """
    Steps:
    1. If length == 0: return None
    2. If length == 1: popped=head; head=tail=None
    3. Else:
         - traverse to node before tail (prev)
         - prev.next = head
         - tail = prev
         - popped.next = None
    4. length -= 1; return popped

    Time Complexity: O(n) (traverse to find prev)
    Space Complexity: O(1)
    """
    def pop_last(self):
        if self.length == 0:
            return None
        popped = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            prev.next = self.head
            self.tail = prev
            popped.next = None
        self.length -= 1
        return popped

    # =======================================================
    # GET (node by index)
    # =======================================================
    """
    Steps:
    1. If index < 0 or index >= length -> return None
    2. Traverse index steps from head
    3. Return node

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        node = self.head
        for _ in range(index):
            node = node.next
        return node

    # =======================================================
    # SET_VALUE (update node's value)
    # =======================================================
    """
    Steps:
    1. Use get(index) to find node
    2. If node exists -> update node.value
    3. Return True or False

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def set_value(self, index, value):
        node = self.get(index)
        if node is None:
            return False
        node.value = value
        return True

    # =======================================================
    # SEARCH (find index of value)
    # =======================================================
    """
    Steps:
    1. Traverse nodes until value found or circle complete
    2. Return index if found else -1

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def search(self, value):
        if self.length == 0:
            return -1
        node = self.head
        idx = 0
        while True:
            if node.value == value:
                return idx
            node = node.next
            idx += 1
            if node == self.head:
                break
        return -1

    # =======================================================
    # REMOVE (by index) - using helpers (pop_first/pop_last/get)
    # =======================================================
    """
    Steps:
    1. If index invalid -> IndexError
    2. If index == 0 -> return pop_first()
    3. If index == length-1 -> return pop_last()
    4. Else:
         - prev = get(index-1)
         - popped = prev.next
         - prev.next = popped.next
         - popped.next = None
         - length -= 1
         - return popped

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def remove_with_helpers(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()
        prev = self.get(index - 1)
        popped = prev.next
        prev.next = popped.next
        popped.next = None
        self.length -= 1
        return popped

    # =======================================================
    # REMOVE_NO_HELPERS (standalone)
    # =======================================================
    """
    Same logic as remove_with_helpers but implemented inline (no helper calls).
    """
    def remove_no_helpers(self, index):
        if index < 0 or index >= self.length:
            raise IndexError("Index out of range")

        # Case: only one node
        if self.length == 1:
            popped = self.head
            self.head = None
            self.tail = None
            self.length -= 1
            popped.next = None
            return popped

        # Remove head
        if index == 0:
            popped = self.head
            self.head = self.head.next
            self.tail.next = self.head
            popped.next = None
            self.length -= 1
            return popped

        # Remove tail
        if index == self.length - 1:
            prev = self.head
            while prev.next != self.tail:
                prev = prev.next
            popped = self.tail
            prev.next = self.head
            self.tail = prev
            popped.next = None
            self.length -= 1
            return popped

        # Remove middle
        prev = self.head
        for _ in range(index - 1):
            prev = prev.next
        popped = prev.next
        prev.next = popped.next
        popped.next = None
        self.length -= 1
        return popped

    # =======================================================
    # TRAVERSE (return list of values)
    # =======================================================
    """
    Steps:
    1. If empty -> return []
    2. Start at head and collect values until returning to head
    3. Return list of values

    Time Complexity: O(n)
    Space Complexity: O(n) (for list of values)
    """
    def traverse(self):
        values = []
        if self.length == 0:
            return values
        node = self.head
        while True:
            values.append(node.value)
            node = node.next
            if node == self.head:
                break
        return values

    # =======================================================
    # DELETE_ALL (clear list)
    # =======================================================
    """
    Steps:
    1. If empty -> nothing to do
    2. Break circular link (optional): tail.next = None
    3. head = tail = None
    4. length = 0

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def delete_all(self):
        if self.head is None:
            return "List already empty"
        # break circular link to help GC (optional)
        self.tail.next = None
        self.head = None
        self.tail = None
        self.length = 0
        return "All nodes deleted!"

    # =======================================================
    # STRING REPRESENTATION
    # =======================================================
    def __str__(self):
        if self.length == 0:
            return "Empty CSLL"
        vals = []
        node = self.head
        while True:
            vals.append(str(node.value))
            node = node.next
            if node == self.head:
                break
        return "  -->  ".join(vals)


# ============================================================
# USAGE EXAMPLE
# ============================================================
if __name__ == "__main__":
    csll = CircularSinglyLinkedList()

    # build list
    csll.append(10)
    csll.append(20)
    csll.append(30)
    csll.prepend(5)
    csll.insert(2, 15)             # [5,10,15,20,30]

    print("CSLL:", csll)           # 5 --> 10 --> 15 --> 20 --> 30
    print("Traverse:", csll.traverse())
    print("Get index 2:", csll.get(2))         # Node(15)
    print("Search 20 at index:", csll.search(20))  # 3
    print("Set index 3 to 25:", csll.set_value(3, 25))
    print("After set:", csll)

    print("Pop first:", csll.pop_first())      # Node(5)
    print("After pop_first:", csll)
    print("Pop last:", csll.pop_last())        # Node(30)
    print("After pop_last:", csll)

    # remove using helpers
    removed = csll.remove_with_helpers(1)      # remove at index 1
    print("Removed (helpers):", removed)
    print("After remove_with_helpers:", csll)

    # rebuild and test remove_no_helpers
    csll.append(99)
    csll.append(100)
    print("Before remove_no_helpers:", csll)
    removed2 = csll.remove_no_helpers(csll.length - 1)  # remove tail via no helper
    print("Removed (no helpers):", removed2)
    print("After remove_no_helpers:", csll)

    # delete all
    print("Delete all:", csll.delete_all())
    print("After delete_all:", csll)

# ============================================================
# COMPLEXITIES (summary)
# ============================================================
"""
- Append:        O(1) time, O(1) space
- Prepend:       O(1) time, O(1) space
- Insert:        O(n) time, O(1) space
- Search:        O(n) time, O(1) space
- Traverse:      O(n) time, O(n) space (for returned list of values)
- Get:           O(n) time, O(1) space
- Set:           O(n) time, O(1) space
- Pop First:     O(1) time, O(1) space
- Pop Last:      O(n) time, O(1) space
- Remove:        O(n) time, O(1) space
- Delete All:    O(1) time, O(1) space
"""
