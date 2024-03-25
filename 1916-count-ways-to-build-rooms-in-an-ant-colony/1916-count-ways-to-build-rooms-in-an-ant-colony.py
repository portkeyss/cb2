class Solution:
    def waysToBuildRooms(self, prevRoom: List[int]) -> int:
        mod = 10**9+7
        n = len(prevRoom)
        children = [[] for _ in range(n)]
        for i,j in enumerate(prevRoom):
            if j>-1: children[j].append(i)
        
        #return all permissible orderings in subtree of k and subtree node counts
        def dfs(k):
            if not children[k]: return 1,1
            orderings = 1
            nodes = 0
            for l in children[k]:
                subtreeOrderings, subtreeNodes= dfs(l)
                orderings = (orderings*comb(nodes+subtreeNodes, nodes))%mod
                orderings = (orderings*subtreeOrderings)%mod
                nodes += subtreeNodes
            nodes += 1
            return orderings,nodes

        return dfs(0)[0]