"""
Problem: Palindrome Linked List (LeetCode 234)

Given the head of a singly linked list, return True if it is a palindrome,
and False otherwise.

Example 1:
Input:  1 → 2 → 2 → 1
Output: True

Example 2:
Input:  1 → 2
Output: False

Constraints:
- The number of nodes is in the range [1, 10^5].
- Node values are between 0 and 9.
"""
# ---------------------------------------------------------------
# Brute Force Approach (Using Array)
# ---------------------------------------------------------------
"""
Idea:
- Traverse the linked list and store all values in an array.
- A list is a palindrome if it equals its reverse.
- Compare array with its reversed version.
- Return True if equal, otherwise False.

Time Complexity: O(n)   (one pass to collect, one pass to compare)
Space Complexity: O(n)  (extra array storage)

⚠️ Downside: Requires O(n) extra space.
"""

class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class BruteForceSolution(object):
    def isPalindrome(self, head):
        arr = []
        curr = head
        while curr:
            arr.append(curr.val)
            curr = curr.next
        return arr == arr[::-1]


# ---------------------------------------------------------------
# Optimal Approach (Fast/Slow Pointer + Reverse Second Half)
# ---------------------------------------------------------------
"""
Idea:
- Use two pointers (slow and fast) to find the middle of the list.
- If length is odd, skip the middle element.
- Reverse the second half of the list in place.
- Compare the first half with the reversed second half.
- If all values match → palindrome, else not.

Algorithm:
1. Edge case: If list has 0 or 1 node → return True
2. Use slow/fast pointers to find middle.
   - slow moves one step, fast moves two steps.
   - When fast reaches end → slow at middle.
3. If odd length → move slow one step forward (skip middle).
4. Reverse second half of list starting from slow.
5. Compare first half (from head) with reversed half.
6. Return True if all matched, else False.

Time Complexity: O(n)   (find middle + reverse + compare = linear)
Space Complexity: O(1)  (reversing in place, just pointers)
"""

class OptimalSolution(object):
    def isPalindrome(self, head):
        if not head or not head.next:
            return True
        
        # Step 1: Find middle
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Step 2: If odd length, skip middle
        if fast:
            slow = slow.next
        
        # Step 3: Reverse second half
        prev = None
        while slow:
            nxt = slow.next
            slow.next = prev
            prev = slow
            slow = nxt
        
        # Step 4: Compare first half and reversed second half
        left, right = head, prev
        while right:
            if left.val != right.val:
                return False
            left = left.next
            right = right.next
        return True


# ---------------------------------------------------------------
# Dry Run Example (Optimal Approach)
# ---------------------------------------------------------------
"""
Example: head = [1 → 2 → 2 → 1]

Step 1: Find middle
- slow = 1, fast = 1
- Move: slow=2, fast=2 (3rd node)
- Move: slow=2 (3rd node), fast=None
=> middle found at slow (3rd node)

Step 2: Reverse second half (2 → 1)
- Iter 1: prev=2, slow=1
- Iter 2: prev=1 → 2, slow=None
Reversed half = [1 → 2]

Step 3: Compare halves
- left=1, right=1 → match
- left=2, right=2 → match
right=None → stop

All matched → return True


Example: head = [1 → 2]
Step 1: Find middle → slow=2, fast=None
Step 2: Reverse half → prev=2
Step 3: Compare → left=1, right=2 → mismatch → return False
"""
