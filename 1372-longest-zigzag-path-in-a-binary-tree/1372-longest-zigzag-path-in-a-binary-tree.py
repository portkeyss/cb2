# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        self.res = 0
        def f(node):
            a, b = 0, 0
            if node.left:
                b = 1+f(node.left)[0]
            if node.right:
                a = 1+f(node.right)[1]
            self.res = max(self.res, a, b)
            return (a, b)
        f(root)
        return self.res