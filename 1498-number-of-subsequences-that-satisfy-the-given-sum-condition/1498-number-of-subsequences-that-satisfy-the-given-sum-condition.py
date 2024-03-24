class Solution:
    def numSubseq(self, nums: List[int], target: int) -> int:
        nums.sort()
        mod = 10**9+7
        n = len(nums)
        res = 0
        i = 0
        j = n-1
        while True:
            while j>=i and nums[i]+nums[j]>target:
                j -= 1
            if j<i: break
            res += pow(2,j-i,mod)
            res %= mod
            i += 1
        return res