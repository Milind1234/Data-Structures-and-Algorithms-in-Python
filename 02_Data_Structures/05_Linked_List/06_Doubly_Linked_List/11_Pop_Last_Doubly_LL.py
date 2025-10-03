class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.prev = None       # Will point to the previous node
        self.next = None       # Will point to the next node

    def __repr__(self):
        return f"Node({self.value})"


class DoublyLinkedList:
    def __init__(self):
        self.head = None       # First node
        self.tail = None       # Last node
        self.length = 0        # Initially empty list

    # ------------------------------
    # Append → insert at the end
    # ------------------------------
    def append(self, value):
        """Append a value at the end of the list in O(1) time."""
        new_node = Node(value)
        if self.head is None:           # Empty list
            self.head = self.tail = new_node
        else:                           # Non-empty list
            self.tail.next = new_node
            new_node.prev = self.tail
            self.tail = new_node
        self.length += 1

    # ------------------------------
    # __str__ → string representation
    # ------------------------------
    def __str__(self):
        result = []
        temp = self.head
        while temp:
            result.append(str(temp.value))
            temp = temp.next
        return " <--> ".join(result) if result else "Empty DLL"

    # ------------------------------
    # pop_last → remove & return tail value
    # ------------------------------
    def pop_last(self):
        """
        Purpose:
        - Remove and return the last node's value (tail).

        Cases:
        1. Empty list: return None
        2. One node: head and tail become None
        3. Multiple nodes: tail moves to tail.prev and links updated

        Returns:
        - The popped node's value, or None if list empty.

        Complexity:
        - Time: O(1)
        - Space: O(1)
        """
        if self.head is None:           # Empty list
            return None

        popped_node = self.tail
        popped_value = popped_node.value

        if self.length == 1:            # One node
            self.head = None
            self.tail = None
        else:                           # More than one node
            self.tail = popped_node.prev
            self.tail.next = None
            popped_node.prev = None     # fully disconnect node

        self.length -= 1
        return popped_value


# ------------------------------------------------------
# Example usage / quick test
# ------------------------------------------------------
if __name__ == "__main__":
    dll = DoublyLinkedList()
    dll.append(10)
    dll.append(20)
    dll.append(30)

    print("DLL contents:", dll)              # 10 <--> 20 <--> 30
    print("Popped value:", dll.pop_last())   # 30
    print("After pop_last:", dll)            # 10 <--> 20
    print("Length:", dll.length)             # 2

    # pop until empty
    print("Popped value:", dll.pop_last())   # 20
    print("Popped value:", dll.pop_last())   # 10
    print("Popped value:", dll.pop_last())   # None (empty)
    print("Final DLL:", dll)                 # Empty DLL
    print("Final Length:", dll.length)       # 0
