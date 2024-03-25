class Solution:
    def recoverArray(self, n: int, sums: List[int]) -> List[int]:
        sums.sort()
        s = sums
        res = []
        while len(s)>1:
            l, r = [],[]
            x = s[1]-s[0]
            hasZero = False
            j = 0
            for i in range(len(s)):
                if s[i]!=inf:
                    if s[i]==0: hasZero = True
                    l.append(s[i])
                    r.append(s[i]+x)
                    j = max(j+1,i+1)
                    while s[j]!=s[i]+x:
                        j+=1
                    s[j] = inf
            if hasZero:
                res.append(x)
                s = l
            else:
                res.append(-x)
                s = r
        return res