# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        tail2 = list2
        while tail2.next is not None:
            tail2 = tail2.next
        idx = 0
        node = list1
        while idx < a-1:
            node = node.next
            idx+=1
        ta = node
        while idx < b+1:
            node = node.next
            idx+=1
        tb = node
        ta.next = list2
        tail2.next = tb
        return list1