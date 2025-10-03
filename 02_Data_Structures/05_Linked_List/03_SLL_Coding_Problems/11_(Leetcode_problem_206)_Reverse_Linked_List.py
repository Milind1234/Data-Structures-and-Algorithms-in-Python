"""
Problem: Reverse Linked List (LeetCode 206)

You are given the head of a singly linked list.
Return the head of the list after reversing it.

Example:
Input:  1 → 2 → 3 → 4 → 5
Output: 5 → 4 → 3 → 2 → 1
"""

# ---------------------------------------------------------------
# Brute Force Approach (using extra space)
# ---------------------------------------------------------------
"""
Idea:
- Traverse the linked list and store all values in an array.
- Then reconstruct a new linked list in reverse order using that array.
- Finally, return the new head.

Time Complexity: O(n)   (one pass to store values, one pass to rebuild list)
Space Complexity: O(n)  (extra array to store node values)

⚠️ Downside: Uses extra space and builds a new list instead of reversing in place.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BruteForceSolution(object):
    def reverseList(self, head):
        if not head:
            return None
        
        # Step 1: Collect values in an array
        values = []
        current = head
        while current:
            values.append(current.val)
            current = current.next
        
        # Step 2: Build new reversed list
        dummy = ListNode(-1)
        curr = dummy
        for val in reversed(values):
            curr.next = ListNode(val)
            curr = curr.next
        
        return dummy.next


# ---------------------------------------------------------------
# Optimal Approach (Iterative - In-place Reversal)
# ---------------------------------------------------------------
"""
Idea:
We reverse the pointers of the linked list one by one using 3 pointers:
1. prev → keeps track of the reversed part (initially None)
2. current → the node we are currently processing
3. temp → saves the next node so we don’t lose it when changing links

Algorithm:
1. Initialize prev = None, current = head
2. While current exists:
    - Save next node: temp = current.next
    - Reverse the link: current.next = prev
    - Move prev forward: prev = current
    - Move current forward: current = temp
3. When loop ends, prev points to the new head.
4. Return prev.

Time Complexity: O(n)   (we traverse list once)
Space Complexity: O(1)  (no extra space used)
"""

class OptimalSolution(object):
    def reverseList(self, head):
        prev = None
        current = head
        while current:
            temp = current.next   # save next node
            current.next = prev   # reverse pointer
            prev = current        # move prev forward
            current = temp        # move current forward
        return prev


# ---------------------------------------------------------------
# Dry Run Example
# ---------------------------------------------------------------
"""
Input: 1 → 2 → 3 → None

Initial:
prev = None
current = 1

Step 1:
temp = 2
current.next = prev   → 1 → None
prev = 1
current = 2

Step 2:
temp = 3
current.next = prev   → 2 → 1 → None
prev = 2
current = 3

Step 3:
temp = None
current.next = prev   → 3 → 2 → 1 → None
prev = 3
current = None

Loop ends → return prev (which is 3)

Final Output: 3 → 2 → 1 → None
"""
