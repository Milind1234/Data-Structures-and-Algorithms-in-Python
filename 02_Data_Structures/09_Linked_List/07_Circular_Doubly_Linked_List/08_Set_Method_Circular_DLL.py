# 🔷 Node Structure
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None  # backward pointer for doubly linked

    def __str__(self):
        return str(self.value)


# 🔷 Circular Doubly Linked List (CDLL)
class CircularDoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0   # initially empty list has 0 length

    # ---------------------------------------------------------------
    # 1️⃣ Append() → Insert node at the end
    # ---------------------------------------------------------------
    def append(self, value):
        new_node = Node(value)
        # Case 1: Empty CDLL
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Case 2: Non-Empty CDLL
            new_node.prev = self.tail
            new_node.next = self.head
            self.tail.next = new_node
            self.head.prev = new_node
            self.tail = new_node

        self.length += 1

    # ---------------------------------------------------------------
    # 2️⃣ __str__() → String Representation
    # ---------------------------------------------------------------
    def __str__(self):
        if self.head is None:
            return "Empty CDLL"
        result = []
        current_node = self.head
        while True:
            result.append(str(current_node.value))
            current_node = current_node.next
            if current_node == self.head:
                break
        return " ◀——▶ ".join(result)

    # ---------------------------------------------------------------
    # 3️⃣ get_node(index) → Get node by index
    # ---------------------------------------------------------------
    def get_node(self, index):
        """
        Purpose:
        Retrieve the node present at a specific index (0-based).

        Steps:
        1. If index < 0 or index >= length → return None (invalid index).
        2. If index is in the **first half** of the list:
             - Start from head.
             - Move forward index times.
        3. If index is in the **second half** of the list:
             - Start from tail.
             - Move backward until index is reached.
        4. Return the node’s value with its index.

        🔍 Visualization:

        CDLL = [10] ◀──▶ [20] ◀──▶ [30] ◀──▶ [40] ◀──▶ [50]

        get_node(1):
        - index=1 is in the first half (head → forward)
        - Traverse: head=10 → next=20
        - Return: "At index 1 Node 20 is present"

        get_node(4):
        - index=4 is in the second half (tail → backward)
        - Traverse: tail=50 (index=4) → found immediately
        - Return: "At index 4 Node 50 is present"

        ⏱️ Time Complexity:
        - Best: O(1) → index at head or tail
        - Average/Worst: O(n/2) → half traversal from closer end
        - Overall: O(n)

        ⏱️ Space Complexity:
        - O(1) → no extra memory used
        """
        if index < 0 or index >= self.length:
            return None

        current_node = None
        if index < self.length // 2:
            # Closer to head → move forward
            current_node = self.head
            for _ in range(index):
                current_node = current_node.next
        else:
            # Closer to tail → move backward
            current_node = self.tail
            for _ in range(self.length - 1, index, -1):
                current_node = current_node.prev

        return f"At index {index} Node {current_node.value} is present"
