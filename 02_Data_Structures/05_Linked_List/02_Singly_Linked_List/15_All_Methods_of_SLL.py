# ============================================================
# Singly Linked List - Full Notes + Implementation
# ============================================================

# ---------------- NODE CLASS ----------------
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


# ---------------- LINKED LIST CLASS ----------------
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.length = 0

    # =======================================================
    # APPEND METHOD
    # =======================================================
    """
    Steps:
    1. Create a new node with given value
    2. If list is empty:
         - head = new_node
         - tail = new_node
    3. Else:
         - tail.next = new_node
         - tail = new_node
    4. Increase length

    ASCII:
    Before: 10 --> 20
    append(30)
    After:  10 --> 20 --> 30

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    # =======================================================
    # PREPEND METHOD
    # =======================================================
    """
    Steps:
    1. Create new node
    2. If list empty:
         - head = new_node
         - tail = new_node
    3. Else:
         - new_node.next = head
         - head = new_node
    4. Increase length

    ASCII:
    Before: 10 --> 20 --> 30
    prepend(5)
    After:  5 --> 10 --> 20 --> 30

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            self.head = new_node
            self.tail = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        self.length += 1

    # =======================================================
    # INSERT METHOD
    # =======================================================
    """
    Steps:
    1. If index == 0: call prepend
    2. If index == length: call append
    3. Else:
         - Traverse to index-1 node
         - new_node.next = temp.next
         - temp.next = new_node
    4. Increase length

    ASCII:
    Before: 10 --> 30 --> 40
    insert(1, 20)
    After:  10 --> 20 --> 30 --> 40

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
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

    # =======================================================
    # POP_FIRST METHOD
    # =======================================================
    """
    Steps:
    1. If length == 0: return "No Node to pop"
    2. popped_node = head
    3. If length == 1:
         - head = None, tail = None
    4. Else:
         - head = head.next
         - popped_node.next = None
    5. Decrease length

    ASCII:
    Before: 10 --> 20 --> 30
    pop_first()
    After:  20 --> 30   (popped: 10)

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
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
        return f"Popped first node: {popped_node.value}"

    # =======================================================
    # POP METHOD
    # =======================================================
    """
    Steps:
    1. If length == 0: return "No Node to Pop"
    2. popped_node = tail
    3. If length == 1:
         - head = None, tail = None
    4. Else:
         - Traverse till second last node
         - tail = second_last, tail.next = None
    5. Decrease length

    ASCII:
    Before: 10 --> 20 --> 30
    pop()
    After:  10 --> 20   (popped: 30)

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def pop(self):
        if self.length == 0:
            return "No Node to Pop"
        popped_node = self.tail
        if self.length == 1:
            self.head = None
            self.tail = None
        else:
            temp_node = self.head
            while temp_node.next != self.tail:
                temp_node = temp_node.next
            self.tail = temp_node
            self.tail.next = None
        self.length -= 1
        return f"Popped last node: {popped_node.value}"

    # =======================================================
    # GET METHOD
    # =======================================================
    """
    Steps:
    1. If index < 0 or index >= length: return None
    2. Traverse index times to reach node
    3. Return node

    ASCII:
    List: 5 --> 10 --> 15 --> 20
    get(2) → Node(15)

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def get(self, index):
        if index < 0 or index >= self.length:
            return None
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return current_node

    # =======================================================
    # REMOVE METHOD
    # =======================================================
    """
    Steps:
    1. If index == 0: call pop_first
    2. Else:
         - Get node before index
         - popped_node = prev.next
         - prev.next = popped_node.next
    3. If removing last node, update tail
    4. Decrease length

    ASCII:
    Before: 5 --> 10 --> 15 --> 20
    remove(2)
    After:  5 --> 10 --> 20  (removed: 15)

    Time Complexity: O(n)
    Space Complexity: O(1)
    """
    def remove(self, index):
        if index < 0 or index >= self.length:
            return "Index out of range"
        if index == 0:
            return self.pop_first()
        prev_node = self.get(index - 1)
        popped_node = prev_node.next
        prev_node.next = popped_node.next
        if index == self.length - 1:
            self.tail = prev_node
        popped_node.next = None
        self.length -= 1
        return f"Removed node with value {popped_node.value} from index {index}"

    # =======================================================
    # DELETE_ALL METHOD
    # =======================================================
    """
    Steps:
    1. Set head = None
    2. Set tail = None
    3. Set length = 0

    ASCII:
    Before: 10 --> 20 --> 30
    delete_all()
    After:  (empty list)

    Time Complexity: O(1)
    Space Complexity: O(1)
    """
    def delete_all(self):
        self.head = None
        self.tail = None
        self.length = 0
        return "All nodes deleted!"

    # =======================================================
    # STRING REPRESENTATION
    # =======================================================
    def __str__(self):
        temp_node = self.head
        result = ""
        while temp_node:
            result += str(temp_node.value)
            if temp_node.next:
                result += " --> "
            temp_node = temp_node.next
        return result


# ============================================================
# USAGE EXAMPLE
# ============================================================
if __name__ == "__main__":
    ll = LinkedList()
    ll.append(10)
    ll.append(20)
    ll.append(30)
    ll.prepend(5)
    ll.insert(2, 15)
    print("Linked List:", ll)
    print(ll.pop_first())
    print("After Pop First:", ll)
    print(ll.pop())
    print("After Pop Last:", ll)
    print(ll.remove(1))
    print("After Remove Index 1:", ll)
    print(ll.delete_all())
    print("After Delete All:", ll)
