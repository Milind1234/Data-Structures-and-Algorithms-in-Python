import QueueLinkedList as queue

class AVLNode:
    def __init__(self , data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1

def preOrderTraversal(rootnode):
    if not rootnode:
        return "Tree is Empty"
    print(rootnode.data)
    preOrderTraversal(rootnode.leftchild)
    preOrderTraversal(rootnode.rightchild)

def inOrderTraversal(rootnode):
    if not rootnode:
        return "Tree is Empty"
    inOrderTraversal(rootnode.leftchild)
    print(rootnode.data)
    inOrderTraversal(rootnode.rightchild)

def postOrderTraversal(rootnode):
    if not rootnode:
        return "Tree is Empty"
    postOrderTraversal(rootnode.leftchild)
    postOrderTraversal(rootnode.rightchild)
    print(rootnode.data)

def levelOrderTraversal(rootnode):
    if not rootnode:
        return "Tree is Empty"
    customQueue = queue.Queue()
    customQueue.enqueue(rootnode)
    while not(customQueue.isEmpty()):
        root = customQueue.dequeue()
        print(root.value.data)
        if root.value.leftchild is not None:
            customQueue.enqueue(root.value.leftchild)
        if root.value.rightchild is not None:
            customQueue.enqueue(root.value.rightchild)

def searchNodeAVL(rootnode , target_node):
    if not rootnode:
        return "Target Not Found"
    
    if rootnode.data == target_node:
        return f"The Target {target_node} is Found"
    
    if target_node < rootnode.data:
        return searchNodeAVL(rootnode.leftchild , target_node)

    if target_node > rootnode.data:
        return searchNodeAVL(rootnode.rightchild , target_node)
    

def getHeight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftchild
    disbalanceNode.leftchild = disbalanceNode.leftchild.rightchild
    newRoot.rightchild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild) , getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild), getHeight(newRoot.rightchild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightchild
    disbalanceNode.rightchild = disbalanceNode.rightchild.leftchild
    newRoot.leftchild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild) , getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild) , getHeight(newRoot.rightchild))
    return newRoot

def getBalance(rootnode):
    if not rootnode:
        return 0
    return getHeight(rootnode.leftchild) - getHeight(rootnode.rightchild)

def insertNode(rootnode , nodevalue):
    if not rootnode:
        return AVLNode(nodevalue)
    elif nodevalue < rootnode.data:
        rootnode.leftchild = insertNode(rootnode.leftchild ,nodevalue)
    else:
        rootnode.rigthchild = insertNode(rootnode.rightchild ,nodevalue)

    rootnode.height = 1 + max(getHeight(rootnode.leftchild) , getHeight(rootnode.rightchild))
    balance = getBalance(rootnode)
    if balance > 1 and nodevalue < rootnode.leftchild.data:
        return rightRotate(rootnode)
    if balance > 1 and nodevalue > rootnode.leftchild.data:
        rootnode.leftchild = leftRotate(rootnode.leftchild)
        return rightRotate(rootnode)
    if balance < -1 and nodevalue > rootnode.rightchild.data:
        return leftRotate(rootnode)
    if balance < -1 and nodevalue < rootnode.leftchild.data:
        rootnode.rightchild = rightRotate(rootnode.rigthchild)
        return leftRotate(rootnode)


newAVL = AVLNode(70)
newAVL = insertNode(newAVL, 30)
newAVL = insertNode(newAVL, 25)
newAVL = insertNode(newAVL, 35)
newAVL = insertNode(newAVL, 20)
newAVL = insertNode(newAVL, 15)
newAVL = insertNode(newAVL, 5)
newAVL = insertNode(newAVL, 10)
newAVL = insertNode(newAVL, 50)
newAVL = insertNode(newAVL, 60)
newAVL = insertNode(newAVL, 70)
newAVL = insertNode(newAVL, 65) 
levelOrderTraversal(newAVL)
