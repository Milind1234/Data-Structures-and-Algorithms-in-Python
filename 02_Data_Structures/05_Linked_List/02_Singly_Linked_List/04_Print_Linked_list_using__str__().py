"""
======================================================
PRINTING LINKED LIST USING __str__ METHOD
======================================================

------------------------------------------------------
WHAT IS COVERED IN THIS NOTE?
------------------------------------------------------
1) Why default print of an object is not readable.
2) What is `__str__` and why it is useful.
3) How to override `__str__` for a Linked List.
4) Full code with step-by-step explanation.
5) Complexity Analysis.
6) ASCII visualization of the process.
7) Common Interview Questions and Answers.
------------------------------------------------------
"""

# =====================================================
# 1) NODE CLASS → BASIC BUILDING BLOCK OF LINKED LIST
# =====================================================
class Node:
    def __init__(self, value):
        self.value = value   # Stores the actual data
        self.next = None     # Pointer to the next node


# =====================================================
# 2) LINKED LIST CLASS
# =====================================================
class LinkedList:
    def __init__(self):
        self.head = None     # Points to first node
        self.tail = None     # Points to last node
        self.length = 0      # Number of nodes

    # -------------------------------------------------
    # __str__ METHOD → Custom Print
    # -------------------------------------------------
    def __str__(self):
        """
        Converts linked list into human-readable string.

        Example Output:
            10 --> 20 --> 30 --> 40
        """
        temp_node = self.head    # Start from head node
        result = ""              # Will store final string

        # Traverse until end of list
        while temp_node is not None:
            # Add current node's value to result
            result += str(temp_node.value)

            # If another node exists, add arrow
            if temp_node.next is not None:
                result += " --> "

            # Move to next node
            temp_node = temp_node.next

        return result

    # -------------------------------------------------
    # APPEND METHOD → Add node at end of linked list
    # -------------------------------------------------
    def append(self, value):
        new_node = Node(value)

        if self.head is None:      # Case 1: Empty list
            self.head = new_node
            self.tail = new_node
        else:                      # Case 2: Existing nodes
            self.tail.next = new_node
            self.tail = new_node

        self.length += 1


# =====================================================
# 3) USAGE EXAMPLE
# =====================================================
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)
new_linked_list.append(60)

# Automatically calls __str__ method
print(new_linked_list)  
# Output: 10 --> 20 --> 30 --> 40 --> 50 --> 60


# =====================================================
# 4) HOW THE __str__ METHOD WORKS (STEP-BY-STEP)
# =====================================================
"""
1) temp_node = self.head
   → Start from the first node.

2) result = ""
   → Empty string to store the final formatted output.

3) while temp_node is not None:
   → Continue looping until the last node.

4) result += str(temp_node.value)
   → Add current node value.

5) if temp_node.next is not None:
       result += " --> "
   → Add arrow if there is another node.

6) temp_node = temp_node.next
   → Move pointer to next node.

7) return result
   → After traversal, return formatted string.
"""


# =====================================================
# 5) ASCII VISUALIZATION
# =====================================================
"""
Initial Linked List:
Head ──► [10|•] ──► [20|•] ──► [30|•] ──► [40|•] ──► [50|•] ──► [60|None]

Traversal Steps:
- Iteration 1: temp_node = 10 → result = "10 --> "
- Iteration 2: temp_node = 20 → result = "10 --> 20 --> "
- Iteration 3: temp_node = 30 → result = "10 --> 20 --> 30 --> "
- Iteration 4: temp_node = 40 → result = "10 --> 20 --> 30 --> 40 --> "
- Iteration 5: temp_node = 50 → result = "10 --> 20 --> 30 --> 40 --> 50 --> "
- Iteration 6: temp_node = 60 → result = "10 --> 20 --> 30 --> 40 --> 50 --> 60"

Loop ends because temp_node = None.
Final Output → "10 --> 20 --> 30 --> 40 --> 50 --> 60"
"""


# =====================================================
# 6) COMPLEXITY ANALYSIS
# =====================================================
"""
TIME COMPLEXITY:
- Traverses all nodes → O(n)

SPACE COMPLEXITY:
- Uses only a string variable → O(1)
"""


# =====================================================
# 7) COMMON INTERVIEW QUESTIONS
# =====================================================
"""
Q1) Why do we override __str__ in Python?
A1) To provide a human-readable string representation of the object 
    instead of the default memory address output.

Q2) What is the difference between __str__ and __repr__?
A2) __str__ → For end users, should be readable.
    __repr__ → For developers, should be unambiguous (used for debugging).

Q3) What happens if we don't implement __str__?
A3) Python prints something like:
    <__main__.LinkedList object at 0x00000234...>

Q4) Can __str__ be used for debugging?
A4) Yes, often __str__ or __repr__ are implemented to easily inspect
    linked list content during development.

Q5) What is the complexity of printing a linked list?
A5) O(n) because it visits each node once.
"""
