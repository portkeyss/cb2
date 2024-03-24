class Solution:
    def maxPower(self, s: str) -> int:
        res = 0
        cur = 0
        for i in range(len(s)):
            if i==0 or s[i]!=s[i-1]:
                cur = 1
            else:
                cur += 1
            res = max(res, cur)
        return res