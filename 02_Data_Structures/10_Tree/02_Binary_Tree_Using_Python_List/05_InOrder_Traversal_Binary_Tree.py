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
    
    def inOrderTraversal(self , index):
        if index > self.lastUsedIndex:
            return 
        self.inOrderTraversal(index * 2)
        print(self.customList[index])
        self.inOrderTraversal((index * 2) + 1)


newBT = BinaryTree(9)

print(newBT.insertNode("1"))
print(newBT.insertNode("2"))
print(newBT.insertNode("3"))
print(newBT.insertNode("4"))
print(newBT.insertNode("5"))
print(newBT.insertNode("6"))
print(newBT.insertNode("7"))

print(newBT)
newBT.inOrderTraversal(1)

