# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countPairs(self, root: TreeNode, distance: int) -> int:
        edges = defaultdict(list)
        leaves = set()
        def f(node):
            if not node.left and not node.right: leaves.add(node)
            if node.left:
                edges[node].append(node.left)
                edges[node.left].append(node)
                f(node.left)
            if node.right:
                edges[node].append(node.right)
                edges[node.right].append(node)
                f(node.right)
        f(root)
        
        res = 0
        for leaf in leaves:
            seen = set()
            q = [leaf]
            seen.add(leaf)
            d = 0
            while q and d<distance:
                t = []
                for y in q:
                    for x in edges[y]:
                        if x not in seen:
                            if x in leaves: res += 1
                            seen.add(x)
                            t.append(x)
                d += 1
                q = t
        return res//2