class Solution:
    def countHomogenous(self, s: str) -> int:
        mod = 10**9+7
        prev = ""
        consecutive = 0
        ans = 0
        for c in s:
            consecutive = 1+(c==prev)*consecutive
            ans = (ans+consecutive)%mod
            prev = c
        return ans