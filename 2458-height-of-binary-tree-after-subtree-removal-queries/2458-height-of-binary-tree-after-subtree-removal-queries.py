# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, root: Optional[TreeNode], queries: List[int]) -> List[int]:
        level = dict()
        depth = dict()
        A = defaultdict(list)

        def dfs(node,d):
            level[node.val] = d
            if not node.left and not node.right:
                depth[node.val] = d
                heapq.heappush(A[d],(-d))
                return d
            depth[node.val] = d
            if node.left: depth[node.val] = max(depth[node.val],dfs(node.left,d+1))
            if node.right: depth[node.val] = max(depth[node.val],dfs(node.right,d+1))
            heapq.heappush(A[d],(-depth[node.val]))
            return depth[node.val]
        
        dfs(root,0)

        res = []
        for x in queries:
            if -A[level[x]][0]>depth[x]: res.append(-A[level[x]][0])
            else:
                y = -A[level[x]][0]
                heapq.heappop(A[level[x]])
                if A[level[x]]: res.append(-A[level[x]][0])
                else: res.append(level[x]-1)
                heapq.heappush(A[level[x]],-y)  
        return res