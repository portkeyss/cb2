class Solution:
    def minDistance(self, houses: List[int], k: int) -> int:
        houses.sort()

        @lru_cache(None)
        def g(a,b):
            dist = sum(houses[i]-houses[a] for i in range(a,b+1))
            ans = dist
            for i in range(a+1,b+1):
                dist += (2*i-a-b-1)*(houses[i]-houses[i-1])
                ans = min(ans,dist)
            return ans
        
        @lru_cache(None)
        def f(a,b,l):
            if l==1: return g(a,b)
            if l>b-a+1: return inf
            ans = inf
            for c in range(a,b):
                ans = min(ans, f(a,c,l-1)+g(c+1,b))
            return ans
        
        return f(0,len(houses)-1,k)