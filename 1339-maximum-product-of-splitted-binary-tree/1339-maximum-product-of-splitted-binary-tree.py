# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        subSum = dict()
        def dfs1(node):
            if node is None: return 0
            subSum[node] = dfs1(node.left)+dfs1(node.right)+node.val
            return subSum[node]
        dfs1(root)
        
        self.res = 0
        def dfs2(node):
            self.res = max(self.res,  subSum[node]*(subSum[root]-subSum[node]))
            if node.left:
                dfs2(node.left)
            if node.right:
                dfs2(node.right)
        dfs2(root)
        return self.res%(10**9+7)