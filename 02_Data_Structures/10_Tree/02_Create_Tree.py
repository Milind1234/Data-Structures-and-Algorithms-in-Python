"""
📘 Topic: General Tree — Drinks Example

Purpose:
---------
To understand how to create a **General Tree (N-ary Tree)** in Python, 
where each node can have multiple children.

This example builds a tree structure for "Drinks" with categories and subcategories
like Hot, Cold, Tea, Coffee, etc.

We also learn how to:
✅ Create nodes
✅ Add children to nodes
✅ Recursively print the entire tree hierarchy
✅ Understand recursion, indentation, and data structure relationships
"""

# -----------------------------
# CLASS DEFINITION
# -----------------------------

class TreeNode:
    def __init__(self, data, children=[]):
        """
        📘 Constructor (__init__):
        -------------------------
        - Initializes a tree node with `data` (value) and `children` (list of subnodes).
        
        Parameters:
        -----------
        data : str/int/any
            The value stored in the node (example: "Drinks", "Hot", "Tea", etc.)
        children : list (optional)
            A list that holds references to child TreeNode objects.

        Example:
        --------
        node = TreeNode("Drinks", [])
        → Creates a root node named "Drinks" with no children yet.

        Internal Working:
        -----------------
        self.data = data           # stores the data (node label)
        self.children = children   # stores the child nodes in a list
        """
        self.data = data
        self.children = children


    def addchild(self, TreeNode):
        """
        📘 addchild() Method:
        ---------------------
        - Adds a new child node to the current node.
        - Helps dynamically build tree branches.

        Parameters:
        -----------
        TreeNode : TreeNode object
            The node that will be appended as a child to the current node.

        Example:
        --------
        root.addchild(TreeNode("Hot", []))
        → Adds a new node "Hot" under "Drinks"

        Internal Working:
        -----------------
        self.children.append(TreeNode)
        → Adds the new child node to the children list of the current node.
        """
        self.children.append(TreeNode)


    def str(self, level=0):
        """
        📘 str() Method (Recursive Tree Printer):
        -----------------------------------------
        - Recursively prints the entire tree in a structured format.
        - Each level of the tree is indented to visualize hierarchy.

        Parameters:
        -----------
        level : int (default=0)
            Represents the depth of the current node in the tree.
            Used to control indentation.

        Working Process:
        ----------------
        1️⃣ Start with the current node’s data.
            → ret = " " * level + str(self.data) + "\n"
            → Adds indentation based on depth level.

        2️⃣ For each child in the node’s children list:
            → Call the same function recursively with level+1.
            → This ensures deeper levels get more indentation.

        3️⃣ Keep combining (concatenating) results into a string.

        4️⃣ Finally, return the whole formatted tree as a string.

        Example of Recursion Flow:
        --------------------------
        Drinks
         Hot
          Tea
           Green Tea
           Black Tea
          Coffee
           Latte
           Cappuccino
         Cold
          Soda
           Coke
           Pepsi
          Juice
           Apple Juice
           Orange Juice
        """
        ret = "   " * level + str(self.data) + "\n"
        for child in self.children:
            ret += child.str(level + 1)
        return ret


# -----------------------------
# TREE CONSTRUCTION
# -----------------------------

# Root node
tree = TreeNode("Drinks", [])

# Adding level 1 children
tree.addchild(TreeNode("Hot", []))
tree.addchild(TreeNode("Cold", []))

# Adding level 2 children to "Hot"
hot = tree.children[0]
hot.addchild(TreeNode("Tea", []))
hot.addchild(TreeNode("Coffee", []))

# Adding level 2 children to "Cold"
cold = tree.children[1]
cold.addchild(TreeNode("Soda", []))
cold.addchild(TreeNode("Juice", []))

# Adding level 3 children to "Tea"
Tea = hot.children[0]
Tea.addchild(TreeNode("Green Tea", []))
Tea.addchild(TreeNode("Black Tea", []))

# Adding level 3 children to "Coffee"
Coffee = hot.children[1]
Coffee.addchild(TreeNode("Latte", []))
Coffee.addchild(TreeNode("Cappuccino", []))

# Adding level 3 children to "Soda"
Soda = cold.children[0]
Soda.addchild(TreeNode("Coke", []))
Soda.addchild(TreeNode("Pepsi", []))

# Adding level 3 children to "Juice"
Juice = cold.children[1]
Juice.addchild(TreeNode("Apple Juice", []))
Juice.addchild(TreeNode("Orange Juice", []))


# -----------------------------
# PRINT TREE
# -----------------------------

print(tree.str())

"""
🌳 OUTPUT (Tree Structure Visualization):

Drinks
 Hot
  Tea
   Green Tea
   Black Tea
  Coffee
   Latte
   Cappuccino
 Cold
  Soda
   Coke
   Pepsi
  Juice
   Apple Juice
   Orange Juice
"""

# -----------------------------
# EXPLANATION
# -----------------------------

"""
📘 How it Works (Step-by-Step):

1️⃣ A `TreeNode` object is created for each node.
    Example: TreeNode("Drinks") → Root node.

2️⃣ We add child nodes using `addchild()`.
    Example:
        tree.addchild(TreeNode("Hot", []))
        tree.addchild(TreeNode("Cold", []))
    → Adds Hot and Cold as children of Drinks.

3️⃣ Each category (Hot, Cold) further gets its own subcategories using the same pattern.

4️⃣ The `str()` function recursively prints each node:
    - Starts with Drinks
    - Prints its children (Hot, Cold)
    - Then recursively prints Hot’s and Cold’s children.

5️⃣ Recursion continues until a node has no children.

🔁 Recursion Tree Example (for "Hot"):
--------------------------------------
str("Hot", level=1)
 → prints " Hot"
 → calls str() on Tea (level=2)
 → calls str() on Coffee (level=2)
 → returns the combined string

📊 Time Complexity:
-------------------
O(n)
→ Each node is visited exactly once.

💾 Space Complexity:
--------------------
O(h)
→ Where 'h' is the height of the tree (because of recursion call stack).
"""

# -----------------------------
# VISUALIZATION IDEA
# -----------------------------

"""
Drinks
├── Hot
│   ├── Tea
│   │   ├── Green Tea
│   │   └── Black Tea
│   └── Coffee
│       ├── Latte
│       └── Cappuccino
└── Cold
    ├── Soda
    │   ├── Coke
    │   └── Pepsi
    └── Juice
        ├── Apple Juice
        └── Orange Juice
"""
