"""
# Definition for a Node.
class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.parent = None
"""

class Solution:
    def lowestCommonAncestor(self, p: 'Node', q: 'Node') -> 'Node':
        ancestors1 = []
        m = p
        while m:
            ancestors1.append(m)
            m = m.parent
            
        ancestors2 = []
        n = q
        while n:
            ancestors2.append(n)
            n = n.parent
        
        i, j = len(ancestors1)-1, len(ancestors2)-1
        res = None
        while ancestors1[i] == ancestors2[j]:
            res = ancestors1[i]
            i -= 1
            j -= 1
        return res