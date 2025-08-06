# ------------------ NODE CLASS ------------------------
class Node:
    def __init__(self, value):
        self.value = value     # Data stored in the node
        self.next = None       # Pointer to the next node


"""
------------------------------------------------------------
LinkedList Class
------------------------------------------------------------
Handles various linked list operations:
    - append()    → Add node at the end
    - prepend()   → Add node at the start
    - insert()    → Insert node at a given index
    - pop_first() → Remove first node
    - pop()       → Remove last node
    - remove()    → Remove node at a given index (focus of this note)
    - get()       → Get node at index
    - __str__()   → String representation of list
------------------------------------------------------------
remove(index) → Remove a node at a given index
------------------------------------------------------------
Steps:
1) Validate index:
   - If index < 0 or index >= length → return "Index out of range"
2) If index == 0 → directly call pop_first()
3) Else:
    - Find the previous node (index-1) using get(index-1)
    - Store the node to be removed (popped_node = prev_node.next)
    - Link previous node to popped_node.next
4) If removed node is the last node → update tail = prev_node
5) Disconnect removed node’s next pointer (popped_node.next = None)
6) Decrement length
7) Return success message with removed node’s value
------------------------------------------------------------
Time Complexity:
- O(n) → Because we traverse the list to reach index-1
- Space Complexity: O(1)
------------------------------------------------------------
Pointer Visualization:
Before removal at index=2:
    head
     ↓
    50 → 10 → 20 → 30 → 40 → None
               ↑
               index=2 (Node to remove = 20)

After removal:
    head
     ↓
    50 → 10 ─────────→ 30 → 40 → None
                (node 20 is disconnected)
------------------------------------------------------------
Example:
Linked List: 50 → 10 → 20 → 30 → 40
remove(2) → Removes node with value 20
Result: 50 → 10 → 30 → 40
------------------------------------------------------------
"""

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
        for _ in range(index - 1):
            temp_node = temp_node.next
        new_node.next = temp_node.next
        temp_node.next = new_node
        self.length += 1
        return "Inserted Successfully"

    def pop_first(self):
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
        return f"Using Pop first method, we popped out the first node that is --> {popped_node.value}"

    def pop(self):
        if self.length == 0:
            return "No Node to Pop"
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next is not self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            temp_node.next = None
        self.length -= 1
        return f"Using Pop method, we popped out the Last node that is --> {popped_node.value}"

    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    def remove(self, index):
        if index < 0 or index >= self.length:
            return "Index out of range"
        if index == 0:
            return self.pop_first()
        if index == self.length:
            return self.pop()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        if index == self.length - 1:  # removing tail
            self.tail = prev_node
        popped_node.next = None
        self.length -= 1
        return f"Removed node with value {popped_node.value} from index {index}"

    def __str__(self):
        temp_node = self.head
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' → '
            temp_node = temp_node.next
        return result


# ------------------- USAGE EXAMPLE --------------------
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40)
new_LinkedList.prepend(50)    # Final: 50 → 10 → 20 → 30 → 40
print("Initial Linked List:", new_LinkedList)

# Removing node at index 2
print("------------------------------------------------------")
print(new_LinkedList.remove(2))  # Removes value 20
print("After removal at index 2:", new_LinkedList)
