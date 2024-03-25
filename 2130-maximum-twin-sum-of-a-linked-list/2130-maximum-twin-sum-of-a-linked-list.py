# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        helper = ListNode(next=head)
        slow = fast = helper
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
        l = slow.next
        slow.next = None
        
        def reverse(h):
            prev = None
            cur = h
            while cur:
                nxt = cur.next
                cur.next = prev
                prev = cur
                cur = nxt
            return prev
        
        x, y = head, reverse(l)
        res = -inf
        while x:
            res = max(res, x.val+y.val)
            x = x.next
            y = y.next
        return res 