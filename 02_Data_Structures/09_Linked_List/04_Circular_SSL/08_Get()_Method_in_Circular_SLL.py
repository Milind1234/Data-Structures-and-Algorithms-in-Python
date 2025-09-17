"""
📌 Problem: Implement get() method in a Circular Singly Linked List (CSLL)

You need to extend the CSLL with a get method that:
✅ Retrieves the node at a given index (0 .. length-1)
✅ Traverses the list correctly while maintaining the circular nature
✅ Raises IndexError for invalid indices
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
In a CSLL, nodes are connected in a circle (tail.next → head).
To access a node at a specific index:
1. Start at head
2. Move forward `index` times
3. Return the node at that position

⚠️ Note: Valid indices are [0 .. length-1]
"""

# ---------------------------------------------------------------
# 📝 Algorithm (Get)
# ---------------------------------------------------------------
"""
get(index):
1. If index == -1 return self.tail
1. elif index < 0 or index >= length → raise IndexError
2. Start from head (current_node = self.head)
3. Repeat index times:
   - current_node = current_node.next
4. Return the node at current_node
"""

# ---------------------------------------------------------------
# ✅ Code Implementation
# ---------------------------------------------------------------

class Node:
    def __init__(self, value):
        self.value = value    
        self.next = None       

    def __str__(self):
        return str(self.value)
    
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
        
    def __str__(self):
        if not self.head:
            return "Empty CSLL"
        temp_node = self.head
        result = []
        while True:
            result.append(str(temp_node.value))
            temp_node = temp_node.next
            if temp_node == self.head:
                break
        return "  -->  ".join(result)
    
    def get(self, index):
        if index == -1:
            return self.tail
        elif index < -1 or index >= self.length:
            raise IndexError("Index Out of Range")
        current_node = self.head
        for _ in range(index):
            current_node = current_node.next
        return f"At index {index}, Node {current_node.value} is present"


# ---------------------------------------------------------------
# ▶️ Driver Code
# ---------------------------------------------------------------
if __name__ == "__main__":
    csLinkedList = CircularSinglyLinkedList()
    csLinkedList.append(10)   
    csLinkedList.append(20)
    csLinkedList.append(30)
    csLinkedList.append(40)   
    
    print("CSLL:", csLinkedList)         # 10 --> 20 --> 30 --> 40
    print(csLinkedList.get(2))           # At index 2, Node 30 is present

# ---------------------------------------------------------------
# 📊 Complexity
# ---------------------------------------------------------------
"""
- Time Complexity: O(n) (traverse up to index nodes)
- Space Complexity: O(1) (no extra storage)
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example
# ---------------------------------------------------------------
"""
CSLL: [10  -->  20  -->  30  -->  40]

get(0):
- Start at head → Node 10
- Output: "At index 0, Node 10 is present"

get(2):
- Start at head (10)
- Step 1: move to 20
- Step 2: move to 30
- Output: "At index 2, Node 30 is present"

get(4):
- IndexError (since length = 4, valid indices = 0..3)
"""
