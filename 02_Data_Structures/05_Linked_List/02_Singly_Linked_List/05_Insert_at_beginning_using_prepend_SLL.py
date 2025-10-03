"""
========================================================
TOPIC: Prepend Method in Singly Linked List
========================================================
In this note, we are learning:
1. What is a linked list (brief)
2. What is prepend operation
3. How prepend works internally
4. Code implementation
5. ASCII visualization of pointer changes
6. Time and space complexity analysis

--------------------------------------------------------
WHAT IS A LINKED LIST?
--------------------------------------------------------
A linked list is a linear data structure where elements (called nodes) are 
connected using pointers. Each node has:
    - value: stores data
    - next: reference (pointer) to the next node

We maintain:
    - head: reference to the first node
    - tail: reference to the last node
    - length: number of nodes in the list

--------------------------------------------------------
WHAT IS PREPEND?
--------------------------------------------------------
Prepend means inserting a new node at the BEGINNING of the linked list.

Example:
Before prepend(60):
head → 10 → 20 → 30 → 40 → 50 → None

After prepend(60):
head → 60 → 10 → 20 → 30 → 40 → 50 → None

--------------------------------------------------------
HOW PREPEND WORKS?
--------------------------------------------------------
Steps:
1. Create a new node (with given value)
2. If linked list is empty:
        head = new_node
        tail = new_node
3. Else:
        new_node.next = head   # link new node to old head
        head = new_node        # update head pointer
4. Increase length by 1

Time Complexity: O(1)  (constant time, just pointer change)
Space Complexity: O(1) (only one new node allocated)
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

    def __str__(self):
        """
        Custom string representation to print linked list nicely.
        Example output: "60 ➡ 10 ➡ 20 ➡ 30 ➡ 40 ➡ 50"
        """
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " ➡ "  # arrow for better visualization
            temp_node = temp_node.next
        return result

    def append(self, value):
        """
        Append method: Insert node at the END of the linked list.
        Steps:
            1. Create a new node
            2. If list is empty:
                    head = new_node
                    tail = new_node
               Else:
                    tail.next = new_node
                    tail = new_node
            3. Increase length
        """
        new_node = Node(value)
        if self.head is None:       # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
        else:                       # Case 2: Non-empty list
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        """
        Prepend method: Insert node at the BEGINNING of the linked list.
        Steps:
            1. Create new node
            2. If list is empty:
                    head = new_node
                    tail = new_node
               Else:
                    new_node.next = head
                    head = new_node
            3. Increase length
        """
        new_node = Node(value)
        if self.head is None:       # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
        else:                       # Case 2: Non-empty list
            new_node.next = self.head
            self.head = new_node
        self.length += 1    

# ------------- TESTING THE IMPLEMENTATION -------------
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)

print("Before Prepend method:", new_linked_list)

new_linked_list.prepend(60)  # adding 60 at the start

print("After Prepend method :", new_linked_list)

"""
--------------------------------------------------------
ASCII VISUALIZATION (Before and After Prepend)
--------------------------------------------------------
Before prepend(60):
Head → [10|•] → [20|•] → [30|•] → [40|•] → [50|None]
Tail ----------------------------^

After prepend(60):
Head → [60|•] → [10|•] → [20|•] → [30|•] → [40|•] → [50|None]
Tail --------------------------------------------^

Where:
 [value|pointer] represents each node
 '•' means link to next node
 None means end of list

--------------------------------------------------------
COMPLEXITY ANALYSIS
--------------------------------------------------------
Time Complexity:
    - Append → O(1)
    - Prepend → O(1)
Space Complexity:
    - O(1) (only one new node created)
"""
