class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += " ➡  "
            temp_node = temp_node.next
        return result

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

    def delete_all(self):
        """
        ------------------------------------------------------------
        delete_all() Method
        ------------------------------------------------------------
        Pseudo-code:
            1. Set head = None
            2. Set tail = None
            3. Set length = 0
            4. Return success message

        Steps:
            Step 1: Break all node connections by setting head and tail to None
            Step 2: Reset length to 0
            Step 3: Return message "All nodes deleted successfully!"

        ASCII Representation:
            Before:
                head → [10] → [20] → [30] → [40] → [50] → None
                tail → [50]

            After:
                head → None
                tail → None
                length = 0

        Time Complexity: O(1)
        Space Complexity: O(1)
        ------------------------------------------------------------
        """
        self.head = None
        self.tail = None
        self.length = 0
        return "All nodes deleted successfully!"

# Usage
new_linked_list = LinkedList()
new_linked_list.append(10)
new_linked_list.append(20)
new_linked_list.append(30)
new_linked_list.append(40)
new_linked_list.append(50)

print(new_linked_list)                # Before delete_all
print(new_linked_list.delete_all())   # Delete all
print(new_linked_list)                # After delete_all (empty)
