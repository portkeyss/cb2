class Solution:
    def kthSmallestSubarraySum(self, nums: List[int], k: int) -> int:
        prefix = [0]
        cur = 0
        for num in nums:
            cur+=num
            prefix.append(cur)
        
        n = len(nums)
        def f(x): #count the number of subarrays of sum<x
            ct = 0
            for i in range(n):
                j = bisect.bisect_left(prefix,prefix[i]+x)
                ct += j-i-1
            return ct
        
        l,r = 1,sum(nums)
        while l<r:
            mid = (l+r+1)//2
            p = f(mid)
            if p<k:
                l = mid
            else:
                r = mid-1
        return l