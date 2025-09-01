# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

# A Node contains:
# - value: the data
# - next: pointer to the next node


# 🔷 LinkedList Structure
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # 🟢 Append: Add element at the end
    def append(self, value):
        new_node = Node(value)
        if self.head is None:       # If list is empty
            self.head = new_node
            self.tail = new_node
        else:                       # Link new node at the end
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # 🟢 Find Middle: Using Slow & Fast Pointers
    def find_middle(self):
        """
        This method finds the middle node of the linked list.
        Technique: Slow & Fast Pointer
        - slow pointer moves 1 step at a time
        - fast pointer moves 2 steps at a time
        When fast reaches end, slow will be at middle
        """
        slow = self.head
        fast = self.head

        # Traverse until fast reaches end
        while fast is not None and fast.next is not None:
            slow = slow.next           # Move 1 step
            fast = fast.next.next      # Move 2 steps

        return slow  # slow now points to the middle node


# ----------------------------------------------------------
# 📝 EXAMPLE USAGE
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)

middle_node = new_linked_list.find_middle()
print("Middle Node Value:", middle_node.value)
# Output: Middle Node Value: 30
# ----------------------------------------------------------


"""
📌 STEP-BY-STEP EXECUTION & VISUALIZATION

🔹 Initial Linked List:
    [10] -> [20] -> [30] -> [40] -> [50] -> None
     ↑slow
     ↑fast

🔹 Iteration 1:
    slow moves 1 step →  [20]
    fast moves 2 steps → [30]

    [10] -> [20] -> [30] -> [40] -> [50] -> None
             ↑slow
                     ↑fast

🔹 Iteration 2:
    slow moves 1 step →  [30]
    fast moves 2 steps → [50]

    [10] -> [20] -> [30] -> [40] -> [50] -> None
                      ↑slow
                                      ↑fast

🔹 Iteration 3:
    fast.next is None → STOP
    slow is at [30] → MIDDLE NODE FOUND

✅ Middle Node = 30

------------------------------------------------------
⏳ TIME COMPLEXITY:
    - O(n)  → Traverses the list once

📦 SPACE COMPLEXITY:
    - O(1)  → Uses only two extra pointers (slow & fast)

💡 INTERVIEW TIP:
    - Works for both odd & even length lists
    - If list has even nodes, slow will point to the second middle node
------------------------------------------------------
"""
