class Solution:
    def waysToSplit(self, nums: List[int]) -> int:
        n = len(nums)
        prefix = [nums[0]]
        for i in range(1, len(nums)):
            prefix.append(nums[i]+prefix[-1])
        res = 0
        s = prefix[-1]
        for i,x in enumerate(prefix):
            j = bisect.bisect_left(prefix, 2*x, i+1, n-1)
            k = bisect.bisect(prefix, (s+x)//2, i+1, n-1)-1
            if j <= k:
                res += (k-j+1)
        return res % (10**9+7)