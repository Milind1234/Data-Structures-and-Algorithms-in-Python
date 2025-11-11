# =====================================================
# 📘 INFORMATION ABOUT TREE (Notes File)
# =====================================================
"""
A **Tree** is a **non-linear data structure** that represents **hierarchical relationships**
between its elements and does **not contain any cycle**.  
It is basically the reversed form of a real-life tree — the **root** is at the **top**,  
and the branches (children) grow **downward**.

---------------------------------------------------------
🔹 WHY IS TREE IMPORTANT?
---------------------------------------------------------
Unlike linear data structures (arrays, linked lists, stacks, queues),
where data is stored sequentially, **trees organize data hierarchically**.  
This helps to:
- Perform faster access and lookup.
- Represent naturally hierarchical data.
- Build flexible and efficient storage models.

Tree structures are used in:
- 📂 File systems (folders → subfolders → files)
- 🧭 Organization hierarchy
- 🌐 XML / HTML DOM representation
- 🔍 Binary Search Trees, Heaps, Tries, and many more.

---------------------------------------------------------
🔹 REAL-LIFE EXAMPLE (Cafe Menu Analogy)
---------------------------------------------------------
Drinks
│
├── Hot
│   ├── Tea → {Green, Black}
│   └── Coffee → {Americano, Latte, Cappuccino}
│
└── Cold
    ├── Non-alcoholic → {Cola, Fanta, Soda}
    └── Alcoholic → {Wine, Beer}

Each main category has subcategories — this is a **hierarchical relationship**.
When we move one step down, we become more specialized.

---------------------------------------------------------
🔹 PROPERTIES OF TREE DATA STRUCTURE
---------------------------------------------------------
1️⃣ **Hierarchical Representation**  
   - Represents data in parent-child form.

2️⃣ **Components of Each Node**  
   - Data (actual information)
   - References to subcategories (children links)

3️⃣ **Base Category and Subcategories**  
   - Topmost category (root) → base.
   - Lower categories → subcategories.

Example (from lecture):
- Root → "Drinks"
- Children → "Hot", "Cold"
- Subchildren → "Tea", "Coffee", etc.

---------------------------------------------------------
🔹 WHY DO WE NEED TREE DATA STRUCTURE?
---------------------------------------------------------
✅ Linear structures become slower as data grows (O(n) traversal).  
✅ Trees allow **faster, structured access**.

Reasons we use Trees:
- To store **hierarchical data** (folders, DOM, org charts).
- To **reduce search time** (e.g., Binary Search Trees).
- To provide **logarithmic complexity** with balancing (AVL, Red-Black).
- To support **multi-way branching** (B-Trees for databases).

📘 Example:
- Binary Search Tree (BST) → Efficient search/insert/delete.
- AVL Tree → Self-balancing tree with guaranteed O(log n) search.
- File System → Folders within folders, all hierarchically stored.

---------------------------------------------------------
🔹 TREE TERMINOLOGY
---------------------------------------------------------

📈 * Diagram:*


             N1
           /    \
         N2      N3
       /  |  \
     N4   N5   N6
    / \
  N7   N8


1️⃣ **Root** — Top node without a parent.  
    Example: N1

2️⃣ **Edge** — Link between a parent and a child.  
    Example: N1 → N2

3️⃣ **Leaf** — Node that has no children.  
    Example: N7, N8, N5, N6

4️⃣ **Sibling** — Children of the same parent.  
    Example: N4 and N5 are siblings.

5️⃣ **Ancestor** — Parent, grandparent, or great-grandparent of a node.  
    Example: Ancestors of N7 → {N4, N2, N1}

6️⃣ **Depth of Node** — Number of edges from the root to the node.  
    Example: depth(N4) = 2  (N1→N2→N4)

7️⃣ **Height of Node** — Number of edges from the node to the deepest leaf.  
    Example: height(N3) = 1  (N3→N6)

8️⃣ **Depth of Tree** — Depth of root node (always 0).

9️⃣ **Height of Tree** — Height of root node (no. of edges to deepest leaf).  
    Example: height(Tree) = 3 (N1→N2→N4→N7)


  
-----------------------------------------------------------------------|
|🔹 COMPARISON BETWEEN DEPTH & HEIGHT                                  |
-----------------------------------------------------------------------|
| Concept     | Definition                            | Example        |
|-------------|---------------------------------------|----------------|
| Depth       | Distance from root to node            | Depth(N4) = 2  |
| Height      | Distance from node to deepest leaf    | Height(N3) = 1 |
| Tree Depth  | Depth of root = 0                     | Root (N1)      |
| Tree Height | Height of root = longest path to leaf | 3              |

---------------------------------------------------------
🔹 COMPLEXITY ANALYSIS (GENERAL)
---------------------------------------------------------
- Traversal (DFS / BFS): **O(n)**
- Insertion / Deletion / Search:
  - Unbalanced Tree → O(n)
  - Balanced Tree (AVL / Red-Black) → O(log n)
- Space Complexity → O(n)

---------------------------------------------------------
🔹 PYTHON REPRESENTATION OF A TREE NODE
---------------------------------------------------------
"""

