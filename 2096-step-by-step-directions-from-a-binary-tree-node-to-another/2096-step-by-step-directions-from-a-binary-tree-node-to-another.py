# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        self.stk = []
        self.path1 = []
        self.path2 = []
        def dfs(tn):
            if tn.val==startValue:
                self.path1 = self.stk.copy()
            elif tn.val==destValue:
                self.path2 = self.stk.copy() 
            if tn.left:
                self.stk.append("L")
                dfs(tn.left)
                self.stk.pop()
            if tn.right:
                self.stk.append("R")
                dfs(tn.right)
                self.stk.pop()
        dfs(root)
        i = j = 0
        while i<len(self.path1) and j<len(self.path2) and self.path1[i]==self.path2[j]:
            i += 1
            j += 1
        path = ["U"]*(len(self.path1)-i)+self.path2[j:]
        return "".join(path)