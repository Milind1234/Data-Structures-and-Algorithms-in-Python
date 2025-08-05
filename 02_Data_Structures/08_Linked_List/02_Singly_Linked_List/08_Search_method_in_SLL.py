"""
========================================================
TOPIC: SEARCHING IN SINGLY LINKED LIST
========================================================
In this note, we cover:
1. Linked List basics (quick recap)
2. search_by_index()  → returns index of target value
3. search_by_node_number() → returns node number (1-based)
4. Complexity analysis
5. Example usage
6. Interview questions

--------------------------------------------------------
WHAT IS SEARCH IN LINKED LIST?
--------------------------------------------------------
Search means traversing the linked list to find the first occurrence 
of a given target value.

We do not have random access like arrays, so:
    - We must start from head
    - Traverse each node sequentially
    - Check values until match is found or list ends
--------------------------------------------------------
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
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def prepend(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
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

    # -------------------------------------------
    # 1) INDEX-BASED SEARCH (0-based indexing)
    # -------------------------------------------
    def search_by_index(self, target_value):
        """
        Returns index of first occurrence of target value.
        If not found → 'Value not found'
        
        Example Output:
        Value 40 found at index 4
        """
        current_node = self.head
        index = 0
        while current_node is not None:
            if current_node.value == target_value:
                return f"Value {target_value} found at index {index}"
            current_node = current_node.next
            index += 1
        return f"Value {target_value} not found in the linked list"

    # -------------------------------------------
    # 2) NODE NUMBER-BASED SEARCH (1-based)
    # -------------------------------------------
    def search_by_node_number(self, target_value):
        """
        Returns node number (starting from 1) of target value.
        If not found → 'Node not found'
        
        Example Output:
        Node 5: 40
        """
        current_node = self.head
        node_number = 1
        while current_node is not None:
            if current_node.value == target_value:
                return f"Node {node_number}: {current_node.value}"
            current_node = current_node.next
            node_number += 1
        return f"Value {target_value} not found in the linked list"


# ------------------ USAGE EXAMPLE ----------------------
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.prepend(50)   # 50 --> 10 --> 20 --> 30 --> 40
print("Linked List:", new_LinkedList)

print(new_LinkedList.search_by_index(40))        # → Value 40 found at index 4
print(new_LinkedList.search_by_index(100))       # → Value not found
print(new_LinkedList.search_by_node_number(40))  # → Node 5: 40
print(new_LinkedList.search_by_node_number(100)) # → Node not found


"""
--------------------------------------------------------
COMPLEXITY ANALYSIS
--------------------------------------------------------
- search_by_index()        → O(n)
- search_by_node_number()  → O(n)
- Space Complexity         → O(1)

--------------------------------------------------------
INTERVIEW QUESTIONS
--------------------------------------------------------
1) Why is linked list search O(n)?
   → Because we must traverse nodes one by one from head to tail.

2) Which is better for searching: Array or Linked List?
   → Array (O(1) with index) but insertion/deletion is costly.
     Linked List is better for dynamic insertions/deletions.

3) Why two search methods (index-based vs node number)?
   → Index-based is standard programming style (0-based).
     Node number (1-based) is often used in explanations or diagrams.

4) How to optimize linked list search?
   → Use hashing or additional indexing but at the cost of extra space.
"""
