class Solution:
    def maxUniqueSplit(self, s: str) -> int:
        n = len(s)
        seen = set()
        
        def dfs(pos):
            if pos==n: return 0
            ans = -inf
            for i in range(pos,n):
                if s[pos:i+1] not in seen:
                    seen.add(s[pos:i+1])
                    ans = max(ans, 1+dfs(i+1))
                    seen.remove(s[pos:i+1])
            return ans
        
        return dfs(0)