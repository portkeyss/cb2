class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0]*n
        prefix = nums[0]
        for i in range(1,n):
            res[i] += i*nums[i]-prefix
            prefix += nums[i]
        postfix = nums[n-1]
        for i in range(n-2,-1,-1):
            res[i] += postfix-(n-1-i)*nums[i]
            postfix += nums[i]
        return res