class Solution:
    def canBeIncreasing(self, nums: List[int]) -> bool:
        n = len(nums)
        i = 0
        while i<n-1 and nums[i]<nums[i+1]: i+=1
        if i==n-1: return True
        j = n-2
        while j>=0 and nums[j]<nums[j+1]: j-=1
        if i<j: return False
        return i==0 or nums[i-1]<nums[i+1] or i==n-2 or nums[i]<nums[i+2]