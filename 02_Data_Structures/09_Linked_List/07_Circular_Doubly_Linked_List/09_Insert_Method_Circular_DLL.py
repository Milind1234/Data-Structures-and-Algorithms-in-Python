
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
    # 2️⃣ Prepend() → Insert node at the beginning
    # ---------------------------------------------------------------
    def prepend(self, value):
        new_node = Node(value)
        if self.length == 0:
            # Case 1: Empty CDLL
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node
            new_node.prev = new_node
        else:
            # Case 2: Non-Empty CDLL
            new_node.next = self.head
            new_node.prev = self.tail
            self.head.prev = new_node
            self.tail.next = new_node
            self.head = new_node

        self.length += 1

    # ---------------------------------------------------------------
    # 3️⃣ __str__() → String Representation
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
    # 4️⃣ get_node(index) → Get node by index
    # ---------------------------------------------------------------
    def get_node(self, index):
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
        return current_node
    
    # ---------------------------------------------------------------
    # 5️⃣ insert(index,value) → insert node at given index
    # ---------------------------------------------------------------
    
    def insert(self, index , value):
        if index < 0 or index > self.length:
            return "Index out of Bound"
        if index == 0 :
            self.prepend(value)
            return
        if index == self.length:
            self.append(value)
            return
        new_node  = Node(value)
        temp_node = self.get_node(index - 1)
        new_node.next = temp_node.next
        new_node.prev = temp_node
        temp_node.next.prev = new_node
        temp_node.next = new_node
        self.length += 1
        
    # -----------------------------------------------------------------------------
    # 5️⃣ insert_direct(index,value) → insert node without using helper func
    # -----------------------------------------------------------------------------
    
    def insert_direct(self , index , value):
        new_node = Node(value)
        #case 1 : Invalid Index
        if index < 0 or index > self.length:
            return "Index out of Bound"
        
        # case 2 : Insert at start (head)
        if index == 0:
            if self.length == 0:
                self.head = new_node
                self.tail = new_node
                new_node.next = new_node
            else:
                new_node.prev = self.head
                new_node.next = self.tail
                self.head.prev = new_node
                self.tail.next = new_node
            self.length += 1
            
        # case 3 : Insert at end(tail)
        if index == self.length:
            new_node.prev = self.tail
            new_node.next = self.head
               
    
# ---------------------------------------------------------------
# ✅ How to Use & Test
# ---------------------------------------------------------------
if __name__ == "__main__":
    CDLL = CircularDoublyLinkedList()
    CDLL.append(10)
    CDLL.append(20)
    CDLL.append(30)
    CDLL.append(40)
    CDLL.append(50)
    print("before insert :", CDLL)
    
    CDLL.insert(0,100)
    print("After insert 100 at index 0:",CDLL)
    
    CDLL.insert(3,110)
    print("After insert 3 at at index 3:",CDLL)
    
    CDLL.insert(8,120)
    print("After insert 120 at index 8:",CDLL)
    
    print("After insert 200 at index 10:",CDLL.insert(10,200))
    