class Solution:
    def minCostSetTime(self, startAt: int, moveCost: int, pushCost: int, targetSeconds: int) -> int:
        m, s = targetSeconds//60, targetSeconds%60
        A = None
        if m==100: A=[[m-1,s+60]]
        else:
            A = [[m,s]]
            if s+60<100 and m>0:
                A.append([m-1,s+60])
        res = inf
        for m,s in A:
            t = 0
            l = None
            if m==0:
                if s//10==0:
                    l = [s%10]
                else:
                    l = [s//10, s%10]
            elif m>=10:
                l = [m//10, m%10, s//10, s%10]
            else:
                l = [m%10, s//10, s%10]
            prev = startAt
            for x in l:
                if prev!=x: t += moveCost
                t += pushCost
                prev = x
            res = min(res, t)
        return res