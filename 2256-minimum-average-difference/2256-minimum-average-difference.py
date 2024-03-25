class Solution:
    def minimumAverageDifference(self, nums: List[int]) -> int:
        n = len(nums)
        j = -1
        ad = math.inf
        sm = sum(nums)
        prefix = 0
        for i,num in enumerate(nums):
            prefix = prefix+num
            x = prefix//n if i==n-1 else abs(prefix//(i+1)-(sm-prefix)//(n-i-1))
            if x<ad:
                ad = x
                j = i
        return j