# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortLinkedList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        A = []
        B = []
        t = head
        while t:
            if t.val>=0: A.append(t.val)
            else:B.append(t.val)
            t = t.next
        t = head
        while t:
            while B:
                t.val = B.pop()
                t = t.next
            for a in A:
                t.val = a
                t = t.next
        return head