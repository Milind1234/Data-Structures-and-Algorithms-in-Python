"""
📌 Problem: Time and Space Complexity of Circular Singly Linked List (CSLL)

This file summarizes the **time complexity** and **space complexity**
for the most common operations on a CSLL.

✅ All operations take O(1) space (constant extra memory).
✅ Time complexity varies depending on whether traversal is needed.
"""

# ---------------------------------------------------------------
# 🧠 Idea
# ---------------------------------------------------------------
"""
A Circular Singly Linked List (CSLL) is like a normal singly linked list,
except the tail points back to the head, forming a circle.

- Each node stores:
  • value
  • pointer to the next node
- The list tracks:
  • head (first node)
  • tail (last node, whose next points to head)
  • length (number of nodes)

Operations can be:
- O(1) if they only involve pointer updates (head/tail).
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
Get (by index)      O(n)                   O(1)
Set (update value)  O(n)                   O(1)
Pop First           O(1)                   O(1)
Pop Last            O(n)                   O(1)
Remove (by index)   O(n)                   O(1)
Delete all nodes    O(1)                   O(1)
"""

# ---------------------------------------------------------------
# ✅ Explanation of Each Operation
# ---------------------------------------------------------------
"""
1. Create
   - Just initializes head, tail, length.
   - Time = O(1), Space = O(1).

2. Append (add to end)
   - Direct access to tail, update pointers.
   - Time = O(1), Space = O(1).

3. Prepend (add to head)
   - Direct access to head, update pointers.
   - Time = O(1), Space = O(1).

4. Insert (at index)
   - Must traverse to index-1 before inserting.
   - Time = O(n), Space = O(1).

5. Search (find value)
   - Traverse until match or circle completes.
   - Time = O(n), Space = O(1).

6. Traverse (print all nodes)
   - Visit each node exactly once.
   - Time = O(n), Space = O(1).

7. Get (node by index)
   - Must traverse until index.
   - Time = O(n), Space = O(1).

8. Set (update node value at index)
   - Requires traversal to index.
   - Time = O(n), Space = O(1).

9. Pop First (remove head)
   - Move head pointer, update tail.next.
   - Time = O(1), Space = O(1).

10. Pop Last (remove tail)
    - Must traverse to node before tail.
    - Time = O(n), Space = O(1).

11. Remove (delete node by index)
    - Traverse to index-1 to unlink.
    - Time = O(n), Space = O(1).

12. Delete all nodes
    - Set head = tail = None, length = 0.
    - Time = O(1), Space = O(1).
"""

# ---------------------------------------------------------------
# 🔎 Dry Run Example for Operations
# ---------------------------------------------------------------
"""
Consider CSLL: [10 → 20 → 30 → 40] (tail.next = head)

1. Append(50):
   tail = 50, tail.next = head
   Result: [10 → 20 → 30 → 40 → 50]
   Time = O(1)

2. Prepend(5):
   head = 5, tail.next = head
   Result: [5 → 10 → 20 → 30 → 40 → 50]
   Time = O(1)

3. Insert(3, 25):
   Traverse to index 2 (O(n))
   Link 20 → 25 → 30
   Result: [5 → 10 → 20 → 25 → 30 → 40 → 50]
   Time = O(n)

4. Search(40):
   Traverse nodes until 40 is found
   Time = O(n)

5. Pop First():
   head moves to 10, tail.next = 10
   Result: [10 → 20 → 25 → 30 → 40 → 50]
   Time = O(1)

6. Pop Last():
   Traverse until node before 50
   tail = 40, tail.next = head
   Result: [10 → 20 → 25 → 30 → 40]
   Time = O(n)

7. Delete all():
   head = None, tail = None, length = 0
   Result: []
   Time = O(1)
"""

# ---------------------------------------------------------------
# 📊 Summary Table (as Python dict)
# ---------------------------------------------------------------
csll_complexities = {
    "Create":          {"time": "O(1)", "space": "O(1)"},
    "Append":          {"time": "O(1)", "space": "O(1)"},
    "Prepend":         {"time": "O(1)", "space": "O(1)"},
    "Insert":          {"time": "O(n)", "space": "O(1)"},
    "Search":          {"time": "O(n)", "space": "O(1)"},
    "Traverse":        {"time": "O(n)", "space": "O(1)"},
    "Get":             {"time": "O(n)", "space": "O(1)"},
    "Set":             {"time": "O(n)", "space": "O(1)"},
    "Pop First":       {"time": "O(1)", "space": "O(1)"},
    "Pop Last":        {"time": "O(n)", "space": "O(1)"},
    "Remove":          {"time": "O(n)", "space": "O(1)"},
    "Delete all nodes":{"time": "O(1)", "space": "O(1)"},
}

if __name__ == "__main__":
    from pprint import pprint
    print("Time and Space Complexity of CSLL Operations:\n")
    pprint(csll_complexities)
