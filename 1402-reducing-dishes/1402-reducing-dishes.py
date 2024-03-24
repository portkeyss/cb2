class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        s = satisfaction
        s.sort()
        n = len(s)
        suffix = 0
        res = 0
        for i in range(n-1,-1,-1):
            suffix += s[i]
            if suffix>0:
                res += suffix
            else:
                break
        return res