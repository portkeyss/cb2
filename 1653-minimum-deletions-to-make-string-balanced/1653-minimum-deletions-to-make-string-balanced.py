class Solution:
    def minimumDeletions(self, s: str) -> int:
        dp = 0
        bcount = 0
        for c in s:
            if c == 'a':
                dp = min(bcount, 1+dp)
            else:
                bcount += 1
        return dp