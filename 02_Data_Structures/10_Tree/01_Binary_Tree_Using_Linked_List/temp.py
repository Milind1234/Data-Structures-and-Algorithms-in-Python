
# -----------------------------
# IMPORT CUSTOM QUEUE
# -----------------------------
import QueueLinkedList as queue  # Custom queue (from previous module)

# -----------------------------
# CLASS DEFINITION
# -----------------------------
class TreeNode:
    def __init__(self, data):
        """
        📘 Constructor (__init__):
        -------------------------
        Creates a new Binary Tree Node.

        Attributes:
        -----------
        data       : Node value
        leftchild  : Pointer to left node
        rightchild : Pointer to right node
        """
        self.data = data
        self.leftchild = None
        self.rightchild = None


# -----------------------------
# TREE CREATION
# -----------------------------
newBT = TreeNode("1")
leftchild = TreeNode("2")
rightchild = TreeNode("3")

newBT.leftchild = leftchild
newBT.rightchild = rightchild

N4 = TreeNode("4")
N5 = TreeNode("5")
leftchild.leftchild = N4
leftchild.rightchild = N5

N6 = TreeNode("6")
rightchild.leftchild = N6


r"""
Tree Visualization:
-------------------
                 1
               /   \
             2       3
            / \     / \
           4   5   6   7
"""

# =============================================================
# 📊 LEVEL ORDER TRAVERSAL (for Visualization)
# =============================================================
def levelOrderTraversal_LinkedList(rootnode):
    """
    Prints the Binary Tree nodes level by level using custom queue.
    """
    if not rootnode:
        return
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootnode)

        while not(customQueue.isEmpty()):
            root = customQueue.dequeue()
            print(root.value.data)
            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)


def insertBT(newNode , rootNode):
    if not rootNode:
        rootNode = newNode
        return " Root Node created Successfully"
    else:
        customQueue = queue.Queue()
        customQueue.enqueue(rootNode)
        while not (customQueue.isEmpty()):
            root = customQueue.dequeue()

            if root.value.leftchild is not None:
                customQueue.enqueue(root.value.leftchild)
            else:
                root.value.leftchild = newNode
                return "Inserted Succesfully"
            
            if root.value.rightchild is not None:
                customQueue.enqueue(root.value.rightchild)
            else:
                root.value.rightchild = newNode
                return "Inserted Successfully"
            
from collections import deque
def insertBT_Deque(rootnode , newNode):
    if not rootnode:
        rootnode = newNode
        return "Inserted"
    else:
        queue = deque([rootnode])
        while queue:
            current = queue.popleft()

            if current.leftchild is None:
                current.leftchild = newNode
                return "Node inserted Successfully"
            else:
                queue.append(current.leftchild)
            
            if current.rightchild is None:
                current.rightchild = newNode
                return "Inserted"
            else:
                queue.append(current.rightchild)


levelOrderTraversal_LinkedList(newBT)
newNode = TreeNode("7")
print(insertBT_Deque(newBT,newNode))
levelOrderTraversal_LinkedList(newBT)