# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topics: Append | String Representation | Traverse
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
        """
        Traverse the CDLL starting from head and collect values
        in a readable format with double links.

        Example:
        [10] ◀——▶ [20] ◀——▶ [30]
        """
        current_node = self.head
        result = ''
        while current_node:
            result += str(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break
            result += ' ◀——▶ '
        return result

    # ---------------------------------------------------------------
    # 3️⃣ traverse() → Print all node values
    # ---------------------------------------------------------------
    def traverse(self):
        """
        Purpose:
        Visit each node in the Circular Doubly Linked List (CDLL)
        starting from the head, and print its value.

        Steps:
        1. Start from head.
        2. Continue moving to `next` node.
        3. Stop when you circle back to head.

        🔍 Visualization:
        CDLL = [10] ◀——▶ [20] ◀——▶ [30] ◀——▶ [40]

        traverse():
        → Print 10
        → Print 20
        → Print 30
        → Print 40
        (then stop when we reach head again)

        ⏱️ Time: O(n) → visits each node once
        ⏱️ Space: O(1) → no extra space used
        """
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next
            if current_node == self.head:
                break


# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
CDLL = CircularDoublyLinkedList()
CDLL.append(10)
CDLL.append(20)
CDLL.append(30)
CDLL.append(40)

print("CDLL:", CDLL) 
# Output: 10 ◀——▶ 20 ◀——▶ 30 ◀——▶ 40

print("Traverse Output:")
CDLL.traverse()
# Output:
# 10
# 20
# 30
# 40
