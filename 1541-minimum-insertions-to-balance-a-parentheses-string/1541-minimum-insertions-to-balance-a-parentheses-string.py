class Solution:
    def minInsertions(self, s: str) -> int:
        A = []
        i = 0
        res = 0
        while i < len(s):
            if s[i]=="(":
                A.append(1)
                i += 1
            else:
                if i+1<len(s) and s[i+1]==")":
                    A.append(-1)
                    i += 2
                else:
                    A.append(-1)
                    res += 1
                    i += 1
        balance = 0
        for p in A:
            balance += p
            if balance < 0:
                res += 1
                balance = 0
        if balance > 0:
            res += 2*balance
        return res