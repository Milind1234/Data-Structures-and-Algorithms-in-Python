"""
======================================================
PRINTING LINKED LIST USING __str__ METHOD
======================================================

----------------------------------------------
1) NODE CLASS
----------------------------------------------
"""
class Node:
    def __init__(self, value):
        self.value = value     # stores node value
        self.next = None       # pointer to next node

"""
----------------------------------------------
2) LINKED LIST CLASS
----------------------------------------------
"""
class LinkedList:
    def __init__(self):
        self.head = None       # start of linked list
        self.tail = None       # end of linked list
        self.length = 0        # number of nodes

    # --------------------------
    # __str__ METHOD
    # --------------------------
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            # Add node value
            result += str(temp_node.value)
            # Add arrow if there is next node
            if temp_node.next is not None:
                result += " --> "
            temp_node = temp_node.next
        return result

    # --------------------------
    # APPEND METHOD
    # --------------------------
    def append(self, value):
        new_node = Node(value)
        if self.head is None:   # empty linked list
            self.head = new_node
            self.tail = new_node
        else:                   # list already has nodes
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

"""
----------------------------------------------
3) USAGE EXAMPLE
----------------------------------------------
"""
new_Linked_List = LinkedList()
new_Linked_List.append(10)
new_Linked_List.append(20)
new_Linked_List.append(30)
new_Linked_List.append(40)
new_Linked_List.append(50)
new_Linked_List.append(60)

print(new_Linked_List)  
# Output: 10 --> 20 --> 30 --> 40 --> 50 --> 60

"""
----------------------------------------
DETAILED EXPLANATION OF __str__ METHOD
----------------------------------------

1) temp_node = self.head
   - Starts traversal from the head node.

2) result = ""
   - Stores string version of linked list.

3) while temp_node is not None:
   - Traverses until last node (None).

4) result += str(temp_node.value)
   - Adds node value to string.

5) if temp_node.next is not None:
       result += " --> "
   - Adds arrow only if another node exists.

6) temp_node = temp_node.next
   - Moves to next node.

7) return result
   - Returns final readable string.

----------------------------------------
EXAMPLE TRACE
----------------------------------------
Linked list: head → [10|next] → [20|next] → [30|None]

Iteration steps:
- Iteration 1:
    temp_node = 10
    result = "10 --> "
- Iteration 2:
    temp_node = 20
    result = "10 --> 20 --> "
- Iteration 3:
    temp_node = 30
    result = "10 --> 20 --> 30"
- End (temp_node = None)

FINAL OUTPUT:
10 --> 20 --> 30

ASCII VISUALIZATION:
Head ──► [10] ──► [20] ──► [30] ──► None
"""

"""
----------------------------------------------
4) WHY USE __str__ METHOD?
----------------------------------------------
- Overrides default object printing.
- Makes linked list output human-readable.
- Automatically called when using print(object).

----------------------------------------------
5) COMPLEXITY
----------------------------------------------
- Time Complexity: O(n) → traverses all nodes
- Space Complexity: O(1) → no extra data structures

----------------------------------------------
6) INTERVIEW POINTS
----------------------------------------------
- __str__ gives readable string representation.
- print(object) → automatically calls __str__.
- Useful for debugging & verifying linked list visually.
"""
