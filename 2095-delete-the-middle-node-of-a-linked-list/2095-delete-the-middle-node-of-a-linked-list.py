# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        helper = ListNode(-1,head)
        l = helper
        n = 0
        while l.next:
            l = l.next
            n += 1
        l = helper
        count = 0
        while count<n//2:
            l = l.next
            count += 1
        l.next = l.next.next
        return helper.next