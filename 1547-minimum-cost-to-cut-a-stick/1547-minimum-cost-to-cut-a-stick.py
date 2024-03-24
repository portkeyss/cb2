class Solution:
    def minCost(self, n: int, cuts: List[int]) -> int:
        cuts.sort()
        cuts = [0]+cuts+[n]
        
        @lru_cache(None)
        def cost(s,e):
            if s==e-1: return 0
            res = inf
            for i in range(s+1,e):
                res = min(res, cuts[e]-cuts[s]+cost(s,i)+cost(i,e))
            return res
        
        return cost(0,len(cuts)-1)