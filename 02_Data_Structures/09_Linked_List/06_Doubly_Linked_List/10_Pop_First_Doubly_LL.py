# 📌 Doubly Linked List with Append, __str__, and pop_first
# --------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Points to the previous node
        self.next = None       # Points to the next node

    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None       # First node
        self.tail = None       # Last node
        self.length = 0        # Initially empty list

    # ------------------------------
    # ✅ Append Method
    # ------------------------------
   
    def append(self, value):
        new_node = Node(value)
        if self.head is None:           # Empty list
            self.head = self.tail = new_node
        else:                           # Non-empty list
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # ✅ __str__ Method
    # ------------------------------
    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.value))
            temp = temp.next
        return " <--> ".join(result) if result else "Empty DLL"

    # ------------------------------
    # ✅ pop_first Method
    # ------------------------------
    """
    Purpose:
    - Remove and return the first node (head) from the list.

    Cases:
    1. Empty list:
         - return None
    2. List with 1 node:
         - head = tail = None
    3. List with >1 node:
         - move head to head.next
         - set new head.prev = None
         - disconnect popped node

    Complexity:
    - Time: O(1)
    - Space: O(1)
    """
    def pop_first(self):
        if self.head is None:           # Case 1: Empty list
            return None

        popped_node = self.head

        if self.length == 1:            # Case 2: One node
            self.head = self.tail = None
        else:                           # Case 3: Multiple nodes
            self.head = self.head.next
            self.head.prev = None
            popped_node.next = None     # fully disconnect node

        self.length -= 1
        return popped_node.value


# ------------------------------------------------------
# 🧪 Example Usage
# ------------------------------------------------------
DLL = DoublyLinkedList()
DLL.append(10)
DLL.append(20)
DLL.append(30)

print("DLL contents:", DLL)        # 10 <--> 20 <--> 30
print("Popped:", DLL.pop_first())  # 10
print("After pop_first:", DLL)     # 20 <--> 30
print("Length:", DLL.length)       # 2
