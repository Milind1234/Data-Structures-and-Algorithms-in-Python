"""
===================================================
🔁 CIRCULAR SINGLY LINKED LIST (CSLL)
===================================================

✅ Problem Statement:
Implement a Circular Singly Linked List (CSLL) that 
supports:
1. Node creation
2. Append (insert at end)
3. Traversal (printing all nodes in circular order)

---------------------------------------------------
📥 Example:
csLinkedList = CircularSinglyLinkedList()
csLinkedList.append(10)
csLinkedList.append(20)
csLinkedList.append(30)
csLinkedList.append(40)

Output:
Head: 10
Tail: 40
Tail.next: 10
Length: 4
Traverse: 10 → 20 → 30 → 40

---------------------------------------------------
🛠️ Explanation of Operations:

1. APPEND (Insert at end)
--------------------------------
Case 1 → Empty list:
- head = new_node
- tail = new_node
- new_node.next = new_node (points to itself)

Case 2 → Non-empty list:
- tail.next = new_node
- new_node.next = head
- tail = new_node

Increment length.

Iteration Walkthrough (append 10, 20, 30, 40):
- Append 10 → head=10, tail=10, tail.next=10, length=1
- Append 20 → tail.next=20, 20.next=head(10), tail=20, length=2
- Append 30 → tail.next=30, 30.next=head(10), tail=30, length=3
- Append 40 → tail.next=40, 40.next=head(10), tail=40, length=4

---------------------------------------------------
2. TRAVERSE
--------------------------------
Start from head and keep moving using next pointers:
- Stop when you come back to head (circular stop condition).
- Prevents infinite loop.

Iteration Walkthrough:
List: 10 → 20 → 30 → 40 → back to 10
Steps:
- current_node = head(10) → print(10)
- move to 20 → print(20)
- move to 30 → print(30)
- move to 40 → print(40)
- next = head → stop

---------------------------------------------------
🧾 Code:
"""

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

print("Head:", csLinkedList.head.value)   
print("Tail:", csLinkedList.tail.value)   
print("Tail.next:", csLinkedList.tail.next.value) 
print("Length:", csLinkedList.length)    
csLinkedList.Traverse()

"""
---------------------------------------------------
⏱ Complexity:

Append:
- Time: O(1)  (always updates tail and head links)
- Space: O(1)

Traverse:
- Time: O(n)  (visits each node once)
- Space: O(1)

===================================================
"""
