class Solution:
    def stoneGameIII(self, stoneValue: List[int]) -> str:
        n = len(stoneValue)
        
        @lru_cache(None)
        def largestSum(start):
            if start == n: return (0,0)
            t = 0
            ans = (-math.inf, -math.inf)
            for i in range(start, min(start+3, n)):
                t += stoneValue[i]
                p, q = largestSum(i+1)
                if t+q > ans[0]:
                    ans = (t+q, p)
            return ans
        
        s1, s2 = largestSum(0)
        if s1 > s2: return "Alice"
        if s1 < s2: return "Bob"
        return "Tie"       