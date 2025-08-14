
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
        result = ''
        while temp_node is not None:
            result += str(temp_node.value)
            if temp_node.next is not None:
                result += ' -> '
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
    
    def remove_duplicates(self):
        if self.head is None:
            return self
    
        seen = set()
        prev = None
        current = self.head
        removed = 0
    
        while current is not None:
            if current.value in seen:
                # remove current node
                prev.next = current.next
                if current is self.tail:
                    self.tail = prev
                removed += 1
                current = prev.next
            else:
                seen.add(current.value)
                prev = current
                current = current.next
    
        self.length -= removed
        return self
    
new_LinkedList = LinkedList()
new_LinkedList.append(10)
new_LinkedList.append(20)
new_LinkedList.append(30)
new_LinkedList.append(40) 
new_LinkedList.append(20)
new_LinkedList.append(10)
print("Linked List:", new_LinkedList)
new_LinkedList.remove_duplicates()
print("After removing dupicated" ,new_LinkedList)

