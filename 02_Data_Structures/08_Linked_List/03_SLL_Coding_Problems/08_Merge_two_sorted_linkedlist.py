# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        prehead = ListNode(-1)
        prev = prehead

        while l1 and l2:
            if l1.val <= l2.val:
                prev.next = l1
                l1 = l1.next
            else:
                prev.next = l2
                l2 = l2.next
            prev = prev.next

        prev.next = l1 if l1 is not None else l2
        return prehead.next

    @staticmethod
    def build_linked_list(values):
        dummy = ListNode()
        current = dummy
        for v in values:
            current.next = ListNode(v)
            current = current.next
        return dummy.next

    @staticmethod
    def print_linked_list(node):
        result = []
        while node:
            result.append(node.val)
            node = node.next
        print(result)


# ✅ Use helper to convert Python list → LinkedList
l1 = Solution.build_linked_list([1,2,4])
l2 = Solution.build_linked_list([1,3,4])

s1 = Solution()
merged = s1.mergeTwoLists(l1, l2)

# ✅ Print merged LinkedList
Solution.print_linked_list(merged)   # [1, 1, 2, 3, 4, 4]
