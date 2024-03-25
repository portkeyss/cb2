class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        n = len(nums)
        valid = [False]*(n+1)
        valid[0] = True
        for i in range(1,n):
            if nums[i]==nums[i-1] and valid[i-1]: valid[i+1] = True
            elif i>=2 and nums[i]==nums[i-1]==nums[i-2] and valid[i-2]: valid[i+1] = True
            elif i>=2 and nums[i]==nums[i-1]+1==nums[i-2]+2 and valid[i-2]: valid[i+1] = True
        return valid[n]