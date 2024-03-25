# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def canMerge(self, trees: List[TreeNode]) -> Optional[TreeNode]:
        n = len(trees)
        A, B, C = dict(), dict(), dict()
        for i,rt in enumerate(trees):    
            if rt.val in A: return None
            A[rt.val]=i
            if rt.left:
                if rt.left.val in B: return None
                B[rt.left.val]=i
            if rt.right:
                if rt.right.val in C: return None
                C[rt.right.val]=i
                
        rootIdx = None
        for v,i in A.items():
            if v not in B and v not in C:
                if rootIdx is None:
                    rootIdx = i
                else:
                    return None
        if rootIdx is None: return None
        
        root = trees[rootIdx]
        self.ops = 0
        def construct(node):
            if node.left:
                if node.left.val in A:
                    x = A[node.left.val]
                    A.pop(node.left.val)
                    node.left = trees[x]
                    self.ops += 1
                    construct(node.left)
            if node.right:
                if node.right.val in A:
                    y = A[node.right.val]
                    A.pop(node.right.val)
                    node.right = trees[y]
                    self.ops += 1
                    construct(node.right)
        
        construct(root)
        if self.ops < n-1: return None
        
        self.prev = -inf
        self.order = True
        def inorder(node):
            if node.left:
                inorder(node.left)
            if node.val<=self.prev:
                self.order = False
            self.prev = node.val
            if node.right:
                inorder(node.right)
        inorder(root)
        return root if self.order else None