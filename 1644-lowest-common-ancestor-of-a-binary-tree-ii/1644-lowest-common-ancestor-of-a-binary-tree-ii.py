# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        stack = []
        A = []
        B = []
        def dfs(node):
            if node is None: return
            stack.append(node)
            if node==p:
                for x in stack:
                    A.append(x)
            if node==q:
                for x in stack:
                    B.append(x)
            dfs(node.left)
            dfs(node.right)
            stack.pop()
        
        dfs(root)
        if A is None or B is None: return None
        A = A[::-1]
        B = B[::-1]
        res = None
        while A and B and A[-1]==B[-1]:
            res = A[-1]
            A.pop()
            B.pop()
        return res