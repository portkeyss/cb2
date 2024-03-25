class Solution:
    def buildWall(self, height: int, width: int, bricks: List[int]) -> int:
        mod = 10**9+7
        @lru_cache(None)
        def getWidthConfig(x):
            if x==0: return [1]
            if x<0: return None
            ans = []
            for b in bricks:
                l = getWidthConfig(x-b)
                if l is not None:
                    for p in l:
                        ans.append((1<<x)|p)
            if ans==[]: return None
            else: return ans
        
        A = getWidthConfig(width)
        if A is None: return 0
        
        edgeOnly = 1+(1<<width)
        
        @lru_cache(None)
        def f(lower,h):
            if h==height: return 1
            ans = 0
            for y in A:
                if lower&y==edgeOnly:
                    ans = (ans+f(y,h+1))%mod
            return ans
        
        return f(edgeOnly, 0)   