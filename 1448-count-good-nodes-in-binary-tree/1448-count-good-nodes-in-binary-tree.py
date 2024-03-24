# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        ct = 0
        stack = []
        def f(node):
            nonlocal ct
            if not node:
                return
            if not stack or node.val >= stack[-1]:
                stack.append(node.val)
                ct += 1
            f(node.left)
            f(node.right)
            if not stack or node.val >= stack[-1]:
                stack.pop()
        f(root)
        return ct