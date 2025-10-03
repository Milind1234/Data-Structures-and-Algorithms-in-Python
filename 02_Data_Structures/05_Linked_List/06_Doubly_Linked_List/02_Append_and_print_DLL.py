# 📌 QUESTION:
# Extend the Doubly Linked List (DLL) to support:
# 1️⃣ Appending new nodes at the end
# 2️⃣ Printing the DLL in a readable format using __str__

# ------------------------------------------------------
# 📘 Doubly Linked List (DLL) - Notes (Append + __str__)
# ------------------------------------------------------

# ✅ Node class: Creates a node with a value, a pointer to the previous node, and a pointer to the next node
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Will point to the previous node
        self.next = None       # Will point to the next node

# ------------------------------------------------------
# 📌 Doubly Linked List with Append and __str__
# ------------------------------------------------------
class DoublyLinkedList:
    def __init__(self):
        self.head = None       # First node of the list
        self.tail = None       # Last node of the list
        self.length = 0        # Initially list is empty

    # ------------------------------
    # ✅ Append Method
    # ------------------------------
    """
    Steps:
    1. Create a new node
    2. If list is empty:
         - set head = tail = new_node
    3. Else:
         - link new_node to tail
         - update tail pointer
    4. Increment length

    ⏱️ Complexity:
    - Time: O(1) → constant-time insertion at the end
    - Space: O(1) → no extra structures used
    """
    def append(self, value):
        new_node = Node(value)
        if self.head is None:          # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
        else:                          # Case 2: Non-empty list
            self.tail.next = new_node  # Link old tail → new node
            new_node.prev = self.tail  # Link new node back to old tail
            self.tail = new_node       # Update tail pointer
        self.length += 1

    # ------------------------------
    # ✅ __str__ Method
    # ------------------------------
    """
    Purpose:
    - Traverse the list from head → tail
    - Build a string representation of nodes
    - Format: "10 <--> 20 <--> 30"

    ⏱️ Complexity:
    - Time: O(n) → must visit all nodes
    - Space: O(n) → result string grows with list size
    """
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' <--> '
            temp_node = temp_node.next
        return result


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(10)   # Appends first node
DLL.append(20)   # Appends second node
DLL.append(30)   # Appends third node

print(DLL)  # Output: 10 <--> 20 <--> 30

# 📌 Diagram after appending 10, 20, 30:
# None <- [10] <-> [20] <-> [30] -> None
# head = 10
# tail = 30
# length = 3
