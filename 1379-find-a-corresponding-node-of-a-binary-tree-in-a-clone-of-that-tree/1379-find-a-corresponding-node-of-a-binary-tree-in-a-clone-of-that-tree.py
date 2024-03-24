# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def getTargetCopy(self, original: TreeNode, cloned: TreeNode, target: TreeNode) -> TreeNode:
        self.signatures = []
        self.path = []
        def f(x):
            if x==target:
                self.path = [p for p in self.signatures]
                return True
            if x is None: return False
            self.signatures.append(0)
            l = f(x.left)
            self.signatures.pop()
            if l: return True
            self.signatures.append(1)
            r = f(x.right)
            self.signatures.pop()
            if r: return True
            return False
        
        f(original)
        res = cloned
        for node in self.path:
            res = res.left if node==0 else res.right
        return res