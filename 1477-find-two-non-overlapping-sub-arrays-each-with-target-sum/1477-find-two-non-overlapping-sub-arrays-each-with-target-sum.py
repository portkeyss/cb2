class Solution:
    def minSumOfLengths(self, arr: List[int], target: int) -> int:
        n = len(arr)
        sm = 0
        idx = {0:0}
        cnd = [inf]*(n+1)
        for i in range(n):
            sm += arr[i] 
            if sm-target in idx:
                cnd[i+1] = min(cnd[i],i+1-idx[sm-target])
            else:
                cnd[i+1] = cnd[i]
            idx[sm] = i+1
        res = inf
        sm = 0
        idx = {0:n+1}
        for i in range(n-1,-1,-1):
            sm += arr[i]
            if sm-target in idx:
                res = min(res, cnd[i]+idx[sm-target]-i-1)
            idx[sm] = i+1
        return res if res<inf else -1