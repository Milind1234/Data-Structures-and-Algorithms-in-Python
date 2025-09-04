"""
========================================================
TOPIC: GET METHOD IN SINGLY LINKED LIST
========================================================
In this note, we cover:
1. Quick recap of linked list structure
2. Why we need a get() method
3. Step-by-step explanation of get() method
4. Code implementation
5. ASCII visualization
6. Complexity analysis
7. Example usage
8. Interview questions

--------------------------------------------------------
WHAT IS GET METHOD?
--------------------------------------------------------
- The get() method is used to access a node at a given index.
- Unlike arrays (which have O(1) access), linked lists require traversal 
  from the head node to reach the target index.
- Example:
    Linked list: Head → [50] → [10] → [20] → [30] → [40] → None
    get(1) → Node value: 10
    get(4) → Node value: 40

--------------------------------------------------------
WHEN TO USE?
--------------------------------------------------------
- To retrieve a value at a specific position
- For debugging or operations where position matters

========================================================
CODE IMPLEMENTATION
========================================================
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

    def append(self, value):
        new_node = Node(value)
        if self.head is None:       # If list is empty
            self.head = new_node
            self.tail = new_node
        else:                       # Add to end
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:       # If list is empty
            self.head = new_node
            self.tail = new_node
        else:                       # Add to beginning
            new_node.next = self.head
            self.head = new_node
        self.length += 1

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

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' --> '
            temp_node = temp_node.next
        return result

    # ====================================================
    # GET METHOD
    # ====================================================
    def get(self, index):
        """
        Purpose: Returns the value at given index.
        
        Steps:
        1) Check if index is valid (0 <= index < length)
        2) Start from head
        3) Move index steps forward
        4) Return node value at that position
        """
        # 1) Validate index
        if index < 0 or index >= self.length:
            return "Index out of range"
        
        # 2) Traverse from head to index
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        
        # 3) Return result
        return f"At Index {index}: {current_node.value} is present"


"""
--------------------------------------------------------
ASCII VISUALIZATION
--------------------------------------------------------
Linked List: Head → [50] → [10] → [20] → [30] → [40] → None

get(1):
Step 1: index = 1 (valid)
Step 2: Traverse once → move to node with value 10
Result: "At Index 1: 10 is present"

get(4):
Step 1: index = 4 (valid)
Step 2: Traverse four times → node with value 40
Result: "At Index 4: 40 is present"
--------------------------------------------------------
"""

# ------------------ USAGE EXAMPLE ----------------------
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.prepend(50)   # Final: 50 --> 10 --> 20 --> 30 --> 40

print("Linked List:", new_LinkedList)
print(new_LinkedList.get(1))  # Output: "At Index 1: 10 is present"
print(new_LinkedList.get(4))  # Output: "At Index 4: 40 is present"
print(new_LinkedList.get(5))  # Output: "Index out of range"

"""
--------------------------------------------------------
TIME & SPACE COMPLEXITY
--------------------------------------------------------
- Time Complexity: O(n) → traverse up to index times
- Space Complexity: O(1) → no extra space used

--------------------------------------------------------
INTERVIEW QUESTIONS
--------------------------------------------------------
1) Why is get() O(n) in linked lists?
   → Because we must traverse nodes sequentially from head.

2) How is get() in a linked list different from an array?
   → Array: O(1) random access; Linked List: O(n) sequential access.

3) How can we improve access speed?
   → Use additional data structures (like skip lists) or 
     switch to dynamic arrays if random access is frequent.
"""
