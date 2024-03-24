"""
# Definition for a Node.
class Node:
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""

class Solution:
    def diameter(self, root: 'Node') -> int:
        """
        :type root: 'Node'
        :rtype: int
        """
        if root is None:
            return 0
        self.diameter = 0
        def dfs(node):
            if node.children == []:
                return 0
            radii = []
            for child in node.children:
                heapq.heappush(radii, -(1+dfs(child)))
            i = 0
            l = []
            while radii and i < 2:
                l.append(-heapq.heappop(radii))
                i += 1
            self.diameter = max(self.diameter, sum(l))
            return l[0]
        dfs(root)
        return self.diameter