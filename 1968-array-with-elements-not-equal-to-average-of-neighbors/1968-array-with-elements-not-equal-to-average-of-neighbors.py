class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        nums.sort()
        n = len(nums)
        res = [-1]*n
        j = 0
        for i in range(0,n,2):
            res[i] = nums[j]
            j += 1
        for i in range(1,n,2):
            res[i] = nums[j]
            j += 1
        return res