"""
======================================================
APPEND METHOD 
======================================================

----------------------------------------------
1) NODE CLASS
----------------------------------------------
"""
class Node:
    def __init__(self, value):
        self.value = value    # stores node value
        self.next = None      # pointer to next node

"""
----------------------------------------------
2) LINKED LIST CLASS
----------------------------------------------
"""
class LinkedList:
    def __init__(self):
        self.head = None      # first node (initially None)
        self.tail = None      # last node (initially None)
        self.length = 0       # size of linked list

    # --------------------------
    # APPEND METHOD
    # --------------------------
    def append(self, value):
        # Step 1: Create new node
        new_node = Node(value)   # O(1)

        # Step 2: Check if linked list is empty
        if self.head is None:
            # Empty list → new node becomes head & tail
            self.head = new_node
            self.tail = new_node
        else:
            # Non-empty list → attach new node at end
            self.tail.next = new_node
            self.tail = new_node

        # Step 3: Increase length
        self.length += 1

    # --------------------------
    # PRINT LIST METHOD
    # --------------------------
    def print_list(self):
        # Start from head
        temp = self.head
        while temp is not None:
            print(temp.value, end=" -> ")
            temp = temp.next
        print("None")  # end of linked list

"""
----------------------------------------------
3) USAGE EXAMPLE
----------------------------------------------
"""
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)

print("Length:", new_linked_list.length)  # Output: 3
print("Elements:")
new_linked_list.print_list()              # Output: 10 -> 20 -> 30 -> None

"""
----------------------------------------------
4) TIME & SPACE COMPLEXITY
----------------------------------------------
APPEND:
- Time: O(1) → Constant time insertion at end
- Space: O(1) → Only one new node created

PRINT_LIST:
- Time: O(n) → Traverses entire linked list
- Space: O(1) → No extra data structures used

----------------------------------------------
5) INTERVIEW POINTS
----------------------------------------------
- Use tail pointer for O(1) append.
- print_list() helps verify insertion visually.
- Complexity:
    • append() → O(1)
    • print_list() → O(n)
"""
