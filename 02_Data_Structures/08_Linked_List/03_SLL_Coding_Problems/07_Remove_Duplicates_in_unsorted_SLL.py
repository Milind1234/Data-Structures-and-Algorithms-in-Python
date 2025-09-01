# 🚀 Remove Duplicates from an Unsorted Linked List
# -------------------------------------------------
# ✅ Approach:
# 1. Use a Dummy Node before head to handle edge cases (like duplicate at head).
# 2. Maintain a HashSet `seen` to track visited values.
# 3. Use two pointers:
#    - `prev` = last unique node kept
#    - `current` = node under inspection
# 4. Traverse:
#    - If value not in seen → keep it (add to set, move forward).
#    - If value already in seen → skip it by rewiring `prev.next = current.next`.

# Time Complexity: O(n)  ⏳
# Space Complexity: O(n) 📦 (because of the set)


# --------------------------------------------
# 🔹 Definition of Linked List Node
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution(object):
    def deleteDuplicates(self, head):
        """
        Removes duplicates from an unsorted linked list.
        Ensures each element appears only once.
        """

        # 🟢 Step 1: Create a dummy node before head
        dummy = ListNode(None)
        dummy.next = head

        # 🟢 Step 2: Initialize a set to track seen values
        seen = set()

        # 🟢 Step 3: Initialize pointers
        prev = dummy       # points to last unique node
        current = head     # node under inspection

        # 🟢 Step 4: Traverse the linked list
        while current:
            if current.val not in seen:
                # Case A: Unique value
                seen.add(current.val)      # record it
                prev = current             # move prev forward
                current = current.next     # move current forward
            else:
                # Case B: Duplicate value
                prev.next = current.next   # skip the duplicate node
                current = prev.next        # move current forward

        # 🟢 Step 5: Return the updated head (after dummy)
        return dummy.next


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
# Input: head = 3 → 3 → 1 → 2 → 2
#
# Initial State:
# dummy → 3 → 3 → 1 → 2 → 2
# seen = {}
# prev = dummy
# current = 3 (first)
#
# Iteration 1 (current = 3):
# - 3 not in seen → add it
# - seen = {3}
# - prev = 3, current = 3 (second one)
# - List so far: 3 → 3 → 1 → 2 → 2
#
# Iteration 2 (current = 3 second one):
# - 3 already in seen → duplicate
# - Skip it: prev.next = current.next
# - List becomes: 3 → 1 → 2 → 2
# - current = 1
#
# Iteration 3 (current = 1):
# - 1 not in seen → add it
# - seen = {3,1}
# - prev = 1, current = 2 (first)
# - List so far: 3 → 1 → 2 → 2
#
# Iteration 4 (current = 2 first one):
# - 2 not in seen → add it
# - seen = {3,1,2}
# - prev = 2, current = 2 (second one)
# - List so far: 3 → 1 → 2 → 2
#
# Iteration 5 (current = 2 second one):
# - 2 already in seen → duplicate
# - Skip it: prev.next = current.next → None
# - List becomes: 3 → 1 → 2
# - current = None (end)
#
# ✅ End:
# Return dummy.next → 3 → 1 → 2
# Final seen = {3,1,2}
#
# ✅ Output: [3, 1, 2]


# ------------------------------------------------
# 🔹 Example Run
if __name__ == "__main__":
    l1 = build_linked_list([3, 3, 1, 2, 2])
    solution = Solution()
    new_head = solution.deleteDuplicates(l1)
    print(linked_list_to_list(new_head))   # Output: [3, 1, 2]
