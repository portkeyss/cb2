class Solution:
    def stoneGameVII(self, stones: List[int]) -> int:
        prefix = [0]
        x = 0
        for s in stones:
            x += s
            prefix.append(x)
        
        @lru_cache(2000)
        def f(i,j):
            if i==j: return 0
            return max(prefix[j+1]-prefix[i+1]-f(i+1,j), prefix[j]-prefix[i]-f(i,j-1))

        return f(0,len(stones)-1)