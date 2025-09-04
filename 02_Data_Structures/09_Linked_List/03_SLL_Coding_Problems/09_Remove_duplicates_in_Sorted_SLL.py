# 🚀 Remove Duplicates from a Sorted Linked List
# ----------------------------------------------
# ✅ Approach:
# 1. Since the list is sorted, duplicates will always appear consecutively.
# 2. Use a single pointer `current` to traverse the list.
# 3. At each step:
#    - Compare current node with the next one.
#    - If values are equal → skip the next node by linking:
#         current.next = current.next.next
#    - Otherwise → move forward normally.
# 4. Return the original head at the end.
#
# Time Complexity: O(n)  ⏳ (single pass)
# Space Complexity: O(1) 📦 (no extra memory)


# --------------------------------------------
# 🔹 Definition of Linked List Node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        Removes duplicates from a sorted linked list.
        Each element appears only once.
        """

        # 🟢 Start from the head
        current = head

        # 🟢 Traverse while next node exists
        while current and current.next:
            if current.val == current.next.val:
                # Case A: Duplicate → skip it
                current.next = current.next.next
            else:
                # Case B: Unique → just move forward
                current = current.next

        # 🟢 Return the cleaned list
        return head


# ------------------------------------------------
# 🔹 Helper Functions (for testing and debugging)
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


# ------------------------------------------------
# 📝 Iteration Walkthrough Example
# Input: head = 1 → 1 → 2 → 3 → 3
#
# Initial State:
# current = 1 (first)
#
# Iteration 1:
# - Compare 1 and next(1) → equal ✅
# - Skip duplicate → current.next = current.next.next
# - List becomes: 1 → 2 → 3 → 3
# - current still at 1
#
# Iteration 2:
# - Compare 1 and next(2) → not equal
# - Move current → now at 2
# - List so far: 1 → 2 → 3 → 3
#
# Iteration 3:
# - Compare 2 and next(3) → not equal
# - Move current → now at 3 (first one)
# - List so far: 1 → 2 → 3 → 3
#
# Iteration 4:
# - Compare 3 and next(3) → equal ✅
# - Skip duplicate → current.next = current.next.next
# - List becomes: 1 → 2 → 3
# - current still at 3
#
# End:
# - current.next = None, stop loop
#
# ✅ Final Output:
# 1 → 2 → 3


# ------------------------------------------------
# 🔹 Example Run
if __name__ == "__main__":
    l1 = build_linked_list([1, 1, 2, 3, 3])
    solution = Solution()
    new_head = solution.deleteDuplicates(l1)
    print(linked_list_to_list(new_head))   # Output: [1, 2, 3]
