# Time and Space Complexity for Tuple Operations

"""
1. Tuple Creation
-----------------
- Time Complexity: O(1)
  Reason: All elements are defined upfront, no resizing.
- Space Complexity: O(n)
  Reason: Requires memory proportional to number of elements (n).

2. Traversing Tuple
--------------------
- Time Complexity: O(n)
  Reason: Each element is visited once.
- Space Complexity: O(1)
  Reason: No additional memory is needed.

3. Accessing an Element by Index
---------------------------------
- Time Complexity: O(1)
  Reason: Direct index-based access.
- Space Complexity: O(1)
  Reason: No extra memory usage.

4. Searching for an Element
----------------------------
- Time Complexity: O(n)
  Reason: Uses linear search (checks elements one by one).
- Space Complexity: O(1)
  Reason: No extra memory is required.

Note:
- Tuples are immutable, so update & delete operations on elements are not allowed.
- Immutability ensures faster read performance and allows tuples to be hashable (usable as dictionary keys).
"""

# Summary Table
"""
+---------------------------+------------------+------------------+
| Operation                 | Time Complexity  | Space Complexity |
+---------------------------+------------------+------------------+
| Tuple Creation            | O(1)            | O(n)            |
| Traversing Tuple          | O(n)            | O(1)            |
| Accessing Element (Index) | O(1)            | O(1)            |
| Searching Element         | O(n)            | O(1)            |
+---------------------------+------------------+------------------+
"""
