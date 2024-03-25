class Solution:
    def minDifference(self, nums: List[int], queries: List[List[int]]) -> List[int]:
        prefix = [[0]*101]
        for i,num in enumerate(nums):
            prefix.append(prefix[-1].copy())
            prefix[-1][num] += 1
        res = []
        for a,b in queries:
            freqs = [x-y for x,y in zip(prefix[b+1],prefix[a])]
            z = 1000
            prev = -10000
            for i in range(1,101):
                if freqs[i]==0: continue
                z=min(z, i-prev)
                prev = i
            if z==1000: z=-1
            res.append(z)
        return res