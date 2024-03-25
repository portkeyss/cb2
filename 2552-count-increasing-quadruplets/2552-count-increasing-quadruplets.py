class Solution:
    def countQuadruplets(self, nums: List[int]) -> int:
        n = len(nums)
        less = [[0]*n for _ in range(n)] #less[i][j]: number of elements with index <i that is smaller than nums[j]
        larger = [[0]*n for _ in range(n)]#larger[i][j]: number of elements with index >i that is larger than nums[j]
        for j in range(n):
            x = 0
            for i in range(j):
                less[i][j] = x
                if nums[i]<nums[j]: x += 1
        for j in range(n):
            y = 0
            for i in range(n-1,j,-1):
                larger[i][j] = y
                if nums[i]>nums[j]:y += 1
                
        res = 0
        for j in range(n):
            for k in range(j+1,n):
                if nums[j]>nums[k]:
                    res += less[j][k]*larger[k][j]
        return res