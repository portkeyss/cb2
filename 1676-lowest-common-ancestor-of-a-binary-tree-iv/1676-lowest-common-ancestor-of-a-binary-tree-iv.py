# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', nodes: 'List[TreeNode]') -> 'TreeNode':
        parent = dict()
        nodes = set(nodes)
        depth = 0
        lowestDepth = -1
        A = defaultdict(set)
        q = [root]
        while q:
            t = []
            for x in q:
                if x in nodes: 
                    if lowestDepth==-1: lowestDepth = depth
                    A[depth].add(x)
                if x.left:
                    parent[x.left]=x
                    t.append(x.left)
                if x.right:
                    parent[x.right]=x
                    t.append(x.right)
            q = t
            depth += 1
        
        for d in range(depth-1,-1,-1):
            if d<=lowestDepth and len(A[d])==1: return A[d].pop()
            for tn in A[d]:
                A[d-1].add(parent[tn])