# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteNodes(self, head: ListNode, m: int, n: int) -> ListNode:   
        helper = ListNode()
        helper.next = head
        l = helper
        while True:
            cnt = 0
            while l and cnt < m:
                cnt += 1
                l = l.next
            if not l:
                break
            p = l
            cnt = 0
            while l and cnt < n:
                cnt += 1
                l = l.next     
            if not l:
                p.next = None
                break
            p.next = l.next
        return head