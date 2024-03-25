# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        helper = ListNode(-1,head)
        t = head
        i = 0
        a = None
        b = None
        while t:
            i += 1
            if i==k:
                a = t
                b = helper
            t = t.next
            if b:
                b = b.next
        a.val, b.val = b.val, a.val
        return head