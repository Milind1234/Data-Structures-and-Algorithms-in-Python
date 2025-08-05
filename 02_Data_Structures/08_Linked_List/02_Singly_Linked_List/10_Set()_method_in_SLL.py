"""
========================================================
LINKED LIST (Set Value Methods)
========================================================
We learn two ways to update the value of a node at a 
specific index in a Singly Linked List.

1) Using get() method (set_value)
2) Without get(), direct traversal (set)
"""

# ------------------ NODE CLASS ------------------------
class Node:
    def __init__(self, value):
        self.value = value     # data stored in node
        self.next = None       # pointer to next node

# ---------------- LINKED LIST CLASS -------------------
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # ---------------------------------------------------
    # Append Method → Add node at end
    # ---------------------------------------------------
    def append(self, value):
        new_node = Node(value)
        if self.head is None:       # If list is empty
            self.head = new_node
            self.tail = new_node
        else:                       # Add to end
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # ---------------------------------------------------
    # Prepend Method → Add node at start
    # ---------------------------------------------------
    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:       # If list is empty
            self.head = new_node
            self.tail = new_node
        else:                       # Add to beginning
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # ---------------------------------------------------
    # Insert Method → Insert at any index
    # ---------------------------------------------------
    def insert(self, index, value):
        new_node = Node(value)
        if index < 0 or index > self.length:
            return "Index out of range"
        if index == 0:
            self.prepend(value)
            return "Inserted Successfully"
        if index == self.length:
            self.append(value)
            return "Inserted Successfully"
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
        return "Inserted Successfully"

    # ---------------------------------------------------
    # Print Linked List
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

    # ===================================================
    # GET METHOD → Returns node object at index
    # ===================================================
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node    # returns node object

    # ===================================================
    # SET VALUE (Using get() method)
    # ===================================================
    """
    Approach:
        1. Fetch node at given index using get()
        2. If node exists → update value
        3. Else → return error message
    Complexity: O(n)
    """
    def set_value(self, index, value):
        temp_node = self.get(index)  # Reuse get()
        if temp_node:
            temp_node.value = value
            return f"Value {value} updated successfully at index {index}"
        return "Index out of range"

    # ===================================================
    # SET (Direct traversal without get())
    # ===================================================
    """
    Approach:
        1. Validate index
        2. Traverse manually to target node
        3. Update node value directly
    Complexity: O(n)
    """
    def set(self, index, value):
        if index < 0 or index >= self.length:
            return "Index out of range"
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        current_node.value = value
        return f"Value {value} updated successfully at index {index}"


"""
--------------------------------------------------------
ASCII VISUALIZATION
--------------------------------------------------------
Initial Linked List:
Head → [50] → [10] → [20] → [30] → [40] → None

set_value(1, 70) or set(1, 70):
    - Traverse to index 1 → node with value 10
    - Update 10 → 70

Result:
Head → [50] → [70] → [20] → [30] → [40] → None

set(3, 100):
    - Traverse to index 3 → node with value 30
    - Update 30 → 100

Result:
Head → [50] → [70] → [20] → [100] → [40] → None

--------------------------------------------------------
TIME & SPACE COMPLEXITY
--------------------------------------------------------
- set_value() → O(n) because get() is O(n)
- set() → O(n) (direct traversal)
- Space → O(1) (no extra space used)

--------------------------------------------------------
INTERVIEW QUESTIONS
--------------------------------------------------------
1) How is setting value different from insertion?
   → Only existing node’s value is changed; no new node.

2) Why can't linked lists do O(1) index access like arrays?
   → Linked lists need traversal due to no index mapping.

3) Which approach is preferred?
   → set_value() for cleaner code (when get() exists),
     set() for performance-critical cases.
"""

# ------------------ USAGE EXAMPLE ----------------------
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.prepend(50)   # Final: 50 --> 10 --> 20 --> 30 --> 40

print("Linked List:", new_LinkedList)
print(new_LinkedList.set_value(1, 70))   # Using get()
print("After set_value:", new_LinkedList)
print(new_LinkedList.set(3, 100))        # Direct traversal
print("After set:", new_LinkedList)
