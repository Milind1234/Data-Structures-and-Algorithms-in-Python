import QueueLinkedList as queue

class AVLTreeNode:
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










if __name__ == "__main__":
    # Create small AVL-like tree manually to demo traversals & search
    # Structure (balanced example):
    #           40
    #        /      \
    #      20        60
    #     /  \      /  \
    #   10   30   50   70

    root = AVLTreeNode(40)

    root.leftchild = AVLTreeNode(20)
    root.rightchild = AVLTreeNode(60)

    root.leftchild.leftchild = AVLTreeNode(10)
    root.leftchild.rightchild = AVLTreeNode(30)

    root.rightchild.leftchild = AVLTreeNode(50)
    root.rightchild.rightchild = AVLTreeNode(70)


    print("\n🔎 Search Examples:")
    print("Search 60:", searchNodeAVL(root, 60))
    print("Search 25:", searchNodeAVL(root, 25))  # not present

    # Single-node example (creation)
    newAVL = AVLTreeNode(10)
    print("\n📌 Single-node AVL created with data =", newAVL.data)
