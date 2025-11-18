class Heap:
    def __init__(self , size):
        self.customList = (size + 1) * [None]
        self.heapSize = 0
        self.maxSize = size + 1

def peekofHeap(rootnode):
    if not rootnode:
        return 
    return rootnode.customList[1]
    
def sizeofHeap(rootnode):
    if not rootnode:
        return
    return rootnode.heapSize

def levelOrderTraversal(rootnode):
    if not rootnode or rootnode.heapSize == 0:
        print("Tree is Empty")
        return
    for i in range(1, rootnode.heapSize + 1):
        print(rootnode.customList[i], end=" ")
    print()

def heapifyTreeInsert(rootnode , index , heapType):
    if not rootnode:
        raise ValueError("rootnode is required")
    parentIndex = int(index/2)
    if index <= 1:
        return 
    if heapType == ("Min" or "MIN"):
        if rootnode.customList[index] < rootnode.customList[parentIndex]:
            temp = rootnode.customList[index]
            rootnode.customList[index] = rootnode.customList[parentIndex]
            rootnode.customList[parentIndex] = temp
        heapifyTreeInsert(rootnode , parentIndex , heapType)
    elif heapType == ("Max" or "MAX"):
        if rootnode.customList[index] > rootnode.customList[parentIndex]:
            temp = rootnode.customList[index]
            rootnode.customList[index] = rootnode.customList[parentIndex]
            rootnode.customList[parentIndex] = temp
        heapifyTreeInsert(rootnode , parentIndex , heapType)

def insertNode(rootnode , node_value , heapType):
    if rootnode.heapSize + 1 == rootnode.maxSize:
        return "The Heap Tree is Full"
    rootnode.customList[rootnode.heapSize + 1] = node_value
    rootnode.heapSize += 1
    heapifyTreeInsert(rootnode , rootnode.heapSize , heapType)
    return f"The value {node_value} has been successfully inserted into {heapType} Heap"


newHeap = Heap(8)
insertNode(newHeap,4,"Max")
insertNode(newHeap,5,"Max")
insertNode(newHeap,6,"Max")
insertNode(newHeap,3,"Max")
insertNode(newHeap,2,"Max")
insertNode(newHeap,1,"Max")
insertNode(newHeap,7,"Max")
print("LevelOrderTraversal for Max Heap")
levelOrderTraversal(newHeap)

newHeap1 = Heap(8)
insertNode(newHeap1,4,"Min")
insertNode(newHeap1,5,"Min")
insertNode(newHeap1,6,"Min")
insertNode(newHeap1,3,"Min")
insertNode(newHeap1,2,"Min")
insertNode(newHeap1,1,"Min")
insertNode(newHeap1,7,"Min")
print("LevelOrderTraversal for Min Heap")
levelOrderTraversal(newHeap1)