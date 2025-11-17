class AVLNode:
    def __init__(self , data):
        self.data = data
        self.leftchild = None
        self.rightchild = None
        self.height = 1

from collections import deque
def levelOrderTraversal(rootnode):
    if not rootnode:
        return "Tree is Empty"
    queue = deque([rootnode])
    while queue:
        root = queue.popleft()
        print(root.data)

        if root.leftchild:
            queue.append(root.leftchild)
        if root.rightchild:
            queue.append(root.rightchild)


def getHeight(rootnode):
    if not rootnode:
        return 0
    return rootnode.height

def getBalance(rootnode):
    if not rootnode:
        return 0
    return getHeight(rootnode.leftchild) - getHeight(rootnode.rightchild)

def rightRotate(disbalanceNode):
    newRoot = disbalanceNode.leftchild
    disbalanceNode.leftchild = disbalanceNode.leftchild.rightchild
    newRoot.rightchild = disbalanceNode
    disbalanceNode.height = 1 + max(getHeight(disbalanceNode.leftchild) , getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild) , getHeight(newRoot.rightchild))
    return newRoot

def leftRotate(disbalanceNode):
    newRoot = disbalanceNode.rightchild
    disbalanceNode.rightchild = disbalanceNode.rightchild.leftchild
    newRoot.leftchild = disbalanceNode
    disbalanceNode.height = 1 +  max(getHeight(disbalanceNode.leftchild) , getHeight(disbalanceNode.rightchild))
    newRoot.height = 1 + max(getHeight(newRoot.leftchild) , getHeight(newRoot.rightchild))
    return newRoot

def insertNode(rootnode, node_value):
    if not rootnode:
        return AVLNode(node_value)
    elif node_value < rootnode.data:
        rootnode.leftchild =  insertNode(rootnode.leftchild , node_value)
    else:
        rootnode.rightchild = insertNode(rootnode.rightchild , node_value)

    rootnode.height = 1 + max(getHeight(rootnode.leftchild),
                              getHeight(rootnode.rightchild))
    
    balance = getBalance(rootnode)
    
    if balance > 1 and node_value < rootnode.leftchild.data:
        return rightRotate(rootnode)
    
    if balance > 1 and node_value > rootnode.leftchild.data:
        rootnode.leftchild = leftRotate(rootnode.leftchild)
        return rightRotate(rootnode)
    
    if balance < -1 and node_value > rootnode.rightchild.data:
        return leftRotate(rootnode)
    
    if balance < -1 and node_value < rootnode.rightchild.data:
        rootnode.rightchild = rightRotate(rootnode.rightchild)
        return leftRotate(rootnode)
    
    return rootnode

    
if __name__ == "__main__":
    # build the AVL using the insertion sequence you provided
    newAVL = AVLNode(30)
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

    # Level order traversal will print the tree node values in BFS order.
    # (Function left unchanged; you asked not to explain it.)
    print("Level order traversal (BFS) of final AVL tree:")
    levelOrderTraversal(newAVL)
