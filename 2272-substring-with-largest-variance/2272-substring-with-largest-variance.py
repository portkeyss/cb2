class Solution:
    def largestVariance(self, s: str) -> int:
        t = list(set(s))
        n = len(t)
        res = 0
        for i in range(n):
            for j in range(n):
                if i==j: continue
                a=b=0
                for c in s:
                    if c!=t[i] and c!=t[j]: continue
                    if c==t[i]: 
                        a += 1   
                    elif c==t[j]:
                        b += 1
                    if a>0 and b>0 and a>b:
                        res = max(res, a-b)
                    if a<b:
                        a = 0
                        b = 0
                a=b=0
                for c in s[::-1]:
                    if c!=t[i] and c!=t[j]: continue
                    if c==t[i]: 
                        a += 1   
                    elif c==t[j]:
                        b += 1
                    if a>0 and b>0 and a>b:
                        res = max(res, a-b)
                    if a<b:
                        a = 0
                        b = 0
        return res