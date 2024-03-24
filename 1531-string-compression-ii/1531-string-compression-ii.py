class Solution:
    def getLengthOfOptimalCompression(self, s: str, k: int) -> int:
        n = len(s)
        
        @lru_cache(None)
        def f(cur, credit, prevLetter, prevCount):
            if cur == n:
                return 0
            ans = math.inf
            
            #cur letter untouched
            if prevLetter == s[cur]:
                if prevCount in [1, 9, 99]:
                    ans = min(ans, 1+f(cur+1, credit, s[cur], 1+prevCount))
                else:
                    ans = min(ans, f(cur+1, credit, s[cur], 1+prevCount))
            else: 
                ans = min(ans, 1+f(cur+1, credit, s[cur], 1))
            
            #delete cur letter
            if credit > 0: #cur letter deleted
                ans = min(ans, f(cur+1, credit-1, prevLetter, prevCount))
            return ans
            
        return f(0, k, "", 0)