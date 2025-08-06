"""
------------------------------------------------------------
Linked List - POP (Remove Last Node)
------------------------------------------------------------
This program demonstrates how to remove the last node from a
singly linked list using the pop() method.

------------------------------------------------------------
1) Node Class
------------------------------------------------------------
- Represents each node in the linked list.
- Contains:
    - value → the data stored in the node.
    - next  → pointer to the next node.
"""

# ------------------ NODE CLASS ------------------------
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.next = None       # Pointer to the next node


"""
------------------------------------------------------------
2) LinkedList Class
------------------------------------------------------------
Handles various linked list operations:
    - append()      → Add node at the end
    - prepend()     → Add node at the start
    - insert()      → Insert node at a given index
    - pop_first()   → Remove first node
    - pop()         → Remove last node (focus of this note)
    - __str__()     → String representation of list
------------------------------------------------------------
pop() method explanation:
------------------------------------------------------------
Steps:
1) If length == 0 → return "No Node to Pop"
2) If length == 1 → set head and tail = None
3) Else:
     - Traverse until temp_node.next is tail
     - Set tail = temp_node
     - Break connection (tail.next = None)
4) Decrement length
5) Return popped node value
------------------------------------------------------------
Time Complexity:
- O(n) → because we traverse the list to find the node before the tail
- Space Complexity: O(1)
------------------------------------------------------------
"""

# ---------------- LINKED LIST CLASS -------------------
class LinkedList:
    def __init__(self):
        self.head = None       # First node reference
        self.tail = None       # Last node reference
        self.length = 0        # Track number of nodes

    def append(self, value):
        """Add node at the end"""
        new_node = Node(value)
        if self.head is None:          # Empty list
            self.head = new_node
            self.tail = new_node
        else:                          # Attach at end
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Add node at the beginning"""
        new_node = Node(value)
        if self.head is None:          # Empty list
            self.head = new_node
            self.tail = new_node
        else:                          # Attach at start
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        """Insert node at given index"""
        if index < 0 or index > self.length:
            return "Index out of range"
        if index == 0:
            self.prepend(value)
            return "Inserted Successfully"
        if index == self.length:
            self.append(value)
            return "Inserted Successfully"
        new_node = Node(value)
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
        return "Inserted Successfully"

    def pop_first(self):
        """Remove first node"""
        if self.length == 0:
            return "No Node to pop"
        popped_node = self.head
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            self.head = self.head.next
            popped_node.next = None
        self.length -= 1
        return f"Using Pop first method, we popped out the first node that is --> {popped_node.value}"

    def pop(self):
        """Remove last node"""
        if self.length == 0:
            return "No Node to Pop"
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            # Traverse until temp_node.next is tail
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        self.length -= 1
        return f"Using Pop method, we popped out the Last node that is --> {popped_node.value}"

    def __str__(self):
        """String representation of linked list"""
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' --> '
            temp_node = temp_node.next
        return result

"""
------------------------------------------------------------
USAGE EXAMPLE
------------------------------------------------------------
"""
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.prepend(50)      # Final: 50 --> 10 --> 20 --> 30 --> 40
print(new_LinkedList)

new_LinkedList.insert(0, 70)    # Insert at head
print(new_LinkedList)

print("__________________________________________________________________")
print(new_LinkedList.pop_first())   # Pop first node
print(f"After popping the first node: {new_LinkedList}")

print("__________________________________________________________________")
print(new_LinkedList.pop())        # Pop last node
print(f"After popping the Last node: {new_LinkedList}")


#______________________________________________________________________________________________________________________________
# ---------------------------------------------------------
# Simplified Code only for Pop() Method
# ---------------------------------------------------------

# ------------------ NODE CLASS ------------------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------------- LINKED LIST CLASS -------------------
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # ---------------------------------------------------
    # POP (Remove last node)
    # ---------------------------------------------------
    def pop(self):
        """
        Removes and returns the last node of the linked list.

        Steps:
        1) If length == 0 -> return "No Node to Pop"
        2) Store tail as popped_node
        3) If only one node -> set head = tail = None
        4) Else traverse till node before tail and make it new tail
        5) Break popped_node link
        6) Decrement length and return value
        """
        if self.length == 0:
            return "No Node to Pop"

        popped_node = self.tail

        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp = self.head
            while temp.next != self.tail:
                temp = temp.next
            self.tail = temp
            self.tail.next = None

        self.length -= 1
        return f"Popped Last Node --> {popped_node.value}"

    def __str__(self):
        temp = self.head
        result = ''
        while temp:
            result += str(temp.value)
            if temp.next:
                result += ' --> '
            temp = temp.next
        return result


# ------------------ USAGE -----------------------------
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    print("Before pop:", ll)
    print(ll.pop())
    print("After pop :", ll)
