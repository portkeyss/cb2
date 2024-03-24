# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pseudoPalindromicPaths (self, root: Optional[TreeNode]) -> int:
        counter = [0]*10
        self.res = 0
        def f(node):
            counter[node.val] += 1
            if node.left is None and node.right is None:
                if sum(counter[i]%2==1 for i in range(1,10))<2:
                    self.res += 1
            if node.left:
                f(node.left)
            if node.right:
                f(node.right)
            counter[node.val] -= 1
        f(root)
        return self.res