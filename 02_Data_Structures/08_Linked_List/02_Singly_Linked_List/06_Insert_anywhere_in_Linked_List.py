"""
========================================================
TOPIC: Insert Method in Singly Linked List
========================================================
In this note, we are learning:
1. What is insert operation
2. Different cases for insert
3. How insert works internally
4. Code implementation (with explanation per condition)
5. ASCII visualization of pointer changes
6. Time and space complexity analysis
7. Common interview questions
"""

# ------------------ NODE CLASS ------------------------
class Node:
    def __init__(self, value):
        self.value = value   # stores data
        self.next = None     # pointer to next node

# ---------------- LINKED LIST CLASS -------------------
class LinkedList:
    def __init__(self):
        self.head = None     # start of list
        self.tail = None     # end of list
        self.length = 0      # length of list

    def append(self, value):
        """Insert node at END (O(1))"""
        new_node = Node(value)
        if self.head is None:        # Empty list
            self.head = new_node
            self.tail = new_node
        else:                        # Non-empty list
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """Insert node at BEGINNING (O(1))"""
        new_node = Node(value)
        if self.head is None:        # Empty list
            self.head = new_node
            self.tail = new_node
        else:                        # Non-empty list
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    def insert(self, index, value):
        """
        Insert node at any index (0 to length)
        Cases:
        1) Invalid index → return False
        2) Empty list → head and tail both point to new node
        3) Index == 0 → insert at beginning
        4) Index in middle or at end → traverse and insert
        """

        # STEP 1: Create new node
        new_node = Node(value)

        # STEP 2: Invalid index check
        # ----------------------------------------
        # If index is negative OR greater than current length → invalid
        # Example: length = 5 → valid indexes = 0 to 5
        # ----------------------------------------
        if index < 0 or index > self.length:
            return False

        # STEP 3: Case 1 - Empty list
        # ----------------------------------------
        # If linked list has no elements,
        # simply make head and tail point to new node
        # ----------------------------------------
        if self.length == 0:
            self.head = new_node
            self.tail = new_node

        # STEP 4: Case 2 - Insert at beginning (index == 0)
        # ----------------------------------------
        # New node next → old head
        # head → new node
        # ----------------------------------------
        elif index == 0:
            new_node.next = self.head
            self.head = new_node

        # STEP 5: Case 3 - Insert in middle or at end
        # ----------------------------------------
        # Traverse to node just before index
        # Example: insert(2, 100) in 10->20->30->40
        # temp_node stops at index 1 (node with value 20)
        # ----------------------------------------
        else:
            temp_node = self.head
            for _ in range(index - 1):
                temp_node = temp_node.next

            # Connect new node to next node
            new_node.next = temp_node.next
            # Connect previous node to new node
            temp_node.next = new_node

        # STEP 6: Increase length
        self.length += 1
        return True

    def __str__(self):
        """String representation for easy printing"""
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' --> '
            temp_node = temp_node.next
        return result

# ----------------- TESTING THE IMPLEMENTATION -----------------
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)
new_linked_list.prepend(60)

print("Before Insert:", new_linked_list)

# Insert at valid index
index = 2
value = 100
status = new_linked_list.insert(index, value)
if status:
    print(f"After inserting {value} at index {index}: ", new_linked_list)
else:
    print(f"Insertion failed: index {index} is out of range.")

"""
--------------------------------------------------------
ASCII VISUALIZATION (Insert at index 2, value 100)
--------------------------------------------------------
Before:
Head → [60] → [10] → [20] → [30] → [40] → [50] → None
Tail -------------------------------------------^

Traverse till index-1 (index=2 → stop at index 1 node [10]):
temp_node = [10]

Link new node:
new_node.next = temp_node.next   (points to node [20])
temp_node.next = new_node        (connect [10] → [100])

After:
Head → [60] → [10] → [100] → [20] → [30] → [40] → [50] → None
Tail --------------------------------------------------^

--------------------------------------------------------
COMPLEXITY ANALYSIS
--------------------------------------------------------
Time Complexity:
    - Insert at beginning (index 0): O(1)
    - Insert at end (index == length): O(n) traversal (if no tail optimization used)
    - Insert in middle: O(n)
Space Complexity:
    - O(1) → Only one extra node created

--------------------------------------------------------
INTERVIEW QUESTIONS & ANSWERS
--------------------------------------------------------

1) How do you handle insertion in an empty linked list?
   - When the linked list is empty (head is None and tail is None), 
     we simply make the new node both head and tail.
     Example:
        head = new_node
        tail = new_node

2) Why is insert at head O(1)?
   - Because we only update:
        new_node.next = head
        head = new_node
     → No traversal is needed, hence O(1) time complexity.

3) Why is insert in middle O(n)?
   - To insert at a given index (other than head or tail), 
     we need to traverse from head to (index - 1) position. 
     This traversal takes O(n) in the worst case.

4) What happens if you insert at index == length?
   - Inserting at index == length means we are adding the node at the end. 
     In our implementation, this behaves like an append operation.

5) How can you make insertion at end O(1)?
   - By maintaining a 'tail' pointer.
     Instead of traversing to the last node every time, 
     we directly attach the new node using tail.next and update tail.

6) What is the difference between linked list insert and array insert?
   - Linked List:
        • No shifting of elements required.
        • Insertion is O(1) if head or tail pointer is used.
   - Array:
        • May need to shift all elements after the index to make space.
        • Average case insertion complexity is O(n).
"""

