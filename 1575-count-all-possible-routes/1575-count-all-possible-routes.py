class Solution:
    def countRoutes(self, locations: List[int], start: int, finish: int, fuel: int) -> int:
        n = len(locations)
        mod = 10**9+7
        
        @lru_cache(None)
        def f(i,l):
            if l<0: return 0
            ans = (i==finish)
            for j in range(n):
                if i!=j:
                    ans = (ans+f(j,l-abs(locations[i]-locations[j])))%mod
            return ans
        
        return f(start,fuel)