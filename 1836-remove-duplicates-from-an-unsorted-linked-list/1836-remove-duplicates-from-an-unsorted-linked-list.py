# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteDuplicatesUnsorted(self, head: ListNode) -> ListNode:
        count = Counter()
        t = head
        while t:
            count[t.val]+=1
            t = t.next
        helper = ListNode(-1,head)
        prev = helper
        t = head
        while t:
            if count[t.val] == 1:
                prev.next = t
                prev = t
            t = t.next
        prev.next = None
        return helper.next