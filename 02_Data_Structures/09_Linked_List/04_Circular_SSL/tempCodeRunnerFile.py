class Node:
    def __init__(self, value):
        self.value = value    
        self.next = None       

class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None       
        self.tail = None       
        self.length = 0        
    
    def append(self, value):
        new_node = Node(value)
        if self.length == 0:                
            self.head = new_node
            self.tail = new_node
            new_node.next = new_node        
        else:                              
            self.tail.next = new_node       
            new_node.next = self.head      
            self.tail = new_node            
        self.length += 1
        
    def Traverse(self):
        current_node = self.head
        while current_node:
            print(current_node.value)
            current_node = current_node.next 
            if current_node == self.head:   
                break

# Driver Code
csLinkedList = CircularSinglyLinkedList()
csLinkedList.append(10)   
csLinkedList.append(20)
csLinkedList.append(30)
csLinkedList.append(40)   