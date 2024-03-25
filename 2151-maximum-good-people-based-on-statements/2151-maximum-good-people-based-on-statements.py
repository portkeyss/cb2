class Solution:
    def maximumGood(self, statements: List[List[int]]) -> int:
        n = len(statements)
        res = 0
        for mask in range(1<<n):
            good = []
            for i in range(n):
                if (1<<i)&mask:
                    good.append(i)
            if len(good)<=res: continue
            fail = False        
            for i in good:
                for j in range(n):
                    if statements[i][j]==0 and j in good or statements[i][j]==1 and j not in good:
                        fail = True
                        break
                if fail: break
            if fail: continue
            res = max(res,len(good))
        return res         