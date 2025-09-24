# 📌 QUESTION:
# Extend the Doubly Linked List (DLL) to support:
# 1️⃣ Append → insert new node at the end
# 2️⃣ Prepend → insert new node at the beginning
# 3️⃣ Print the DLL using __str__

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes (Append + Prepend)
# ------------------------------------------------------

# ✅ Node class: Creates a node with a value, a pointer to the previous node, and a pointer to the next node
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Points to the previous node
        self.next = None       # Points to the next node


# ------------------------------------------------------
# 📌 DLL Implementation
# ------------------------------------------------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None       # First node of the list
        self.tail = None       # Last node of the list
        self.length = 0        # Initially list is empty

    # ------------------------------
    # ✅ __str__ Method
    # ------------------------------
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <-> '
            temp_node = temp_node.next
        return result

    # ------------------------------
    # ✅ Append Method
    # ------------------------------
    def append(self, value):
        new_node = Node(value)
        if self.head is None:          # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
        else:                          # Case 2: Non-empty list
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # ✅ Prepend Method
    # ------------------------------
    """
    Purpose:
    Insert a new node at the **beginning** of the list.

    Steps:
    1. Create a new node.
    2. If list empty:
         - head = tail = new_node
    3. Else:
         - new_node.next = head
         - head.prev = new_node
         - head = new_node
    4. Increase length

    🔍 Visualization:

    Case 1: Empty DLL
    -----------------
    Before: head = None, tail = None
    After prepending(100):

        None <- [100] -> None
        head = 100, tail = 100

    Case 2: Non-Empty DLL
    ---------------------
    Before (head=10):
        None <- [10] <-> [20] <-> [30] -> None

    Prepend(100):
        Step 1: new_node = [100]
        Step 2: new_node.next = head   (100.next → 10)
        Step 3: head.prev = new_node   (10.prev → 100)
        Step 4: head = new_node        (head → 100)

    After:
        None <- [100] <-> [10] <-> [20] <-> [30] -> None

    🔗 Pointer changes:
    - new_node.next → old head (10)
    - old head.prev → new_node (100)
    - head → new_node (100)

    ⏱️ Time: O(1) → direct pointer updates
    ⏱️ Space: O(1) → no extra structures
    """
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:          # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
        else:                          # Case 2: Non-empty list
            new_node.next = self.head
            self.head.prev = new_node
            self.head = new_node
        self.length += 1


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(10)     # [10]
DLL.append(20)     # [10 <-> 20]
DLL.append(30)     # [10 <-> 20 <-> 30]
DLL.prepend(100)   # [100 <-> 10 <-> 20 <-> 30]

print(DLL)   # Output: 100 <-> 10 <-> 20 <-> 30

# 📌 Diagram after operations:
# None <- [100] <-> [10] <-> [20] <-> [30] -> None
# head = 100
# tail = 30
# length = 4
