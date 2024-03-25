class Solution:
    def buildArray(self, nums: List[int]) -> List[int]:
        shift = 10000
        n = len(nums)
        for i in range(n):
            if nums[i] < 0: continue  
            p = nums[i] 
            j = i
            while nums[j] != i:
                k = nums[j]
                nums[j] = nums[k]-shift
                j = k
            nums[j] = p-shift
        for i in range(n):
            nums[i] += shift
        return nums