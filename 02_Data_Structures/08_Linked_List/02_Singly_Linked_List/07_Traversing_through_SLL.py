"""
========================================================
TOPIC: Traversing Nodes in a Singly Linked List
========================================================
In this note, we are learning:
1. What is traversal
2. Why traversal is important
3. How traversal works internally
4. Code implementation
5. Pointer flow visualization
6. Time and space complexity analysis
7. Interview questions & answers

--------------------------------------------------------
WHAT IS TRAVERSAL?
--------------------------------------------------------
Traversal means visiting each node of the linked list one by one
and performing an operation (like printing values, counting nodes, 
or searching for an element).

In an array, traversal is easy because of indexes, 
but in a linked list, we must start from the head node and 
follow the `next` pointers until we reach the end (`None`).

--------------------------------------------------------
WHY IS TRAVERSAL IMPORTANT?
--------------------------------------------------------
- To display all nodes
- To search for an element
- To apply operations like sum, min, max, etc.
- Forms the basis of many algorithms like:
    • reverse linked list
    • detect loops
    • find middle node

--------------------------------------------------------
HOW TRAVERSAL WORKS INTERNALLY?
--------------------------------------------------------
Steps:
1) Start with `head` node.
2) Visit current node and perform operation (e.g., print value).
3) Move pointer to next node (`current_node = current_node.next`).
4) Repeat until current_node becomes `None`.

--------------------------------------------------------
CODE IMPLEMENTATION
--------------------------------------------------------
"""
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0
        
    def append(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
        
    def prepend(self,value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1
        
    def insert(self, index, value):
    # 1) Create a new node
        new_node = Node(value)

    # 2) Handle invalid index
        if index < 0 or index > self.length:
            return "Index out of range"
    
    # 3) Insert at head (index 0)
        if index == 0:
            self.prepend(value)      # uses existing prepend()
            return "Inserted Successfully"
        
        # 4) Insert at tail (index == length)
        if index == self.length:
            self.append(value)       # uses existing append()
            return "Inserted Successfully"
        
        # 5) Insert in middle
        temp_node = self.head
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
    
        # 6) Increase length
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
    
    def traverse(self):
        current_node = self.head
        node_number = 1  # Start counting from 1
        while current_node is not None:
            print(f"Node {node_number}: {current_node.value}")
            current_node = current_node.next
            node_number += 1

# TEST
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.prepend(50)
print(new_LinkedList)         
print(new_LinkedList.insert(5,100))  # Valid (append at end)
print(new_LinkedList)
new_LinkedList.traverse()
"""
--------------------------------------------------------
ASCII VISUALIZATION
--------------------------------------------------------
Example Linked List:
Head → [50|•] → [10|•] → [20|•] → [30|•] → [40|•] → [100|None]
Tail -----------------------------------------------^

Pointer movement:
Step 1: current_node = head (50)
Step 2: print 50 → move to 10
Step 3: print 10 → move to 20
Step 4: print 20 → move to 30
Step 5: print 30 → move to 40
Step 6: print 40 → move to 100
Step 7: print 100 → move to None → loop ends.

--------------------------------------------------------
TIME & SPACE COMPLEXITY
--------------------------------------------------------
Time Complexity:
- O(n) → visits every node once.
Space Complexity:
- O(1) → uses only one extra pointer (current_node).

--------------------------------------------------------
INTERVIEW QUESTIONS
--------------------------------------------------------
1) Why is linked list traversal O(n)?
   - Because each node is visited once sequentially.

2) Can we traverse backward in a singly linked list?
   - No, because nodes only have reference to next, 
     not previous (use doubly linked list for that).

3) What happens if head is None?
   - List is empty, so traversal loop never runs.

4) Can traversal modify nodes?
   - Yes, we can change node values or links inside the loop 
     (commonly used in algorithms like reversal).

5) Is recursion good for traversal?
   - Possible but not preferred for very large lists 
     (stack overflow risk). Iterative traversal is safer.

--------------------------------------------------------
KEY TAKEAWAY
--------------------------------------------------------
- Traversal is the foundation for all linked list operations.
- It always takes O(n) time for n nodes.
- Simple pointer iteration makes traversal memory-efficient (O(1)).
"""
