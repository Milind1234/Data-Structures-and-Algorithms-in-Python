# note.py
# ------------------------------------------------------
# 📘 Circular Doubly Linked List (CDLL) - Notes File
# ✅ Topic: Time and Space Complexity of CDLL
# ------------------------------------------------------

"""
📌 Problem: Time and Space Complexity of Circular Doubly Linked List (CDLL)

This file summarizes the **time complexity** and **space complexity**
for the most common operations on a CDLL.

✅ All operations take O(1) extra space (constant overhead per operation).
✅ Time complexity varies depending on whether traversal is needed.
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
A Circular Doubly Linked List (CDLL) is a linear data structure where each node has:
  • value
  • pointer to next node
  • pointer to previous node

The list tracks:
  • head (first node)
  • tail (last node)
  • length (number of nodes)

Additionally:
  • head.prev points to tail
  • tail.next points to head
  → making the structure circular.

Operations can be:
- O(1) if they involve only head/tail pointer updates.
- O(n) if traversal is required (search, insert at middle, remove at middle, etc.).
"""

# ---------------------------------------------------------------
# 📝 Time & Space Complexities
# ---------------------------------------------------------------
"""
Operation           Time Complexity        Space Complexity
-----------------------------------------------------------
Create              O(1)                   O(1)
Append              O(1)                   O(1)
Prepend             O(1)                   O(1)
Insert (middle)     O(n)                   O(1)
Search              O(n)                   O(1)
Traverse            O(n)                   O(1)
Reverse Traverse    O(n)                   O(1)
Get (by index)      O(n)                   O(1)
Set (update value)  O(n)                   O(1)
Pop First           O(1)                   O(1)
Pop Last            O(1)                   O(1)
Remove (by index)   O(n)                   O(1)
Delete all nodes    O(1)                   O(1)
"""

# ---------------------------------------------------------------
# ✅ Explanation of Each Operation
# ---------------------------------------------------------------
"""
1. Create
   - Initialize head, tail, length.
   - Time = O(1), Space = O(1).

2. Append (add to end)
   - Use tail pointer, update tail.next, head.prev, and reassign tail.
   - Time = O(1), Space = O(1).

3. Prepend (add to head)
   - Update head.prev, tail.next, and reassign head.
   - Time = O(1), Space = O(1).

4. Insert (at index)
   - Traverse to index-1 before inserting.
   - Time = O(n), Space = O(1).

5. Search (find value)
   - Traverse nodes until found.
   - Time = O(n), Space = O(1).

6. Traverse (forward)
   - Visit all nodes from head (stop when head repeats).
   - Time = O(n), Space = O(1).

7. Reverse Traverse (backward)
   - Visit all nodes from tail (stop when tail repeats).
   - Time = O(n), Space = O(1).

8. Get (node by index)
   - Must traverse to index (optimized by choosing head/tail).
   - Time = O(n), Space = O(1).

9. Set (update node value at index)
   - Traverse to node, then update value.
   - Time = O(n), Space = O(1).

10. Pop First (remove head)
    - Update head = head.next, fix circular links.
    - Time = O(1), Space = O(1).

11. Pop Last (remove tail)
    - Update tail = tail.prev, fix circular links.
    - Time = O(1), Space = O(1).

12. Remove (by index)
    - Traverse to index, unlink node.
    - Time = O(n), Space = O(1).

13. Delete all nodes
    - Set head = tail = None, length = 0.
    - Time = O(1), Space = O(1).
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example for Operations
# ---------------------------------------------------------------
"""
Consider CDLL: [10 ⇄ 20 ⇄ 30 ⇄ 40] (circular)

1. Append(50):
   tail = 50, links updated
   Result: [10 ⇄ 20 ⇄ 30 ⇄ 40 ⇄ 50] (circular)
   Time = O(1)

2. Prepend(5):
   head = 5, links updated
   Result: [5 ⇄ 10 ⇄ 20 ⇄ 30 ⇄ 40 ⇄ 50] (circular)
   Time = O(1)

3. Insert(3, 25):
   Traverse to index 2 (O(n))
   Link 20 ⇄ 25 ⇄ 30
   Result: [5 ⇄ 10 ⇄ 20 ⇄ 25 ⇄ 30 ⇄ 40 ⇄ 50]
   Time = O(n)

4. Pop First():
   head moves to 10, circular links preserved
   Result: [10 ⇄ 20 ⇄ 25 ⇄ 30 ⇄ 40 ⇄ 50]
   Time = O(1)

5. Pop Last():
   tail moves to 40, circular links preserved
   Result: [10 ⇄ 20 ⇄ 25 ⇄ 30 ⇄ 40]
   Time = O(1)

6. Remove(25):
   Search + unlink 25
   Result: [10 ⇄ 20 ⇄ 30 ⇄ 40]
   Time = O(n)
"""

# ---------------------------------------------------------------
# 📊 Summary Table (as Python dict)
# ---------------------------------------------------------------
cdll_complexities = {
    "Create":          {"time": "O(1)", "space": "O(1)"},
    "Append":          {"time": "O(1)", "space": "O(1)"},
    "Prepend":         {"time": "O(1)", "space": "O(1)"},
    "Insert":          {"time": "O(n)", "space": "O(1)"},
    "Search":          {"time": "O(n)", "space": "O(1)"},
    "Traverse":        {"time": "O(n)", "space": "O(1)"},
    "Reverse Traverse":{"time": "O(n)", "space": "O(1)"},
    "Get":             {"time": "O(n)", "space": "O(1)"},
    "Set":             {"time": "O(n)", "space": "O(1)"},
    "Pop First":       {"time": "O(1)", "space": "O(1)"},
    "Pop Last":        {"time": "O(1)", "space": "O(1)"},
    "Remove":          {"time": "O(n)", "space": "O(1)"},
    "Delete all nodes":{"time": "O(1)", "space": "O(1)"},
}

if __name__ == "__main__":
    from pprint import pprint
    print("Time and Space Complexity of CDLL Operations:\n")
    pprint(cdll_complexities)
