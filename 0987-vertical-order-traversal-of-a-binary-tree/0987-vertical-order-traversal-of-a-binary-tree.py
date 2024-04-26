# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def verticalTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        
        self.hq = [] # heap queue for (column, row, nodes value)
        self.traversal(root, 0, 0)
        res = []
        prev_col = -10000 # define an initially out of bound previous column
        while self.hq:
            col, _, val = heapq.heappop(self.hq)           
            if col == prev_col:
                res[-1].append(val)
            else:
                res.append([val])
            prev_col= col      
        return res
    
    def traversal(self, root, row, col):
        if not root:
            return
        heapq.heappush(self.hq, (col, row, root.val))
        self.traversal(root.left, row+1, col-1)
        self.traversal(root.right, row+1, col+1)
        