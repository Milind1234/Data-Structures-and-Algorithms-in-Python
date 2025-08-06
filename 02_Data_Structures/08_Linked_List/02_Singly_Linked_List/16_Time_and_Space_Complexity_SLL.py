"""
============================================================
SINGLY LINKED LIST – TIME & SPACE COMPLEXITY (Quick Notes)
============================================================

(1) Creating an Empty SLL
-------------------------
Time Complexity   : O(1)
Space Complexity  : O(1)
Reason            : Only initializes head, tail, and length.
ASCII:
   head → None
   tail → None

(2) append(value)
-----------------
Time Complexity   : O(1)
Space Complexity  : O(1)
Reason            : Tail pointer is maintained → No traversal.
ASCII:
   Before: 10 → 20 → None
   append(30)
   After:  10 → 20 → 30 → None

(3) prepend(value)
------------------
Time Complexity   : O(1)
Space Complexity  : O(1)
Reason            : Insert at start, just update head pointer.
ASCII:
   Before: 10 → 20 → 30 → None
   prepend(5)
   After:  5 → 10 → 20 → 30 → None

(4) insert(index, value)
------------------------
Time Complexity   : O(n)   (may traverse entire list)
Space Complexity  : O(1)
Reason            : Temporary pointer to find index.
ASCII:
   Before: 10 → 30 → 40 → None
   insert(1, 20)
   After:  10 → 20 → 30 → 40 → None

(5) search(value)
-----------------
Time Complexity   : O(n)
Space Complexity  : O(1)
Reason            : May need to check all nodes.
ASCII:
   Search(30)
   10 → 20 → 30 → 40 → None
           ↑ found

(6) traverse()
--------------
Time Complexity   : O(n)
Space Complexity  : O(1)
Reason            : Visits each node once.
ASCII:
   head → 10 → 20 → 30 → 40 → None

(7) get(index)
--------------
Time Complexity   : O(n)
Space Complexity  : O(1)
Reason            : Traverses up to given index.
ASCII:
   get(2)
   10 → 20 → 30 → 40 → None
               ↑ index 2

(8) set_value(index, value)
---------------------------
Time Complexity   : O(n)
Space Complexity  : O(1)
Reason            : Uses get() internally.
ASCII:
   Before: 10 → 20 → 30 → 40 → None
   set_value(2, 35)
   After:  10 → 20 → 35 → 40 → None

(9) pop_first()
---------------
Time Complexity   : O(1)
Space Complexity  : O(1)
Reason            : Remove head directly.
ASCII:
   Before: 10 → 20 → 30 → None
   pop_first()
   After:  20 → 30 → None

(10) pop()
----------
Time Complexity   : O(n)
Space Complexity  : O(1)
Reason            : Must find second last node.
ASCII:
   Before: 10 → 20 → 30 → None
   pop()
   After:  10 → 20 → None

(11) remove(index)
------------------
Time Complexity   : O(n)
Space Complexity  : O(1)
Reason            : Traverse to index-1 and update pointers.
ASCII:
   Before: 10 → 20 → 30 → 40 → None
   remove(2)
   After:  10 → 20 → 40 → None

(12) delete_all()
-----------------
Time Complexity   : O(1)
Space Complexity  : O(1)
Reason            : Just set head & tail = None and length = 0.
ASCII:
   Before: 10 → 20 → 30 → None
   delete_all()
   After:  None

============================================================
"""
