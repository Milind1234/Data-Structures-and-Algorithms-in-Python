# 🚀 LeetCode 203. Remove Linked List Elements
# --------------------------------------------
# ✅ Problem:
# Given the head of a linked list and an integer val,
# remove all nodes from the list that have Node.val == val.
#
# Example:
# Input:  head = [1,2,6,3,4,5,6], val = 6
# Output: [1,2,3,4,5]
#
# --------------------------------------------
# ✅ Approach:
# 1. Use a **dummy node** pointing to the head.
#    - Handles edge case where head itself must be removed.
# 2. Use two pointers:
#    - prev → last valid node
#    - current → node under inspection
# 3. Traverse list:
#    - If current.val == val → skip it (prev.next = current.next).
#    - Else → move prev forward (prev = current).
#    - Always move current forward (current = current.next).
# 4. Return dummy.next (the real head).
#
# Time Complexity: O(n)  ⏳
# Space Complexity: O(1) 📦


# --------------------------------------------
# 🔹 Definition of Linked List Node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def removeElements(self, head, val):
        """
        Removes all nodes with value == val from linked list.
        """
        # 🟢 Step 1: Create dummy node
        dummy = ListNode(-1)
        dummy.next = head

        # 🟢 Step 2: Initialize pointers
        prev = dummy
        current = head

        # 🟢 Step 3: Traverse
        while current:
            if current.val == val:
                # Case A: Remove current node
                prev.next = current.next
            else:
                # Case B: Keep current node → move prev forward
                prev = current
            # Always move current forward
            current = current.next

        # 🟢 Step 4: Return new head
        return dummy.next


# --------------------------------------------
# 📝 Iteration Walkthrough Example
# Input: head = 1 → 2 → 6 → 3 → 4 → 5 → 6, val = 6
#
# Initial:
# dummy → 1 → 2 → 6 → 3 → 4 → 5 → 6
# prev = dummy, current = 1
#
# Iteration 1: current = 1
# - 1 != 6 → keep it
# - prev = 1, current = 2
#
# Iteration 2: current = 2
# - 2 != 6 → keep it
# - prev = 2, current = 6
#
# Iteration 3: current = 6
# - 6 == val → remove it
# - prev.next = 3
# - List: 1 → 2 → 3 → 4 → 5 → 6
# - prev = 2, current = 3
#
# Iteration 4: current = 3
# - 3 != 6 → keep it
# - prev = 3, current = 4
#
# Iteration 5: current = 4
# - 4 != 6 → keep it
# - prev = 4, current = 5
#
# Iteration 6: current = 5
# - 5 != 6 → keep it
# - prev = 5, current = 6
#
# Iteration 7: current = 6
# - 6 == val → remove it
# - prev.next = None
# - List: 1 → 2 → 3 → 4 → 5
#
# End: current = None
#
# ✅ Final Output:
# 1 → 2 → 3 → 4 → 5


# --------------------------------------------
# 🔹 Helper Functions (for testing)
def build_linked_list(values):
    """Converts Python list → Linked List"""
    dummy = ListNode(0)
    current = dummy
    for v in values:
        current.next = ListNode(v)
        current = current.next
    return dummy.next

def linked_list_to_list(head):
    """Converts Linked List → Python list"""
    result = []
    while head:
        result.append(head.val)
        head = head.next
    return result


# --------------------------------------------
# 🔹 Example Run
if __name__ == "__main__":
    s = Solution()
    head = build_linked_list([1,2,6,3,4,5,6])
    new_head = s.removeElements(head, 6)
    print(linked_list_to_list(new_head))   # Output: [1,2,3,4,5]
