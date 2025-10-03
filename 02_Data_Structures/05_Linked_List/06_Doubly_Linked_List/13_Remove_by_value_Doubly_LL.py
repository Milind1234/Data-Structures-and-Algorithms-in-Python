# note_remove_by_index.py
# ---------------------------------------------------------------------
# Title : DLL — Remove By Index (two styles)
# Style : Compact technical notes + code + small self-checks
# Goal  : Show both remove implementations (helper + direct) with
#         explicit micro-step pointer snapshots for each removal case.
# ---------------------------------------------------------------------

class Node:
    """DLL node: value, prev, next"""
    def __init__(self, value):
        self.value = value
        self.prev = None
        self.next = None

    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    """Minimal Doubly Linked List supporting append and two remove methods."""
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ---------- helpers ----------
    def __str__(self):
        out = []
        cur = self.head
        while cur:
            out.append(str(cur.value))
            cur = cur.next
        return " <-> ".join(out) if out else "Empty DLL"

    def append(self, value):
        n = Node(value)
        if not self.head:
            self.head = self.tail = n
        else:
            self.tail.next = n
            n.prev = self.tail
            self.tail = n
        self.length += 1

    def get_node(self, index):
        """Return node at index or None. Optimized traversal."""
        if index < 0 or index >= self.length:
            return None
        if index < self.length // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.length - 1, index, -1):
                cur = cur.prev
        return cur

    def pop_first(self):
        """Remove first node and return value (helper)."""
        if not self.head:
            return None
        p = self.head
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.head = p.next
            self.head.prev = None
            p.next = None
        self.length -= 1
        return p.value

    def pop_last(self):
        """Remove last node and return value (helper)."""
        if not self.head:
            return None
        p = self.tail
        if self.length == 1:
            self.head = self.tail = None
        else:
            self.tail = p.prev
            self.tail.next = None
            p.prev = None
        self.length -= 1
        return p.value

    # =================================================================
    # 1) remove_element(index)  — uses helpers (get_node, pop_first, pop_last)
    # =================================================================
    def remove_element(self, index):
        """
        Remove node at `index`. Uses helper functions.
        Returns removed value or None if index invalid.
        """
        if index < 0 or index >= self.length:
            return None
        if index == 0:
            return self.pop_first()
        if index == self.length - 1:
            return self.pop_last()

        target = self.get_node(index)          # helper finds node
        # unlink
        target.prev.next = target.next
        target.next.prev = target.prev
        target.prev = None
        target.next = None
        self.length -= 1
        return target.value

    # =================================================================
    # 2) remove_element_direct(index) — completely self-contained
    # =================================================================
    def remove_element_direct(self, index):
        """
        Remove node at `index` WITHOUT calling pop_first/pop_last/get_node.
        Returns removed value or None if index invalid.
        """
        if index < 0 or index >= self.length:
            return None

        # --- head case (manual) ---
        if index == 0:
            p = self.head
            if self.length == 1:
                self.head = self.tail = None
            else:
                # micro-step changes:
                # 1) new_head = old_head.next
                # 2) new_head.prev = None
                # 3) old_head.next = None
                new_head = p.next
                self.head = new_head
                new_head.prev = None
                p.next = None
            self.length -= 1
            return p.value

        # --- tail case (manual) ---
        if index == self.length - 1:
            p = self.tail
            # micro-step changes:
            # 1) new_tail = old_tail.prev
            # 2) new_tail.next = None
            # 3) old_tail.prev = None
            new_tail = p.prev
            self.tail = new_tail
            new_tail.next = None
            p.prev = None
            self.length -= 1
            return p.value

        # --- middle case (manual traversal) ---
        # choose direction by proximity
        if index < self.length // 2:
            cur = self.head
            for _ in range(index):
                cur = cur.next
        else:
            cur = self.tail
            for _ in range(self.length - 1, index, -1):
                cur = cur.prev

        # micro-step unlinking:
        # 1) left = cur.prev
        # 2) right = cur.next
        # 3) left.next = right
        # 4) right.prev = left
        # 5) cur.prev = cur.next = None
        left = cur.prev
        right = cur.next
        left.next = right
        right.prev = left
        cur.prev = None
        cur.next = None
        self.length -= 1
        return cur.value


# ---------------------------------------------------------------------
# Compact visual helper: show pointers as strings (for small debugging)
# ---------------------------------------------------------------------
def snapshot(dll):
    """Return compact snapshot showing head/tail and list representation."""
    h = dll.head.value if dll.head else None
    t = dll.tail.value if dll.tail else None
    return f"Head={h}  Tail={t}  List={dll}"


# ---------------------------------------------------------------------
# Self-check / quick tests (run this file directly)
# ---------------------------------------------------------------------
if __name__ == "__main__":
    # build [10 <-> 20 <-> 30 <-> 40]
    dll = DoublyLinkedList()
    for v in (10, 20, 30, 40):
        dll.append(v)

    print("Initial:", snapshot(dll))
    # remove with helper: remove head
    removed = dll.remove_element(0)
    print("Removed (helper idx=0):", removed, "|", snapshot(dll))
    # list now [20 <-> 30 <-> 40]

    # remove direct: remove middle (index 1 -> value 30)
    removed2 = dll.remove_element_direct(1)
    print("Removed (direct idx=1):", removed2, "|", snapshot(dll))
    # list now [20 <-> 40]

    # remove direct: remove tail (index len-1 -> 1)
    removed3 = dll.remove_element_direct(dll.length - 1)
    print("Removed (direct tail):", removed3, "|", snapshot(dll))
    # list now [20]

    # final remove direct head
    removed4 = dll.remove_element_direct(0)
    print("Removed (direct last head):", removed4, "|", snapshot(dll))
    # list now Empty

    # edge checks
    print("Invalid remove (should None):", dll.remove_element(0))
    print("Invalid direct remove (should None):", dll.remove_element_direct(-1))

# ---------------------------------------------------------------------
# End of file
# ---------------------------------------------------------------------
