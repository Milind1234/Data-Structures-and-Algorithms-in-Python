"""
Time and Space Complexity of List Operations in Python

1. Creating an Empty List
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   Explanation: Just initializes an empty list object with metadata like length and capacity.

2. Creating a List with N Elements
   - Time Complexity: O(n)
   - Space Complexity: O(n)
   Explanation: Allocates memory for n elements and initializes them.

3. Inserting a Value in a List
   - Time Complexity: O(n) [Worst case: inserting at the beginning]
   - Space Complexity: O(1)
   Explanation: Inserting at index 0 shifts all elements right. No extra space is needed.

4. Traversing a List
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   Explanation: Must visit every element, but no additional space is used.

5. Accessing a Given Cell (Index)
   - Time Complexity: O(1)
   - Space Complexity: O(1)
   Explanation: Direct access using index is constant time and requires no extra space.

6. Searching for a Value (Linear Search)
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   Explanation: May have to check all elements. Space remains constant.

7. Deleting a Value from the List
   - Time Complexity: O(n)
   - Space Complexity: O(1)
   Explanation: Deleting shifts all elements left, but no new space is used.

Summary:
- Most operations have space complexity O(1), except creation which is O(n) when elements are added.
- Access is fast (O(1)), but insertions/deletions at ends/middle can cost O(n) in time.
"""
