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
print("Traversing through Linked List")
new_LinkedList.traverse()