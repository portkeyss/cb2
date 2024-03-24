class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        m = floor(log(max(a,b,c),2))+1
        res = 0
        for i in range(m+1):
            if (1<<i)&(a|b)==(1<<i)&c: continue
            if (1<<i)&c: 
                res += 1
            else:
                if (1<<i)&a and (1<<i)&b: res += 2
                else: res += 1
        return res