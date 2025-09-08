"""
Problem: Middle of the Linked List (LeetCode 876)

Given the head of a singly linked list, return the middle node of the linked list.

If there are two middle nodes, return the second middle node.

Example 1:
Input:  1 → 2 → 3 → 4 → 5
Output: 3 → 4 → 5

Example 2:
Input:  1 → 2 → 3 → 4 → 5 → 6
Output: 4 → 5 → 6
"""

# ---------------------------------------------------------------
# Brute Force Approach (Using Array)
# ---------------------------------------------------------------
"""
Idea:
- Traverse the linked list and store all nodes in an array.
- The middle node is at index n//2 (0-based indexing).
- Return that node.

Time Complexity: O(n)   (one pass to collect, direct access to middle)
Space Complexity: O(n)  (extra array to store nodes)

⚠️ Downside: Requires O(n) extra space.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BruteForceSolution(object):
    def middleNode(self, head):
        nodes = []
        curr = head
        while curr:
            nodes.append(curr)
            curr = curr.next
        return nodes[len(nodes)//2]


# ---------------------------------------------------------------
# Optimal Approach (Fast and Slow Pointer)
# ---------------------------------------------------------------
"""
Idea:
- Use two pointers: slow and fast.
- Move slow one step at a time, fast two steps at a time.
- When fast reaches the end, slow will be at the middle.
- For even-length lists, this naturally returns the second middle.

Algorithm:
1. Initialize slow = head, fast = head.
2. While fast and fast.next exist:
    - Move slow one step.
    - Move fast two steps.
3. When loop ends, slow points to the middle node.
4. Return slow.

Time Complexity: O(n)   (traverses list once)
Space Complexity: O(1)  (only pointers used)
"""

class OptimalSolution(object):
    def middleNode(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# ---------------------------------------------------------------
# Dry Run Example (Optimal Approach)
# ---------------------------------------------------------------
"""
Example A: head = [1 → 2 → 3 → 4 → 5]

Step 1: Initialize slow=1, fast=1
Step 2: Move pointers:
- Iter 1: slow=2, fast=3
- Iter 2: slow=3, fast=5
- Iter 3: fast=None → stop

Result: slow=3 → return node with value 3 (middle)

--------------------------------------------------

Example B: head = [1 → 2 → 3 → 4 → 5 → 6]

Step 1: Initialize slow=1, fast=1
Step 2: Move pointers:
- Iter 1: slow=2, fast=3
- Iter 2: slow=3, fast=5
- Iter 3: slow=4, fast=None → stop

Result: slow=4 → return node with value 4 (second middle, as required)
"""
