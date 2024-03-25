class Solution:
    def subsetXORSum(self, nums: List[int]) -> int:
        #This method is somewhat nonintuitive
        a = 0
        for num in nums:
            a |= num
        return a*(1<<(len(nums)-1))