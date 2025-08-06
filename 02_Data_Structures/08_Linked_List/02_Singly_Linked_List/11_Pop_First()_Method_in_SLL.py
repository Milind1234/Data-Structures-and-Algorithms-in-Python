# =========================================================
# POP FIRST METHOD - LINKED LIST (FULL CODE WITH NOTES)
# =========================================================

# ------------------ NODE CLASS ------------------------
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.next = None       # Pointer to the next node

# ---------------- LINKED LIST CLASS -------------------
class LinkedList:
    def __init__(self):
        self.head = None       # First node reference
        self.tail = None       # Last node reference
        self.length = 0        # Track number of nodes

    # ---------------------------------------------------
    # APPEND (Add node at end)
    # ---------------------------------------------------
    def append(self, value):
        new_node = Node(value)
        # Case 1: List is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Case 2: Attach new node at tail
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1   # Update length

    # ---------------------------------------------------
    # PREPEND (Add node at start)
    # ---------------------------------------------------
    def prepend(self, value):
        new_node = Node(value)
        # Case 1: List is empty
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            # Case 2: Point new node to current head
            new_node.next = self.head
            self.head = new_node
        self.length += 1   # Update length

    # ---------------------------------------------------
    # INSERT (Insert node at index)
    # ---------------------------------------------------
    def insert(self, index, value):
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
        # Traverse to node just before target index
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
        return "Inserted Successfully"

    # ---------------------------------------------------
    # POP FIRST (Remove first node)
    # ---------------------------------------------------
    def pop_first(self):
        # Case 1: List is empty
        if self.length == 0:
            return f"No Node to pop"

        # Store reference of node to be removed
        popped_node = self.head

        # Case 2: List has only one node
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            # Case 3: More than one node
            self.head = self.head.next
            popped_node.next = None   # Disconnect the popped node

        self.length -= 1  # Reduce length
        return f"Using Pop first method, we popped out the first node that is --> {popped_node.value}"

    # ---------------------------------------------------
    # STRING REPRESENTATION (Print linked list)
    # ---------------------------------------------------
    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' --> '
            temp_node = temp_node.next
        return result

# =========================================================
# USAGE EXAMPLE
# =========================================================
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.prepend(50)       # Final: 50 --> 10 --> 20 --> 30 --> 40
print(new_LinkedList)

new_LinkedList.insert(0, 70)     # Insert at head
print(new_LinkedList)

print(new_LinkedList.pop_first())  # Pop first node
print(f"After popping the first node: {new_LinkedList}")

"""
---------------------------------------------------------
EDGE CASES HANDLED
---------------------------------------------------------
1) Empty list (length == 0):
   - Returns None because nothing to pop.

2) Single node list (length == 1):
   - Sets both head and tail to None.

3) Multiple nodes:
   - Moves head pointer to the next node and disconnects old head.

---------------------------------------------------------
COMPLEXITY
---------------------------------------------------------
Time Complexity: O(1)  -> We always remove the first node directly.
Space Complexity: O(1) -> No extra space used.

---------------------------------------------------------
INTERVIEW QUESTIONS
---------------------------------------------------------
1) Why is pop_first O(1)?
   -> Because we do not traverse the list, we just move head pointer.

2) What do we do when length == 1?
   -> Set both head and tail to None.

3) Can pop_first remove from empty list?
   -> Yes, but it returns None (nothing to pop).
"""
#______________________________________________________________________________________________________________________________
# ---------------------------------------------------------
# Simplified Code only for Pop_first
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
    # POP_FIRST (Remove first node)
    # ---------------------------------------------------
    def pop_first(self):
        """
        Removes and returns the first node of the linked list.

        Steps:
        1) If length == 0 -> return "No Node to pop"
        2) Store the head in popped_node
        3) If only one node exists -> set head = tail = None
        4) Else move head to next node & break popped_node link
        5) Decrement length and return value
        """

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
        return f"Popped First Node --> {popped_node.value}"

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
    print("Before pop_first:", ll)
    print(ll.pop_first())
    print("After pop_first :", ll)
