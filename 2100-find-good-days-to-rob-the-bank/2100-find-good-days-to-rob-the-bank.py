class Solution:
    def goodDaysToRobBank(self, security: List[int], time: int) -> List[int]:
        n = len(security)
        if time==0: return list(range(n))
        A = [0]*n
        for i in range(1,n):
            if security[i]<=security[i-1]:
                A[i] = A[i-1]+1
            else:
                A[i] = 0
        res = []
        x = 0
        for i in range(n-2,-1,-1):
            if security[i]<=security[i+1]:
                x += 1
                if A[i]>=time and x>=time:
                    res.append(i)
            else:
                x = 0
        return res