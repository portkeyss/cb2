# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDistance(self, root: TreeNode, p: int, q: int) -> int:
        if p==q: return 0
        self.stack = []
        self.s1 = None
        self.s2 = None
        def preorder(node):
            self.stack.append(node.val)
            if node.val == p: self.s1=self.stack.copy()
            elif node.val == q: self.s2=self.stack.copy()
            if node.left:
                preorder(node.left)
            if node.right:
                preorder(node.right)
            self.stack.pop()
        preorder(root)
        i = j = 0
        while i < len(self.s1) and j < len(self.s2) and self.s1[i]==self.s2[j]:
            i += 1
            j += 1
        return len(self.s1)-i + len(self.s2)-j