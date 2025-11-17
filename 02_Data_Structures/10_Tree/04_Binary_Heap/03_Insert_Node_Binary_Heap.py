class Heap:
    def __init__(self , size):
        self.customList = (size+1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekOfHeap(rootnode):
    if not rootnode:
        return "Tree is Empty"
    else:
        return rootnode.customList[1]
        
def sizeOfHeap(rootnode): 
    if not rootnode:
        return "Tree is Empty"
    else:
        return rootnode.heapSize
    
def levelOrderTraversal(rootnode):
    if not rootnode:
        return "Tree is Empty"
    else:
        for i in range(1 , rootnode.heapSize+1):
            print(rootnode.customList[i])
    
newBinaryHeap = Heap(5)
print(sizeOfHeap(newBinaryHeap))

