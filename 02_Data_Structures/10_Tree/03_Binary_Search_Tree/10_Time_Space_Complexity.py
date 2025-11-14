r"""
📘 Topic: Time & Space Complexity Summary for Binary Search Tree (BST)
======================================================================

🎯 Goal:
--------
To summarize the **time and space complexities** of all major operations we performed
on a Binary Search Tree (BST) using Linked List implementation.

This includes:
- Create BST  
- Insert Node  
- Traverse BST  
- Search Node  
- Delete Node  
- Delete Entire BST  


======================================================================
🌳 1. Create Binary Search Tree
======================================================================

✔ We only initialize **one root node**  
✔ No traversal, no recursion

⏱ Time Complexity: **O(1)**  
📦 Space Complexity: **O(1)**  


======================================================================
🌳 2. Insert a Node (BST Insert Operation)
======================================================================

Insertion follows BST property:

- If value ≤ root → go to left subtree  
- If value > root → go to right subtree  
- Continue until empty spot found  

Since each decision divides the tree roughly in half → recursion depth = height of tree.

⏱ Time Complexity:  
- **O(log N)** → For balanced BST  
- Worst case (skewed tree) → O(N)

📦 Space Complexity:  
- **O(log N)** (due to recursive calls stored on the stack)  
- Worst case (skewed) → O(N)


======================================================================
🌳 3. Traverse BST (Preorder / Inorder / Postorder / Level-order)
======================================================================

Traversal must visit **every node exactly once**, so:

⏱ Time Complexity: **O(N)**  
📦 Space Complexity:  
- For DFS (Pre/In/Post): O(N) recursive stack  
- For BFS (Level-order): O(N) queue storage  

Therefore: **O(N)** space complexity for traversal.


======================================================================
🌳 4. Search for a Node in BST
======================================================================

BST search narrows the search path:

- If target < root → left subtree  
- If target > root → right subtree  

Same behavior as binary search logic on a tree.

⏱ Time Complexity:  
- **O(log N)** (balanced)  
- **O(N)** (skewed)

📦 Space Complexity:  
- **O(log N)** (recursive stack)  
- Worst case → O(N)


======================================================================
🌳 5. Delete Node from BST
======================================================================

Deletion also requires searching first.  
So complexity matches the search behavior.

⏱ Time Complexity:  
- **O(log N)** (balanced)  
- **O(N)** (skewed tree)

📦 Space Complexity:  
- **O(log N)** recursion depth  
- Worst case → O(N)


======================================================================
🌳 6. Delete Entire BST
======================================================================

We simply:
- Set `root.data = None`
- Set `root.leftchild = None`
- Set `root.rightchild = None`

Python garbage collector removes remaining nodes automatically.

⏱ Time Complexity: **O(1)**  
📦 Space Complexity: **O(1)**  


======================================================================
📊 Summary Table
======================================================================

Operation                     | Time      | Space
------------------------------|-----------|---------
Create BST                    | O(1)      | O(1)
Insert Node                   | O(log N)  | O(log N)
Search Node                   | O(log N)  | O(log N)
Delete Node                   | O(log N)  | O(log N)
Traverse BST                  | O(N)      | O(N)
Delete Entire BST             | O(1)      | O(1)


======================================================================
✅ Section Completed — Binary Search Tree
======================================================================

✔ You learned structure and rules of BST  
✔ Performed ALL main BST operations  
✔ Understood complexities for each one  
✔ Built recursive logic for insert, search, delete  
✔ Mastered traversal using queues and recursion  

🔜 **Next Section: AVL Tree**  
A self-balancing BST with guaranteed O(log N) height.

See you in the next section! 🌱
"""
