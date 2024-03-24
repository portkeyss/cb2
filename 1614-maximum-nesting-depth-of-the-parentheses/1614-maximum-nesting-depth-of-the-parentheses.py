class Solution:
    def maxDepth(self, s: str) -> int:
        balance = 0
        res = 0
        for c in s:
            if c == "(": 
                balance += 1
                res = max(res, balance)
            elif c == ")":
                balance -= 1
        return res