# =====================================================
# 🔹 Tree Node Implementation
# =====================================================

class TreeNode:
    """
    Represents a node in a tree.
    Each node contains data and references (children).
    """
    def __init__(self, data):
        self.data = data
        self.children = []  # list of child TreeNode objects

    def add_child(self, child):
        """Add a new child to this node"""
        self.children.append(child)

    def __repr__(self):
        return f"TreeNode({self.data})"


# =====================================================
# 🔹 BUILDING SAMPLE TREE (From Lecture)
# =====================================================
def build_sample_tree():
    r"""
    Builds the sample tree shown in lecture:
        N1
       /  \
     N2    N3
    / \     \
   N4  N5   N6
  / \
 N7 N8
    """
    N1 = TreeNode("N1")
    N2, N3 = TreeNode("N2"), TreeNode("N3")
    N4, N5, N6 = TreeNode("N4"), TreeNode("N5"), TreeNode("N6")
    N7, N8 = TreeNode("N7"), TreeNode("N8")

    N1.add_child(N2); N1.add_child(N3)
    N2.add_child(N4); N2.add_child(N5)
    N3.add_child(N6)
    N4.add_child(N7); N4.add_child(N8)

    return N1


# =====================================================
# 🔹 CALCULATE DEPTH OF A NODE
# =====================================================
def node_depth(root, target, current_depth=0):
    """Return the depth of the given target node."""
    if root == target:
        return current_depth
    for child in root.children:
        depth = node_depth(child, target, current_depth + 1)
        if depth is not None:
            return depth
    return None


# =====================================================
# 🔹 CALCULATE HEIGHT OF A NODE
# =====================================================
def node_height(node):
    """Return the height of a node (edges to deepest leaf)."""
    if not node.children:
        return 0
    return 1 + max(node_height(child) for child in node.children)


# =====================================================
# 🔹 DEMONSTRATION
# =====================================================
if __name__ == "__main__":
    root = build_sample_tree()
    N2 = root.children[0]
    N4 = N2.children[0]
    N3 = root.children[1]

    print("Depth of N4:", node_depth(root, N4))   # 2
    print("Height of N3:", node_height(N3))       # 1
    print("Height of Tree:", node_height(root))   # 3


# =====================================================
# 🔹 SUMMARY
# =====================================================
"""
✅ A Tree is a non-linear, hierarchical data structure with no cycles.
✅ Each node contains data and references to subnodes.
✅ Used widely in filesystems, databases, parsers, search algorithms, etc.
✅ Depth → Root to Node
✅ Height → Node to Deepest Leaf
✅ Tree’s height = Height of root node
✅ Traversals and operations typically O(n)
✅ Specialized trees (BST, AVL, Red-Black) optimize performance
"""
