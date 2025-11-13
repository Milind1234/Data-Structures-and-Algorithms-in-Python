class BinaryTree:
    def __init__(self, size):
        self.customList = size * [None]
        self.lastUsedIndex = 0
        self.maxsize = size

    def __str__(self):
        return f"The Binary Tree Array -> {self.customList[1:self.lastUsedIndex+1]}"
    
    def insertNode(self , node_value):
        if self.lastUsedIndex + 1 == self.maxsize:
            return " The Binary tree is Full"
        self.customList[self.lastUsedIndex + 1 ] = node_value
        self.lastUsedIndex += 1
        return f"The Node {node_value} is Inserted Successfully"
    
    def levelOrderTraversal(self , index):
        for i in range(index, self.lastUsedIndex+1):
            print(self.customList[i])

    def deleteNodeBT(self , delete_value):
        if self.lastUsedIndex == 0:
            return "There is no node to delete"
        for i in range(1,self.lastUsedIndex+1):
            if self.customList[i] == delete_value:
                self.customList[i] = self.customList[self.lastUsedIndex]
                self.customList[self.lastUsedIndex] = None
                self.lastUsedIndex -= 1
                return f"The Node {delete_value} has been successfully deleted"

newBT = BinaryTree(9)

print(newBT.insertNode("1"))
print(newBT.insertNode("2"))
print(newBT.insertNode("3"))
print(newBT.insertNode("4"))
print(newBT.insertNode("5"))
print(newBT.insertNode("6"))
print(newBT.insertNode("7"))

print(newBT)

print(newBT.deleteNodeBT("3"))
newBT.levelOrderTraversal(1)