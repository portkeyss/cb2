# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def balanceBST(self, root: TreeNode) -> TreeNode:
        seq = []
        def inorder(node):
            if node is None: return
            inorder(node.left)
            seq.append(node.val)
            inorder(node.right)
       
        def construct(s, e):
            if s > e: return None
            if s == e: return TreeNode(seq[s])
            mid = (s+e+1)//2
            node = TreeNode(seq[mid])
            l = construct(s, mid-1)
            r = construct(mid+1, e)
            node.left = l
            node.right = r
            return node
        
        inorder(root)
        return construct(0, len(seq)-1)